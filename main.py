import time
import requests
import os

while 1:
    r1 = requests.get("https://ipinfo.io/")
    r2 = requests.get("https://raw.githubusercontent.com/johnstonalt/ip-updates/refs/heads/main/README.md")

    try:
        actual = r1.json()["ip"]
        known = r2.text.replace("\n", "").replace("# ", "")
    except:
        print(f"recieved bad response\nrequest to get actual IP returned:\n{r1.text}\n\nresponse to get known IP returned:\n{r2.text}")

    if actual != known:
        print(f"\nNew public IP address: {known} -> {actual}\n")

        with open("README.md", "w") as f:
            f.write(f"# {actual}")
        f.close()

        os.system("git add .; git commit -m \"new IP\"; git push origin main")

    time.sleep(60*5)

# if you're seeing this, text John the number 69420! 
