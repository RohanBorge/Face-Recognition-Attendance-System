from tkinter import*        #tkinter = library used for developed GUI 
from tkinter import ttk     #ttk = stylish toolkit avaialable
from PIL import Image,ImageTk # PIL = For image processing for crop and all
from tkinter import messagebox
import mysql.connector
import cv2


class Student: 
    def __init__(self,root):  #for call the init =constructor, argument =self
        self.root=root  #initiliza the root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognization System")

#======variable======
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

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
        img3=Image.open(r"C:\Users\rohan\OneDrive\Desktop\Face Recognization System\college_images\Bg3.jpeg")
        img3=img3.resize((1550,740),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=140,width=1550,height=740)
                     
#label title
        title_lb1=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM", font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lb1.place(x=0,y=0,width=1550,height=45)

        main_frame=Frame(bg_img,bd=3,bg="white")
        main_frame.place(x=0,y=47,width=1800,height=750)

#left side lable
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",14,"bold"),fg="black")
        Left_frame.place(x=10,y=10,width=740,height=575)

        img_left=Image.open(r"C:\Users\rohan\OneDrive\Desktop\Face Recognization System\college_images\raisinghand.jpg")
        img_left=img_left.resize((760,130),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lb1=Label(Left_frame,image=self.photoimg_left)
        f_lb1.place(x=5,y=0,width=725,height=120)

#current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",14,"bold"),fg="red")
        current_course_frame.place(x=5,y=125,width=725,height=120)

#department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),fg="black",bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=20,state="readonly")
        dep_combo["values"]=("Select Department","Engineering","IT","Diploma","Pharmacy","Hotel Management",)
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

#Course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),fg="black",bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=20,state="readonly")
        course_combo["values"]=("Select Course","MCA","MBA","MMS","BCA","Bio-Tech","M.pharm","D.Pharm","M.sc","B.Tech","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

#year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),fg="black",bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=20,state="readonly")
        year_combo["values"]=("Select Year","2022-23","2023-24","2024-25","2025-26")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

#semester
        sem_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),fg="black",bg="white")
        sem_label.grid(row=1,column=2,padx=10,sticky=W)

        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=20,state="readonly")
        sem_combo["values"]=("Select Semester","sem-I","sem-II","sem-III","sem-IV","sem-V","sem-VI")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

       

#class student information
        class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",14,"bold"),fg="red")
        class_Student_frame.place(x=5,y=250,width=725,height=230)

#student id
        studentId_label=Label(class_Student_frame,text="Student ID :",font=("times new roman",12,"bold"),fg="black",bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentId_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

#student name
        studentName_label=Label(class_Student_frame,text="Student Name :",font=("times new roman",12,"bold"),fg="black",bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

#class division
        class_div_label=Label(class_Student_frame,text="Class Division :",font=("times new roman",12,"bold"),fg="black",bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        # class_div_entry=ttk.Entry(class_Student_frame,textvariable=self.var_div,width=20,font=("times new roman",12,"bold"))
        # class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        div_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),width=18,state="readonly")
        div_combo["values"]=("A","B","C")
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        div_combo.current(0)



#Roll no
        roll_no_label=Label(class_Student_frame,text="Roll No :",font=("times new roman",12,"bold"),fg="black",bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_Student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

#gender
        gender_label=Label(class_Student_frame,text="Gender :",font=("times new roman",12,"bold"),fg="black",bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=18,state="readonly")
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        gender_combo.current(0)


#DOB
        DOB_label=Label(class_Student_frame,text="DOB :",font=("times new roman",12,"bold"),fg="black",bg="white")
        DOB_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        DOB_entry=ttk.Entry(class_Student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        DOB_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

#Email
        email_label=Label(class_Student_frame,text="Email :",font=("times new roman",12,"bold"),fg="black",bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_Student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
#phone no
        phone_label=Label(class_Student_frame,text="Phone No :",font=("times new roman",12,"bold"),fg="black",bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_Student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

#teacher name
        teacher_label=Label(class_Student_frame,text="Teacher Name :",font=("times new roman",12,"bold"),fg="black",bg="white")
        teacher_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_Student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #Address no
        address_label=Label(class_Student_frame,text="Address :",font=("times new roman",12,"bold"),fg="black",bg="white")
        address_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_Student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0)

        self.var_radio2=StringVar()
        radiobtn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=5,column=1)

        #button frames
        btn_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=480,width=725,height=35)

        save_btn=Button(btn_frame,width=19,text="Save",command=self.add_data,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0,padx=1)

        update_btn=Button(btn_frame,width=19,text="Update",command=self.update_data,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1,padx=2)

        delete_btn=Button(btn_frame,width=19,text="Delete",command=self.delete_data,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2,padx=3)

        reset_btn=Button(btn_frame,width=19,text="Reset",command=self.reset_data,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3,padx=4)

        btn_frame1=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=5,y=513,width=725,height=35)

        take_photo_btn=Button(btn_frame1,width=39,command=self.generate_dataset,text="Take Photo Sample",font=("times new roman",12,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,width=39,text="UpdatePhoto Sample",font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1,padx=2)

         #Right side lable
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",14,"bold"),fg="black")
        Right_frame.place(x=770,y=10,width=740,height=575)

        img_right=Image.open(r"C:\Users\rohan\OneDrive\Desktop\Face Recognization System\college_images\Student1.jpg")
        img_right=img_right.resize((760,130),Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lb1=Label(Right_frame,image=self.photoimg_right)
        f_lb1.place(x=5,y=0,width=725,height=120)


        #======Search System==========

        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",14,"bold"),fg="red")
        Search_frame.place(x=5,y=125,width=725,height=68)

        search_label=Label(Search_frame,text="Search By:",font=("times new roman",12,"bold"),fg="black",bg="lightgreen")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(Search_frame,font=("times new roman",12,"bold"),width=15,state="readonly")
        search_combo["values"]=("Select ","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(Search_frame,width=20,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(Search_frame,width=14,text="Search",font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(Search_frame,width=14,text="Show All",font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)

        #=========table frame=========

        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=200,width=725,height=345)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","rollno","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("rollno",text="RollNo")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("rollno",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=120)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


        #===================function declaration=============

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
             try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Rohan@123",database="face_recognization")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                    self.var_dep.get(),
                                                                                                                    self.var_course.get(),
                                                                                                                    self.var_year.get(),
                                                                                                                    self.var_semester.get(),
                                                                                                                    self.var_std_id.get(),
                                                                                                                    self.var_std_name.get(),
                                                                                                                    self.var_div.get(),
                                                                                                                    self.var_roll.get(),
                                                                                                                    self.var_gender.get(),
                                                                                                                    self.var_dob.get(),
                                                                                                                    self.var_email.get(),
                                                                                                                    self.var_phone.get(),
                                                                                                                    self.var_address.get(),
                                                                                                                    self.var_teacher.get(),
                                                                                                                    self.var_radio1.get()

                     
                         ))
                
                
                conn.commit()
                self.fetch_data()
                conn.close() 
                messagebox.showinfo("Success", "Student details has been Added Successfully" ,parent=self.root)
             except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)   
                        
    #========fetch data====================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Rohan@123",database="face_recognization")
        my_cursor=conn.cursor()  
        my_cursor.execute("select * from Student")
        data=my_cursor.fetchall()

        if len(data)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                        self.student_table.insert("",END,values=i)
                conn.commit() #beacause data will be continued add
        conn.close()     


        #======get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
       
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])


