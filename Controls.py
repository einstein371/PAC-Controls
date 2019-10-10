import RPi.GPIO as GPIO
import Adafruit_ADS1x15
import time

#GPIO to LCD Mapping using BCM
OLED_GND = 14
OLED_VCC  = 1
OLED_SCL = 5 
OLED_SDA = 3
Encoder_CLK = 17
dt = 18
clk = 17
GAIN = 1

#OLED Display
GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_UP)

clkLastState = GPIO.input(clk)

def my_callback(channel):  
    global clkLastState
    global counter
    try:
                clkState = GPIO.input(clk)
                if clkState != clkLastState:
                        dtState = GPIO.input(dt)
                        if dtState != clkState:
                                counter += 1
                        else:
                                counter -= 1
                        print (counter)
                clkLastState = clkState
                #sleep(0.01)
    finally:
                print ("Ending")

while True:
	values[i] = adc.read_adc(i, gain=GAIN)
	time.sleep(0.5)

counter = 0
clkLastState = GPIO.input(clk)
GPIO.add_event_detect(17, GPIO.FALLING  , callback=my_callback, bouncetime=300)  
raw_input=input("Enter anything")
GPIO.cleanup()