A simple raspberry pi based image display for an exhibition.
All the media materials are copyrighted and should not be used by any third-party.

To set up the photo viewer, download the [Raspberry Pi Imager](https://www.raspberrypi.com/software/) software and burn the legacy os onto the sd card.
The code assumes there is an `adlugosz` user and will attempt to run from that home directory.

In order to prevent display issues, add the following lines to the config.txt file in the boot sector of the SD card:
```
hdmi_force_hotplug=1
config_hdmi_boost=9
```

After this is done execute the commands in the [setup.sh] file in order to prep the os.

If using a Raspberry PI Zero, make sure its getting 1A of power instead of the more common 500mA.