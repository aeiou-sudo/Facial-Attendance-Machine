import os
import numpy as np
from PIL import Image
import PIL
from mtcnn.mtcnn import MTCNN
from matplotlib import pyplot
from numpy import asarray
from keras_vggface.utils import preprocess_input
from keras_vggface.vggface import VGGFace
from scipy.spatial.distance import cosine
import cv2
from numpy import expand_dims
from datetime import date, datetime
def readCam():
    print("Reading")
    camencoding = []
    detector = MTCNN()
    cap = cv2.VideoCapture(0)
    i = 1
    # starting the camera inside a loop to continuesly capture the frames and it will the working inrealtime
    while True:
        ret, frame = cap.read()
        faces = detector.detect_faces(frame)
        # detect a face when someone passes throught the camera's view
        if faces:
            x1, y1, w, h = faces[0]['box']
            x2, y2 = x1+w, y1+h
            faces = cv2.rectangle(frame, (x1, y1),(x2, y2), (255,255,255), 2)
            croped = frame[y1:y2,x1:x2]
            cv2.imshow("faces", faces)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            faceEncoding = Image.fromarray(croped)
            faceEncoding = faceEncoding.resize((224,224))
            face_array = asarray(faceEncoding)
            pixels = face_array.astype('float32')
            samples = expand_dims(pixels, axis=0)
            samples = preprocess_input(samples, version=2)
            model = VGGFace(model='resnet50', include_top=False, input_shape=(224, 224, 3), pooling='avg')
            yhat = model.predict(samples)
            camencoding = yhat
            compare(camencoding)
        else:
            # print("Empty")
            continue

def compare(x):
    # print("Comparing")
    for i, name in zip(loaded_arr, classnames):
        score = cosine(x, i)
        # from the encoding values campare the values
        #  set a threshold value of .3
        if score < .3:
            markAttendance(name)
def markAttendance(name):
    with open('Attendance.csv','r+') as f:
        # reading the attendance file
        myDataList = f.readlines()
        nameList = []
        timeInList = []
        timeOutList = []
        # splitting the files line by line and seperating the items using ','
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
            timeInList.append(entry[1])
            timeOutList.append(entry[2])
        # check whether the person has already checkedin
        # if not enter the name and currrent time into the attendance file
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%d-%m-%Y %H:%M:%S.%f')
            f.writelines(f'{name},{dtString},{0}\n')
        else:
            # if the name is already in the list means that the person has already checkedin
            # check the attendance leaving file to verify that the person hasn't been marked as checkedout
            index = nameList.index(name)
            previousTime = timeInList[index]
            previousTime = previousTime.strip()
            prev = datetime.strptime(previousTime,'%d-%m-%Y %H:%M:%S.%f')
            now = datetime.now()
            diff = str(now - prev)
            diff = diff.split(':')
            minutes = int(diff[1])
            if minutes >= 1:
                if int(timeOutList[index]) == 0:
                    print("Reached Here")
                else:
                    print("Reached Here elae")

                # with open('AttendanceLeave.csv','r+') as l:
                #     leavingList = l.readlines()
                #     leavingName = []
                #     leavingTime = []
                #     for lines in leavingList:
                #         entries = lines.split(',')
                #         leavingName.append(entries[0])
                #         leavingTime.append(entries[1])
                #     # if the person's name is in the leaving list then there is an issue so need to check the file if there is a marking
                #     # if name exist then notify them to contact the admin
                #     if name not in leavingName:
                #         leavingNow = datetime.now()
                #         leavingTimeString = leavingNow.strftime('%d-%m-%Y %H:%M:%S.%f')
                #         l.writelines(f'{name},{leavingTimeString}\n')
                #     else:
                #         leavingIndex = leavingName.index(name)
                #         previousLeavingTime = leavingTime[leavingIndex]
                #         previousLeavingTime = previousLeavingTime.strip()
                #         preLeave = datetime.strptime(previousLeavingTime,'%d-%m-%Y %H:%M:%S.%f')
                #         nowTime = datetime.now()
                #         diffLeave = str(nowTime - preLeave)
                #         diffLeave = diffLeave.split(':')
                #         minutesLeave = int(diffLeave[1])
                #         if minutesLeave >= 1:
                #             print("Multiple entries detected please contact the admin")

def retriveEncode():
    path = 'Encodings'
    global loaded_arr
    loaded_arr = []
    global classnames
    classnames = []
    # loading the encodings and class names from the folder
    myList = os.listdir(path)
    for item in myList:
        if item.lower().endswith('txt'):
            loaded_arr.append(np.load(f'{path}/{item}'))
            classnames.append(os.path.splitext(item)[0])
# retriveEncode()
# readCam()
markAttendance("Eldho")