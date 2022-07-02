import time
import random
import datetime
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from functools import partial 

from DR_class import Employ

class Doctor():
    def __init__(self,root):
        self.root = root 
        self.root.title("Doctor Managment System")
        self.root.geometry("1200x800")
        self.root.configure(background ="#789e9e")

        ################# we will Declare all function together ######
        Id1 = tk.StringVar()
        Id2 = tk.StringVar()
        Id3 = tk.StringVar()
        name  = tk.StringVar()
        address = tk.StringVar() 
        mobile = tk.StringVar()
        jop = tk.StringVar()
        Date = tk.StringVar()
        Experiences = tk.StringVar()
        Manger = tk.StringVar()
        Spes  = tk.StringVar()
        degree = tk.StringVar()
        Salary = tk.StringVar()
        
        def exitbtn():
            exitbtn =tkinter.messagebox.askyesno("Doctor Managment system","Are you sure you want to exit?")
            if exitbtn > 0:
                root.destroy()

        def resetfunc():
            Id1.set("")
            name.set("")
            Date.set("")
            Spes.set("")
            address.set("")
            Salary.set("")
            Experiences.set("")
            jop.set("")
            mobile.set("")
            degree.set("")
            Manger.set("")
        def exit_fun():
            exitbtn =tkinter.messagebox.askyesno("Are you sure you want to exit?")
            if exitbtn > 0:
                root.destroy()


        
        def Adding():
            e1 = Employ()
            e1.adding(Id1,name,address, mobile, jop, Date,Experiences,Manger, Spes, degree, Salary)

        adding = partial(Adding,Id1,name,address, mobile, jop, Date,Experiences,Manger, Spes, degree, Salary)

       
        def get_info():


            
            e1 = Employ()
            x = e1.get_info(str(Id2))
            a,b,c,d,e,f,h,i,j,k,l = str(x[0]),x[1],x[2],x[3],x[4],x[5],str(x[6]),x[7],x[8],x[9],str(x[10])
            TextPrescription.insert(END,a+"\n\n"+b+"\n\n"+c+"\n\n"+d+"\n\n"+e+"\n\n"+f+"\n\n"+h+"\n\n"+i+"\n\n"+j+"\n\n"+k+"\n\n"+l)
            return 

        ############ Title lable ###########
        title = Label(self.root,text= "Doctor And Nurses Management System",font= ("monotype corsiva",42,"bold"),bd= 5,relief= GROOVE,bg="#b7d8d6",fg="black")
        title.pack(side= TOP,fill=X)
        #### frame
        
        Buttons_Frame = Frame(self.root, width= 1000,height= 300, bd= 4,relief= RIDGE, bg= "#789e9e")
        Buttons_Frame.place(x=0,y=580)

        Data_FrameRight = LabelFrame(self.root, width= 750,text="Registration",font=("arial",12,"italic bold"),height= 390, bd= 7,pady=1,relief= RIDGE, bg= "#789e9e")
        Data_FrameRight.place(x = 600,y = 100)

        Data_FrameLeft = LabelFrame(self.root, width= 1000,text="Information",font=("arial",12,"italic bold"),height= 390, bd= 7,pady=1,relief= RIDGE, bg= "#789e9e")
        Data_FrameLeft.place(x=0,y=100)

        Information = Label(Data_FrameRight,bg = "white",font=("arial",12,"bold"),text = "ID\n\nName\n\nAdress\n\nmobile\n\nJop\n\nDate\n\nExperience\n\nManager\n\nSpecialization\n\nDegree\n\nSalary")
        Information.grid(row = 0,column = 0)

        
        Idlbl = Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="ID",bg="#789e9e")
        Idlbl.grid(row= 0,column=0,padx= 10 ,pady=5,sticky= W)
        Idtxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=Id1)
        Idtxt.grid(row= 0,column=1,padx= 10 ,pady=5,sticky= E)

        Namelbl = Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Name",bg="#789e9e")
        Namelbl.grid(row= 1,column=0,padx= 10 ,pady=5,sticky= W)
        Nametxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=name)
        Nametxt.grid(row= 1,column=1,padx= 10 ,pady=5,sticky= E)

       

        Addresslbl = Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Adress",bg="#789e9e")
        Addresslbl.grid(row= 2,column=0,padx= 10 ,pady=5,sticky= W)
        Addresstxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=address)
        Addresstxt.grid(row= 2,column=1,padx= 10 ,pady=5,sticky= E)

        Mobilelbl = Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Mobile",bg="#789e9e")
        Mobilelbl.grid(row= 3,column=0,padx= 10 ,pady=5,sticky= W)
        Mobiletxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=mobile)
        Mobiletxt.grid(row= 3,column=1,padx= 10 ,pady=5,sticky= E)

        Joblbl = Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Dr or Nurs",padx=2,bg="#789e9e")
        Joblbl.grid(row= 4,column=0,padx= 10,pady = 5,sticky= W)
        Jobcmb = ttk.Combobox(Data_FrameLeft,width=25,textvariable=jop,state= "randomly",font=("arial",12,"bold"))
        Jobcmb['values'] = ("","Doctor","Nurse")
        Jobcmb.current(0)
        Jobcmb.grid(row= 4,column=1,padx= 10 ,pady=5,sticky= E)


        Datelbl = Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Date",bg="#789e9e")
        Datelbl.grid(row= 5,column= 0,padx= 10 ,pady=5,sticky= W)
        Datetxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=Date)
        Datetxt.grid(row= 5,column=1,padx= 10 ,pady=5,sticky= E)

        Experiencelbl = Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Experience",bg="#789e9e")
        Experiencelbl.grid(row= 6,column=0,padx= 10 ,pady=5,sticky= W)
        Experiencetxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=Experiences)
        Experiencetxt.grid(row= 6,column=1,padx= 10 ,pady=5,sticky= E)


        Managerlbl = Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Manger",bg="#789e9e")
        Managerlbl.grid(row= 7,column=0,padx= 10 ,pady=5,sticky= W)
        Managertxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=Manger)
        Managertxt.grid(row= 7,column=1,padx= 10 ,pady=5,sticky= E)

        Speclbl = Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="specialization",bg="#789e9e")
        Speclbl.grid(row= 8,column=0,padx= 10 ,pady=5,sticky= W)
        Spectxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=Spes)
        Spectxt.grid(row= 8,column=1,padx= 10 ,pady=5,sticky= E)

        Degreelbl = Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Degree",padx=2,bg="#789e9e")
        Degreelbl.grid(row= 9,column=0,padx= 10,pady = 5,sticky= W)
        Degreecmb = ttk.Combobox(Data_FrameLeft,width=25,textvariable=degree,state= "randomly",font=("arial",12,"bold"))
        Degreecmb['values'] = ("","B","M","Phd")
        Degreecmb.current(0)
        Degreecmb.grid(row= 9,column=1,padx= 10 ,pady=5,sticky= E)

        Salarylbl = Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Salary",bg="#789e9e")
        Salarylbl.grid(row= 10,column=0,padx= 10 ,pady=5,sticky= W)
        Salarytxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=Salary)
        Salarytxt.grid(row= 10,column=1,padx= 10 ,pady=5,sticky= E)
        

        ############## Information #################

        #Infolbl = Label(Data_FrameRight,font=("arial",12,"bold"),width=20,text="Enter ID",bg="#789e9e")
        #Infolbl.grid(row= 1,column=1,padx= 10 ,pady=5,sticky= W)
        Infotxt = Entry(Data_FrameRight,font=("arial",12,"bold"),width=27,textvariable=Id2)
        Infotxt.grid(row=1,column=1,padx= 10 ,pady=5,sticky= E)

        ############## DELETE ID ################
        Deletelbl = Label(Buttons_Frame,font=("arial",12,"bold"),width=20,text="DELETE",bg="#789e9e")
        Deletelbl.grid(row= 0,column=0,padx= 10 ,pady=5,sticky= W)
        Deletetxt = Entry(Buttons_Frame,font=("arial",12,"bold"),width=27,textvariable=Id3)
        Deletetxt.grid(row= 1,column=0,padx= 10 ,pady=5,sticky= E)


        ################### Buttons #####################
        Addbtn = Button(Data_FrameLeft,text="ADD",bg= "#fe615a",activebackground= "#cc6686",font=("arial",15,"bold"),width=15,command= Adding)
        Addbtn.grid(row= 100 ,column=0,padx=15)

        Updatebtn = Button(Data_FrameLeft,text="Update",bg= "#fe615a",activebackground= "#cc6686",font=("arial",15,"bold"),width=15)
        Updatebtn.grid(row= 100 ,column=1,padx=15)

        Infobtn = Button(Data_FrameRight,text="Information",bg= "#fe615a",activebackground= "#cc6686",font=("arial",15,"bold"),width=15,command= get_info)
        Infobtn.grid(row= 1 ,column=0,padx=15)

        Deletebtn = Button(Buttons_Frame,text="Delete",bg= "#fe615a",activebackground= "#cc6686",font=("arial",15,"bold"),width=15)
        Deletebtn.grid(row= 2 ,column=0,padx=15)

        Resetbtn = Button(Buttons_Frame,text="Reset",bg= "#fe615a",activebackground= "#cc6686",font=("arial",15,"bold"),width=15, command= resetfunc)
        Resetbtn.grid(row= 1 ,column=1,padx=15)

        Exitbtn = Button(Buttons_Frame,text="Exit",bg= "#fe615a",activebackground= "#cc6686",font=("arial",15,"bold"),width=15,command= exit_fun)
        Exitbtn.grid(row= 2 ,column=1,padx=15)



        ################ Text ############################
        TextPrescription = Text(Data_FrameRight,font=("arial",12,"bold"),width= 50,height= 21,padx= 3,pady= 5)
        TextPrescription.grid(row= 0,column=1)
        #TextPrescriptionData = Text(Data_Framedata,font=("arial",12,"bold"),width= 203,height=12)
        #TextPrescriptionData.grid(row = 1,column =0 )


        




       

       














if __name__ == "__main__":
    root = Tk()
    app = Doctor(root)
    root.mainloop()