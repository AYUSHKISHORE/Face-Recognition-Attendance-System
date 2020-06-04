#softpage
from Tkinter import *
import os
from datetime import datetime;
from PIL import Image,ImageTk
import urllib2
#creating instance of TK
root=Tk()

photo=ImageTk.PhotoImage(Image.open("C:\\Python27\\working face recg\\best2.jpg"))
root.configure(background='black')

root.geometry("1000x654")
def creator():
    
    os.system("dataSetCreator.py")
    
def train():
    
    os.system("trainner.py")

def takeattend():

    os.system("detector.py")
    

def close():

    root.destroy()

def attend():
    os.startfile("C:\\Python27\\working face recg\\attendance\\"+str(datetime.now().date())+'.xls')
def slide():
    os.startfile("C:\\Python27\\working face recg\\ppt_project"+'.pptx')

def send():
    c=urllib2.urlopen('http://localhost/FaceRecog_emailer/sendmailer.php')
    thpage=c.read()
    print(thpage)

root.title("FACE RECOGNITION ATTENDANCE SYSTEM")
Label(root,image=photo,bg='black',height=650,width=983).grid(row=0,rowspan=380,columnspan=100,sticky=N+E+W+S,padx=7,pady=7)

Button(root,text="DataSet Creator",font=("times new roman",20,'bold','italic'),bg="orange",fg='black',command=creator,height=0,width=18).grid(row=320,column=0,columnspan=2,sticky=W+E+N+S,padx=70,pady=7)

Button(root,text="Train Dataset",font=("times new roman",20,'bold','italic'),bg="orange",fg='black',command=train,height=1,width=18).grid(row=330,column=0,columnspan=2,sticky=N+E+W+S,padx=70,pady=7)

Button(root,text="Recognize + Attendance",font=('times new roman',20,'bold','italic'),bg="orange",fg="black",command=takeattend,height=1,width=18).grid(row=340,column=0,columnspan=2,sticky=N+E+W+S,padx=70,pady=7)

Button(root,text="View Attendance Sheet",font=('times new roman',20,'bold','italic'),bg="orange",fg="black",command=attend,height=1,width=18).grid(row=350,column=0,columnspan=2,sticky=N+E+W+S,padx=70,pady=7)

Button(root,text=" Exit  ",font=('times new roman',20,'bold','italic'),bg="orange",fg="black",command=close,height=1,width=18).grid(row=350,column=96,columnspan=4,sticky=N+E+W+S,padx=60,pady=7)

#Button(root,text="Developers",font=('times new roman',20,'bold','italic'),bg="orange",fg="black",command=close,height=1,width=18).grid(row=330,column=96,columnspan=4,sticky=N+E+W+S,padx=60,pady=7)
Button(root,text="Project Report",font=('times new roman',20,'bold','italic'),bg="orange",fg="black",command=slide,height=1,width=18).grid(row=340,column=96,columnspan=4,sticky=N+E+W+S,padx=60,pady=7)

Button(root,text="Send Attendance",font=('times new roman',20,'bold','italic'),bg="orange",fg="black",command=send,height=1,width=18).grid(row=330,column=96,columnspan=4,sticky=N+E+W+S,padx=60,pady=7)


root.mainloop()
