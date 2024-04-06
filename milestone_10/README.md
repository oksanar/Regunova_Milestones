# Milestone 10

## Set environment

```bash
python3 -m venv .venv
. .venv/bin/activate
pip3 install -r requirements.txt
```

# Testing

Add project to PYTHONPATH:

```bash
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

Run unit tests:

```bash
python3 test/server_unit_tests.py
python3 test/fetch_report_unit_tests.py
```
