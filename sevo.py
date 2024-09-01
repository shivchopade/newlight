from gpiozero import AngularServo
from time import sleep

servo = AngularServo(18, min_pulse_width=0.0006,max_pulse_width=0.0023)
count = 6
while(count>0):
    servo.angle=90
    sleep(0.5)
    servo.angle=0
    sleep(0.5)
    servo.angle=-90
    sleep(0.5)
    count -= 1