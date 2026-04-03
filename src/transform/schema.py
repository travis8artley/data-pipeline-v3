REQUIRED_KEYS = {"url", "status"}


def validate(records: list[dict]) -> None:
    for idx, record in enumerate(records):
        missing = REQUIRED_KEYS - set(record.keys())
        if missing:
            raise ValueError(f"record {idx} missing keys: {sorted(missing)}")
