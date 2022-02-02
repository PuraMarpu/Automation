import cv2 
import os
import dropbox
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')

def AccessCamera():
    camera = cv2.VideoCapture(0)
    Bool = True
    while Bool:
        path, img = camera.read()
        t = cv2.imwrite('something.png', img)
        print(t)
        Bool = False
    
    camera.release()

AccessCamera()

def main():
    Dropb = dropbox.Dropbox('TOKEN')

    with open('something.png', 'rb') as file:
        Dropb.files_upload(file.read(), '/Automation--')

    print('Done')

main()

