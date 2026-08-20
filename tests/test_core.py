from health_check import tcp_ok, report, http_ok

def test_tcp_closed():
    c = tcp_ok("127.0.0.1", 1, timeout=0.2)
    assert c.ok is False

def test_report_fail():
    r = report([tcp_ok("127.0.0.1", 1, timeout=0.2)])
    assert r["ok"] is False
