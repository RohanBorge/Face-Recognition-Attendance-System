from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk  #pip install  pillow
from tkinter import messagebox
import mysql.connector
import tkinter
import _tkinter
from time import strftime
from datetime import datetime
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
from main import Face_Recoznization_System
import cv2


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root): 
        self.root=root
        self.root.title("Login")
        self.root.geometry("1800x800+0+0")



# Fetching database credentials from environment variables
db_host = os.getenv('DB_HOST', 'localhost')
db_user = os.getenv('DB_USER', 'root')
db_password = os.getenv('DB_PASSWORD', 'Rohan@123')
db_name = os.getenv('DB_NAME', 'face_recognization')

# Establishing the connection using environment variables
conn = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)
cursor = conn.cursor()

# Your face recognition code logic

# At the end, close the cursor and connection



         #==========variables=============
        # self.var_fname=StringVar()
        # self.var_lname=StringVar()
        # self.var_contact=StringVar()
        self.var_email=StringVar()
        # self.var_securityQ=StringVar()
        # self.var_securityA=StringVar()
        self.var_pass=StringVar()
        # self.var_confpass=StringVar()

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\rohan\OneDrive\Desktop\Face Recognization System\college_images\bg2.jpg")

        lb1_bg=Label(self.root,image=self.bg)
        lb1_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)


        img1=Image.open(r"C:\Users\rohan\OneDrive\Desktop\Face Recognization System\college_images\LoginIconAppl.png")
        img1=img1.resize((100,100),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        #Label
        username=lb1=Label(frame,text="Username",font=("time new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("time new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lb1=Label(frame,text="Password",font=("time new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("time new roman",15,"bold"),show='*')
        self.txtpass.place(x=40,y=250,width=270)

        #icon images
        img2=Image.open(r"C:\Users\rohan\OneDrive\Desktop\Face Recognization System\college_images\lock-512.png")
        img2=img2.resize((25,25),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg2.place(x=650,y=323,width=25,height=25)

        img3=Image.open(r"C:\Users\rohan\OneDrive\Desktop\Face Recognization System\college_images\lock-512.png")
        img3=img3.resize((25,25),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg3.place(x=650,y=394,width=25,height=25)

        #login btn
        loginbtn=Button(frame,text="Login",command=self.login,font=("time new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #register btn
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("time new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=10,y=350,width=170)

        #forget pass btn
        forgetpassbtn=Button(frame,text="Forget Password",command=self.forget_password_window,font=("time new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgetpassbtn.place(x=10,y=385,width=170)


    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)    

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Rohan@123", database="face_recognization")
            my_cursor = conn.cursor()

        # Select query to fetch user based on email and password
        query = "SELECT * FROM register WHERE email = %s AND password = %s"
        values = (self.txtuser.get(), self.txtpass.get())
        my_cursor.execute(query, values)
        
        row = my_cursor.fetchone()  # Fetch the first row

        if row is None:
            messagebox.showerror("Error", "Invalid Username or Password")
        else:
            messagebox.showinfo("Success", "Welcome to our system")

            # Optionally, open the main system window or perform additional actions here
            self.new_window = Toplevel(self.root)
            self.app = Face_Recoznization_System(self.new_window)

        conn.commit()
        conn.close()

    #=============================reset password==============
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select the security question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Rohan@123",database="face_recognization")
            my_cursor=conn.cursor()
            qury=("select * from register where email=%s and securityQ=%s and securityA=%s")
            vlaue=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(qury,vlaue)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")    
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showerror("Info","your password has been reset,Please login new password",parent=self.root2)
                self.root2.destroy()






    #================================================= forget password
    def forget_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Rohan@123",database="face_recognization")
            my_cursor=conn.cursor()
            query="select * from register where email=%s"
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            # print(row)
            
            if row==None:
                messagebox.showerror("Error","Please enter the valid user name!!")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+250")

                l=Label(self.root2,text="Forget Password",font=("times new roman",12,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Questions",font=("times new roman",15,"bold"),bg="gray",fg="black")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"))
                self.combo_security_Q["values"]=("Select","Your Birth Place","your bestfriend name","Your pet name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)

                security_A=Label(self.root2,text=" Security Answer",font=("times new roman",15,"bold"),bg="gray",fg="black")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security.place(x=50,y=180,width=250)
                
                new_password=Label(self.root2,text="Enter New Password",font=("times new roman",15,"bold"),bg="gray",fg="black")
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),bg="red",fg="black")
                btn.place(x=130,y=290)







                    

                








class Register:
    def __init__(self,root): 
        self.root=root
        self.root.title("Register")
        self.root.geometry("1800x800+0+0")

        #==========variables=============
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()


        #======================bg image=============

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\rohan\OneDrive\Desktop\Face Recognization System\college_images\bg_img1.jpg")

        lb1_bg=Label(self.root,image=self.bg)
        lb1_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="gray")
        frame.place(x=520,y=100,width=800,height=550)

        #=======================Left image
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\rohan\OneDrive\Desktop\Face Recognization System\college_images\coffe.JPG")
        left_lb1=Label(self.root,image=self.bg1)
        left_lb1.place(x=50,y=100,width=470,height=550)

        #==========Main Frame
        # frame=Frame(self.root,bg="white")
        # frame.place(x=520,y=100,width=800,height=550)

        register_lb1=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lb1.place(x=20,y=20)


        #======================label and entry=========

        #------------------------row1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="gray")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)


        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="gray",fg="black")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        #----------------------------row2

        l_contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="gray",fg="black")
        l_contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="gray",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

        #-----------------------------row 3
        security_Q=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),bg="gray",fg="black")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"))
        self.combo_security_Q["values"]=("Select","Your Birth Place","your bestfriend name","Your pet name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text=" Security Answer",font=("times new roman",15,"bold"),bg="gray",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)

        #----------------------------------row 4
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="gray",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15),show='*')
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="gray",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15),show='*')
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        #=================check button======
        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree the terms & conditions",font=("times new roman",15,"bold"),onvalue=1,offvalue=0)
        self.checkbtn.place(x=50,y=380)

        #=================buttons===========
        img=Image.open(r"C:\Users\rohan\OneDrive\Desktop\Face Recognization System\college_images\register-now-button1.jpg")
        img=img.resize((180,45),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="white")
        b1.place(x=100,y=430,width=180)

        img1=Image.open(r"C:\Users\rohan\OneDrive\Desktop\Face Recognization System\college_images\loginpng.png")
        img1=img1.resize((150,45),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="white")
        b1.place(x=570,y=480,width=150)


        #===============================function declaration===============
    def register_data(self):
          if self.var_fname.get()== "" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","all fields are required")
          elif self.var_pass.get()!= self.var_confpass.get():
            messagebox.showerror("Error","Password & confirm password must be same ")
          elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and conditions")
          else:
             conn=mysql.connector.connect(host="localhost",username="root",password="Rohan@123",database="face_recognization")
             my_cursor=conn.cursor()
             query=("select * from register where email=%s")
             value=(self.var_email.get(),)
             my_cursor.execute(query,value)
             row=my_cursor.fetchone()
             if row!=None:
                messagebox.showerror("Error","User already exist,please try another email")
             else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                   
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()
                                                                                       
                                                                                       ))
             conn.commit()
             conn.close()
             messagebox.showinfo("Success","Register Successfully",parent=self.root)

    def return_login(self):
        self.root.destroy()         




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


cursor.close()
conn.close()

if __name__=="__main__":
    main()
           
        
        
