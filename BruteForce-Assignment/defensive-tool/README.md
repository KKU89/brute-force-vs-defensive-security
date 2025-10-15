Defensive Tool — Rate Limiter & Account Lockout

This is a simple Python Flask server that protects a login page from brute force attacks.

What It Does:

- Tracks failed login attempts for each user or IP address.
- If someone enters the wrong password 3 times, their account is locked for 1 minute.
- Shows a lockout message on the web page and sends a special error code (429) for scripts.

How to Use:

1. Open a terminal in this folder.
2. Install Flask:
pip install flask
3. Run the server:
4. Open [http://127.0.0.1:5001/](http://127.0.0.1:5001/) in your browser.
5. Try logging in with wrong passwords to see the lockout in action.

NOTE:-This tool is for lab/demo use only. Do not use it on real websites.

