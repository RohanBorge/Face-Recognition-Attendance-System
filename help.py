from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1800x800+0+0")
        self.root.title("Face Recognition System")


        title_lb1=Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lb1.place(x=0,y=0,width=1540,height=57)


        img_top=Image.open(r"college_images\desk.jpeg")
        img_top=img_top.resize((1540,730),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lb1=Label(self.root,image=self.photoimg_top)
        f_lb1.place(x=0,y=55,width=1540,height=730)

        dev_label=Label(f_lb1,text="Email:-rohanborge71@gmail.com",font=("times new roman",16,"bold"),fg="blue",bg="white")
        dev_label.place(x=550,y=200)

        dev_label1=Label(f_lb1,text="Get a quick support!! ",font=("times new roman",16,"bold"),fg="blue",bg="white")
        dev_label1.place(x=640,y=5)

        dev_label2=Label(f_lb1,text="App Info... ",font=("times new roman",16,"bold"),fg="red",bg="white")
        dev_label2.place(x=8,y=40)

        dev_label2=Label(f_lb1,text=" -A facial recognition attendance system ",font=("times new roman",16,"bold"),fg="blue",bg="white")
        dev_label2.place(x=8,y=80)

        dev_label3=Label(f_lb1,text="uses facial recognition technology to ",font=("times new roman",16,"bold"),fg="blue",bg="white")
        dev_label3.place(x=8,y=120)

        dev_label4=Label(f_lb1,text="identify and verify a person using the ",font=("times new roman",16,"bold"),fg="blue",bg="white")
        dev_label4.place(x=8,y=160)

        dev_label5=Label(f_lb1,text=" features person's facial features and ",font=("times new roman",16,"bold"),fg="blue",bg="white")
        dev_label5.place(x=8,y=200)

        dev_label6=Label(f_lb1,text="automatically mark attendance.",font=("times new roman",16,"bold"),fg="blue",bg="white")
        dev_label6.place(x=8,y=240)

        dev_label7=Label(f_lb1,text="Rules",font=("times new roman",16,"bold"),fg="red",bg="white")
        dev_label7.place(x=8,y=300)

        dev_label8=Label(f_lb1,text="1.Students are required to log into the system.",font=("times new roman",16,"bold"),fg="blue",bg="white")
        dev_label8.place(x=8,y=340)

        dev_label9=Label(f_lb1,text="2.The system administrator should enroll all the",font=("times new roman",16,"bold"),fg="blue",bg="white")
        dev_label9.place(x=8,y=380)

        dev_label10=Label(f_lb1,text=" students who will be using the system.",font=("times new roman",16,"bold"),fg="blue",bg="white")
        dev_label10.place(x=8,y=410)

        dev_label11=Label(f_lb1,text="This involves capturing their facial images ",font=("times new roman",16,"bold"),fg="blue",bg="white")
        dev_label11.place(x=8,y=440)

        dev_label12=Label(f_lb1,text="and storing them securely in the system's database.",font=("times new roman",16,"bold"),fg="blue",bg="white")
        dev_label12.place(x=8,y=470)

        dev_label12=Label(f_lb1,text="3.Students need to click on the take photo sample",font=("times new roman",16,"bold"),fg="blue",bg="white")
        dev_label12.place(x=8,y=520)


        dev_label13=Label(f_lb1,text=" button to add your photo to the database to help us with facial recognition.",font=("times new roman",16,"bold"),fg="blue",bg="white")
        dev_label13.place(x=8,y=550)

        dev_label14=Label(f_lb1,text="4.Then click on train dataset button.",font=("times new roman",16,"bold"),fg="blue",bg="white")
        dev_label14.place(x=8,y=590)

        dev_label15=Label(f_lb1,text="5.Go to the face detectors. They will compare those images to pre-registered images of students in a database. ",font=("times new roman",16,"bold"),fg="blue",bg="white")
        dev_label15.place(x=8,y=630)

        dev_label16=Label(f_lb1,text="6.It will update your attendance status in a database and generate a report.",font=("times new roman",16,"bold"),fg="blue",bg="white")
        dev_label16.place(x=8,y=670)

        # dev_label17=Label(f_lb1,text=" ",font=("times new roman",16,"bold"),fg="blue",bg="white")
        # dev_label17.place(x=8,y=570)



        


        






if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop() 