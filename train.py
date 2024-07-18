#5

from tkinter import*        #tkinter = library used for developed GUI 
from tkinter import ttk     #ttk = stylish toolkit avaialable
from PIL import Image,ImageTk # PIL = For image processing for crop and all
from tkinter import messagebox
import mysql.connector
import cv2
import  os
import numpy as np


class Train: 
    def __init__(self,root):  #for call the init =constructor, argument =self
        self.root=root  #initiliza the root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognization System")



        title_lb1=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lb1.place(x=0,y=0,width=1550,height=57)

        img_top=Image.open(r"C:\Users\rohan\OneDrive\Desktop\Face Recognization System\college_images\facialrecognition.png")
        img_top=img_top.resize((1530,315),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lb1=Label(self.root,image=self.photoimg_top)
        f_lb1.place(x=0,y=55,width=1535,height=250)

        #button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="red",fg="white")
        b1_1.place(x=0,y=300,width=1535,height=60)


        img_bottom=Image.open(r"C:\Users\rohan\OneDrive\Desktop\Face Recognization System\college_images\ai.jpeg")
        img_bottom=img_bottom.resize((1530,490),Image.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lb1=Label(self.root,image=self.photoimg_bottom)
        f_lb1.place(x=0,y=360,width=1535,height=490)


    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #geray  scale image
            imageNp=np.array(img,'uint8')    #unit8 is a datatype
            id=int(os.path.split(image)[1].split('.')[1])


          #  D:\Python Project TY\data\user.3.20.jpg
          # 0                         from \user index 1 is started 


            faces.append(imageNp) 
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
           


        #===============================train the classifier and save==============
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        # clf.write("classifier.xml")
        # clf.write("classifier.xml")
        cv2.destroyAllWindows()
        
        messagebox.showinfo("Result","Training dataset Completed!!!")



      




if __name__ == "__main__": #call main function
    root=Tk()   #call to root with the toolkit(TK)
    obj=Train(root)  #class obj 
    root.mainloop()