#Update function 
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
             try:
                 Update=messagebox.askyesno("Update","Do you want to update this students details",parent=self.root)
                 if Update>0:
                     conn=mysql.connector.connect(host="localhost",username="root",password="Rohan@123",database="face_recognization")
                     my_cursor=conn.cursor() 
                     my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                    
                                                                                                                    self.var_dep.get(),
                                                                                                                    self.var_course.get(),
                                                                                                                    self.var_year.get(),
                                                                                                                    self.var_semester.get(),
                                                                                                                    
                                                                                                                    self.var_std_name.get(),
                                                                                                                    self.var_div.get(),
                                                                                                                    self.var_roll.get(),
                                                                                                                    self.var_gender.get(),
                                                                                                                    self.var_dob.get(),
                                                                                                                    self.var_email.get(),
                                                                                                                    self.var_phone.get(),
                                                                                                                    self.var_address.get(),
                                                                                                                    self.var_teacher.get(),
                                                                                                                    self.var_radio1.get(),
                                                                                                                    self.var_std_id.get()
                                                                                      
                                                                                                           
                     ))
                 else:
                      if not Update:
                           return
                 messagebox.showinfo("Success","Student Details successfully update completed",parent=self.root)
                 conn.commit()
                 self.fetch_data()
                 conn.close()
                 
             except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


#delete function
    def delete_data(self):
        if self.var_std_id.get=="":
                messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
                try:
                        delete=messagebox.askyesno("Student Delete Page ","Do you want to Delete this Students Record",parent=self.root)
                        if delete>0:
                                conn=mysql.connector.connect(host="localhost",username="root",password="Rohan@123",database="face_recognization")
                                my_cursor=conn.cursor()
                                sql="delete from student where Student_id=%s"
                                val=(self.var_std_id.get(),)
                                my_cursor.execute(sql,val)
                        else:
                                if not delete:
                                        return
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Delete","Successfully Deleted Student Record",parent=self.root)
                except Exception as es:
                        messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)  

 
    #Reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course ")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")


    #========================= generate data set or set a photo sample=========
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                messagebox.showerror("Error","All Fields are required",parent=self.root)

        else:
                try:
                        conn=mysql.connector.connect(host="localhost",username="root",password="Rohan@123",database="face_recognization")
                        my_cursor=conn.cursor()
                        my_cursor.execute("select *from student")
                        myresult=my_cursor.fetchall()
                        id=0
                        for x in myresult:
                                id+=1
                        my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(

                                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                                        self.var_std_id.get()==id+1
                                                                                                                                                                                                 ))
                        conn.commit()
                        self.fetch_data()
                        self.reset_data()
                        conn.close()


                        # =====load predefined data on face frontal from opencv=======
                        face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                        def face_cropped(img):
                                gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                                faces=face_classifier.detectMultiScale(gray,1.3,5)
                                #sacling factor=1.3 
                                #minimum neighbor=5

                                for(x,y,w,h) in faces:
                                        face_cropped=img[y:y+h,x:x+w]
                                        return face_cropped

                        cap=cv2.VideoCapture(0)
                        img_id=0
                        while True:
                                ret,my_frame=cap.read()
                                if face_cropped(my_frame) is not None:
                                        img_id+=1
                                        face=cv2.resize(face_cropped(my_frame),(450,450))
                                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                                        cv2.imwrite(file_name_path,face)
                                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                                        cv2.imshow("Cropped Face",face)

                                if cv2.waitKey(1)==13 or int(img_id)==100:
                                        break
                        cap.release()
                        cv2.destroyAllWindows()
                        messagebox.showinfo("Result","Generating data sets completed..")

                except Exception as es:
                        messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)






if __name__ == "__main__": #call main function
    root=Tk()   #call to root with the toolkit(TK)
    obj=Student(root)  #class obj 
    root.mainloop()

