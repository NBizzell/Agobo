import agobo
import time
import mouth

agobo.init

speed = 50
angle = 1.08
space = 10

try:
  while True:
    mouth.smile()
    agobo.forward(speed)
    dist = agobo.getDistance()
    print "distance: ", int(dist)
    if dist < space:
      mouth.sad()
      agobo.spinRight(speed)
      time.sleep(angle)
      agobo.stop()
      dist = agobo.getDistance()
      if dist < (space*2):
        mouth.oh()
        agobo.spinLeft(speed)
        time.sleep(angle*2)
        agobo.stop()
        dist = agobo.getDistance()
        if dist < (space*2):
          mouth.conf1()
          agobo.spinLeft(speed)
          time.sleep(angle)
  time.sleep(0.25)
  mouth.smile()
except KeyboardIterupt:
  print
  
finally:
  agobo.cleanup()
  
