from tkinter.ttk import *
import DP
import cv2
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk

master = tk.Tk()
master.title("Cardiovascular Disease & Treatment Using ML")
master.geometry("1200x650")
#master.resizable(False, False)


def file_opener1():
    checkall="";
    Height=0
    Weight=0
    BPLow=0
    BPHigh=0
    Cholesterol=0
    Glucose=0
    Smoke=0
    Alcohol=0
    Active=0
    Symptoms=0
    age=0
    gender=0
    
    if aa2.get()!='':
        Height=int(str(aa2.get()))
        if int(str(aa2.get()))<100 or int(str(aa2.get()))>250:
            checkall+="Enter Valid Height Value,"
    else:
        checkall+="Enter Height,"

    if aa3.get()!='':
        Weight=int(str(aa3.get()))
        if int(str(aa3.get()))<30 or int(str(aa3.get()))>200:
            checkall+="Enter Valid Weight Value,"
    else:
        checkall+="Enter Weight,"

    if aa4.get()!='':
        BPLow=int(str(aa4.get()))
        if int(str(aa4.get()))<50 or int(str(aa4.get()))>100:
            checkall+="Enter Valid BP Low Value,"
    else:
        checkall+="Enter BP Low,"

    if aa5.get()!='':
        BPHigh=int(str(aa5.get()))
        if int(str(aa5.get()))<100 or int(str(aa5.get()))>200:
            checkall+="Enter Valid BP High Value,"        
    else:
        checkall+="Enter BP High,"

    if aa6.get()!='':
        Cholesterol=int(str(aa6.get()).split("-")[0])
    else:
        checkall+="Select Cholesterol Level,"

    if aa7.get()!='':
        Glucose=int(str(aa7.get()).split("-")[0])
    else:
        checkall+="Select Glucose Level,"

    if aa8.get()!='':
        Smoke=int(str(aa8.get()).split("-")[0])
    else:
        checkall+="Select Smoke,"

    if aa9.get()!='':
        Alcohol=int(str(aa9.get()).split("-")[0])
    else:
        checkall+="Select Alcohol,"

    if aa10.get()!='':
        Active=int(str(aa10.get()).split("-")[0])
    else:
        checkall+="Select Active,"
        
    if aa11.get()!='':
        Symptoms=int(str(aa11.get()).split("-")[0])
    else:
        checkall+="Select Symptoms,"

    if aa12.get()!='':
        age=int(str(aa12.get()))
        if int(str(aa12.get()))<15 or int(str(aa12.get()))>110:
            checkall+="Enter Valid age Value,"        
    else:
        checkall+="Enter age,"

    if aa13.get()!='':
        gender=int(str(aa13.get()).split("-")[0])
    else:
        checkall+="Select Gender,"
        
    if checkall!='':
        messagebox.showinfo(title="Alert Message", message=checkall)
    else:
        print([Height,Weight,BPLow,BPHigh,Cholesterol,Glucose,Smoke,Alcohol,Active,Symptoms,age,gender])
        DP.openNewWindow(master,"cardio_train1.xlsx","cardiovasculartreatment.csv",Height,Weight,BPLow,BPHigh,Cholesterol,Glucose,Smoke,Alcohol,Active,Symptoms,age,gender)


def OpenLR():
    DPLOGISTIC.openNewWindow(master,"cardio_train1.xlsx","cardiovasculartreatment.csv")

    #if bb1.get()!='':
    #    DPLOGISTIC.openNewWindow(master,"cardio_train1.xlsx","cardiovasculartreatment.csv")
    #else:
    #    messagebox.showinfo(title="Alert Message", message="Select a File")

def OpenKNN():
    DPKNN.openNewWindow(master,"cardio_train1.xlsx","cardiovasculartreatment.csv")
    #if bb1.get()!='':
    #    DP.openNewWindow(master,"cardio_train1.xlsx","cardiovasculartreatment.csv")
    #else:
    #    messagebox.showinfo(title="Alert Message", message="Select a File")


