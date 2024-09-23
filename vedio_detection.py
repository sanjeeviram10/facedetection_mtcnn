import cv2
from mtcnn import MTCNN

cam = cv2.VideoCapture(0)
detector=MTCNN()

while True:
    ret,frame = cam.read()

    output =  detector.detect_faces(frame)

    for i in output:
        x,y,width,height = i['box']
        cv2.rectangle(frame,pt1=(x,y),pt2=(x+width,y+height),color=(255,0,0),thickness=3)
        


    cv2.imshow('win',frame)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break


cam.release()
cv2.destroyAllWindows()