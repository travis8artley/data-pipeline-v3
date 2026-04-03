import json
from pathlib import Path

def write_json(path: str, rows: list[dict]) -> None:
    Path(path).write_text(json.dumps(rows, indent=2), encoding='utf-8')
