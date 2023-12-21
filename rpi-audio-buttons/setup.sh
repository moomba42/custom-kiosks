sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install -y python3-pip omxplayer fonts-freefont-ttf
sudo pip3 install adafruit-blinka

cd ~
mkdir logs
wget -P ~/ https://github.com/Moomba42/custom-kiosks/archive/refs/heads/main.zip
unzip main.zip
rm main.zip
cd custom-kiosks-main
cd rpi-audio-buttons
chmod 755 launcher.sh
sudo crontab -e
# Add the following line:
# @reboot sh /home/adlugosz/custom-kiosks-main/rpi-audio-buttons/launcher.sh >/home/adlugosz/logs/cronlog 2>&1
sudo reboot
