import time
import os
import board
import digitalio
import logging
from subprocess import Popen, PIPE, DEVNULL

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.info("Audio buttons started")

button1 = digitalio.DigitalInOut(board.D2)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP

button2 = digitalio.DigitalInOut(board.D3)
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.UP

button3 = digitalio.DigitalInOut(board.D17)
button3.direction = digitalio.Direction.INPUT
button3.pull = digitalio.Pull.UP

button4 = digitalio.DigitalInOut(board.D27)
button4.direction = digitalio.Direction.INPUT
button4.pull = digitalio.Pull.UP

button5 = digitalio.DigitalInOut(board.D23)
button5.direction = digitalio.Direction.INPUT
button5.pull = digitalio.Pull.UP

button6 = digitalio.DigitalInOut(board.D13)
button6.direction = digitalio.Direction.INPUT
button6.pull = digitalio.Pull.UP

button7 = digitalio.DigitalInOut(board.D19)
button7.direction = digitalio.Direction.INPUT
button7.pull = digitalio.Pull.UP

button8 = digitalio.DigitalInOut(board.D26)
button8.direction = digitalio.Direction.INPUT
button8.pull = digitalio.Pull.UP

process = None

class Player:
    def __init__(self) -> None:
        self.process = None
    
    def stop(self):
        if self.process is not None:
            if self.process.poll() is None:
                self.process = None
            else:
                try:
                    self.process.stdin.write('q') # send quit command
                    self.process.terminate()
                    self.process.wait()
                except EnvironmentError as e:
                    logger.error("Can't stop process")
                else:
                    self.process = None        
    def play(self, path):
        self.stop()
        self.process = Popen(['omxplayer', path], stdin=PIPE, stdout=DEVNULL, close_fds=True, bufsize=0)

player = Player()

while True:
    if not button1.value:
        print("Button 1 pressed!")
        player.play('audio/gluszec.wav')

    if not button2.value:
        print("Button 2 pressed!")
        player.play('audio/jelen.wav')

    if not button3.value:
        print("Button 3 pressed!")
        player.play('audio/nietoperze.wav')

    if not button4.value:
        print("Button 4 pressed!")
        player.play('audio/orzel.wav')

    if not button5.value:
        print("Button 5 pressed!")
        player.play('audio/pszczoly.wav')

    if not button6.value:
        print("Button 6 pressed!")
        player.play('audio/sowa.wav')

    if not button7.value:
        print("Button 7 pressed!")
        player.play('audio/wilk.wav')

    if not button8.value:
        print("Button 8 pressed!")
        player.play('audio/zaby.wav')

    time.sleep(.25)