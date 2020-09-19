#https://tutorials-raspberrypi.com/raspberry-pi-servo-motor-control/
#https://www.electronicwings.com/raspberry-pi/raspberry-pi-pwm-generation-using-python-and-c
#https://www.youtube.com/watch?v=LXURLvga8bQ
import RPi.GPIO as GPIO
import time

"""
servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization
"""

class Servo_FS90R():
  def __init__(self,servoPIN,freq=50):
    self.servoPIN=servoPIN
    self.freq=freq
    self.stop_position_usec=1500 # width of pulse for stop servo
    self.max_CW_usec=700 # width of pulse for maximum clock wise direction speed
    self.max_CCW_usec = 2300 # width of pulse for maximum counter clock wise direction speed
    self.dead_bandwith_usec=93
    self.period_usec=1e6/self.freq


    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(self.servoPIN, GPIO.OUT)
    self.p=GPIO.PWM(self.servoPIN, self.freq)  #  default GPIO 17 for PWM with 50Hz



  def speed_2_impulse_width(self,speed_in_percent):
    if speed_in_percent>100:
      speed_in_percent=100
      print('Value speed_in_percent is out of range (above 100 %)!. Value changed to 100')
    if speed_in_percent<-100:
      speed_in_percent=-100
      print('Value speed_in_percent is out of range! (below -100 %. Value changed to -100')

    x1=-100
    x2=100
    y1=self.max_CW_usec
    y2=self.max_CCW_usec
    a=(y2-y1)/(x2-x1)
    b=(y1*x2-y2*x1)/(x2-x1)
    print('slope=',a,'intercept=',b)
    impulse_width=a*speed_in_percent+b
    print('impulse width=',impulse_width)
    print('period=',self.period_usec)
    return 100*impulse_width/self.period_usec


  def start_speed(self,speed_in_percent):
    duty_cycle=self.speed_2_impulse_width(speed_in_percent)
    self.p.start(duty_cycle)


  def change_speed(self,speed_in_percent):
    duty_cycle = self.speed_2_impulse_width(speed_in_percent)
    self.p.ChangeDutyCycle(duty_cycle)

  def stop(self):

    self.p.stop()


###############################################
srv=Servo_FS90R(servoPIN=12)
print(srv.speed_2_impulse_width(0))

srv.start_speed(7.5)
try:
  while True:
    srv.change_speed(0)
    time.sleep(0.5)

    srv.change_speed(0)
    time.sleep(0.5)

    srv.change_speed(0)
    time.sleep(0.5)

    """
    p.ChangeDutyCycle(10)
    time.sleep(0.5)

    p.ChangeDutyCycle(7.5)
    time.sleep(0.5)

    p.ChangeDutyCycle(10)
    time.sleep(0.5)
    p.ChangeDutyCycle(12.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(10)
    time.sleep(0.5)
    p.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(5)
    time.sleep(0.5)
    p.ChangeDutyCycle(2.5)
    time.sleep(0.5)
  """
except KeyboardInterrupt:
  #srv.stop()
  GPIO.cleanup()