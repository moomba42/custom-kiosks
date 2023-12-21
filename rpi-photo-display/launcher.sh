#!/bin/sh

cd /home/adlugosz/custom-kiosks-main/rpi-photo-display
setterm -blank 0 -powerdown 0 -powersave off
sudo python3 viewer.py