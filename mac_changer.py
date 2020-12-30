#!/usr/bin/env python3

import subprocess

interface = "wlan0"
new_mac = "00:1:22:33:44:77"

print("[+] Changing MAC address for " + interface + " to " + new_mac)

subprocess.call("ifconfig " + interface " down", shell=True)  # the true allows to run Linux commands through function
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + "up", shell=True)
