from datetime import datetime
import time

gStartHour = 10
gEndHour = 17
gHostsPath = "C:\\Windows\\System32\\drivers\\etc\\hosts"
gHome = "127.0.0.1"
gWebsites = ["facebook.com", "www.facebook.com"]
gLines = []
for w in gWebsites:
    gLines.append(gHome + " " + w + "\n")

while True:
    tNow = datetime.now()
    if (gStartHour <= tNow.hour < gEndHour):
        with open(gHostsPath, "r+") as gHost:
            tContent = gHost.readlines()
            for l in gLines:
                if l not in tContent:
                    gHost.write(l)
        tTimeEnd = datetime(tNow.year, tNow.month, tNow.day, gEndHour)
    else:
        with open(gHostsPath, "r+") as gHost:
            tContent = gHost.readlines()
            gHost.seek(0)
            for c in tContent:
                if c not in gLines:
                    gHost.write(c)
            gHost.truncate(gHost.tell())
        tTimeEnd = datetime(tNow.year, tNow.month, tNow.day + 1, gStartHour)

    while (tTimeEnd - datetime.now()).total_seconds() > 295:
        time.sleep(300)
    while (tTimeEnd - datetime.now()).total_seconds() > 5:
        time.sleep(60)
