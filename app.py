#!/usr/bin/env python3
class HealthChecker:
    def check_services(self):
        services = ["database", "redis", "api"]
        results = {s: "UP" if s != "redis" else "degraded" for s in services}
        return results
if __name__ == "__main__":
    print("Health Check:", HealthChecker().check_services())
