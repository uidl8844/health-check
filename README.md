# health-check

Probe HTTP URLs and TCP hosts. Exit 1 if any check fails.

```bash
python -m health_check --http http://127.0.0.1:8080/health --tcp 127.0.0.1:22
```
