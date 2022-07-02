from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

from functools import partial





class Patient:
    def __init__(self,root):
        self.root = root
        self.root.title("Hospetal Management System")
        self.root.geometry("1366x768+0+0")

        ########### variables ##########

        PatientId = StringVar()
        PatientName = StringVar()
        PatientAge = StringVar()
        gander = StringVar()
        PatientAddress = StringVar()
        PatirentMobile = StringVar()
        Date = StringVar()
        Deses = StringVar()
        blood = StringVar()
        clinec = StringVar()
        Numberofroom = StringVar()
        copanion =StringVar()

        detils =StringVar()
       
        lbltitle = Label(self.root,bd = 20,relief=RIDGE,text = "قسم ادارة المرضي",fg = "red",bg="white",font=("times new roman",50,"bold"))
        lbltitle.pack(side= TOP,fill=X)


        ########### data frame #######
        Dataframe = Frame(self.root,bd= 20,relief=RIDGE)
        Dataframe.place(x = 0 ,y = 130,width=1360,height=300)

        dataframelift = Label(Dataframe,bd=5,relief=RIDGE,padx=5,font=("times new roman",12,"bold"))
        dataframelift.place(x = 0 , y=5,width=800,height=250)

        dataframeright = Label(Dataframe,bd=5,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Prescription")
        dataframeright.place(x = 860 , y=5,width=450,height=250) 

        ############# buttons ############
        Buttonframe = Frame(self.root,bd= 20,relief=RIDGE,bg= "white")
        Buttonframe.place(x = 0 ,y = 420,width=1360,height=75)

        ############# Deteils frame ############
        Detailsframe = Frame(self.root,bd=2,relief=RIDGE)
        Detailsframe.place(x = 0 ,y = 500,width=1360,height=200)

        ############ data ##################
        lablId = Label(dataframelift,text= "الرقم القومي",font=("times new roman",12,"bold"),padx=2,pady=6)
        lablId.grid(row = 0,column =1)
        Id = Entry(dataframelift,font=("times new roman",12,"bold"),width=33,textvariable= PatientId)
        Id.grid(row=0,column=0)


        lablnameofpatient = Label(dataframelift,text= "الاسم",font=("times new roman",12,"bold"),padx=2,pady=6)
        lablnameofpatient.grid(row = 1,column =1)
        txtname = Entry(dataframelift,font=("times new roman",12,"bold"),width=33,textvariable=PatientName)
        txtname.grid(row=1,column=0)

        lablAge = Label(dataframelift,text= "السن",font=("times new roman",12,"bold"),padx=2,pady=6)
        lablAge.grid(row = 2,column =1)
        txtAge = Entry(dataframelift,font=("times new roman",12,"bold"),width=33,textvariable= PatientAge)
        txtAge.grid(row=2,column=0)

        lablgender = Label(dataframelift,text= "النوع",font=("times new roman",12,"bold"),padx=2,pady=6)
        lablgender.grid(row = 3,column =1)
        txtgender = ttk.Combobox(dataframelift,font=("times new roman",12,"bold"),width= 31,textvariable=gander)
        txtgender["value"] = ("","mail","femail")
        txtgender.grid(row = 3,column=0)

        lablAddress = Label(dataframelift,text= "العنوان",font=("times new roman",12,"bold"),padx=2,pady=6)
        lablAddress.grid(row = 4,column =1)
        txtAddress = Entry(dataframelift,font=("times new roman",12,"bold"),width=33,textvariable=PatientAddress)
        txtAddress.grid(row=4,column=0)

        lablmobile = Label(dataframelift,text= "رقم الهاتف",font=("times new roman",12,"bold"),padx=2,pady=6)
        lablmobile.grid(row = 5,column =1)
        txtmobile = Entry(dataframelift,font=("times new roman",12,"bold"),width=33,textvariable=PatirentMobile)
        txtmobile.grid(row=5,column=0)


       
        #########################
        lablDate = Label(dataframelift,text= "تاريخ الدخول",font=("times new roman",12,"bold"),padx=2,pady=6)
        lablDate.grid(row = 0,column =4)
        txtDate = Entry(dataframelift,font=("times new roman",12,"bold"),width=33,textvariable=Date)
        txtDate.grid(row=0,column=3)

        lablDeses = Label(dataframelift,text= "امراض مزمنة",font=("times new roman",12,"bold"),padx=2,pady=6)
        lablDeses.grid(row = 1,column =4)
        txtDeses = Entry(dataframelift,font=("times new roman",12,"bold"),width=33,textvariable=Deses)
        txtDeses.grid(row=1,column=3)

        lablblood = Label(dataframelift,text= "فصيلة الدم",font=("times new roman",12,"bold"),padx=2,pady=6)
        lablblood.grid(row = 2,column =4)
        txtblood = Entry(dataframelift,font=("times new roman",12,"bold"),width=33,textvariable=blood)
        txtblood.grid(row=2,column=3)

        lablclinec = Label(dataframelift,text= "القسم التابع له",font=("times new roman",12,"bold"),padx=2,pady=6)
        lablclinec.grid(row = 3,column =4)
        txtclinec = Entry(dataframelift,font=("times new roman",12,"bold"),width=33,textvariable=clinec)
        txtclinec.grid(row=3,column=3)

        lablroomNumber = Label(dataframelift,text= "رقم الغرفة",font=("times new roman",12,"bold"),padx=2,pady=6)
        lablroomNumber.grid(row = 4,column =4)
        txtroom = Entry(dataframelift,font=("times new roman",12,"bold"),width=33,textvariable=Numberofroom)
        txtroom.grid(row=4,column=3)

        lablcompanion = Label(dataframelift,text= "المرافق",font=("times new roman",12,"bold"),padx=2,pady=6)
        lablcompanion.grid(row = 5,column =4)
        txtcompanion = Entry(dataframelift,font=("times new roman",12,"bold"),width=33,textvariable=copanion)
        txtcompanion.grid(row=5,column=3)


        ##############
       


        def Idd():
            d = Id.get()
            return int(d)

        def name():
            n = txtname.get()
            return str(n)

        def age():
            n = txtAge.get()
            return str(n)

        def Gander():
            n = txtgender.get()
            return str(n)

        def address():
            n = txtAddress.get()
            return str(n)

        def mobile():
            n = txtmobile.get()
            return str(n)

        def date():
            n = txtDate.get()
            return str(n)

        def deses():
            n = txtDeses.get()
            return str(n)

        def Blood():
            n = txtblood.get()
            return str(n)

        def Clinec():
            n = txtclinec.get()
            return str(n)

        def Room():
            n = txtroom.get()
            return str(n)

        def Companion():
            n = txtcompanion.get()
            return str(n)



        def rect():
            PatientId.set("")
            PatientName.set("")
            PatientAge.set("")
            gander.set("")
            PatientAddress.set("")
            PatirentMobile.set("")
            Date.set("")
            Deses.set("") 
            blood.set("")
            clinec.set("") 
            Numberofroom.set("") 
            copanion.set("")

            return
            


        def exit_fun(self):
            exitbtn =messagebox.askyesno("Are you sure you want to exit?")
            if exitbtn > 0:
                root.destroy()

        ############ Dataframeright txt ################
        #self.txtprescription = Text(dataframeright,font=("times new roman",12,"bold"),width=54,height=14,padx=2,pady=10)
        #self.txtprescription.grid(row=0,column=0)

        #self.txtdata = Text(Detailsframe,font=("times new roman",12,"bold"),width=168,height=9,padx=2,pady=10)
        #self.txtdata.grid(row=0,column=0)


         # ############# Functionality Daclartion ####

        def get_info(ID):
            conn = mysql.connector.connect(host = "localhost",username= "root",password = "Adminuser",database = "hospetaldb")
            my_cursor = conn.cursor()
            sql = f"SELECT * FROM hospetal1 WHERE Id = {ID}"
            my_cursor.execute(sql)
            myresult = my_cursor.fetchall()
            for x in myresult:

                return x

            conn.commit()
            conn.close()


       



        def Evalution(ID):
            y = get_info(ID)

            if(y == None):
                return True
            else:
                return False

        def update():
            d= str(Id.get())

            if (d == ""):

                messagebox.showerror("Error","Pleas Enter ID")

            else:


                if(d.isnumeric()):
                    d1 = int(d)
                    if(not (Evalution(d1))):
                    
                        
                        x = get_info(d1)
                        list1 = [name(),age(),Gander(),address(),mobile(),date(),deses(),Blood(),Clinec(),Room(),Companion()]
                        list2 = []
                        for i in range(len(list1)):
                            if list1[i] == '':
                                list2.append(x[i+1])

                            else: 
                                list2.append(list1[i])


                        conn = mysql.connector.connect(host = "localhost",username= "root",password = "Adminuser",database = "hospetaldb")
                        mycursor = conn.cursor()

                        sql = """
                        UPDATE hospetal1 SET name = %s, age = %s, gander = %s, address = %s, mobile = %s, date = %s, deses = %s, blood = %s, clinec = %s, room = %s,companion = %s  WHERE Id = %s
                                """
                        val = (list2[0],list2[1],list2[2],list2[3],list2[4],list2[5],list2[6],list2[7],list2[8],list2[9],list2[10],d1)        
                        mycursor.execute(sql,val)
                        conn.commit()
                        conn.close()
                        messagebox.showinfo("success","data has been update")


                    else:
                        messagebox.showerror("Error", "This Id is not exist")

                else:
                    messagebox.showerror("Erro","This id is not valid")


       
        def iPrescriptionData():
            if(str(Id.get()) == ""):

                messagebox.showerror("Error","pleas Enter ID")

            else:

                d= str(Id.get())

                if(d.isnumeric()):
                    d1 = int(d)
                    if(Evalution(d1)):
                            conn = mysql.connector.connect(host = "localhost",username= "root",password = "Adminuser",database = "hospetaldb")
                            my_cursor = conn.cursor()
                            my_cursor.execute("insert into hospetal1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(Idd(),name(),age(),Gander(),address(),mobile(),date(),deses(),Blood(),Clinec(),Room(),Companion()))


                            conn.commit()
                            conn.close()
                            messagebox.showinfo("success","Recording has been insrted")


                    else:
                        messagebox.showerror("Error", "This Id is alrdy exist")

                else:
                    messagebox.showerror("Erro","This id is not valid")







        ############### Buttons #######################
       


        btnprescriptionData = Button(Buttonframe,text="ادراح مريض",font=("times new roman",12,"bold"),bg= "green",width=24,height = 1,command=iPrescriptionData)
        btnprescriptionData.grid(row=0,column=1)    

        btnUpdate = Button(Buttonframe,text="تحديث بيانات",font=("times new roman",12,"bold"),bg= "green",width=24,height = 1,command= update)
        btnUpdate.grid(row=0,column=2)    


        btnDelete = Button(Buttonframe,text="حذف مريض",font=("times new roman",12,"bold"),bg= "green",width=24,height = 1)
        btnDelete.grid(row=0,column=3)    


        btnClear = Button(Buttonframe,text="مسح",font=("times new roman",12,"bold"),bg= "green",width=24,height = 1,command= rect)
        btnClear.grid(row=0,column=4)    


        btnExit = Button(Buttonframe,text="خروج",font=("times new roman",12,"bold"),bg= "green",width=20,height = 1,command=exit_fun)
        btnExit.grid(row=0,column=5) 

        # ################# Table ###############
        # ################# scrolbar ############
        
        scroll_x = ttk.Scrollbar(Detailsframe,orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe,orient= VERTICAL)
        self.hospetal_table = ttk.Treeview(Detailsframe,columns=("ID","Name","Age","Gander","Address","Mobile","Date",
                    "Deses","Blood","clinec","Room","Companion"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side = BOTTOM,fill=X)
        scroll_y.pack(side = RIGHT,fill= Y)
        self.hospetal_table.pack()


        scroll_x.config(command=self.hospetal_table.xview())
        scroll_y.config(command=self.hospetal_table.yview())

        #scroll_x = ttk.Scrollbar(command= self.hospetal_table.xview)
        #scroll_y = ttk.Scrollbar(command= self.hospetal_table.yview)
        
        self.hospetal_table.heading("ID",text = "المرافق")
        self.hospetal_table.heading("Name",text = "رقم الغرفة")
        self.hospetal_table.heading("Age",text = "القسم")
        self.hospetal_table.heading("Gander",text = "فصيلة الدم")
        self.hospetal_table.heading("Address",text = "الامراض المزمنة")
        self.hospetal_table.heading("Mobile",text = "تاريخ الدخول")
        self.hospetal_table.heading("Date",text = "رقم الهاتف")
        self.hospetal_table.heading("Deses",text = "العنوان")
        self.hospetal_table.heading("Blood",text = "النوع")
        self.hospetal_table.heading("clinec",text = "السن")
        self.hospetal_table.heading("Room",text = "الاسم")
        self.hospetal_table.heading("Companion",text = "الرقم القومي")
       

        self.hospetal_table["show"] = "headings"

        
        self.hospetal_table.column("ID",width = 100)
        self.hospetal_table.column("Name",width = 100)
        self.hospetal_table.column("Age",width = 100)
        self.hospetal_table.column("Gander",width = 100)
        self.hospetal_table.column("Address",width = 100)
        self.hospetal_table.column("Mobile",width = 100)
        self.hospetal_table.column("Date",width = 100)
        self.hospetal_table.column("Deses",width = 100)
        self.hospetal_table.column("Blood",width = 100)
        self.hospetal_table.column("clinec",width = 100)
        self.hospetal_table.column("Room",width = 100)
        self.hospetal_table.column("Companion",width = 100)


        
       
        


        self.hospetal_table.pack(fill = BOTH,expand=1)

        def getIfo():
            d= str(Id.get())
            if(d == ""):
                messagebox.showerror("Error","pleas Enter ID")

            else:


                if(d.isnumeric()):
                    d1 = int(d)
                    if(Evalution(d1)):
                        messagebox.showerror("Error", "This Id is not exist")

                    else:
                        
                        x = get_info(Idd())

                        a,b,c,d,e,f,h,i,j,k,l,m = str(x[11]),str(x[10]),str(x[9]),str(x[8]),str(x[7]),str(x[6]),str(x[5]),str(x[4]),str(x[3]),str(x[2]),str(x[1]),str(x[0])
                        self.hospetal_table.insert(parent = '', index='end',text = '',values = (a,b,c,d,e,f,h,i,j,k,l,m))
                        self.hospetal_table.pack()

                        return

                else:
                    messagebox.showerror("Erro","This id is not valid")

            



        #def rect():
            #self.hospetal_table.insert(parent = '', index = 'end',text = '',values= ('','','','','','','','','','','',''))
            #self.hospetal_table.pack()



        btnprescription = Button(Buttonframe,text="استعلام",font=("times new roman",12,"bold"),bg= "green",width=24,height = 1,command= getIfo)
        btnprescription.grid(row=0,column=0)

        btnDelete = Button(Buttonframe,text="حذف مريض",font=("times new roman",12,"bold"),bg= "green",width=24,height = 1)
        btnDelete.grid(row=0,column=3)

class Employee:
    def __init__(self,pro):
        self.pro = pro
        self.pro.title("Hospetal Management System")
        self.pro.geometry("1366x768")
        ## header ####
        lbltitle = Label(self.pro,bd = 20,relief=RIDGE,text= "ادارة الطاقم الطبي",fg = "red",bg="white",font=("times new roman",50,"bold"))
        lbltitle.pack(side= TOP,fill=X)

        


        ####################### Frames ###########
        ########### data frame #######
        Dataframe = Frame(self.pro,bd= 20,relief=RIDGE)
        Dataframe.place(x = 0 ,y = 130,width=1360,height=300)

        dataframelift = Label(Dataframe,bd=5,relief=RIDGE,padx=5,font=("times new roman",12,"bold"))
        dataframelift.place(x = 0 , y=5,width=800,height=250)

        dataframeright = Label(Dataframe,bd=5,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Prescription")
        dataframeright.place(x = 860 , y=5,width=450,height=250) 

        ############# buttons ############
        Buttonframe = Frame(self.pro,bd= 20,relief=RIDGE,bg= "white")
        Buttonframe.place(x = 0 ,y = 420,width=1360,height=75)

        ############# Deteils frame ############
        Detailsframe = Frame(self.pro,bd=2,relief=RIDGE)
        Detailsframe.place(x = 0 ,y = 500,width=1360,height=200)


        ########################## Data ######################
        Id = StringVar()
        name = StringVar()
        age = StringVar()
        address = StringVar()
        mobile = StringVar() 
        joptitle = StringVar()
        Exp = StringVar()
        Degree = StringVar()
        salary = StringVar()
        #############################
        
        ######################################################
        def LAb(X,Y,txt):
            Idlb = Label(dataframelift,text= txt,font = ("arial",12,"bold"))
            Idlb.place(x = X,y = Y)
        ############ DATA ENTRY ###############
        LAb(700,0,"الرقم القومي")
        LAb(730, 50,"الاسم")
        LAb(730, 100,"السن")
        LAb(720, 150,"العنوان")
        LAb(710,200,"رقم الهاتف")
        ###########
        ID = Entry(dataframelift,width= 33,bd=5,font=("arial",8,"bold"))
        ID.place(x = 450,y =5)
        Name = Entry(dataframelift,width= 33,bd=5,font=("arial",8,"bold"))
        Name.place(x = 450,y =55)
        Age = Entry(dataframelift,width= 33,bd=5,font=("arial",8,"bold"))
        Age.place(x = 450,y =105)
        Address = Entry(dataframelift,width= 33,bd=5,font=("arial",8,"bold"))
        Address.place(x = 450,y =155)
        Mobile = Entry(dataframelift,width= 33,bd=5,font=("arial",8,"bold"))
        Mobile.place(x = 450,y =205)

        

        ###############
        LAb(300, 0,"المسمي الوظيفي")
        LAb(300,50,"عدد سنين الخبرة")
        LAb(300,100,"الدرجة العلمية")
        LAb(300, 150, "تاريخ الانضمام")
        LAb(300, 200, "الراتب")

        ###########
        Jop = Entry(dataframelift,width= 33,bd=5,font=("arial",8,"bold"))
        Jop.place(x = 50,y =5)
        Ex = Entry(dataframelift,width= 33,bd=5,font=("arial",8,"bold"))
        Ex.place(x = 50,y =55)
        Deg = Entry(dataframelift,width= 33,bd=5,font=("arial",8,"bold"))
        Deg.place(x = 50,y =105)
        Date = Entry(dataframelift,width= 33,bd=5,font=("arial",8,"bold"))
        Date.place(x = 50,y =155)
        Salary = Entry(dataframelift,width= 33,bd=5,font=("arial",8,"bold"))
        Salary.place(x = 50,y =205)

        

        def getint(data):
            b = data.get()
            return int(b)

        def getstring(data):
            a = data.get()
            return str(a)

        def getfloat(data):
            f = data.get()
            return float(f) 

        #########

        


        


        ########### Table and scroll bar #########

        scroll_x = ttk.Scrollbar(Detailsframe,orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe,orient= VERTICAL)
        self.hospetal_table = ttk.Treeview(Detailsframe,columns=("salary","Date","degree","Ex","job","Mobile","Address","Age","Name","ID"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side = BOTTOM,fill=X)
        scroll_y.pack(side = RIGHT,fill= Y)
        self.hospetal_table.pack()


        scroll_x.config(command=self.hospetal_table.xview())
        scroll_y.config(command=self.hospetal_table.yview())

        #scroll_x = ttk.Scrollbar(command= self.hospetal_table.xview)
        #scroll_y = ttk.Scrollbar(command= self.hospetal_table.yview)
        
        self.hospetal_table.heading("ID",text = "الرقم القومي")
        self.hospetal_table.heading("Name",text = " الاسم")
        self.hospetal_table.heading("Age",text = "السن")
        self.hospetal_table.heading("Address",text = "العنوان")
        self.hospetal_table.heading("Mobile",text = " رقم الهاتف")
        self.hospetal_table.heading("job",text = "المسمي الوظيفي")
        self.hospetal_table.heading("Ex",text = "رقم الهاتف")
        self.hospetal_table.heading("degree",text = "الدرجة العلمية")
        self.hospetal_table.heading("Date",text = "التاريخ")
        self.hospetal_table.heading("salary",text = "الراتب")
        
       

        self.hospetal_table["show"] = "headings"

        
        self.hospetal_table.column("ID",width = 100)
        self.hospetal_table.column("Name",width = 150)
        self.hospetal_table.column("Age",width = 50)
        self.hospetal_table.column("Address",width = 150)
        self.hospetal_table.column("Mobile",width = 100)
        self.hospetal_table.column("job",width = 100)
        self.hospetal_table.column("degree",width = 150)
        self.hospetal_table.column("Date",width = 150)
        self.hospetal_table.column("salary",width = 150)
        


        


    


#if __name__ == "__main__":
#    root = Tk()
#    app = Employee(root)
#    root.mainloop()

        

#if __name__ == "__main__":
#    root = Tk()
#    app = Patient(root)
#    root.mainloop()