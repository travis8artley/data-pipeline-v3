from ingest.fetch_sources import fetch_sources
from transform.normalize import normalize
from load.write_json import write_json


def run(urls: list[str], output_path: str) -> list[dict]:
    fetched = fetch_sources(urls)
    normalized = normalize(fetched)
    write_json(output_path, normalized)
    return normalized
