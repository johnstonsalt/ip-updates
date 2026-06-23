import time
import requests
import os

known = ""
kr = requests.get("https://raw.githubusercontent.com/johnstonsalt/ip-updates/refs/heads/main/README.md")
known = kr.text.replace("\n", "").replace("# ", "")

while 1:
    actual = ""
    failed = False

    try:
        r = requests.get("http://api.ipify.org")
        actual = r.text
    except:
        print("failed to get actual IP address")
        failed = True

    if failed == False:
        if actual != known:
            print(f"\nNew public IP address: {known} -> {actual}\n")

            with open("README.md", "w") as f:
                f.write(f"# {actual}")
            f.close()

            os.system("git add .; git commit -m \"new IP\"; git push origin main")
            known = actual
 
    time.sleep(60)

# if you're seeing this, text John the number 420!
