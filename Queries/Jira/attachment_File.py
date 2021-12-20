import requests

# attachment files

subdomain = "company"
key = "TECH-001"

url = f"https://{subdomain}.atlassian.net/rest/api/3/issue/{key}/attachments"

payload = {}
files = [
    ('file', ('file_name.json', open('/home/user/file.json', 'rb'), 'application/json'))
]
headers = {
    'X-Atlassian-Token': 'no-check',
    'Authorization': '',
    'Cookie': ''
}

response = requests.post(url, headers=headers, data=payload, files=files)

print(response.text)
