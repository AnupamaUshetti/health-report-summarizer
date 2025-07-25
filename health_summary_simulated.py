server_health_report = """
Server: Prod-Server-01
CPU Usage: 87%
Memory Usage: 92%
Disk Usage: 73%
SSL Certificate: Expires in 10 days
Uptime: 99.9%
Recent Errors: 12x HTTP 500 in last hour
"""

simulated_ai_summary = """
AI-Generated Summary

-> CPU and Memory usage are high (87%, 92%) — consider scaling or investigating heavy processes.
-> SSL Certificate expires in 10 days — renew it to avoid service interruption.
-> 12 HTTP 500 errors detected — check backend application logs.
-> Disk usage is moderate (73%) — monitor regularly.
-> Uptime is stable at 99.9% — no immediate concerns.
"""

print("{Server Health Report}")
print(server_health_report)

print("{AI Summary}")
print(simulated_ai_summary)