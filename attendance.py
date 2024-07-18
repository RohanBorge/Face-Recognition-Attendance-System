from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]

class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1800x800+0+0")
        self.root.title("Face Recognition System")


mydata=[]

class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1800x800+0+0")
        self.root.title("Face Recognition System")

        #=====variables=======
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        

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





        #first image
        img=Image.open(r"college_images\smart-attendance.jpg")
        img=img.resize((800,200),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lb1=Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=750,height=200)

        #second image
        img1=Image.open(r"college_images\Student.jpg")
        img1=img1.resize((800,200),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lb1=Label(self.root,image=self.photoimg1)
        f_lb1.place(x=750,y=0,width=800,height=200)

        #bg image
        img3=Image.open(r"college_images\bg_img1.jpg")
        img3=img3.resize((1800,800),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1800,height=630)

        title_lb1=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkblue")
        title_lb1.place(x=0,y=0,width=1800,height=57)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=60,width=1480,height=600)

        #left side lable
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text=" Student Attendance Details",font=("times new roman",14,"bold"),fg="red")
        Left_frame.place(x=10,y=10,width=770,height=565)

        img_left=Image.open(r"college_images\Student_Handraise.jpeg")
        img_left=img_left.resize((760,130),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lb1=Label(Left_frame,image=self.photoimg_left)
        f_lb1.place(x=5,y=0,width=755,height=120) 

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=2,y=125,width=755,height=350)

        #label entry
        #attendance id
        attendanceId_label=Label(left_inside_frame,text="Attendance ID :",font=("times new roman",12,"bold"),fg="black",bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceId_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",12,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Roll
        rollLable=Label(left_inside_frame,text=" Roll :",font=("times new roman",12,"bold"),fg="black",bg="white")
        rollLable.grid(row=0,column=2,padx=4,pady=8,sticky=W)

        atten_roll=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",12,"bold"))
        atten_roll.grid(row=0,column=3,pady=8,sticky=W)

        #name
        nameLable=Label(left_inside_frame,text="Name :",font=("times new roman",12,"bold"),fg="black",bg="white")
        nameLable.grid(row=1,column=0)

        atten_name=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",12,"bold"))
        atten_name.grid(row=1,column=1,padx=10,pady=5,sticky=W)


        #department
        depLable=Label(left_inside_frame,text="Department :",font=("times new roman",12,"bold"),fg="black",bg="white")
        depLable.grid(row=1,column=2)

        atten_dep=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",12,"bold"))
        atten_dep.grid(row=1,column=3,pady=8,sticky=W)

        #time
        timeLable=Label(left_inside_frame,text="Time :",font=("times new roman",12,"bold"),fg="black",bg="white")
        timeLable.grid(row=2,column=0)

        atten_time=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",12,"bold"))
        atten_time.grid(row=2,column=1,pady=8,sticky=W)

        #Date
        dateLable=Label(left_inside_frame,text="Date:",font=("times new roman",12,"bold"),fg="black",bg="white")
        dateLable.grid(row=2,column=2)

        atten_date=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",12,"bold"))
        atten_date.grid(row=2,column=3,pady=8,sticky=W)

        #Attendance
        attendanceLable=Label(left_inside_frame,text="Attendance Status:",font=("times new roman",12,"bold"),fg="black",bg="white")
        attendanceLable.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font="comicsansns 11 bold",state="readonly")
        self.atten_status["value"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)


        #button frames
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=4,y=300,width=685,height=35)

        save_btn=Button(btn_frame,width=17,text="Import csv ",command=self.importCsv,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0,padx=3)

        update_btn=Button(btn_frame,width=17,text="Export csv",command=self.exportCsv,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1,padx=3)

        update_btn = Button(btn_frame, width=17, text="Update", command=self.update_data, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=2, padx=3)

        reset_btn=Button(btn_frame,width=17,text="Reset",command=self.reset_data,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3,padx=3)













        #right  side lable
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"),fg="red")
        Right_frame.place(x=800,y=10,width=660,height=555)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=645,height=450)

        #=======Scroll bar table===============
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"   #used to remove extra space at the begining of the table
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)


        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)



        #====================fetch data=================
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children()) 
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i) 

    #import csv 
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found to Export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo(" Data Export","Your data exported To"+os.path.basename(fln)+"Successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']  
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")

        # Implement the update_data method in the Attendance class
    def update_data(self):
        selected_row = self.AttendanceReportTable.focus()
        if selected_row:
        # Get the updated values from the Entry widgets
            new_id = self.var_atten_id.get()
            new_roll = self.var_atten_roll.get()
            new_name = self.var_atten_name.get()
            new_dep = self.var_atten_dep.get()
            new_time = self.var_atten_time.get()
            new_date = self.var_atten_date.get()
            new_attendance = self.var_atten_attendance.get()

        # Update the data in mydata list
            for index, row in enumerate(mydata):
                if row[0] == new_id:  # Assuming ID is unique
                    mydata[index] = [new_id, new_roll, new_name, new_dep, new_time, new_date, new_attendance]
                    break

        # Refresh the Treeview with updated data
            self.fetchData(mydata)
            messagebox.showinfo("Update", "Attendance record updated successfully.")
        else:
            messagebox.showerror("Error", "Please select a record to update.")
             

                    
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("Status")

cursor.close()
conn.close()

            








        




if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()  
