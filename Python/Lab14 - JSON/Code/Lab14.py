#!/usr/bin/env python3
import sys
import json
import urllib.request

url = "https://ipinfo.io/" + sys.argv[0] + "/json"
print(url)
with urllib.request.urlopen(url) as response:

    myDict = json.loads(response.read().decode())

try:
    outputHostname  = f"Hostname  :{myDict['hostname']}\n"
    outputCity      = f"City      :{myDict['city']}\n"
    outputRegion    = f"Region     :{myDict['region']}\n"
    outputCountry   = f"Country    :{myDict['country']}\n"
    outputLoc       = f"Loc        :{myDict['loc']}\n"
    outputPostal    = f"Postal     :{myDict['postal']}\n"
    outputPhone     = f"Phone      :{myDict['phone']}\n"
    outputOrg       = f"Org        :{myDict['org']}\n"
    output = f"{outputHostname}{outputCity}{outputRegion}   {outputCountry}{outputLoc}{outputPostal}{outputPhone}{outputOrg}"

    print(output)
except:
    output = f"IP Address: {myDict['ip']}\n"
    print(output)