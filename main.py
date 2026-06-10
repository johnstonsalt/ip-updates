import time
import requests
import os

while 1:
    actual = requests.get("https://ipinfo.io/").json()["ip"]
    known = requests.get("https://raw.githubusercontent.com/johnstonalt/ip-updates/refs/heads/main/README.md").text.replace("\n", "").replace("# ", "")

    if actual != known:
        print(f"New public IP address: {known} -> {actual}")

        with open("README.md", "w") as f:
            f.write(f"# {actual}")
        f.close()

        os.system("git add .; git commit -m \"new IP\"; git push origin main")

    time.sleep(60*5)

# if you're seeing this, text John the number 69420! 
