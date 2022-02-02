import cv2 
import dropbox

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
    Dropb = dropbox.Dropbox('sl.BBS7VB5Q17zs9UVtik6i-yqA2ppabPmwp8eTsW0KHfnoyMAiBr5OUXf8IE2ZDwJ55McE9PtK9ywpWFsRDOVK7FgE49FMGGyPie4AQ2WTUI_EZQcntfqct6ryRXfUDObhm7t6NDNJwGgM')

    with open('something.png', 'rb') as file:
        Dropb.files_upload(file.read(), '/Automation--')

    print('Done')

main()

