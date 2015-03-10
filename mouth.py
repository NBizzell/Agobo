import RPI.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(31, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)

#smile

def smile():
  GPIO.output(31, 0)
  GPIO.output(32, 0)
  GPIO.output(33, 1)
  GPIO.output(35, 1)
  GPIO.output(36, 0)
  GPIO.output(37, 1)
  GPIO.output(38, 1)
  GPIO.output(40, 0)
  
#sad

def sad():
  GPIO.output(31, 0)
  GPIO.output(32, 1)
  GPIO.output(33, 1)
  GPIO.output(35, 0)
  GPIO.output(36, 0)
  GPIO.output(37, 0)
  GPIO.output(38, 1)
  GPIO.output(40, 1)
  
  
#Oh

def oh():
  GPIO.output(31, 0)
  GPIO.output(32, 1)
  GPIO.output(33, 1)
  GPIO.output(35, 1)
  GPIO.output(36, 0)
  GPIO.output(37, 1)
  GPIO.output(38, 1)
  GPIO.output(40, 1)
  
  
#confused

def conf1():
  GPIO.output(31, 1)
  GPIO.output(32, 1)
  GPIO.output(33, 1)
  GPIO.output(35, 0)
  GPIO.output(36, 0)
  GPIO.output(37, 1)
  GPIO.output(38, 1)
  GPIO.output(40, 0)
