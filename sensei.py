import RPi.GPIO as GPIO
import time
import sys
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN)
GPIO.setup(3,GPIO.OUT)
import gammu
sm=gammu.StateMachine()
sm.ReadConfig(Filename='/home/pi/.gammurc')
sm.Init()
message ={
 'Text' :'Someone unfamiliar is in your house',
 'SMSC' :{'Location' :1},
 'Number':'01515287327',
}
J=0
while True:
    i=GPIO.input(11)
    if i==0:
	print "No intruder",i
	GPIO.output(3,0)
	time.sleep(1)
    elif i==1:
	print "Intruder detected",i
	GPIO.output(3,1)
	time.sleep(1)   
	J=J+1
	if J>3:
	   sm.DialVoice('01515287327')
	   J=0