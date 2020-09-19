#https://github.com/firmata/firmata_test

from pyfirmata import Arduino, util
import time
board = Arduino('/dev/ttyACM0')


while True:
    time.sleep(1.0)
    board.digital[13].write(1)
    time.sleep(1.0)
    board.digital[13].write(0)