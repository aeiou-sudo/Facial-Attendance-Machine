import os
import numpy as np
from keras_vggface.utils import preprocess_input
from keras_vggface.vggface import VGGFace
from mtcnn.mtcnn import MTCNN
from PIL import Image
from numpy import asarray
from numpy import expand_dims
from matplotlib import pyplot
def encodeFaceData():
    count = 0
    print("Encoding . . .")
    image = []
    classnames =[]
    encodeClassNames = []
    path = 'images'
    pathToEncode = 'Encodings'
    myList = os.listdir(path)
    myEncodeList = os.listdir(pathToEncode)
    print(myEncodeList)
    # loading images from the folder and appending into a list
    # also appending the image names into a list
    for entry in myEncodeList:
        encodeClassNames.append(os.path.splitext(entry)[0])
    for images in myList:
        if images.lower().endswith(('.png', '.jpg', '.jpeg')):
            if (os.path.splitext(images)[0]) not in encodeClassNames:
                pixels = pyplot.imread(f'{path}/{images}')
                image.append(pixels)
                classnames.append(os.path.splitext(images)[0])
        else :
            print("File Unknown " + os.path.splitext(images)[0] + "\n")
    detector = MTCNN()
    for i, cl in zip(image, classnames):
        # detecting faces from the image set
        faces = detector.detect_faces(i)
        if faces:
            x1, y1, w, h = faces[0]['box']
            # only one face is choosen from multiples faces
            x2, y2 = x1 + w, y1 + h
            faces = i[y1:y2, x1:x2]
            faces = Image.fromarray(faces)
            faces = faces.resize((224,224))
            # resizing the face to feed into the algorithm
            face_array = asarray(faces)
            pixels = face_array.astype('float32')
            samples = expand_dims(pixels, axis=0)
            samples = preprocess_input(samples, version=2)
            model = VGGFace(model='resnet50', include_top=False, input_shape=(224, 224, 3), pooling='avg')
            # predicting the encoding or feature extracting
            yhat = model.predict(samples)
            print(classnames[count])
            path = 'Encodings'
            with open(os.path.join(path, f'{classnames[count]}.txt'), 'xb') as file:
                # saving the encodings to a folder Encodings with image name as file name
                np.save(file, yhat)
            count = count + 1
        else:
            print(f'Face not detected for {cl} \n')
            continue

encodeFaceData()