
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

Motor2_input1 = 18 
Motor2_input2 =	14
Motor2_enable = 23

io.setup(Motor2_input1, io.OUT)
io.setup(Motor2_input2, io.OUT)
io.setup(Motor2_enable, io.OUT)

M2_enable = io.PWM(Motor2_enable,100)
M2_enable.start(0)
M2_enable.ChangeDutyCycle(0)

io.setup(9, io.IN)

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

def motor1_forward():
	io.output(Motor1_input1,False)
	io.output(Motor1_input2,True)
	io.output(Motor1_enable,True)

def motor1_reverse():
	io.output(Motor1_input1,True)
	io.output(Motor1_input2,False)
	io.output(Motor1_enable,True)

def motor2_forward():
	io.output(Motor2_input1,True)
	io.output(Motor2_input2,False)
	io.output(Motor2_enable,True)

def motor2_reverse():
	io.output(Motor2_input1,False)
	io.output(Motor2_input2,True)
	io.output(Motor2_enable,True)


def toggleSteering(direction):

	if(direction == "right"):
		motor1_forward()
		motor2_forward()
		M1_enable.ChangeDutyCycle(20)
		M2_enable.ChangeDutyCycle(15)

	if(direction == "left"):
		motor1_forward()
		motor2_forward()
		M2_enable.ChangeDutyCycle(20)
		M1_enable.ChangeDutyCycle(15)

def sensorSteering():
	input_state = io.input(9)
	while True:
		input_state = io.input(9)
		if input_state == False:
			toggleSteering("left")
			print("0")
			time.sleep(0.05)
		if input_state == True:
			toggleSteering("right")
			print("1")
			time.sleep(0.05)
while True:
	char = getch()
	if(char == "w"):
		motor1_forward()
		motor2_forward()
		M1_enable.ChangeDutyCycle(51)
		M2_enable.ChangeDutyCycle(47)
		print("Forward")
	if(char == "d"):
		toggleSteering("right")
		print("Turning right")
	if(char == "a"):
		toggleSteering("left")
		print("Turning left")
	if(char == "s"):
		motor1_reverse()
		motor2_reverse()
		M1_enable.ChangeDutyCycle(53)
		M2_enable.ChangeDutyCycle(47)
		print("Reverse")
	if(char == "t"):
		sensorSteering()
	if(char == "x"):
		print("Program ended")
		break
	char = ""

io.cleanup()
