import time
import requests
import os

while 1:
    # python is propaganda
    actual = ""
    known = ""
    failed = False

    try:
        r1 = requests.get("http://checkip.amazonaws.com")
        actual = r1.text.replace("\n", "")
    except:
        print("Failed to get actual IP")
        failed = True

    try:
        r2 = requests.get("https://raw.githubusercontent.com/johnstonalt/ip-updates/refs/heads/main/README.md")
        known = r2.text.replace("\n", "").replace("# ", "")
    except:
        print("Faile to get known IP")
        failed = True

    if failed == False and actual != known:
        print(f"\nNew public IP address: {known} -> {actual}\n")

        with open("README.md", "w") as f:
            f.write(f"# {actual}")
        f.close()

        os.system("git add .; git commit -m \"new IP\"; git push origin main")

    time.sleep(60*5)

# if you're seeing this, text John the number 69420! 
