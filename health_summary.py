import openai

client = openai.OpenAI(api_key = "api-key")

server_health_report = """
Server: Prod-Server-01
CPU Usage: 87%
Memory Usage: 92%
Disk Usage: 73%
SSL Certificate: Expires in 10 days
Uptime: 99.9%
Recent Errors: 12x HTTP 500 in last hour
"""

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful DevOps assistant."},
        {"role": "user", "content": "Summarise the following server health report:\n\nCPU: 87%\nMemory: 92%\nDisk: 73%\nSSL: Expires in 10 days\nErrors: 12 HTTP 500s"}
    ]
)

print("AI Generated Summary")
print(response['choices'][0]['message']['content'])