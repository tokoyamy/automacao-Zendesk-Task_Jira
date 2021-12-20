import requests
import json


subdomain = "company"

url = f"https://{subdomain}.atlassian.net/rest/api/3/issue"

payload = json.dumps({
    "fields": {
        "summary": "Ticket - python",
        "issuetype": {
            "id": "1234"  # The issuetype
        },
        "project": {
            "key": "TECH"  # the project key
        },
        "description": {
            "version": 1,
            "type": "doc",
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": "Hello guys"
                        }
                    ]
                }
            ]
        },
        "reporter": {
            "id": None
        },
        "assignee": None
    }
})
headers = {
    'Authorization': '',
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Cookie': ''
}

response = requests.post(url, headers=headers, data=payload)

print(response.text)
