#!/usr/bin/python3
import sys
sys.path.append(r'/opt/ezblock')
import cv2
import time
import numpy as np
from ezblock import __reset_mcu__
from ezblock import run_command
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
#Video_Car
###############################################################
#This program will provide a First Person View
#from the PiCar-X! Use the keyboards WSAD keys to control
#the direction of movement, and the O and P to adjust the speed.

camera = PiCamera()
camera.resolution = (640,480)
camera.framerate = 24
camera.image_effect = "none"  #"none","negative","solarize","emboss","posterise","cartoon",
rawCapture = PiRGBArray(camera, size=camera.resolution)

power_val = 0

try:
    while True:
        for frame in camera.capture_continuous(rawCapture, format="bgr",use_video_port=True):# use_video_port=True
            img = frame.array
            cv2.imshow("video", img)

            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                camera.close()
                continue
            elif k == ord('o'):
                if power_val <=90:
                    power_val += 10
                    print("power_val:",power_val)
            elif k == ord('p'):
                if power_val >=10:
                    power_val -= 10
                    print("power_val:",power_val)
            elif k == ord('w'):
                # print("w:",)
                set_dir_servo_angle(0)
                forward(power_val)
            elif k == ord('a'):
                set_dir_servo_angle(-30)
                forward(power_val)
            elif k == ord('s'):
                set_dir_servo_angle(0)
                backward(power_val)
            elif k == ord('d'):
                set_dir_servo_angle(30)
                forward(power_val)
            elif k == ord('f'):
                stop()

            elif k == ord('t'):
                camera.close()
                break
            rawCapture.truncate(0)

        print("take a photo wait...")
        picture_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        picture_path = '/home/pi/Pictures/' + picture_time + '.jpg'

        a_t = "sudo raspistill -t 250  -w 2592 -h 1944 " + " -o " + picture_path

        print(a_t)
        run_command(a_t)

        # Vilib.shuttle_button()
        camera = PiCamera()
        camera.resolution = (640,480)
        camera.framerate = 24
        camera.image_effect = "none"  #"none","negative","solarize","emboss","posterise","cartoon",
        rawCapture = PiRGBArray(camera, size=camera.resolution)
finally:
    stop()
    camera.close()
