# Architecture

```mermaid
flowchart LR
  A["Source URLs"] --> B["ingest.fetch_sources"]
  B --> C["transform.normalize"]
  C --> D["transform.schema.validate"]
  D --> E["load.write_json"]
```

## Design Notes

- Stage isolation keeps failures localized and debuggable.
- Validation runs before sink writes to avoid partial bad output.
- Pipeline function returns records so callers can chain downstream work.
