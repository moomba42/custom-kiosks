# Photo display

A simple raspberry pi based image display for an exhibition.
All the media materials are copyrighted and should not be used by any third-party.

## Configuration
To set up the photo viewer, download the [Raspberry Pi Imager](https://www.raspberrypi.com/software/) software and burn the legacy os onto the sd card.
The code assumes there is an `adlugosz` user and will attempt to run from that home directory.

After this is done execute the commands in the [setup.sh](setup.sh) file in order to prep the os. 

### Turning off screen blanking
Run the following command to open the raspberry pi config and disable screen blanking under display options:
```
sudo raspi-config
```

## Autorun
Save this in /etc/xdg/autostart/photoviewer.dekstop:
```
[Desktop Entry]
Type=Application
Name=Photoviewer
Exec=/bin/sh /home/adlugosz/custom-kiosks-main/rpi-photo-display/launcher.sh
```

Then reboot

## Troubleshooting
- If using a Raspberry PI Zero, make sure its getting 1A of power instead of the more common 500mA.
- In order to prevent display issues, add the following lines to the config.txt file in the boot sector of the SD card:
    ```
    hdmi_force_hotplug=1
    config_hdmi_boost=9
    ```
