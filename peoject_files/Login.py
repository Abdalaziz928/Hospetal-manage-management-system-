from tkinter import *
from tkinter import ttk

from PIL import Image,ImageTk
from tkinter import messagebox
import time
import random
import datetime
from functools import partial

from main import Patient

from main import Employee
	

#window
tkWindow = Tk()  
tkWindow.geometry('1366x768')  
tkWindow.title('نظام ادارة المستشفي')


##### Login page ###
def mangepp():
    
    logwindow = Tk()
    logwindow.geometry('500x500')
    logwindow.title('تسجيل الدخول')
    data = Frame(logwindow,width=500,height=500,bg="dark slate gray")
    data.grid(row=0,column=0)
    username = Label(data,text='اسم المستخدم',bg="dark slate gray",font=("times new roman",12,"bold"))
    username.place(x = 400,y = 50)
    useEnt = Entry(logwindow,width=27,bg='white',font=("times new roman",12,"bold"))
    useEnt.place(x=150,y=50)
    username = Label(data,text='كلمة المرور',bg="dark slate gray",font=("times new roman",12,"bold"))
    username.place(x = 400,y = 150)
    PasEn = Entry(logwindow,width=27,bg='white',font=("times new roman",12,"bold"))
    PasEn.place(x=150,y=150)

    def loginn():
        userName = str(useEnt.get())
        PasWord = str(PasEn.get())

        if userName == 'Admin' and PasWord == '1234':
            if __name__ == "__main__":
                root = Tk()
                app = Patient(root)
                root.mainloop()

            

        # code of run employee

        elif(userName == 'Ahmed' and PasWord == '12345'):
            if __name__ == "__main__":
               pro = Tk()
               app = Employee(pro)
               pro.mainloop()

        else:
            messagebox.showerror("Error","كلمة المرور غير صحيحة")

            logwindow.destroy()


    loginbt = Button(data,text='تسجيل الدخول',font=('arial',12,'bold'),width=10,bg='gold',bd=5,command= loginn)
    loginbt.place(x = 200,y = 200)
    


    

    logwindow.mainloop()


def Ext():
    exitbtn =messagebox.askyesno("Are you sure you want to exit?")
    if exitbtn > 0:
        tkWindow.destroy()


#################### Frams ##############

pagesFrame = Frame(tkWindow,width= 310,height=900,bg= "dark slate gray",bd=20)
pagesFrame.place(x = 1050,y = 0)

img =ImageTk.PhotoImage(Image.open('hos.jpg'))
panel = Label(tkWindow, image = img)
panel.place(x =100, y = 100)


############## PAges buttons 

mangeP = Button(pagesFrame,text="قسم ادارة المرضي",width= 27,height=5,bg="gold",bd=5,command=mangepp)
mangeP.place(x=45,y=100)


mangeP = Button(pagesFrame,text='قسم ادارة الطاقم الطبي',width= 27,height=5,bg="gold",bd = 5 ,command = mangepp)
mangeP.place(x=45,y=200)


mangeP = Button(pagesFrame,text=' بنك الدم',width= 27,height=5,bg="gold",bd = 5)
mangeP.place(x=45,y=300)


mangeP = Button(pagesFrame,text='قسم الاسعاف',width= 27,height=5,bg="gold",bd=5)
mangeP.place(x=45,y=400)

mangeP = Button(pagesFrame,text='خروج',width= 27,height=5,bg="gold",bd=5,command=Ext)
mangeP.place(x=45,y=500)









tkWindow.mainloop()








