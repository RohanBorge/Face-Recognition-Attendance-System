from tkinter import*        #tkinter = library used for developed GUI 
from tkinter import ttk     #ttk = stylish toolkit avaialable
from PIL import Image,ImageTk # PIL = For image processing for crop and all
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import  os
import numpy as np
import csv
import tkinter as tk



class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.current_session = None  # Initialize current_session attribute

        # Initialize GUI elements and image placeholders
        self.initialize_gui()

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

    def initialize_gui(self):
        title_lb1 = tk.Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lb1.place(x=0, y=0, width=1550, height=57)

        img_top = Image.open(r"C:\Users\rohan\OneDrive\Desktop\Face Recognization System\college_images\face_detector1.jpg")
        img_top = img_top.resize((650, 700), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lb1 = tk.Label(self.root, image=self.photoimg_top)
        f_lb1.place(x=0, y=56, width=650, height=700)

        img_bottom = Image.open(r"C:\Users\rohan\OneDrive\Desktop\Face Recognization System\college_images\Train Data.jpg")
        img_bottom = img_bottom.resize((950, 700), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lb2 = tk.Label(self.root, image=self.photoimg_bottom)
        f_lb2.place(x=650, y=56, width=950, height=700)

        b1_1 = tk.Button(f_lb2, text="Face Recognition", cursor="hand2", command=self.face_recog, font=("times new roman", 18, "bold"), bg="peachpuff", fg="firebrick")
        b1_1.place(x=360, y=620, width=200, height=40)

    def mark_attendance(self, i, r, n, d):
        if self.current_session is None:
            with open("Students.csv", "a", newline="\n") as f:
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                writer = csv.writer(f)
                writer.writerow([i, r, n, d, dtString, d1, "Present"])
                self.current_session = True  # Set current_session flag after marking attendance

    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                

                conn=mysql.connector.connect(host="localhost",username="root",password="Rohan@123",database="face_recognization")
                my_cursor=conn.cursor()
                 
                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n) if n else "N/A"

              
            
                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r) if r else "N/A"

                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d) if d else "N/A"

                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i) if i else "N/A"

                

                

            
                if confidence>85:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Dep:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    self.mark_attendance(i,r,n,d)
                    

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                coord=[x,y,w,h]
            
            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img

        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)  # we use 0 bcoz we use laptop camera here to recognize the face

        
        while True:
            ret,img=video_cap.read()
            if not ret:
                print("Failed to grab frame")
                break
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recogintion",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
        return

if __name__ == "__main__":
    root = tk.Tk()
    obj = Face_Recognition(root)
    root.mainloop()
