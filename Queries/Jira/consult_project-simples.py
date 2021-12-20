import requests


projectIdOrKey = ""

url = f"https://your-domain.atlassian.net/rest/api/3/project/{projectIdOrKey}"

payload = {}
headers = {
    'Authorization': '',
    'Cookie': ''
}

response = requests.get(url, headers=headers, data=payload)

print(response.text)
