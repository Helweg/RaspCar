
import RPi.GPIO as io
io.setmode(io.BCM)
import sys, tty, termios, time

Motor1_input1 = 2
Motor1_input2 = 4
Motor1_enable = 17

io.setup(Motor1_input1, io.OUT)
io.setup(Motor1_input2, io.OUT)
io.setup(Motor1_enable, io.OUT)

M1_enable = io.PWM(Motor1_enable,100)
M1_enable.start(0)
M1_enable.ChangeDutyCycle(0)

Motor2_input1 = 14 
Motor2_input2 =	18
Motor2_enable = 23

io.setup(Motor2_input1, io.OUT)
io.setup(Motor2_input2, io.OUT)
io.setup(Motor2_enable, io.OUT)

M2_enable = io.PWM(Motor2_enable,100)
M2_enable.start(0)
M2_enable.ChangeDutyCycle(0)

def getch():
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	return ch

io.output(Motor1_input1,False)
io.output(Motor1_input2,False)
io.output(Motor1_enable,False)

def motor_forward():
	io.output(Motor1_input1,True)
	io.output(Motor1_input2,False)
	io.output(Motor1_enable,True)
	io.output(Motor2_input1,False)
	io.output(Motor2_input2,True)
	io.output(Motor2_enable,True)
	print("Forward")

def motor_reverse():
	io.output(Motor1_input1,False)
	io.output(Motor1_input2,True)
	io.output(Motor1_enable,True)
	io.output(Motor2_input1,True)
	io.output(Motor2_input2,False)
	io.output(Motor2_enable, True)
	print("Reverse")

while True:
	char = getch()
	if(char == "w"):
		motor_forward()
		M1_enable.ChangeDutyCycle(55)
		M2_enable.ChangeDutyCycle(45)
	if(char == "s"):
		motor_reverse()
		M1_enable.ChangeDutyCycle(53)
		M2_enable.ChangeDutyCycle(47)
	if(char == "x"):
		print("Program ended")
		break
	#M1_enable.ChangeDutyCycle(0)
	#M2_enable.ChangeDutyCycle(0)

	char = ""

io.cleanup()
