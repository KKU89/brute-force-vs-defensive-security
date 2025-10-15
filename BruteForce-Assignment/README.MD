Offensive vs Defensive Security — Group Assignment

Welcome to our cybersecurity assignment!  
Here, we show how a simple brute force attack works—and how a smart defense can stop it.

What’s Inside:

-offensive-tool:
  Our brute force script. It tries lots of passwords on a test login page, just like a real attacker would.

-defensive-tool: 
  Our defense: a Flask server that blocks anyone who fails to log in too many times. After three wrong tries, you’re locked out for a minute!

-Name-Teams.txt: 
  Who did what in our group.

-Name-Proposal.pdf:
  Our project plan and attack/defense idea.


How to Try It Yourself:-

1. Go to the `defensive-tool` folder and start the server:
2. Open your browser at [http://127.0.0.1:5001/](http://127.0.0.1:5001/) and try logging in.
3. In another terminal, run the brute force script from `offensive-tool`:
4. Watch how the server blocks repeated failed logins!

 Why We Did This:

-Offensive:
Shows how easy it is to break weak passwords with a simple script.

-Defensive: 
Proves that even basic protections (like rate limiting and lockouts) can stop brute force attacks.

Notes:

- This project is for learning only.  
- Please don’t use these scripts on real websites or outside your lab.

---

Made by our team for Application and Data Security.



