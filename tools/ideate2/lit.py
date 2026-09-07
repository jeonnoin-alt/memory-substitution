#!/usr/bin/env python3
"""Literature collectors for ideate2, written for a restricted network.

Reachable from this node (2026-09-07): Semantic Scholar (key + pinned IP), HuggingFace Papers.
Blocked here but implemented behind a probe so the same code works elsewhere: arXiv export/HTML,
ar5iv, OpenAlex. Full-text sections are read through whichever of {arxiv html, ar5iv} is reachable;
otherwise a WebSearch job spec is emitted for the harness (Claude Code WebSearch is server-side).

Key handling: S2_API_KEY from the environment or /home/work/.s2_env (mode 600). Never printed.
"""
from __future__ import annotations
import os, re, json, time, socket, hashlib
from dataclasses import dataclass, asdict, field
from typing import Any, Optional
import requests

S2_HOST = "api.semanticscholar.org"
KEY_FILE = "/home/work/.s2_env"


def _load_key() -> Optional[str]:
    k = os.environ.get("S2_API_KEY")
    if k:
        return k
    try:
        for line in open(KEY_FILE):
            if line.startswith("S2_API_KEY="):
                return line.split("=", 1)[1].strip()
    except OSError:
        pass
    return None


def reachable(host: str, timeout: float = 4.0) -> bool:
    try:
        socket.create_connection((host, 443), timeout=timeout).close()
        return True
    except OSError:
        return False


@dataclass
class Paper:
    id: str                      # canonical: arXiv id if known, else s2:<paperId> / doi:<doi>
    title: str
    abstract: str = ""
    tldr: str = ""
    year: Optional[int] = None
    date: str = ""               # YYYY-MM-DD when known
    venue: str = ""
    citations: Optional[int] = None
    arxiv: str = ""
    doi: str = ""
    url: str = ""
    pdf: str = ""
    sources: list = field(default_factory=list)   # channels that returned it
    queries: list = field(default_factory=list)   # queries that returned it
    axes: list = field(default_factory=list)
    sections: dict = field(default_factory=dict)  # {"limitations": "...", "conclusion": "..."}
    keywords: list = field(default_factory=list)
    relevance: float = 0.0        # embedding relevance to its axis (prescan --rerank)

    def key(self) -> str:
        if self.arxiv:
            return "arxiv:" + re.sub(r"v\d+$", "", self.arxiv)
        if self.doi:
            return "doi:" + self.doi.lower()
        return "title:" + re.sub(r"[^a-z0-9]", "", self.title.lower())[:80]


