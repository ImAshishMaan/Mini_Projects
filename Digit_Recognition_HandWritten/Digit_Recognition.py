# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 09:47:27 2020

@author: ashish maan
"""
import tensorflow as tf
import numpy as np
import cv2


state = False
def Draw(event, x, y, flags, param):
    global state
    
    if event == cv2.EVENT_LBUTTONDOWN:
        state = True  
    elif event == cv2.EVENT_LBUTTONUP:
        state = False
    elif event == cv2.EVENT_MOUSEMOVE:
        if state == True:
            cv2.circle(canvas, (x,y), 10, (255,0,0), -1)

canvas = np.zeros([400,400,1],dtype='uint8')*255
cv2.namedWindow('Draw')
cv2.setMouseCallback('Draw',Draw)


while True:
    cv2.imshow('Draw',canvas)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('p'):
        img = canvas/255
        img = cv2.resize(canvas, (28,28)).reshape(1,28,28)
        predict = tf.keras.models.load_model('mnist.h5')
        result = predict.predict_classes(img)
        print(result)
    elif key == ord('c'):
        canvas[:,:] = 0
cv2.destroyAllWindows()




