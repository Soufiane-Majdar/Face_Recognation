import cv2
import numpy as np
import face_recognition
import os


path = 'persons'
images = []
classNames = []
personList = os.listdir(path)
print(personList)

for person in personList:
    curImg = cv2.imread(f'{path}/{person}')
    images.append(curImg)
    classNames.append(os.path.splitext(person)[0])