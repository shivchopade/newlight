import time
from gpiozero import LED

led1 = LED(17)
led2 = LED(27)
led3 = LED(10)
led4 = LED(7)
count = 0
while count < 6:
	led1.on()
	led2.off()
	led3.on()
	led4.off()
	time.sleep(1)
	led1.off()
	led2.on()
	led3.off()
	led4.on()
	time.sleep(1)
	count += 1
