import RPI.GPIO as GPIO
import time

IN1 = 17
IN2 = 27
ENA = 22


GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)

# Initialize PWM
pwm = GPIO.PWM(ENA, 1000)  # 1000 Hz frequency
pwm.start(0)


def motor_forward(speed):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    pwm.ChangeDutyCycle(speed)


def motor_backward(speed):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    pwm.ChangeDutyCycle(speed)


def motor_stop():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    pwm.ChangeDutyCycle(0)


try:
    while True:
        print("Moving forward")
        motor_forward(50)  # 50% speed
        time.sleep(2)

        print("Stopping")
        motor_stop()
        time.sleep(1)

        print("Moving backward")
        motor_backward(50)  # 50% speed
        time.sleep(2)

        print("Stopping")
        motor_stop()
        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting program")

finally:
    motor_stop()
    pwm.stop()
    GPIO.cleanup()