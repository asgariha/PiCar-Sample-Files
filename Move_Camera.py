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
from picamera.array import PiRGBArray
###############################################################
#Move_Camera
###############################################################
dir_servo_angle_calibration(0)
camera_servo1_angle_calibration(0)
camera_servo2_angle_calibration(0)

if __name__ == "__main__":
    try:           
        for angle in range(0,35):
            set_camera_servo1_angle(angle)
            time.sleep(0.01)
        for angle in range(35,-35,-1):
            set_camera_servo1_angle(angle)
            time.sleep(0.01)
        for angle in range(-35,0):
            set_camera_servo1_angle(angle)
            time.sleep(0.01)
        for angle in range(0,35):
            set_camera_servo2_angle(angle)
            time.sleep(0.01)
        for angle in range(35,-35,-1):
            set_camera_servo2_angle(angle)
            time.sleep(0.01)
        for angle in range(-35,0):
            set_camera_servo2_angle(angle)
            time.sleep(0.01)
            
        for i in [0, 10, 20, 30, 20, 10, 0, -10, -20, -30, -20, -10, 0]:
            set_camera_servo1_angle(i)
            delay(500)
            
        for i in [0, 10, 20, 30, 20, 10, 0, -10, -20, -30, -20, -10, 0]:
            set_camera_servo2_angle(i)
            delay(500)

    finally:
        forward(0)
        
    





