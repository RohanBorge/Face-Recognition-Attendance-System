from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk  #pip install  pillow
from tkinter import messagebox
import mysql.connector



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
        db_host = os.getenv('DB_HOST', 'localhost')
        db_user = os.getenv('DB_USER', 'root')
        db_password = os.getenv('DB_PASSWORD', 'Rohan@123')
        db_name = os.getenv('DB_NAME', 'face_recognization')
        conn = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )
        cursor = conn.cursor()


        #======================bg image=============

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\rohan\OneDrive\Desktop\Face Recognization System\college_images\bg_img1.jpg")

        lb1_bg=Label(self.root,image=self.bg)
        lb1_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="white")
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
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)


        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        #----------------------------row2

        l_contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

        #-----------------------------row 3
        security_Q=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"))
        self.combo_security_Q["values"]=("Select","Your Birth Place","your bestfriend name","Your pet name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text=" Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)

        #----------------------------------row 4
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
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

            




if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()                 



















