#this is only smile and eye detector and face without our project configuration
import numpy as np
import cv2
face_detector=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_detector=cv2.CascadeClassifier("haarcascade_eye.xml")
smile_detector=cv2.CascadeClassifier("haarcascade_smile.xml")
EYE_COUNTER=0
EYE_TOTAL=0
SMILE_COUNTER=0
SMILE_TOTAL=0
cap=cv2.VideoCapture(0)
while(True):
    ret,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_detector.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=img[y:y+h,x:x+w]
        eyes=eye_detector.detectMultiScale(roi_gray)
        if len(eyes)==0:
            EYE_COUNTER=1
        else:
            if EYE_COUNTER==1:
                EYE_TOTAL+=1
                EYE_COUNTER=0
            #for(ex,ey,ew,eh) in eyes:
                #cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        smiles=smile_detector.detectMultiScale(roi_gray,1.8,20)
        if len(smiles)==0:
            SMILE_COUNTER=1
        else:
            if SMILE_COUNTER==1:
                SMILE_TOTAL+=1;
                SMILE_COUNTER=0
            #for(sx,sy,sw,sh) in smiles:
                #cv2.rectangle(roi_color,(sx,sy),(sx+sw,sy+sh),(0,255,0),2)
    cv2.putText(img,"Blinks: {}".format(EYE_TOTAL),(10,30),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,225),2)
    cv2.putText(img,"Smiles: {}".format(SMILE_TOTAL),(510,30),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,225),2)
    cv2.putText(img,"maintain blink and smile",(180,460),cv2.FONT_HERSHEY_SIMPLEX,0.7,(225,0,0),2)
    cv2.imshow("frame",img)
    if cv2.waitKey(1)&0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
