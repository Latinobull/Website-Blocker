import time
from datetime import datetime as dt

host_temp = "hosts"
hosts_path_Windows = "C:\Windows\System32\drivers\etc\hosts"
host_path_Mac = "/etc/hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com", "www.twitter.com", "twitter.com"]

while True:
    if (
        dt(dt.now().year, dt.now().month, dt.now().day, 8)
        < dt.now()
        < dt(dt.now().year, dt.now().month, dt.now().day, 16)
    ):
        print("Working Hours")
        with open(hosts_path_Windows, "r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        print("Party Hours!!")
        with open(hosts_path_Windows, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(5)