  #!/usr/bin/python3
import sys
sys.path.append(r'/opt/ezblock')
import cv2
import time
import numpy as np
from ezblock import __reset_mcu__
__reset_mcu__()
time.sleep(0.01)

from picarmini import forward
from picarmini import stop
from ezblock import Pin
from ezblock import ADC
from ezblock import delay
from ezblock import Ultrasonic
from picarmini import set_dir_servo_angle
from picarmini import set_camera_servo1_angle
from picarmini import set_camera_servo2_angle
from picarmini import dir_servo_angle_calibration
from picarmini import camera_servo1_angle_calibration
from picarmini import camera_servo2_angle_calibration
from ezblock import TTS
from Music import sound_effect_play
from picamera import PiCamera
from picamera.array import PiRGBArray
###############################################################
#Grayscale_Sensor
###############################################################
adc_A0=ADC("A0")
adc_A1=ADC("A1")
adc_A2=ADC("A2")

for i in range(10):
    print(f"Grayscale: {adc_A0.read()} {adc_A1.read()} {adc_A2.read()}")
    delay(500)
