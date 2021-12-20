import requests

#

queue_id = ""
subdomain = "company"

url = f"https://{subdomain}.zendesk.com/api/v2/views/{queue_id}/tickets"

payload = {}
headers = {
    'Authorization': ''
}

response = requests.get(url, headers=headers, data=payload)

print(response.text)
