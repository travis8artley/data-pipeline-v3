from typing import Iterable

def fetch_sources(urls: Iterable[str]) -> list[dict]:
    return [{"url": u, "status": "fetched"} for u in urls]
