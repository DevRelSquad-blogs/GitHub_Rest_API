import requests

headers = {
    "Authorization": "token YOUR_PERSONAL_ACCESS_TOKEN",
    "Accept": "application/vnd.github.v3+json"
}

url = "https://api.github.com/repos/YOUR_USERNAME/new-repo/issues"
data = {
    "title": "Issue Title",
    "body": "Issue description."
}
response = requests.post(url, headers=headers, json=data)
print(response.json())
