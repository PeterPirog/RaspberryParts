#https://github.com/firmata/firmata_test

from pyfirmata import Arduino, util
import time
board = Arduino('/dev/ttyACM1')

print('Firmata version:',board.get_firmata_version())


while True:

    board.digital[13].write(1)
    time.sleep(0.5)
    board.digital[13].write(0)
    time.sleep(0.5)


