# Week 1 — Python for AI engineers

Goal: write typed Python you can trust before you call any LLM.

## Setup

```bash
cd week-01-python-foundations
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## This week you will build

1. A typed CLI: `ops-ingest path/to/file.json|csv`
2. Pydantic models that reject bad rows instead of silently passing them
3. Ten pytest tests (happy path + failures)
4. An HTTP client with retries/timeouts (Sunday)

## Definition of done

- [ ] `pytest` passes with at least 10 tests
- [ ] CLI prints validated JSON or a clear validation error
- [ ] You can explain every control-flow branch without reading the file
- [ ] Short note in this README: one thing that broke and how you fixed it

## What broke / what I learned

_Fill this in on Sunday._
