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
# supported datatypes example

# boot.py -- run on boot-up
import os
import machine
uart = machine.UART(0, 115200)
os.dupterm(uart)

