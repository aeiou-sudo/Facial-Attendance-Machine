import os
import os.path
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
            # cv2.imshow("faces", croped)
            # if cv2.waitKey(1) & 0xFF == ord('q'):
            #     break
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
        if score < .35:
            markAttendance(name, score)
def markAttendance(name, score):
    mbits = pyplot.imread('mbits.jpeg')
    mbits = cv2.cvtColor(mbits, cv2.COLOR_BGR2RGB)
    path = f'{date.today()}.csv'
    if not (os.path.isfile(path)):
        f = open(path,'w')
        print("File Created")
        f.close()
    nameList = []
    timeInList = []
    timeOutList = []

    scoreList = []
    with open(path,'r') as filer:
        myDataList = filer.readlines()

        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
            timeInList.append(entry[1])
            timeOutList.append(entry[2])
            scoreList.append(entry[5])
    if name not in nameList:
        with open(path,'a') as filea:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            filea.writelines(f'{name},{dtString},0,NA,0,{score}')
        mbits =cv2.putText(mbits,f'Welcome {name}', (2500,2500), cv2.FONT_HERSHEY_SIMPLEX, 5, (0,0,0), 2, cv2.LINE_AA)
        cv2.imshow('Preview', mbits)
        if cv2.waitKey(100):
            cv2.destroyAllWindows()
    else:
        index = nameList.index(name)
        timeIn = timeInList[index]
        timeIn = timeIn.strip()
        timeIn = datetime.strptime(timeIn,'%H:%M:%S')
        now = datetime.now()
        timeOut = now.strftime('%H:%M:%S')
        now = datetime.strptime(timeOut,'%H:%M:%S')
        inTimeDifference = str(now - timeIn)
        inTimeDifference = inTimeDifference.split(':')
        minutes = int(inTimeDifference[1])
        hours = int(inTimeDifference[0])
        if minutes >= 1:#minutes >= 5
             with open(path,'w') as filew:
                for line in myDataList:
                    entry = line.split(',')
                    if entry[0] == name:
                        if minutes >= 5:#hours >=7
                            filew.writelines(f'{name},{timeInList[index]},{timeOut},FULL,{minutes},{scoreList[index]}')#hours
                            mbits =cv2.putText(mbits,f'Bye {name}', (2500,2500), cv2.FONT_HERSHEY_SIMPLEX, 5, (0,0,0), 2, cv2.LINE_AA)
                            cv2.imshow('Preview', mbits)
                            if cv2.waitKey(100):
                                cv2.destroyAllWindows()
                        elif minutes >= 3:#hours >= 4
                            filew.writelines(f'{name},{timeInList[index]},{timeOut},HALF,{minutes},{scoreList[index]}')#hours
                            mbits =cv2.putText(mbits,f'Bye {name}', (2500,2500), cv2.FONT_HERSHEY_SIMPLEX, 5, (0,0,0), 2, cv2.LINE_AA)
                            cv2.imshow('Preview', mbits)
                            if cv2.waitKey(100):
                                cv2.destroyAllWindows()
                        else:
                            filew.writelines(f'{name},{timeInList[index]},{timeOut},NA,{minutes},{scoreList[index]}')#hours
                    else:
                            filew.writelines(line)
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
retriveEncode()
readCam()