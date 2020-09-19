class DefaultServo():
    def __init__(self):
        #Servo general info
        self.model='' #model name eg. 'MG90S' , 'FS90R'
        self.servo_range=None  #angle in degrees, for continous servo value = 360
        self.size='' # 'micro' , "medium', 'standard
        self.weight_g=None
        self.connections='' #description how to connect pins

        #Operating speed
        self.time_per_60deg_min_volt=None  # servo speed for minimum voltage
        self.time_per_60deg_max_volt = None # servo speed for maximum voltage
        self.time_per_60deg = None

        #Define operating Voltage
        self.minimum_operating_voltage_V=None
        self.minimum_operating_voltage_V=None

        #Define Torque
        self.torque_minimum_voltage=None
        self.torque_maximum_voltage = None

        #Time properties
        self.dead_band_us=None
            #for servo motor with closed loop
        self.time_right_us=None
        self.time_left_us=None
        self.time_middle_us=None

    def info(self):
        try:
            self.time_per_60deg is None
        except:
            self.time_per_60deg=self.time_per_60deg_max_volt


        print('\nDescription of {} servo motor:'.format(self.model))
        print('\tRange [deg]: {}'.format(self.servo_range))
        print('\tSize: {}'.format(self.size))
        print('\tWeight [g]: {}'.format(self.weight_g))
        print('\tHow to connect: {}'.format(self.connections))


class _MG90S(DefaultServo):
    def __init__(self):
        #Servo general info
        self.model='MG90S'
        self.servo_range=180.0
        self.size='Micro'
        self.weight_g=13.4
        self.connections="Red - Vcc, Brown - Ground, Orange - PWM"

        #Operating speed
        self.time_per_60deg_min_volt=0.1
        self.time_per_60deg_max_volt = 0.1

        #Define operating Voltage
        self.minimum_operating_voltage_V=4.8
        self.minimum_operating_voltage_V=6.0

        #Define Torque
        self.torque_minimum_voltage=1.8
        self.torque_maximum_voltage = 2.2

        #Time properties
        self.dead_band_us=5
        self.time_right_us=2000.0
        self.time_left_us=1000.0
        self.time_middle_us=1500.0


servo=_MG90S()
servo.info()