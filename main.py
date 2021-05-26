import wiringpi
import time
from datetime import datetime
from sh import gphoto2 as gp
import signal, os, subprocess

def stopgp():
    p = subprocess.Popen(['ps', '-A'],stdout=subprocess.PIPE)
    out, err = p.communicate()
    for line in out.splitlines():
        if b'gvfsd-gphoto2' in line:

            pid= int(line.split(None,1)[0])
            os.kill (pid, signal.SIGKILL)

triggerCommand= ["--trigger-capture"]

stopgp()
gpio = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_GPIO)
solenoidpin = 18
gpio.pinMode(solenoidpin, gpio.OUTPUT)
wiringpi.pinMode(solenoidpin,1)
gpio.digitalWrite(solenoidpin, gpio.HIGH)
time.sleep(0.25)
gpio.digitalWrite(solenoidpin, gpio.LOW)
gpio.digitalWrite(solenoidpin, gpio.HIGH)
time.sleep(0.2)
gpio.digitalWrite(solenoidpin, gpio.LOW)
gp(triggerCommand)