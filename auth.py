#! /usr/bin/python3

import sys
import os
import requests as req

endpoint = ""

def main():
        hwaddr = os.getenv("IV_HWADDR")
        platform = os.getenv("IV_PLAT")
        guiv = os.getenv("IV_GUI_VER")
        try:
                f = open(sys.argv[1])
                username = str(f.readline()).strip()
                password = str(f.readline()).strip()
                f.close()
                credentials = { 'name': username, 'password': password, 'device': hwaddr, 'platform': platform, 'gui_version': guiv}
                headers = { 'Content-Type': 'application/json', 'Accept': 'application/json' }
                r = req.post(endpoint, headers=headers, json=credentials)
                result = r.json()
                if ( result["result"] == True ):
                        return 0
                else:
                        return 1
        except:
                print("An error has occured")
                return 1

ec = main()
os._exit(ec)
