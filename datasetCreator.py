#dataset Creator
import cv2
import sqlite3
import numpy as np
from playsound import playsound

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam=cv2.VideoCapture(0)

def insertOrUpdate(Id,Name,Sec,RollNo):
    conn=sqlite3.connect("FaceDetection.db")
    cmd="SELECT * FROM Person WHERE ID="+str(Id)
    cursor=conn.execute(cmd)#this will give row by row detail
    isRecordExist=0
    for row in cursor:
        isRecordExist=1
    if(isRecordExist==1):
        cmd="UPDATE Person SET Name"+str(Name)+" WHERE ID="+str(Id)
    else:
        cmd="INSERT INTO Person(ID,Name,Sec,RollNo) Values("+str(Id)+","+str(Name)+","+str(Sec)+","+str(RollNo)+")"
    conn.execute(cmd)#we didn't need cursor as we didn't update it
    conn.commit()
    conn.close()
id=raw_input('enter user id')
name=raw_input('enter your name ( in double quotes )')
sec=raw_input('enter the sec ( in double quotes )')
roll=raw_input('enter the roll no')
insertOrUpdate(id,name,sec,roll)
sampleNum=0;
while(True):
    ret,img=cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5);
    for (x,y,w,h) in faces:
        sampleNum=sampleNum+1;
        cv2.imwrite("dataSet/User."+str(id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.waitKey(100);
    cv2.imshow("Face",img);
    cv2.waitKey(1)
    if(sampleNum>100):
        playsound('sound.mp3')
        break
cam.release()
cv2.destroyAllWindows()
