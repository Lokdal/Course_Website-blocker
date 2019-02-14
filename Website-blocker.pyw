from datetime import datetime
import time
import json


with open("settings.txt", "r") as tFile:
    iSettings = json.load(tFile)
    if iSettings["demo_version"]:
        gHostsPath = "demo_hosts"
    else:
        gHostsPath = "C:\\Windows\\System32\\drivers\\etc\\hosts"
    gStartHour = int(iSettings["start_hour"])
    gEndHour = int(iSettings["end_hour"])

gWebsites = []
gHome = "127.0.0.1"

with open("sites.txt", "r") as tFile:
    for line in tFile:
        gWebsites.append(gHome + " " + line)
    gWebsites[-1] = gWebsites[-1] + "\n"


while True:
    tNow = datetime.now()
    if (gStartHour <= tNow.hour < gEndHour):
        with open(gHostsPath, "r+") as tHosts:
            tContent = tHosts.readlines()
            for l in gWebsites:
                if l not in tContent:
                    tHosts.write(l)
        tTimeEnd = datetime(tNow.year, tNow.month, tNow.day, gEndHour)
    else:
        with open(gHostsPath, "r+") as tHosts:
            tContent = tHosts.readlines()
            tHosts.seek(0)
            for c in tContent:
                if c not in gWebsites:
                    tHosts.write(c)
            tHosts.truncate(tHosts.tell())
        tTimeEnd = datetime(tNow.year, tNow.month, tNow.day + 1, gStartHour)

    while (tTimeEnd - datetime.now()).total_seconds() > 295:
        time.sleep(300)
    while (tTimeEnd - datetime.now()).total_seconds() > 5:
        time.sleep(60)