label = tk.Label(master ,width=65,text = "Cardiovascular Disease & Treatment",font=("Times New Roman Bold", 25), bg="green", fg="white").grid(row=0, column=0,columnspan=4)


#Ltemp1 = tk.Label(master,width=20,text="hi",font=("arial", 25)).grid(row=1,column=3,padx=20,pady=5)


L1 = tk.Label(master,width=30,text="Set Patient Parameters",font=("Times New Roman", 20),fg="purple").grid(row=1,column=0,padx=20,pady=5,columnspan=2)

L2 = tk.Label(master ,width=20,text = "Height(CM)(100 to 250)",font=("Times New Roman", 15), justify="left").grid(row=2, column=0,padx=5, pady=5)
aa2 = tk.StringVar()
a2 = tk.Entry(master,width=20,textvariable=aa2,font=("Times New Roman", 15)).grid(row=2, column=1,padx=5, pady=5)

L3 = tk.Label(master ,width=20,text = "Weight(KG)(30 to 200)",font=("Times New Roman", 15)).grid(row=3, column=0,padx=5, pady=5)
aa3 = tk.StringVar()
a3 = tk.Entry(master,width=20,textvariable=aa3,font=("Times New Roman", 15)).grid(row=3, column=1,padx=5, pady=5)

L4 = tk.Label(master ,width=20,text = "BP Low(50 to 100)",font=("Times New Roman", 15), justify="left").grid(row=4, column=0,padx=5, pady=5)
aa4 = tk.StringVar()
a4 = tk.Entry(master,width=20,textvariable=aa4,font=("Times New Roman", 15)).grid(row=4, column=1,padx=5, pady=5)

L5 = tk.Label(master ,width=20,text = "BP High(100 to 200)",font=("Times New Roman", 15)).grid(row=5, column=0,padx=5, pady=5)
aa5 = tk.StringVar()
a5 = tk.Entry(master,width=20,textvariable=aa5,font=("Times New Roman", 15)).grid(row=5, column=1,padx=5, pady=5)

L6 = tk.Label(master ,width=20,text = "Cholesterol",font=("Times New Roman", 15)).grid(row=6, column=0,padx=5, pady=5)
aa6 = tk.StringVar()
a6 = ttk.Combobox(master,width=19,textvariable=aa6,font=("Times New Roman", 15))    
a6['values']=('1-Normal','2-High','3-Higher')
a6.grid(row = 6,column = 1,padx=5, pady=5)
a6.current()
#a6 = tk.Entry(master,width=20,textvariable=aa6,font=("Times New Roman italic", 15)).grid(row=6, column=1,padx=5, pady=5)

L7 = tk.Label(master ,width=20,text = "Glucose",font=("Times New Roman", 15)).grid(row=7, column=0,padx=5, pady=5)
aa7 = tk.StringVar()
a7 = ttk.Combobox(master,width=19,textvariable=aa7,font=("Times New Roman", 15))    
a7['values']=('1-Normal','2-High','3-Higher')
a7.grid(row = 7,column = 1,padx=5, pady=5)
a7.current()
#a7 = tk.Entry(master,width=20,textvariable=aa7,font=("Times New Roman italic", 15)).grid(row=7, column=1,padx=5, pady=5)

L8 = tk.Label(master ,width=20,text = "Smoke",font=("Times New Roman", 15)).grid(row=8, column=0,padx=5, pady=5)
aa8 = tk.StringVar()
a8 = ttk.Combobox(master,width=19,textvariable=aa8,font=("Times New Roman", 15))    
a8['values']=('1-No','2-Yes')
a8.grid(row = 8,column = 1,padx=5, pady=5)
a8.current()
#a8 = tk.Entry(master,width=25,textvariable=aa8,font=("Times New Roman italic", 15)).grid(row=8, column=1,padx=5, pady=5)

