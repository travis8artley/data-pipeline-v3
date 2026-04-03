import json
import tempfile
from pathlib import Path

from src.pipeline.run_pipeline import run
from src.transform.schema import validate


def test_run_pipeline_writes_output():
    with tempfile.TemporaryDirectory() as td:
        output = Path(td) / "out.json"
        rows = run(["https://example.com/a", "https://example.com/b"], str(output))
        validate(rows)
        persisted = json.loads(output.read_text(encoding="utf-8"))
        assert len(persisted) == 2
        assert persisted[0]["status"] == "fetched"


def test_schema_validation_rejects_missing_fields():
    try:
        validate([{"url": "x"}])
    except ValueError:
        return
    raise AssertionError("expected ValueError")
