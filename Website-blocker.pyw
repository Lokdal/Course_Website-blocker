import datetime
import time
import json

# Read the settings from the file. Note that the demo_version argument should
# be set to True unless you truly want to modify your system's host file.

with open("settings.txt", "r") as tFile:
    iSettings = json.load(tFile)
    if iSettings["demo_version"]:
        gHostsPath = "demo_hosts"
    else:
        gHostsPath = "C:\\Windows\\System32\\drivers\\etc\\hosts"
    gStartTime = datetime.time(int(iSettings["start_hour"]),
                               int(iSettings["start_minutes"]))
    gEndTime = datetime.time(int(iSettings["end_hour"]),
                             int(iSettings["end_minutes"]))
    gHome = iSettings["home_IP"]

with open("sites.txt", "r") as tFile:
    gWebsites = []
    for line in tFile:
        gWebsites.append(gHome + " " + line)
    gWebsites[-1] = gWebsites[-1] + "\n"

while True:
    tNow = datetime.datetime.now()
    if (gStartTime <= tNow.time() < gEndTime):
        with open(gHostsPath, "r+") as tHosts:
            tContent = tHosts.readlines()
            for w in gWebsites:
                if w not in tContent:
                    tHosts.write(w)
        tTimeEnd = datetime.datetime(tNow.year, tNow.month, tNow.day,
                                     gEndTime.hour, gEndTime.minute)
    else:
        with open(gHostsPath, "r+") as tHosts:
            tContent = tHosts.readlines()
            tHosts.seek(0)
            for c in tContent:
                if c not in gWebsites:
                    tHosts.write(c)
            tHosts.truncate(tHosts.tell())
        tTimeEnd = datetime.datetime(tNow.year, tNow.month, tNow.day + 1,
                                     gStartTime.hour, gStartTime.minute)

# The behavior of the next two while loops aims to provide resilience
# to system hybernation and sleep. In the worst case scenario, which is very
# unlikely, the user will have to wait 5 minutes past gEndTime.

    while (tTimeEnd - datetime.datetime.now()).total_seconds() > 295:
        time.sleep(300)
    while (tTimeEnd - datetime.datetime.now()).total_seconds() > 55:
        time.sleep(60)
    while (tTimeEnd - datetime.datetime.now()).total_seconds() > 5:
        time.sleep(10)
