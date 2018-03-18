# boot.py -- run on boot-up
import os
import machine
uart = machine.UART(0, 115200)
os.dupterm(uart)

