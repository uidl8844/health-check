from __future__ import annotations
from dataclasses import dataclass, asdict
import socket
import urllib.error
import urllib.request

@dataclass
class Check:
    name: str
    ok: bool
    detail: str

def http_ok(url: str, timeout: float = 3.0, expect: int = 200) -> Check:
    try:
        req = urllib.request.Request(url, method="GET")
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            code = getattr(resp, "status", 200)
            ok = code == expect
            return Check(url, ok, f"status {code}")
    except Exception as e:
        return Check(url, False, str(e))

def tcp_ok(host: str, port: int, timeout: float = 2.0) -> Check:
    s = socket.socket()
    s.settimeout(timeout)
    try:
        s.connect((host, port))
        return Check(f"{host}:{port}", True, "open")
    except Exception as e:
        return Check(f"{host}:{port}", False, str(e))
    finally:
        s.close()

def report(checks: list[Check]) -> dict:
    return {"ok": all(c.ok for c in checks), "checks": [asdict(c) for c in checks]}
