import openai

openai.api_key = "api-key"

server_health_report = """
Server: Prod-Server-01
CPU Usage: 87%
Memory Usage: 92%
Disk Usage: 73%
SSL Certificate: Expires in 10 days
Uptime: 99.9%
Recent Errors: 12x HTTP 500 in last hour
"""
prompt = f"Summarize the following server health report: {server_health_report}"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful DevOps assistant."},
        {"role": "user", "content": prompt}
    ]
)

print("AI Generated Summary")
print(response.choices[0].message.content)