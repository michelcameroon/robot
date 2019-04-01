import RPi.GPIO as GPIO
# Import the GPIO Limbrary
import time
#Import the Time library

# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


# Define GPIO pins to use on the Pi
pinTrigger = 17
pinEcho = 18
#Add variables to set how close to an obstacle the robot can go, how long to re$
#right for. You should change these variables to suit your robot.
# Distance Variables
HowNear = 15.0
ReverseTime = 0.5
TurnTime = 0.75
#And add the GPIO setup line to the others:
# Set pins as output and input
GPIO.setup(pinTrigger, GPIO.OUT)
GPIO.setup(pinEcho, GPIO.IN)


# Set the Variables for the GPIO motor pins
pinMotorAForwards = 10
pinMotorABackwards = 9
pinMotorBForwards = 8
pinMotorBBackwards = 7

# Set the GPIO pin mode
GPIO.setup(pinMotorAForwards, GPIO.OUT)
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinMotorBForwards, GPIO.OUT)
GPIO.setup(pinMotorBBackwards, GPIO.OUT)


#def IsNearObstacle(localHowNear):
#localHowNear = 80

def IsNearObstacle(localHowNear):

    Distance = Measure()
#    Distance = 68

    print("IsNearObstacle: "+str(Distance))
    if Distance < localHowNear:
        return True
    else:
        return False


def Forwards():
    GPIO.output(pinMotorAForwards, 1)
    GPIO.output(pinMotorABackwards, 0)
    GPIO.output(pinMotorBForwards, 1)
    GPIO.output(pinMotorBBackwards, 0)


def Left():
    GPIO.output(pinMotorAForwards, 0)
    GPIO.output(pinMotorABackwards, 1)
    GPIO.output(pinMotorBForwards, 1)
    GPIO.output(pinMotorBBackwards, 0)

def Backwards():
    GPIO.output(pinMotorAForwards, 0)
    GPIO.output(pinMotorABackwards, 1)
    GPIO.output(pinMotorBForwards, 0)
    GPIO.output(pinMotorBBackwards, 1)

def StopMotors():
    GPIO.output(pinMotorAForwards, 0)
    GPIO.output(pinMotorABackwards, 0)
    GPIO.output(pinMotorBForwards, 0)
    GPIO.output(pinMotorBBackwards, 0)


def Right():
    GPIO.output(pinMotorAForwards, 1)
    GPIO.output(pinMotorABackwards, 0)
    GPIO.output(pinMotorBForwards, 0)
    GPIO.output(pinMotorBBackwards, 1)

def AvoidObstacle():
    # Back off a little
    print("Backwards")
    Backwards()
    time.sleep(1)
    StopMotors()


    # Turn right
    print("Right")
    Right()
    time.sleep(1)
    StopMotors()


#In the code above, you pass in a variable to say how close you can get to an o$
#new function that does the measurement using the ultrasonic sensor.
# Take a distance measurement
def Measure():
    GPIO.output(pinTrigger, True)
    time.sleep(0.00001)
    GPIO.output(pinTrigger, False)
    StartTime = time.time()
    StopTime = StartTime


    while GPIO.input(pinEcho)==0:
        StartTime = time.time()
        StopTime = StartTime


#    while GPIO.input(pinEcho)==0:
#        StartTime = time.time()
#        StopTime = StartTime



  while GPIO.input(pinEcho)==1:
        StopTime = time.time()
        # If the sensor is too close to an object, the Pi cannot
        # see the echo quickly enough, so it has to detect that
        # problem and say what has happened
        if StopTime-StartTime >= 0.04:
            print("Hold on there! You're too close for me to see.")
            StopTime = StartTime
            break


    ElapsedTime = StopTime - StartTime
    Distance = (ElapsedTime * 34326)/2

    print(Distance)


    return Distance



#Forwards()
#time.sleep(1)

HowNear = Measure()

#limit = 20.0
limit = 30.0


print (HowNear)

while HowNear > limit:
    print (HowNear)
    Forwards()
    time.sleep(0.005)
HowNear = Measure()
    #print (HowNear)


    #Forwards()
    #time.sleep(0.005)



#    time.sleep(0.010)
#    HowNear = Measure()
#    print (HowNear)



print("after while")
StopMotors()
#AvoidObstacle()



#if IsNearObstacle() == True
#    StopMotors()else
#    Left()
#    time.sleep(0.5)

#time.sleep(1)

#AvoidObstacle()
#time.sleep(0.5)

#Left()
#time.sleep(0.5)


StopMotors()



GPIO.cleanup()
