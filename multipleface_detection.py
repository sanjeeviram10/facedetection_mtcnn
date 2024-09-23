from mtcnn import MTCNN
import cv2
detector = MTCNN()

img= cv2.imread("img2.jpg")
output = detector.detect_faces(img)
print(output)

for i in output:
    x,y,width,height = i['box']

    left_eyex,left_eyey = i['keypoints']['left_eye']
    right_eyex,right_eyey = i['keypoints']['right_eye']
    nosex,nosey = i['keypoints']['nose']
    mouth_leftx,mouth_lefty = i['keypoints']['mouth_left']
    mouth_rightx,mouth_righty = i['keypoints']['mouth_right']

    cv2.circle(img,center=(left_eyex,left_eyey),color=(255,0,0),thickness=3,radius=2)
    cv2.circle(img,center=(right_eyex,right_eyey),color=(255,0,0),thickness=3,radius=2)
    cv2.circle(img,center=(nosex,nosey),color=(255,0,0),radius=2,thickness=3)
    cv2.circle(img,center=(mouth_leftx,mouth_lefty),color=(255,0,0),radius=2,thickness=3)
    cv2.circle(img,center=(mouth_rightx,mouth_righty),color=(255,0,0),radius=2,thickness=3)
    cv2.rectangle(img,pt1=(x,y),pt2=(x+width,y+height),color=(255,0,0),thickness=3)

cv2.imshow("window",img)
cv2.waitKey(0)