L9 = tk.Label(master ,width=20,text = "Alcohol",font=("Times New Roman", 15)).grid(row=9, column=0,padx=5, pady=5)
aa9 = tk.StringVar()
a9 = ttk.Combobox(master,width=19,textvariable=aa9,font=("Times New Roman", 15))    
a9['values']=('1-No','2-Yes')
a9.grid(row = 9,column = 1,padx=5, pady=5)
a9.current()
#a9 = tk.Entry(master,width=20,textvariable=aa9,font=("Times New Roman italic", 15)).grid(row=9, column=1,padx=5, pady=5)

L10 = tk.Label(master ,width=20,text = "Active",font=("Times New Roman", 15)).grid(row=10, column=0,padx=5, pady=5)
aa10 = tk.StringVar()
a10 = ttk.Combobox(master,width=19,textvariable=aa10,font=("Times New Roman", 15))    
a10['values']=('1-No','2-Yes')
a10.grid(row = 10,column = 1,padx=5, pady=5)
a10.current()
#a10 = tk.Entry(master,width=20,textvariable=aa10,font=("Times New Roman italic", 15)).grid(row=10, column=1,padx=5, pady=5)

L11 = tk.Label(master ,width=20,text = "Symptoms",font=("Times New Roman", 15)).grid(row=11, column=0,padx=5, pady=5)
aa11 = tk.StringVar()
a11 = ttk.Combobox(master,width=19,textvariable=aa11,font=("Times New Roman", 15))    
a11['values']=('1- Chest pain','2- Left shoulder & arms pain','3- Breath shortness','4- Sweating')
a11.grid(row = 11,column = 1,padx=5, pady=5)
a11.current()
#a11 = tk.Entry(master,width=25,textvariable=aa11,font=("Times New Roman italic", 15)).grid(row=11, column=1,padx=5, pady=5)

L12 = tk.Label(master ,width=20,text = "Age In Year(15 to 110)",font=("Times New Roman", 15)).grid(row=12, column=0,padx=5, pady=5)
aa12 = tk.StringVar()
a12 = tk.Entry(master,width=20,textvariable=aa12,font=("Times New Roman", 15)).grid(row=12, column=1,padx=5, pady=5)

L13 = tk.Label(master ,width=20,text = "Gender",font=("Times New Roman", 15)).grid(row=13, column=0,padx=5, pady=5)
aa13 = tk.StringVar()
a13 = ttk.Combobox(master,width=19,textvariable=aa13,font=("Times New Roman", 15))    
a13['values']=('1-Male','2-Female')
a13.grid(row = 13,column = 1,padx=5, pady=5)
a13.current()
#a13 = tk.Entry(master,width=25,textvariable=aa11,font=("Times New Roman italic", 15)).grid(row=11, column=1,padx=5, pady=5)

btnb2 = tk.Button(master,text="Decision Making Using ML",width=25,command=file_opener1,font=("Times New Roman",15),bg="black", fg="white").grid(row=3, column=2,padx=5, pady=1)

#btn1 = tk.Button(master,text="LOGISTIC REGRESSION",width=50,command=lambda:OpenLR()).grid(row=4, column=2,padx=15, pady=20)

#btn2 = tk.Button(master,text="K-Nearest Neighbour",width=50,command=lambda:OpenKNN()).grid(row=5, column=2,padx=15, pady=20)

#btn3 = tk.Button(master,text="Ensemble classification",width=50,command=lambda:OpenKNN()).grid(row=6, column=2,padx=15, pady=20)

btn4 = tk.Button(master,text="Exit",width=25,command=master.destroy,font=("Times New Roman", 15),bg="black", fg="white").grid(row=4, column=2,padx=5, pady=1)


#btn1 = ttk.Button(window , text="Set",command=lambda:setTextInput("hi")).grid(row=5,column=1)


master.mainloop()
