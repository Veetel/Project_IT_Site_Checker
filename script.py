import requests
import datetime
import os

ci = os.environ.get("CI") == "true"
if ci :
    urls =["https://google.com", "https://github.com" , "https://invalid.tld"]
else:
    user_input = input("Enter website URLs separated by commas: \n")
    urls = [] 

    ## url.strip cut spaces around urls

    for raw_url in user_input.split(","):
        url = raw_url.strip()
        if not url.startswith("https://") and not url.startswith("http://"):
            url = "https://" + url

        urls.append(url)


with open("log.txt","a") as file : ## Open a file and auto close it. Sililar to open() and close()
    for url in urls:
            
        try:
            response = requests.get(url)
            if response.status_code == 200:
                status =f"{url} is reachable"
            else :
                status =f"{url} send status code {response.status_code}"

            
        except requests.exceptions.RequestException as exception:
            status = f"{url} unreachable "

        logLine = f"[{datetime.datetime.now()}] {status}"
        print(logLine)
        file.write(logLine + "\n")