# --------------------------------------------------------------------------- #
class S2Client:
    """Semantic Scholar Graph API with key, IP pinning and 1 req/s throttle."""
    FIELDS = "title,year,venue,citationCount,externalIds,abstract,tldr,openAccessPdf,publicationDate,url"

    def __init__(self, pin_ip: Optional[str] = None, min_interval: float = 1.1):
        self.key = _load_key()
        self.pin_ip = pin_ip or os.environ.get("S2_PIN_IP") or self._probe()
        self.min_interval = min_interval
        self._last = 0.0
        self.ok = bool(self.pin_ip)

    def _probe(self) -> Optional[str]:
        try:
            ips = sorted({i[4][0] for i in socket.getaddrinfo(S2_HOST, 443)})
        except socket.gaierror:
            return None
        for ip in ips:
            try:
                socket.create_connection((ip, 443), timeout=3).close()
                return ip
            except OSError:
                continue
        return None

    _LOCK = os.path.join(os.environ.get("S2_LOCK_DIR", "/tmp"), "s2_throttle.lock")

    def _throttle_across_processes(self):
        """One request per min_interval across every process on this node (subagents run s2cli.py concurrently)."""
        import fcntl
        try:
            fd = os.open(self._LOCK, os.O_RDWR | os.O_CREAT, 0o666)
        except OSError:
            wait = self.min_interval - (time.time() - self._last)
            if wait > 0: time.sleep(wait)
            return
        try:
            fcntl.flock(fd, fcntl.LOCK_EX)
            try:
                last = float(os.read(fd, 64).decode() or "0")
            except ValueError:
                last = 0.0
            wait = self.min_interval - (time.time() - last)
            if wait > 0:
                time.sleep(wait)
            os.lseek(fd, 0, 0); os.ftruncate(fd, 0); os.write(fd, str(time.time()).encode())
        finally:
            fcntl.flock(fd, fcntl.LOCK_UN); os.close(fd)

    def _get(self, path: str, params: dict, timeout: float = 30) -> Optional[dict]:
        if not self.ok:
            return None
        self._throttle_across_processes()
        headers = {"x-api-key": self.key} if self.key else {}
        url = f"https://{S2_HOST}{path}"
        s = requests.Session()
        # pin: connect to the IP but keep the hostname for SNI/Host
        from requests.adapters import HTTPAdapter
        from urllib3.util import connection as _conn
        orig = _conn.create_connection
        pin = self.pin_ip

        def patched(address, *a, **kw):
            host, port = address
            if host == S2_HOST:
                return orig((pin, port), *a, **kw)
            return orig(address, *a, **kw)
        _conn.create_connection = patched
        try:
            for attempt in range(4):
                self._last = time.time()
                r = s.get(url, params=params, headers=headers, timeout=timeout)
                if r.status_code == 429:
                    time.sleep(2.0 * (attempt + 1)); self._throttle_across_processes(); continue
                if r.status_code == 200:
                    return r.json()
                if r.status_code == 404:
                    return None
                time.sleep(1.0)
            return None
        except requests.RequestException:
            return None
        finally:
            _conn.create_connection = orig

    @staticmethod
    def _to_paper(p: dict, query: str = "") -> Paper:
        ext = p.get("externalIds") or {}
        return Paper(
            id=("arxiv:" + ext["ArXiv"]) if ext.get("ArXiv") else ("s2:" + str(p.get("paperId"))),
            title=p.get("title") or "", abstract=p.get("abstract") or "",
            tldr=((p.get("tldr") or {}).get("text") or ""), year=p.get("year"),
            date=p.get("publicationDate") or "", venue=p.get("venue") or "",
            citations=p.get("citationCount"), arxiv=ext.get("ArXiv") or "", doi=ext.get("DOI") or "",
            url=p.get("url") or "", pdf=((p.get("openAccessPdf") or {}).get("url") or ""),
            sources=["s2"], queries=[query] if query else [])

    def search(self, query: str, limit: int = 10, year_from: Optional[int] = None) -> list[Paper]:
        params = {"query": query, "limit": limit, "fields": self.FIELDS}
        if year_from:
            params["year"] = f"{year_from}-"
        d = self._get("/graph/v1/paper/search", params)
        return [self._to_paper(p, query) for p in (d or {}).get("data", [])]

    def paper(self, ident: str) -> Optional[Paper]:
        d = self._get(f"/graph/v1/paper/{ident}", {"fields": self.FIELDS})
        return self._to_paper(d) if d else None

    def recommendations(self, arxiv_id: str, limit: int = 10) -> list[Paper]:
        d = self._get(f"/recommendations/v1/papers/forpaper/arXiv:{arxiv_id}",
                      {"limit": limit, "fields": self.FIELDS})
        return [self._to_paper(p) for p in (d or {}).get("recommendedPapers", [])]


# --------------------------------------------------------------------------- #
class HFClient:
    """HuggingFace Papers: arXiv indexed within a day; abstract + AI summary/keywords."""
    BASE = "https://huggingface.co/api/papers"

    def __init__(self):
        self.ok = reachable("huggingface.co")

    def _get(self, url: str, params: dict | None = None) -> Any:
        for attempt in range(3):
            try:
                r = requests.get(url, params=params, timeout=25, headers={"Accept": "application/json"})
                if r.status_code == 200:
                    return r.json()
                if r.status_code == 404:
                    return None
            except requests.RequestException:
                pass
            time.sleep(1.5 * (attempt + 1))
        return None

    @staticmethod
    def _to_paper(p: dict, query: str = "") -> Paper:
        p = p.get("paper", p)
        return Paper(id="arxiv:" + p.get("id", ""), title=p.get("title") or "",
                     abstract=" ".join((p.get("summary") or "").split()),
                     tldr=" ".join((p.get("ai_summary") or "").split()),
                     date=(p.get("publishedAt") or "")[:10],
                     year=int((p.get("publishedAt") or "0000")[:4]) or None,
                     arxiv=p.get("id", ""), url=f"https://huggingface.co/papers/{p.get('id','')}",
                     sources=["hf"], queries=[query] if query else [],
                     keywords=list(p.get("ai_keywords") or []))

    def search(self, query: str, limit: int = 12) -> list[Paper]:
        d = self._get(f"{self.BASE}/search", {"q": query, "limit": limit}) if self.ok else None
        return [self._to_paper(p, query) for p in (d or [])[:limit]]

    def paper(self, arxiv_id: str) -> Optional[Paper]:
        d = self._get(f"{self.BASE}/{arxiv_id}") if self.ok else None
        return self._to_paper(d) if d else None


