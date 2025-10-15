from flask import Flask, request, render_template_string
import time

app = Flask(__name__)

# In-memory failed attempts tracker
attempts = {}

LOCKOUT_THRESHOLD = 3  # 3 galat attempts allowed
LOCKOUT_TIME = 60      # 1 minute lockout

LOGIN_PAGE = '''
<form method="POST" action="/login">
  Username: <input name="username"><br>
  Password: <input name="password" type="password"><br>
  <input type="submit" value="Login">
</form>
{% if msg %}<p>{{ msg }}</p>{% endif %}
'''

@app.route("/", methods=["GET"])
def root():
    return render_template_string(LOGIN_PAGE, msg=None)

@app.route("/login", methods=["GET", "POST"])
def login():
    ip = request.remote_addr
    username = request.form.get("username", "")
    password = request.form.get("password", "")

    key = username or ip
    now = time.time()

    # Purane lockout hatao
    if key in attempts and now - attempts[key][0] > LOCKOUT_TIME:
        attempts.pop(key)

    # Agar lockout hai
    if key in attempts and attempts[key][1] >= LOCKOUT_THRESHOLD:
        msg = "Account Locked: Too many failed attempts. Try after 1 min."
        return render_template_string(LOGIN_PAGE, msg=msg), 429

    # Login attempt
    if password == "admin":
        attempts.pop(key, None)
        return render_template_string(LOGIN_PAGE, msg="Login successful!"), 200
    else:
        if key not in attempts:
            attempts[key] = [now, 1]
        else:
            attempts[key][1] += 1
            attempts[key][0] = now
        if attempts[key][1] >= LOCKOUT_THRESHOLD:
            msg = "Account Locked: Too many failed attempts. Try after 1 min."
            return render_template_string(LOGIN_PAGE, msg=msg), 429
        else:
            msg = f"Login failed! Attempt {attempts[key][1]}/{LOCKOUT_THRESHOLD}"
            return render_template_string(LOGIN_PAGE, msg=msg), 401

if __name__ == "__main__":
    app.run(debug=True, port=5001)
