from tkinter import*        #tkinter = library used for developed GUI 
from tkinter import ttk 
import tkinter
import _tkinter
from time import strftime
from datetime import datetime    #ttk = stylish toolkit avaialable
from PIL import Image,ImageTk # PIL = For image processing for crop and all
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help


class Face_Recoznization_System: 
    def __init__(self,root):  #for call the init =constructor, argument =self
        self.root=root  #initiliza the root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognization System")

        #First Image
        img=Image.open(r"C:\Users\rohan\OneDrive\Desktop\Face Recognization System\college_images\logo_bvimit.png")
        img=img.resize((250,160),Image.LANCZOS) #resize the image covert higher level image to low level image
        self.photoimg=ImageTk.PhotoImage(img) #var=photoimg,

        first_label=Label(self.root,image=self.photoimg)
        first_label.place(x=0,y=0,width=250,height=160)

        # Title
        
        title_lbl=Label(root,text="BHARATI VIDYAPEETH'S \n Institute of Management & Information Technology \n Navi-Mumbai, Mumbai ",font=("times new roman",30,"bold"),fg="black")
        title_lbl.place(x=290,y=0)

        
        #third image
        img2=Image.open(r"C:\Users\rohan\OneDrive\Desktop\Face Recognization System\college_images\logo_50years.png")
        img2=img2.resize((250, 140),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        first_label=Label(self.root,image=self.photoimg2)
        first_label.place(x=1250,y=0,width=250,height=140)

        
        #bg image
        img3=Image.open(r"C:\Users\rohan\OneDrive\Desktop\Face Recognization System\college_images\bg_img1.jpg")
        img3=img3.resize((1550,740),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=140,width=1550,height=740)
 
                     
        #label title
        title_lb1=Label(bg_img,text="FACE RECOGNIZATION ATTENDENCE SYSTEM SOFTWARE", font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lb1.place(x=0,y=0,width=1550,height=45)

        
        #====================time====================
        def time():
                string = strftime('%H:%M:%S %p')
                lb1.config(text=string)
                lb1.after(1000,time)

        lb1=Label(title_lb1,font=('times new roman',14,'bold'),background='white',foreground='green')
        lb1.place(x=0,y=0,width=110,height=50)
        time()

        #student button
        img4=Image.open(r"C:\Users\rohan\OneDrive\Desktop\Face Recognization System\college_images\Student1.jpg")
        img4=img4.resize((220,220),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)

        #detect face
        img5=Image.open(r"C:\Users\rohan\OneDrive\Desktop\Face Recognization System\college_images\face_detector1.jpg")
        img5=img5.resize((220,220),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)

        #Attendence
        img6=Image.open(r"C:\Users\rohan\OneDrive\Desktop\Face Recognization System\college_images\report.jpg")
        img6=img6.resize((220,220),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendence",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)


        #Help Desk
        img7=Image.open(r"college_images\help_Desk.jpg")
        img7=img7.resize((220,220),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)

        #Train Data
        img8=Image.open(r"C:\Users\rohan\OneDrive\Desktop\Face Recognization System\college_images\Train Data.jpg")
        img8=img8.resize((220,220),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=580,width=220,height=40)

        #Photos Face Button
        img9=Image.open(r"college_images\opencv_face_reco_more_data.jpg")
        img9=img9.resize((220,220),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,command=self.open_img,cursor="hand2")
        b1.place(x=500,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=580,width=220,height=40)

        #Developer
        img10=Image.open(r"C:\Users\rohan\OneDrive\Desktop\Face Recognization System\college_images\KPIs-and-Agile-software-development-metrics-for-teams-1.jpg")
        img10=img10.resize((220,220),Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=800,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=580,width=220,height=40)

        #Exit face button
        img11=Image.open(r"college_images\exit.jpg")
        img11=img11.resize((220,220),Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1100,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=580,width=220,height=40)

   

        # =========function button===========

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    
    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Do you want to exit ?",parent=self.root)   
        if self.iExit>0:
                self.root.destroy()
        else:
                return

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window) 

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window) 

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)  

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)   

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window) 








if __name__ == "__main__": #call main function
    root=Tk()   #call to root with the toolkit(TK)
    obj=Face_Recoznization_System(root)  #class obj 
    root.mainloop()

        