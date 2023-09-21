import time
import os
import board
import digitalio

print("press a button!")

button1 = digitalio.DigitalInOut(board.D2)
button1.direction = digitalio.Direction.INPUT

button2 = digitalio.DigitalInOut(board.D3)
button2.direction = digitalio.Direction.INPUT

button3 = digitalio.DigitalInOut(board.D17)
button3.direction = digitalio.Direction.INPUT

button4 = digitalio.DigitalInOut(board.D27)
button4.direction = digitalio.Direction.INPUT

button5 = digitalio.DigitalInOut(board.D23)
button5.direction = digitalio.Direction.INPUT

button6 = digitalio.DigitalInOut(board.D13)
button6.direction = digitalio.Direction.INPUT

button7 = digitalio.DigitalInOut(board.D19)
button7.direction = digitalio.Direction.INPUT

button8 = digitalio.DigitalInOut(board.D26)
button8.direction = digitalio.Direction.INPUT

while True:

    # omxplayer -o local <file>
    # omxplayer -o hdmi <file>
    # omxplayer -o both <file>
    if button1.value:
        os.system('omxplayer audio/gluszec.wav &')

    if button2.value:
        os.system('omxplayer audio/jelen.wav &')

    if button3.value:
        os.system('omxplayer audio/nietoperze.wav &')

    if button4.value:
        os.system('omxplayer audio/orzel.wav &')

    if button5.value:
        os.system('omxplayer audio/pszczoly.wav &')

    if button6.value:
        os.system('omxplayer audio/sowa.wav &')

    if button7.value:
        os.system('omxplayer audio/wilk.wav &')

    if button8.value:
        os.system('omxplayer audio/zaby.wav &')

    time.sleep(.25)