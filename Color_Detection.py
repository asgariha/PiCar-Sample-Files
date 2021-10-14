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
#Color_Detection
###############################################################
color_dict = {'red':[0,4],'orange':[5,18],'yellow':[22,37],'green':[42,85],'blue':[92,110],'purple':[115,165],'red_2':[165,180]}

kernel_5 = np.ones((5,5),np.uint8)

def color_detect(img,color_name):

    resize_img = cv2.resize(img, (160,120), interpolation=cv2.INTER_LINEAR)
    hsv = cv2.cvtColor(resize_img, cv2.COLOR_BGR2HSV)

    color_type = color_name

    mask = cv2.inRange(hsv,np.array([min(color_dict[color_type]), 60, 60]), np.array([max(color_dict[color_type]), 255, 255]) )
    if color_type == 'red':
            mask_2 = cv2.inRange(hsv, (color_dict['red_2'][0],0,0), (color_dict['red_2'][1],255,255))
            mask = cv2.bitwise_or(mask, mask_2)

    morphologyEx_img = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel_5,iterations=1)

    contours, hierarchy = cv2.findContours(morphologyEx_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    color_area_num = len(contours)

    if color_area_num > 0:
        for i in contours:
            x,y,w,h = cv2.boundingRect(i)

            if w >= 8 and h >= 8:
                x = x * 4
                y = y * 4
                w = w * 4
                h = h * 4
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                cv2.putText(img,color_type,(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2)

    return img,mask,morphologyEx_img

#init camera
print("start color detect")
camera = PiCamera()
camera.resolution = (640,480)
camera.framerate = 24
rawCapture = PiRGBArray(camera, size=camera.resolution)

for frame in camera.capture_continuous(rawCapture, format="bgr",use_video_port=True):
    img = frame.array
    img,img_2,img_3 =  color_detect(img,'red')
    cv2.imshow("video", img)
    cv2.imshow("mask", img_2)
    cv2.imshow("morphologyEx_img", img_3)
    rawCapture.truncate(0)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        camera.close()
        break