# --------------------------------------------------------------------------- #
class OpenAlexClient:
    """Implemented for unrestricted nodes; blocked here (probe decides)."""
    def __init__(self, mailto: str = "research@example.org"):
        self.ok = reachable("api.openalex.org")
        self.mailto = mailto

    @staticmethod
    def _abstract(inv: dict | None) -> str:
        if not inv:
            return ""
        pos = sorted((i, w) for w, idxs in inv.items() for i in idxs)
        return " ".join(w for _, w in pos)

    def search(self, query: str, limit: int = 10, year_from: Optional[int] = None) -> list[Paper]:
        if not self.ok:
            return []
        params = {"search": query, "per-page": limit, "mailto": self.mailto}
        if year_from:
            params["filter"] = f"from_publication_date:{year_from}-01-01"
        try:
            r = requests.get("https://api.openalex.org/works", params=params, timeout=25)
            d = r.json() if r.status_code == 200 else {}
        except requests.RequestException:
            return []
        out = []
        for w in d.get("results", []):
            ids = w.get("ids") or {}
            arx = ""
            for loc in (w.get("locations") or []):
                u = (loc.get("landing_page_url") or "")
                m = re.search(r"arxiv\.org/abs/([0-9.]+)", u)
                if m:
                    arx = m.group(1); break
            out.append(Paper(id=("arxiv:" + arx) if arx else ("openalex:" + w.get("id", "")),
                             title=w.get("display_name") or "", abstract=self._abstract(w.get("abstract_inverted_index")),
                             year=w.get("publication_year"), date=w.get("publication_date") or "",
                             venue=((w.get("primary_location") or {}).get("source") or {}).get("display_name") or "",
                             citations=w.get("cited_by_count"), arxiv=arx,
                             doi=(ids.get("doi") or "").replace("https://doi.org/", ""), url=w.get("id", ""),
                             sources=["openalex"], queries=[query]))
        return out


class ArxivClient:
    """arXiv export API; blocked here (probe decides)."""
    def __init__(self):
        self.ok = reachable("export.arxiv.org")

    def search(self, query: str, limit: int = 10) -> list[Paper]:
        if not self.ok:
            return []
        try:
            r = requests.get("https://export.arxiv.org/api/query",
                             params={"search_query": f"all:{query}", "max_results": limit,
                                     "sortBy": "submittedDate", "sortOrder": "descending"}, timeout=25)
        except requests.RequestException:
            return []
        out = []
        for entry in re.findall(r"<entry>(.*?)</entry>", r.text, re.S):
            g = lambda tag: (re.search(rf"<{tag}>(.*?)</{tag}>", entry, re.S) or [None, ""])[1]
            aid = re.sub(r".*/abs/", "", g("id")).strip()
            out.append(Paper(id="arxiv:" + re.sub(r"v\d+$", "", aid), title=" ".join(g("title").split()),
                             abstract=" ".join(g("summary").split()), date=g("published")[:10],
                             year=int(g("published")[:4] or 0) or None, arxiv=re.sub(r"v\d+$", "", aid),
                             url=f"https://arxiv.org/abs/{aid}", sources=["arxiv"], queries=[query]))
        return out


