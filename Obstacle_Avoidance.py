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
#Obstacle_Avoidance
###############################################################
if __name__ == "__main__":
    try:
        trig_pin = Pin("D2")
        echo_pin = Pin("D3")
        sonar = Ultrasonic(trig_pin, echo_pin)
        forward(30)
        while True:
            distance = sonar.read()
            print("distance: ",distance)
            if distance > 0 and distance < 300:
                if distance < 25:
                    set_dir_servo_angle(-35)
                else:
                    set_dir_servo_angle(0)
    finally:
        forward(0)
        stop()
