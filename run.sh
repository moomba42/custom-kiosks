
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install python3-pip
sudo pip3 install adafruit-blinka

wget -P ~/ https://github.com/Moomba42/rpi-audio-buttons/archive/refs/heads/main.zip
unzip main.zip
cd rpi-audio-buttons-main
sudo python3 ./buttons.py
