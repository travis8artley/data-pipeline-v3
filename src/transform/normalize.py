def normalize(records: list[dict]) -> list[dict]:
    return [{k.lower(): v for k, v in r.items()} for r in records]
