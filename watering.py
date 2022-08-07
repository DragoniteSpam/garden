# Adapted from here:
# http://web.archive.org/web/20220501075205/https://www.raspberrypi.com/news/raspberry-pi-zero-waters-your-plants-and-records-growth-timelapse/
# http://web.archive.org/web/20210822053232/https://www.explainingcomputers.com/sample_code/Watering.py

import time
import RPi.GPIO as GPIO

#Set up variables: interval in minutes, water in seconds
water_interval = 1
water_time = 5

sensor_gpio = []
power_gpio = []
sensor_led = []
valve_gpio = []

#Sensor A: GPIO 29, Relay 1: GPIO 37, Relay 2: GPIO 38, LED: 7
#Sensor B: GPIO 3, Relay 1: GPIO 35, Relay 2: GPIO 36, LED: 5
GPIO.setmode(GPIO.BOARD)

def sensor_setup(init_water_interval, init_water_time):
    global water_interval, water_time
    global sensor_gpio, power_gpio, sensor_led, valve_gpio
    
    water_interval = init_water_interval
    water_time = init_water_time
    # Sensors: these are the pins that read the input values from
    # the water sensors
    sensor_gpio = [
        29, 3
    ]
    
    for sensor in sensor_gpio:
        GPIO.setup(sensor, GPIO.IN)
    
    # Power: turn the moisture sensors on or off so that they last longer
    power_gpio = [
        38, 36
    ]
    
    for power in power_gpio:
        GPIO.setup(power, GPIO.OUT)

    # LEDs: the little flashing lights you can enable on the sensors
    sensor_led = [
        7, 5
    ]
    
    for led in sensor_led:
        GPIO.setup(led, GPIO.OUT)
    
    # Valves: two pins that can enable and disable the water valves
    # which i would like to install later
    valve_gpio = [
        37, 35
    ]
    
    for valve in valve_gpio:
        GPIO.setup(valve, GPIO.OUT)

def sensor_update():
    global water_interval, water_time
    global sensor_gpio, power_gpio, sensor_led, valve_gpio
    
    #Turn on the lights
    for led in sensor_led:
        GPIO.output(led, True)
    
    # Enable the sensors
    for power in power_gpio:
        GPIO.output(power, True)
    
    #Check if dry, and if so open valves for water(ing) time
    for i in range(len(sensor_gpio)):
        if (GPIO.input(sensor_gpio[i])) == 1:
            GPIO.output(valve_gpio[i], True)
            print("sensor %d: needs water" % i)
        else:
            print("sensor %d: already wet..." % i)
    
    time.sleep(water_time)
    
    # Close all valves
    for i in range(len(valve_gpio)):
        GPIO.output(valve_gpio[i], False)
    
    # Disable the sensors
    for power in power_gpio:
        GPIO.output(power, True)
    
    # Turn off the lights
    for led in sensor_led:
        GPIO.output(led, False)

def sensor_wait():
    global water_interval, water_time
    global sensor_gpio, power_gpio, sensor_led, valve_gpio
    
    #Wait for interval period, flashing LED every 30 seconds
    count_AA = 0
    while count_AA < (water_interval * 2):
        count_BB = 0
        while count_BB < 5:
            for led in sensor_led:
                GPIO.output(led, True)
            time.sleep(0.5)
            for led in sensor_led:
                GPIO.output(led, False)
            time.sleep(0.5)
            count_BB = count_BB + 1
        time.sleep(25)
        count_AA = count_AA + 1
