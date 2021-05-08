''' Using pytesserect OCR-engine to perfrom OCR ''' 

import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab
import time


pytesseract.pytesseract.tesseract_cmd = 'E:/ML_projects/OCR_new/tesserect_OCR/tesseract.exe'

img = cv2.imread('new.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# to get the text
text = pytesseract.image_to_string(img)
print(text[:-4])

# detecting individual characters
image_height, image_width, _ = img.shape

boxes = pytesseract.image_to_boxes(img)
for box in boxes.splitlines():
    box = box.split() #[text, x, y, width, height]
    print(boxes)
    x, y, w, h = int(box[1]), int(box[2]), int(box[3]), int(box[4])
    cv2.rectangle(img, (x, image_height-y), (w, image_height-h), (0, 0, 255), 1)
    cv2.putText(img, box[0], (x, image_height-y+25), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 4)
    
cv2.imshow('Image', img)


# detecting words
image_height, image_width, _ = img.shape

boxes = pytesseract.image_to_data(img)
for count, box in enumerate(boxes.splitlines()):
    if count!=0:
        box = box.split() #[text, x, y, width, height]
        print(box)
        if len(box) == 12:
            x, y, w, h = int(box[6]), int(box[7]), int(box[8]), int(box[9])
            cv2.rectangle(img, (x, y), (w+x, h+y), (0, 0, 255), 1)
            cv2.putText(img, box[11], (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 4)
            
cv2.imshow('Image', img)
            
            
# detecting only numbers
image_height, image_width, _ = img.shape
config = r'--oem 3 --psm 6 outputbase digits'

boxes = pytesseract.image_to_data(img, config=config)
for count, box in enumerate(boxes.splitlines()):
    if count!=0:
        box = box.split() #[text, x, y, width, height]
        print(box)
        if len(box) == 12:
            x, y, w, h = int(box[6]), int(box[7]), int(box[8]), int(box[9])
            cv2.rectangle(img, (x, y), (w+x, h+y), (0, 0, 255), 1)
            cv2.putText(img, box[11], (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 4)
            
cv2.imshow('Image', img)
                

# detecting individual numbers
image_height, image_width, _ = img.shape
config = r'--oem 3 --psm 6 outputbase digits'

boxes = pytesseract.image_to_boxes(img, config=config)
for box in boxes.splitlines():
    box = box.split() #[text, x, y, width, height]
    print(boxes)
    x, y, w, h = int(box[1]), int(box[2]), int(box[3]), int(box[4])
    cv2.rectangle(img, (x, image_height-y), (w, image_height-h), (0, 0, 255), 1)
    cv2.putText(img, box[0], (x, image_height-y+25), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 4)
    
cv2.imshow('Image', img)
    
