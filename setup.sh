
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install -y python3-pip omxplayer fonts-freefont-ttf
sudo pip3 install adafruit-blinka

cd ~
mkdir logs
wget -P ~/ https://github.com/Moomba42/rpi-audio-buttons/archive/refs/heads/main.zip
unzip main.zip
rm main.zip
cd rpi-audio-buttons-main
chmod 755 launcher.sh
sudo crontab -e
# Add the following line:
# @reboot sh ~/rpi-audio-buttons-main/launcher.sh >~/logs/cronlog 2>&1
sudo reboot
