from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1800x800+0+0")
        self.root.title("Face Recognition System")


        title_lb1=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lb1.place(x=0,y=0,width=1540,height=57)


        img_top=Image.open(r"college_images\dev.jpg")
        img_top=img_top.resize((1540,730),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lb1=Label(self.root,image=self.photoimg_top)
        f_lb1.place(x=0,y=55,width=1540,height=730)


        #frame
        main_frame=Frame(f_lb1,bd=2,bg="white")
        main_frame.place(x=1000,y=2,width=500,height=300)

        img_top1=Image.open(r"college_images\tony.jpg")
        img_top1=img_top1.resize((200,200),Image.LANCZOS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lb1=Label(main_frame,image=self.photoimg_top1)
        f_lb1.place(x=300,y=0,width=200,height=200)

         #developer info
        dev_label=Label(main_frame,text="Hello ! i am Rohan.",font=("times new roman",16,"bold"),fg="black",bg="white")
        dev_label.place(x=0,y=5)

        dev_label1=Label(main_frame,text="I am currently studying MCA.",font=("times new roman",16,"bold"),fg="black",bg="white")
        dev_label1.place(x=0,y=35)

        dev_label2=Label(main_frame,text="This is my sem 2 project,",font=("times new roman",16,"bold"),fg="black",bg="white")
        dev_label2.place(x=0,y=70)

        dev_label3=Label(main_frame,text="Facial Recognition Attendance",font=("times new roman",16,"bold"),fg="black",bg="white")
        dev_label3.place(x=0,y=105)

        dev_label4=Label(main_frame,text="System.",font=("times new roman",16,"bold"),fg="black",bg="white")
        dev_label4.place(x=0,y=140)















if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()         