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
from grayscale_module import Grayscale_Module
###############################################################
# Line_Tracking
###############################################################
if __name__=='__main__':
    try:
        gm = Grayscale_Module(500)
        power = 10
        while True:
            gm_val_list = gm.get_grayscale_data()
            print("gm_val_list:",gm_val_list)
            gm_status = gm.get_line_status(gm_val_list)
            print("gm_status:",gm_status)

            if gm_status == 'forward':
                forward(power)

            elif gm_status == 'left':
                set_dir_servo_angle(12)
                forward(px_power)

            elif gm_status == 'right':
                set_dir_servo_angle(-12)
                forward(px_power)
            else:
                set_dir_servo_angle(0)
                stop()
    finally:
        stop()
