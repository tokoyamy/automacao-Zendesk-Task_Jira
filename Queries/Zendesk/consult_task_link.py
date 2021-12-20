import requests

Ticket_id = "1234"
subdomain = "company"

url = f"https://{subdomain}.zendesk.com/api/services/jira/links/?ticket_id={Ticket_id}"

payload = ""
headers = {
    'Authorization': ' '
}

response = requests.get(url, headers=headers, data=payload)

print(response.text)