# --------------------------------------------------------------------------- #
class SectionReader:
    """Return {"limitations":..., "conclusion":..., "method":...} for an arXiv id.

    Order: arXiv HTML → ar5iv → (unreachable) emit a WebSearch job for the harness.
    """
    SECTION_PATTERNS = {
        "limitations": r"(limitation|limitations|broader impact|future work)",
        "conclusion": r"(conclusion|conclusions|discussion)",
        "method": r"(method|methods|approach|methodology)",
    }

    def __init__(self, jobs_dir: str | None = None):
        self.html_ok = reachable("arxiv.org")
        self.ar5iv_ok = reachable("ar5iv.labs.arxiv.org")
        self.jobs_dir = jobs_dir

    @classmethod
    def parse_html(cls, html: str, max_words: int = 600) -> dict:
        text = re.sub(r"<script.*?</script>|<style.*?</style>", " ", html, flags=re.S)
        heads = list(re.finditer(r"<h[1-3][^>]*>(.*?)</h[1-3]>", text, re.S | re.I))
        out = {}
        for i, h in enumerate(heads):
            title = re.sub(r"<[^>]+>", "", h.group(1)).strip().lower()
            for name, pat in cls.SECTION_PATTERNS.items():
                if name in out or not re.search(pat, title):
                    continue
                end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
                body = re.sub(r"<[^>]+>", " ", text[h.end():end])
                body = re.sub(r"\s+", " ", body).strip()
                out[name] = " ".join(body.split()[:max_words])
        return out

    def read(self, arxiv_id: str) -> dict:
        urls = []
        if self.html_ok:
            urls.append(f"https://arxiv.org/html/{arxiv_id}")
        if self.ar5iv_ok:
            urls.append(f"https://ar5iv.labs.arxiv.org/html/{arxiv_id}")
        for u in urls:
            try:
                r = requests.get(u, timeout=30)
                if r.status_code == 200 and "<h" in r.text:
                    sec = self.parse_html(r.text)
                    if sec:
                        sec["_source"] = u
                        return sec
            except requests.RequestException:
                continue
        return {"_source": "unreachable", "_job": self.websearch_job(arxiv_id)}

    def websearch_job(self, arxiv_id: str) -> dict:
        """Job spec for a harness subagent with WebSearch (server-side, not firewalled)."""
        job = {
            "kind": "section_read", "arxiv": arxiv_id, "tools": ["WebSearch"], "model": "opus",
            "prompt": (f"Using WebSearch only (at most 4 searches), find the text of the Limitations / Future work "
                       f"and Conclusion sections of arXiv:{arxiv_id}, and one sentence stating its method. Search "
                       f"'arxiv {arxiv_id} limitations', 'arxiv {arxiv_id} conclusion', and the paper title. Return "
                       f"ONLY JSON: {{\"arxiv\": \"{arxiv_id}\", \"limitations\": \"<=250 words or 'not found'\", "
                       f"\"conclusion\": \"<=200 words or 'not found'\", \"method\": \"one sentence\", "
                       f"\"sources\": [urls]}}. Quote or closely paraphrase; do not invent."),
        }
        if self.jobs_dir:
            os.makedirs(self.jobs_dir, exist_ok=True)
            with open(os.path.join(self.jobs_dir, f"section_{arxiv_id.replace('/', '_')}.json"), "w") as f:
                json.dump(job, f, indent=1)
        return job


# --------------------------------------------------------------------------- #
def dedupe(papers: list[Paper]) -> list[Paper]:
    seen: dict[str, Paper] = {}
    for p in papers:
        k = p.key()
        if k in seen:
            q = seen[k]
            q.sources = sorted(set(q.sources + p.sources)); q.queries = sorted(set(q.queries + p.queries))
            q.axes = sorted(set(q.axes + p.axes))
            for f in ("abstract", "tldr", "venue", "date", "doi", "pdf", "url"):
                if not getattr(q, f) and getattr(p, f):
                    setattr(q, f, getattr(p, f))
            if q.citations is None and p.citations is not None:
                q.citations = p.citations
            if not q.keywords and p.keywords:
                q.keywords = p.keywords
        else:
            seen[k] = p
    return list(seen.values())


def recency_score(date: str, today: str | None = None, half_life_days: int = 365) -> float:
    if not date:
        return 0.2
    try:
        from datetime import date as D
        y, m, d = (int(x) for x in date[:10].split("-"))
        t = D.fromisoformat(today) if today else D.today()
        age = (t - D(y, m, d)).days
    except Exception:
        return 0.2
    if age <= 365:
        return 1.0
    return 0.5 ** ((age - 365) / half_life_days)


def rank(papers: list[Paper], today: str | None = None) -> list[Paper]:
    import math
    def score(p: Paper) -> float:
        cit = math.log1p(p.citations or 0) / math.log1p(500)
        rank_bonus = min(len(p.queries), 3) / 3.0
        return 0.5 * recency_score(p.date or (f"{p.year}-06-30" if p.year else ""), today) + 0.3 * min(cit, 1.0) + 0.2 * rank_bonus
    return sorted(papers, key=score, reverse=True)


def save_jsonl(papers: list[Paper], path: str) -> None:
    with open(path, "w") as f:
        for p in papers:
            f.write(json.dumps(asdict(p), ensure_ascii=False) + "\n")


def load_jsonl(path: str) -> list[Paper]:
    return [Paper(**json.loads(l)) for l in open(path) if l.strip()]


if __name__ == "__main__":
    import sys
    q = " ".join(sys.argv[1:]) or "agent memory prompt optimization"
    s2, hf = S2Client(), HFClient()
    print("S2 reachable:", s2.ok, "pin:", s2.pin_ip, "| key:", "yes" if s2.key else "no", "| HF:", hf.ok)
    ps = dedupe(s2.search(q, 5, year_from=2025) + hf.search(q, 5))
    for p in rank(ps):
        print(f"  {p.date or p.year} {str(p.citations):>4} {'/'.join(p.sources):5s} {p.id:16s} {p.title[:70]}")
