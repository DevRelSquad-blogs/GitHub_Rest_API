import requests

headers = {
    "Authorization": "token YOUR_PERSONAL_ACCESS_TOKEN",
    "Accept": "application/vnd.github.v3+json"
}

url = "https://api.github.com/user/repos"
data = {
    "name": "new-repo",
    "private": False
}
response = requests.post(url, headers=headers, json=data)
print(response.json())
