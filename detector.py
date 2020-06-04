#detector
import cv2
import numpy as np
import sqlite3
from PIL import Image
import xlsxwriter
from datetime import datetime
import time
import write
from playsound import playsound

start=time.time()
period=20
faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_detector=cv2.CascadeClassifier("haarcascade_eye.xml")
smile_detector=cv2.CascadeClassifier("haarcascade_smile.xml")
EYE_COUNTER=0
EYE_TOTAL=0
SMILE_COUNTER=0
SMILE_TOTAL=0
cam=cv2.VideoCapture(0)
rec=cv2.createLBPHFaceRecognizer();
rec.load("recognizer\\trainningData.yml")
path='dataSet'
cl=int(0);
rw=int(0);
flag=0;
filename='filename';
dict={
        'item1':1
}
def getProfile(id):
    conn=sqlite3.connect('FaceDetection.db')
    cmd="SELECT * FROM Person WHERE ID="+str(id)
    cursor=conn.execute(cmd)
    profile=None
    for row in cursor:
        profile=row
    conn.close()
    return profile
id=0
nm=0;

font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX,1,1,0,1,1)
while(True):
    ret,img=cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=img[y:y+h,x:x+w]
        eyes=eye_detector.detectMultiScale(roi_gray)
        if len(eyes)==0:
            EYE_COUNTER=1
        else:
            if EYE_COUNTER==1:
                EYE_TOTAL+=1
                EYE_COUNTER=0
            for(ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        smiles=smile_detector.detectMultiScale(roi_gray,1.8,20)
        if len(smiles)==0:
            SMILE_COUNTER=1
        else:
            if SMILE_COUNTER==1:
                SMILE_TOTAL+=1;
                SMILE_COUNTER=0
            for(sx,sy,sw,sh) in smiles:
                cv2.rectangle(roi_color,(sx,sy),(sx+sw,sy+sh),(0,255,0),2)                
        cv2.putText(img,"Blinks: {}".format(EYE_TOTAL),(10,30),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,225),2)
        cv2.putText(img,"Smiles: {}".format(SMILE_TOTAL),(510,30),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,225),2)
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        if(conf<60):
            profile=getProfile(id)
            if(profile!=None):
                cv2.cv.PutText(cv2.cv.fromarray(img),str(profile[1]),(x,y+h+30),font,255);#name
                cv2.cv.PutText(cv2.cv.fromarray(img),str(profile[2]),(x,y+h+60),font,255);#sec
                cv2.cv.PutText(cv2.cv.fromarray(img),str(profile[3]),(x,y+h+90),font,255);#roll
                #cv2.cv.PutText(cv2.cv.fromarray(img),str(profile[0]),(x,y+h+120),font,255);#id
                if((str(id)) not in dict):
                    if(EYE_TOTAL>0 and SMILE_TOTAL>0):
                        print('EYE DETECT count')
                        print(EYE_TOTAL)
                        print('SMILE DETECT count')
                        print(SMILE_TOTAL)
                        filename=write.output('attendance','class1',id,profile[1],'present');
                        dict[str(id)]=str(id);
            else :
                cv2.cv.PutText(cv2.cv.fromarray(img),"unknown",(x,y+h+30),font,255);
                id='unknown'
                flag=flag+1;
                break;
    cv2.imshow("Face",img)
    if flag==10:
        playsound('transactionSound.mp3')
        print("Transaction Blocked")
        break
    if time.time()>start+period:
        playsound('sound.mp3')
        break;
    if(cv2.waitKey(1)==ord('q')):
        break;
cam.release()
cv2.destroyAllWindows()
