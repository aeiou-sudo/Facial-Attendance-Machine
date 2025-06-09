import os
import os.path
name = input("Enter name: ")
pathImage = f'images/{name}.jpeg'
pathEncode = f'Encodings/{name}.TXT'
if os.path.isfile(pathImage):
    os.remove(pathImage)
    if os.path.isfile(pathEncode):
        os.remove(pathEncode)
        print(f'{name} is removed from database')
    else:
        print(f'{name} is removed from image set')
elif os.path.isfile(pathEncode):
    os.remove(pathEncode)
    print(f'{name} is removed from encode set')
else:
    print(f'{name} doesn\'t exist')


