from mtcnn import MTCNN
import cv2
detector = MTCNN()

img= cv2.imread("img1.jpg.webp")
output = detector.detect_faces(img)
print(output)

x,y,width,height = output[0]['box']

left_eyex,left_eyey = output[0]['keypoints']['left_eye']
right_eyex,right_eyey = output[0]['keypoints']['right_eye']
nosex,nosey = output[0]['keypoints']['nose']
mouth_leftx,mouth_lefty = output[0]['keypoints']['mouth_left']
mouth_rightx,mouth_righty = output[0]['keypoints']['mouth_right']

cv2.circle(img,center=(left_eyex,left_eyey),color=(255,0,0),thickness=3,radius=2)
cv2.circle(img,center=(right_eyex,right_eyey),color=(255,0,0),thickness=3,radius=2)
cv2.circle(img,center=(nosex,nosey),color=(255,0,0),radius=2,thickness=3)
cv2.circle(img,center=(mouth_leftx,mouth_lefty),color=(255,0,0),radius=2,thickness=3)
cv2.circle(img,center=(mouth_rightx,mouth_righty),color=(255,0,0),radius=2,thickness=3)
cv2.rectangle(img,pt1=(x,y),pt2=(x+width,y+height),color=(255,0,0),thickness=3)

cv2.imshow("window",img)
cv2.waitKey(0)


