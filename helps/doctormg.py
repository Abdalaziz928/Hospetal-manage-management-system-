import time
import random
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

class Doctor():
    def __init__(self,root):
        self.root = root 
        self.root.title("Doctor Managment System")
        self.root.geometry("1400x900")
        self.root.configure(background ="black")

        ################# we will Declare all function together ######
        Date_of_Registration = StringVar()
        Date_of_Registration.set(time.strftime("%d/%m/%y"))
        DrId = StringVar()
        Drname  = StringVar()
        DateofBirth  = StringVar()
        Spes  = StringVar()
        Govtpri = StringVar()
        surgeries  = StringVar()
        Experiences = StringVar()
        Nurses  = StringVar()
        Drmobile = StringVar()
        PtName = StringVar()
        Apptime = StringVar()
        ptAge  = StringVar()
        PatientAddress  = StringVar()
        Ptmobile = StringVar()
        Disease = StringVar()
        case  = StringVar()
        BenfitCard = StringVar()

        def exitbtn():
            exitbtn =tkinter.messagebox.askyesno("Doctor Managment system","Are you sure you want to exit?")
            if exitbtn > 0:
                root.destroy()

        def resetfunc():
            DrId.set("")
            Drname.set("")
            DateofBirth.set("")
            Spes.set("")
            Govtpri.set("")
            surgeries.set("")
            Experiences.set("")
            Nurses.set("")
            Drmobile.set("")
            PtName.set("")
            Apptime.set("")
            ptAge.set("")
            PatientAddress.set("")
            Ptmobile.set("")
            Disease.set("")
            case.set("")
            BenfitCard.set("")
        def deletrfun():
            pass

        def presctptiondatafun():
            pass
        def presctptionfun():
            pass


        ############ Title lable ###########
        title = Label(self.root,text= "Doctor Management System",font= ("monotype corsiva",42,"bold"),bd= 5,relief= GROOVE,bg="#b7d8d6",fg="black")
        title.pack(side= TOP,fill=X)
        #### frame
        Manage_Frame = Frame(self.root, width= 1510,height= 400, bd= 5,relief= RIDGE, bg= "#789e9e")
        Manage_Frame.place(x=0,y=80)

        Buttons_Frame = Frame(self.root, width= 200,height= 55, bd= 4,relief= RIDGE, bg= "#eef3db")
        Buttons_Frame.place(x=0,y=460)

        Data_FrameLeft = LabelFrame(Manage_Frame, width= 1510,text="General Information",font=("arial",12,"italic bold"),height= 390, bd= 7,pady=1,relief= RIDGE, bg= "#789e9e")
        Data_FrameLeft.pack(side= LEFT)

        Data_Framedata = LabelFrame(self.root, width= 1510,text= "Doctor Details",font= ("arial",12,"italic bold"),height= 390, bd= 7,relief= RIDGE, bg= "#b7d8d6")
        Data_Framedata.place(x = 0, y = 520)

        Data_FrameRight = LabelFrame(Manage_Frame, width= 1510,text= "Patents Information",font= ("arial",15,"italic bold"),height= 390, bd= 7,relief= RIDGE, bg= "#789e9e")
        Data_FrameRight.pack(side=LEFT)

        

        DrIdlbl = Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Doctor ID",bg="#789e9e")
        DrIdlbl.grid(row= 0,column=0,padx= 10 ,pady=5,sticky= W)
        DrIdtxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=DrId)
        DrIdtxt.grid(row= 0,column=1,padx= 10 ,pady=5,sticky= E)

        DrNamelbl = Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Doctor Name",bg="#789e9e")
        DrNamelbl.grid(row= 1,column=0,padx= 10 ,pady=5,sticky= W)
        DrNametxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=Drname)
        DrNametxt.grid(row= 1,column=1,padx= 10 ,pady=5,sticky= E)

       

        Dateofbirthlbl = Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Date of birht",bg="#789e9e")
        Dateofbirthlbl.grid(row= 2,column=0,padx= 10 ,pady=5,sticky= W)
        Dateofbirthtxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=DateofBirth)
        Dateofbirthtxt.grid(row= 2,column=1,padx= 10 ,pady=5,sticky= E)

        Speslbl = Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Specialisation",bg="#789e9e")
        Speslbl.grid(row= 3,column=0,padx= 10 ,pady=5,sticky= W)
        Speslbltxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=Spes)
        Speslbltxt.grid(row= 3,column=1,padx= 10 ,pady=5,sticky= E)

        GovtPrilbl = Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Gov/Privte",padx=2,bg="#789e9e")
        GovtPrilbl.grid(row= 4,column=0,padx= 10,pady = 5,sticky= W)
        GovtPricmb = ttk.Combobox(Data_FrameLeft,width=25,textvariable=Govtpri,state= "randomly",font=("arial",12,"bold"))
        GovtPricmb['values'] = ("","Government","Private")
        GovtPricmb.current(0)
        GovtPricmb.grid(row= 4,column=1,padx= 10 ,pady=5,sticky= E)


        Surgerieslbl = Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Total Surgeries",bg="#789e9e")
        Surgerieslbl.grid(row= 5,column= 0,padx= 10 ,pady=5,sticky= W)
        Surgerieslbltxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=surgeries)
        Surgerieslbltxt.grid(row= 5,column=1,padx= 10 ,pady=5,sticky= E)

        Experiencelbl = Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Experience in years",bg="#789e9e")
        Experiencelbl.grid(row= 6,column=0,padx= 10 ,pady=5,sticky= W)
        Experiencelbltxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=Experiences)
        Experiencelbltxt.grid(row= 6,column=1,padx= 10 ,pady=5,sticky= E)


        Nurseslbl = Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Nurses under Dr",bg="#789e9e")
        Nurseslbl.grid(row= 7,column=0,padx= 10 ,pady=5,sticky= W)
        Nursestxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=Nurses)
        Nursestxt.grid(row= 7,column=1,padx= 10 ,pady=5,sticky= E)

        DrMobilelbl = Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Doctor Mobile No",bg="#789e9e")
        DrMobilelbl.grid(row= 8,column=0,padx= 10 ,pady=5,sticky= W)
        DrMobiletxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=Drmobile)
        DrMobiletxt.grid(row= 8,column=1,padx= 10 ,pady=5,sticky= E)

        Datelbl = Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Date",bg="#789e9e")
        Datelbl.grid(row= 0,column=2,padx= 10 ,pady=5,sticky= W)
        Datetxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=Date_of_Registration)
        Datetxt.grid(row= 0,column=3,padx= 10 ,pady=5,sticky= E)

        PtNamelbl = Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Patient Name",bg="#789e9e",padx=2)
        PtNamelbl.grid(row= 1,column=2,padx= 10 ,pady=5,sticky= W)
        PtNametxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=PtName)
        PtNametxt.grid(row= 1,column=3,padx= 10 ,pady=5,sticky= E)

        Apptimelbl = Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Appointment",bg="#789e9e",padx=2)
        Apptimelbl.grid(row= 2,column=2,padx= 10 ,pady=5,sticky= W)
        Apptimetxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=Apptime)
        Apptimetxt.grid(row= 2,column=3,padx= 10 ,pady=5,sticky= E)


        PtAgelbl = Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Patient Age",bg="#789e9e",padx=2)
        PtAgelbl.grid(row= 3,column=2,padx= 10 ,pady=5,sticky= W)
        PtAgetxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=ptAge)
        PtAgetxt.grid(row= 3,column=3,padx= 10 ,pady=5,sticky= E)

        PtAddresslbl = Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Patient Address",bg="#789e9e",padx=2)
        PtAddresslbl.grid(row= 4,column=2,padx= 10 ,pady=5,sticky= W)
        PtAddresstxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=PatientAddress)
        PtAddresstxt.grid(row= 4,column=3,padx= 10 ,pady=5,sticky= E)

        PtMobilelbl = Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Patient Mobile NO",bg="#789e9e",padx=2)
        PtMobilelbl.grid(row= 5,column=2,padx= 10 ,pady=5,sticky= W)
        PtMobiletxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=Ptmobile)
        PtMobiletxt.grid(row= 5,column=3,padx= 10 ,pady=5,sticky= E)

        Diseaselbl = Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Patient Disease",bg="#789e9e",padx=2)
        Diseaselbl.grid(row= 6,column=2,padx= 10 ,pady=5,sticky= W)
        Diseasetxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=Disease)
        Diseasetxt.grid(row= 6,column=3,padx= 10 ,pady=5,sticky= E)



        
        Caselbl = Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Case",padx=2,bg="#789e9e")
        Caselbl.grid(row= 7,column=2,padx= 10,pady = 5,sticky= W)
        Casecmb = ttk.Combobox(Data_FrameLeft,width=25,textvariable=case,state= "randomly",font=("arial",12,"bold"))
        Casecmb['values'] = ("","New Case","Old")
        Casecmb.current(0)
        Casecmb.grid(row= 7,column=3,padx= 10 ,pady=5,sticky= E)

        BenefitCardlbl = Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Benefit Card",padx=2,bg="#789e9e")
        BenefitCardlbl.grid(row= 8,column=2,padx= 10,pady = 5,sticky= W)
        BenefitCardcmb = ttk.Combobox(Data_FrameLeft,width=25,textvariable=BenfitCard,state= "randomly",font=("arial",12,"bold"))
        BenefitCardcmb['values'] = ("","Ayushman","Health Instance","Senior Citizen","Army card")
        BenefitCardcmb.current(0)
        BenefitCardcmb.grid(row= 8,column=3,padx= 10 ,pady=5,sticky= E)


        ################# Text presctption ###################

        TextPrescription = Text(Data_FrameRight,font=("arial",12,"bold"),width= 55,height= 17,padx= 3,pady= 5)
        TextPrescription.grid(row= 0,column=0)
        TextPrescriptionData = Text(Data_Framedata,font=("arial",12,"bold"),width= 203,height=12)
        TextPrescriptionData.grid(row = 1,column =0 )


        ################ Bottuns #############

        Prescriptionbtn = Button(Buttons_Frame,text="ADD_New_Doctor",bg= "#fe615a",activebackground= "#cc6686",font=("arial",15,"bold"),width=15)
        Prescriptionbtn.grid(row= 0 ,column=0,padx=15)

        DoctorDetailbtn = Button(Buttons_Frame,text="Doctor Detailes",bg= "#fe615a",activebackground= "#cc6686",font=("arial",15,"bold"),width=15)
        DoctorDetailbtn.grid(row= 0 ,column=1,padx=15)

        Resetbtn = Button(Buttons_Frame,text="Reset",bg= "#fe615a",activebackground= "#cc6686",font=("arial",15,"bold"),width=15)
        Resetbtn.grid(row= 0 ,column=2,padx=15)

        Deletebtn = Button(Buttons_Frame,text="Delete",bg= "#fe615a",activebackground= "#cc6686",font=("arial",15,"bold"),width=15)
        Deletebtn.grid(row= 0 ,column=3,padx=15)

        Deletebtn = Button(Buttons_Frame,text="Update",bg= "#fe615a",activebackground= "#cc6686",font=("arial",15,"bold"),width=15)
        Deletebtn.grid(row= 0 ,column=4,padx=15)

        Exitbtn = Button(Buttons_Frame,text="Exit",bg= "#fe615a",activebackground= "#cc6686",font=("arial",15,"bold"),width=15)
        Exitbtn.grid(row= 0 ,column=5,padx=15)


        Prescriptiondatarow = Label(Data_Framedata,bg="White",font=("arial",12,"bold"),text="Data\tDoctor ID\tDate of Birth\tSpecialisation\tGove/privete\tSurgergies\tExperience\tNurses\t\tDr Mobile No")

        Prescriptiondatarow.place(x= 0,y=0)






        

        




        



        










        


