#!/usr/bin/env python3

import subprocess

subprocess.call("ifconfig", shell=True)  # the true allows to run Linux commands through function