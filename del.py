import requests

headers = {
    "Authorization": "token YOUR_PERSONAL_ACCESS_TOKEN",
    "Accept": "application/vnd.github.v3+json"
}

url = "https://api.github.com/repos/YOUR_USERNAME/new-repo"
response = requests.delete(url, headers=headers)
print(response.status_code)  # Should return 204 if deletion is successful
