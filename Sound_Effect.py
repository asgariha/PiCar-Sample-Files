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
#Sound_Effect
################################################################!/usr/bin/python3
from Music import *

count = None

__tts__ = TTS()


def forever():
  global count
  __tts__.say('Ready')
  count = 3
  for count2 in range(3):
    __tts__.say(count)
    count = count - 1
  sound_effect_play('Weapon_Continue_Shooting.wav',50)

if __name__ == "__main__":
    while True:
        forever()  
