import requests

url = "https://api.github.com/user"
headers = {
    "Authorization": "token YOUR_PERSONAL_ACCESS_TOKEN",
    "Accept": "application/vnd.github.v3+json"
}

response = requests.get(url, headers=headers)

# Check the status code first
print(f"Status Code: {response.status_code}")

# Print the raw response text to see what is being returned
print(f"Response Text: {response.text}")
