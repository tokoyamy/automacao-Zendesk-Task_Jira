import requests
import json

# Link jira issue in zendesk

subdomain = "company"

url = f"https://{subdomain}.zendesk.com/api/services/jira/links"

payload = json.dumps({
    "link": {
        "ticket_id": 1234,
        "issue_id": 1234,
        "issue_key": "TECH-001"
    }
})
headers = {
    'Content-Type': 'application/json',
    'Authorization': ' '
}

response = requests.post(url, headers=headers, data=payload)

print(response.text)
