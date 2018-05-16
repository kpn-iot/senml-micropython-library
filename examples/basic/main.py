# _  __  ____    _   _ 
# | |/ / |  _ \  | \ | |
# | ' /  | |_) | |  \| |
# | . \  |  __/  | |\  |
# |_|\_\ |_|     |_| \_|
# 
# (c) 2018 KPN
# License: GNU General Public License v3.0.
# Author: Jan Bogaerts
# 
# basic example

from kpn_senml import *
import utime as time


pack = SenmlPack("device")

while True:
    with SenmlRecord("test", value=1) as rec:           # use a with statement to automatically remove the item from the list when it goes out of scope
        pack.add(rec)
        print(pack.to_json())
    time.sleep(1)

