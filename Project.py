from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from tkinter.font import BOLD
import datetime
from tkinter import Tk, StringVar, messagebox, ttk, END, IntVar, DISABLED, NORMAL

import pymysql

# Creating Class


class PMS:
    def __init__(self, root):
        self.turns = 1
        self.root = root
        self.mainmenu()

# ==================================MAIN MENU=======================================
    def mainmenu(self):
        self.menubar = Menu(self.root)
        self.root.geometry("%dx%d+%d+%d" % (500, 400, 390, 130))
        self.root.config(menu=self.menubar)
        self.Exit_menu = Menu(self.menubar, tearoff=0)
        self.Exit_menu.add_command(label='Exit', command=self.root.destroy)
        self.menubar.add_cascade(label="Exit", menu=self.Exit_menu)
        self.root.iconbitmap(R'myimages\parko.ico')
        self.root.title("Parking Management System")
        # creating help menu option
        self.help_menu = Menu(self.menubar, tearoff=0)

        # add menu items to help menu
        self.help_menu.add_command(label='About')
        self.help_menu.add_command(
        label='Contact us', command="Create and develop by ADITYA")
        self.menubar.add_cascade(label="Help", menu=self.help_menu)

        self.img1 = Image.open("myimages\parking.jpg")
        self.bg_img = ImageTk.PhotoImage(self.img1.resize((500, 450), Image.ANTIALIAS))

        # Creating a Canvas
        self.canvas = Canvas(self.root, width=400, height=450)
        self.canvas.pack(expand=True, fill=BOTH)

        # Adding image in cavas
        self.canvas.create_image(0, 0, image=self.bg_img, anchor="nw")

        self.canvas.create_rectangle(
            10, 160, 485, 200, outline="#c7c5c5", fill="#000000", width=3)

        # Add a text in canvas
        self.canvas.create_text(250, 180, font=("apple-system", 17, BOLD), text="Welcome To Parking Management System", fill="#ffffff")

        btn = Button(self.root, text="ADMIN", fg="Black", bg="#FFFFFF", width=16,
                     bd=6, activebackground="#BBBBBB", command=self.loginWindow).place(x=85, y=210)
        btn1 = Button(self.root, text="OPERATOR", bg="#FFFFFF", width=15, bd=6,
                      activebackground="#BBBBBB", command=self.operatorWindow).place(x=290, y=210)

#==================================FORGOT PASSWORD=================================

    def checkotp(self):
        if self.otp1.get() == str(self.otp):
            self.subForgotFrame()
        else:
            messagebox.showerror("Error","Wrong OTP")    
            exit()
    def otprun(self):
        self.forgotframe = Toplevel(self.root)
        self.forgotframe.title("Parking Management System")
        # Left = int(self.forgotframe.winfo_screenwidth() - 500)/2
        # Top = int(self.forgotframe.winfo_screenheight() - 450)/2
        self.forgotframe.geometry("400x200+450+220")
        self.forgotframe.iconbitmap(R'myimages\parko.ico')
        self.forgotframe['background'] = '#003e53'
        self.forgotframe.resizable(False, False)

        self.otp1 = tk.StringVar()

        # title = Label(self.forgotframe, text="Forgot Password", font=(
        #     "Walbaum Display", 18, "bold"), fg="white", bg="#003e53").place(x=40, y=20)

        # First Row
        vid = Label(self.forgotframe, text="Enter OTP  :", font=(
            "Walbaum Display", 11, "bold"), fg="white", bg="#003e53").place(x=80, y=65)
        txt_vid = Entry(self.forgotframe, font=("apple-system", 11),textvariable=self.otp1
                        ).place(x=190, y=65, width=130)

        btn = Button(self.forgotframe, text="Confirm", font=("Walbaum Display", 10, "bold"),
                     command=self.checkotp, fg="black", bg="light gray", width=10, height=1).place(x=190, y=110)
        

    def forgotten(self):
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        import smtplib
        import random
         
        # create message object instance
        msg = MIMEMultipart()
        
        self.otp = random.randint(1000,9999)
        # print(self.otp)
         
        message = f"Your OTP to reset your password is {self.otp}\nDo not disclose this with anyone\n\nThank You\nRegards\nGroup2"
         
        # setup the parameters of the message
        password = "12345678Aa@"
        msg['From'] = "selfmotivation2000@gmail.com"
        msg['To'] = "abhay.dhupar151785@gmail.com"
        msg['Subject'] = "Reset your PMS password"
         
        # add in the message body
        msg.attach(MIMEText(message, 'plain'))
         
        #create server
        server = smtplib.SMTP('smtp.gmail.com: 587')
         
        server.starttls()
         
        # Login Credentials for sending the mail
        server.login(msg['From'], password)
         
         
        # send the message via the server.
        server.sendmail(msg['From'], msg['To'], msg.as_string())
         
        server.quit()
     
        # print ("successfully sent email to %s:" % (msg['To']))
        messagebox.showinfo("Forgot","Send an mail to abh*************85.com")
        self.Loginwin.destroy()

        self.otprun()
# =================================LOGIN WINDOW====================================
    
    def loginWindow(self):
        self.Loginwin = Toplevel(self.root)
        self.Loginwin.title("Parking Management System")
        self.Loginwin.geometry("400x200+450+220")
        self.Loginwin["bg"] = "#003e53"
        self.Loginwin.iconbitmap(R'myimages\parko.ico')
        self.user_var = tk.StringVar()
        self.pass_var = tk.StringVar()
        
        self.userid = Label(self.Loginwin, text="Username : ", bg="#003e53", fg="white", font=("apple-system", 10, "bold")).place(x=60, y=45)
        self.txt_user = Entry(self.Loginwin, font=("apple-system", 10), textvariable=self.user_var).place(x=140, y=45, width=200)
        self.password = Label(self.Loginwin, text="Password : ", bg="#003e53", fg="white", font=("apple-system", 10, "bold")).place(x=60, y=75)
        self.txt_pass = Entry(self.Loginwin, font=("apple-system", 10,"bold"),show="*", textvariable=self.pass_var).place(x=140, y=75, width=200)
        
        self.Log_but = Button(self.Loginwin, text="Login", width=15,command=self.login)
        self.Log_but.place(x=140, y=120)
        
        self.Forgot = Button(self.Loginwin, text="forgot password?",bg="white",fg='blue', width=15,command=self.forgotten)
        self.Forgot.place(x=260, y=120)

        
        

    def login(self):
        import pymysql as pm

        con = pm.connect(host="localhost", user="root", password="", db="parking management")
        
        cur = con.cursor()
        cur.execute("select userid,password from admincred")
        both = cur.fetchall()
        self.id = both[0][0]
        self.passw = both[0][1]
        if self.id == self.user_var.get().lower() and self.passw == self.pass_var.get():
            messagebox.showinfo("Login Info", "Login Successful")
            self.Loginwin.destroy()
            self.adminWindow()
        else:
            messagebox.showerror("Error","Invalid id or password")
            self.turns+=1
            if self.turns>3:
                messagebox.showerror("Error","Login limit exceeded")
                exit()
            self.loginWindow()
            
            


# ==================================================================================
#                             ADMIN FRAMES & MENU
# ==================================================================================

    # =======================FRAME 1================================

    def Display(self):
        
        self.Frame1 = Toplevel(self.AdminWindow)
        LeftPos = int(self.Frame1.winfo_screenwidth() - 600)/2
        TopPos = int(self.Frame1.winfo_screenheight() - 450)/2
        self.Frame1.geometry("%dx%d+%d+%d" % (500, 400, LeftPos, TopPos))
        self.Frame1.title("Parking Management System")
        self.Frame1['background'] = '#003e53'
        self.Frame1.resizable(False, False)
        self.Frame1.iconbitmap(R"myimages\parko.ico")
        
        scrollbar = Scrollbar(self.Frame1)
        scrollbar.pack(side=RIGHT, fill=Y)
        textbox = Text(self.Frame1, width=64, height=24)
        label1 = Label(self.Frame1, text="   V no.          V Type    Passengers               Mobile                 Slot acq.           Name                     ", width=69)
        label1.pack()
        
        
        import pymysql as pm

        con = pm.connect(host="localhost", user="root", password="", db="parking management")
        
        cur = con.cursor()
        cur.execute("select Vehicleno,VehicleType,Passengers,Mobile,Slot,Name from information")

        for rows in cur:
            k = 0
            for j in rows:
                if k==0:
                    textbox.insert(END,' ')
                textbox.insert(END,j)
                textbox.insert(END,'\t')
                k+=1
                if k==1:
                    textbox.insert(END,'  ')
                if k==4:
                    textbox.insert(END,'\t')
                

            textbox.insert(END,'\n')
        textbox.config(state=DISABLED)
        textbox.pack()
        
        textbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=textbox.yview)

        
    # =======================SUB FRAME 2 (2 wheeler)================================
    def wheeler2(self):
        self.Frame2.destroy()
        self.subFrame2a = Toplevel(self.AdminWindow)
        LeftPos = int(self.subFrame2a.winfo_screenwidth() - 600)/2
        TopPos = int(self.subFrame2a.winfo_screenheight() - 450)/2
        self.subFrame2a.geometry("%dx%d+%d+%d" % (500, 400, LeftPos, TopPos))
        self.subFrame2a.title("Parking Management System")
        self.subFrame2a['background'] = '#003e53'
        self.subFrame2a.resizable(False, False)
        self.subFrame2a.iconbitmap(R"myimages\parko.ico")

        scrollbar = Scrollbar(self.subFrame2a)
        scrollbar.pack(side=RIGHT, fill=Y)
        textbox = Text(self.subFrame2a, width=64, height=24)
        label1 = Label(self.subFrame2a, text="   V no.          V Type    Passengers               Mobile                 Slot acq.           Name                     ", width=69)
        label1.pack()
        
        
        import pymysql as pm

        con = pm.connect(host="localhost", user="root", password="", db="parking management")
        
        cur = con.cursor()
        cur.execute("select Vehicleno,VehicleType,Passengers,Mobile,Slot,Name from information where VehicleType='2'")

        for rows in cur:
            k = 0
            for j in rows:
                textbox.insert(END,j)
                textbox.insert(END,'\t')
                k+=1
                if k==1:
                    textbox.insert(END,'  ')
                if k==4:
                    textbox.insert(END,'\t')
                

            textbox.insert(END,'\n')
        textbox.config(state=DISABLED)
        textbox.pack()
        
        textbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=textbox.yview)


    # =======================SUB FRAME 2 (4 wheeler)================================
    def wheeler4(self):
        self.Frame2.destroy()
        self.subFrame2b = Toplevel(self.AdminWindow)
        LeftPos = int(self.subFrame2b.winfo_screenwidth() - 600)/2
        TopPos = int(self.subFrame2b.winfo_screenheight() - 450)/2
        self.subFrame2b.geometry("%dx%d+%d+%d" % (500, 400, LeftPos, TopPos))
        self.subFrame2b.title("Parking Management System")
        self.subFrame2b['background'] = '#003e53'
        self.subFrame2b.resizable(False, False)
        self.subFrame2b.iconbitmap(R"myimages\parko.ico")

        scrollbar = Scrollbar(self.subFrame2b)
        scrollbar.pack(side=RIGHT, fill=Y)
        textbox = Text(self.subFrame2b, width=64, height=24)
        label1 = Label(self.subFrame2b, text="   V no.          V Type    Passengers               Mobile                 Slot acq.           Name                     ", width=69)
        label1.pack()
        
        
        import pymysql as pm

        con = pm.connect(host="localhost", user="root", password="", db="parking management")
        
        cur = con.cursor()
        cur.execute("select Vehicleno,VehicleType,Passengers,Mobile,Slot,Name from information where VehicleType='2'")

        for rows in cur:
            k = 0
            for j in rows:
                textbox.insert(END,j)
                textbox.insert(END,'\t')
                k+=1
                if k==1:
                    textbox.insert(END,'  ')
                if k==4:
                    textbox.insert(END,'\t')
                

            textbox.insert(END,'\n')
        textbox.config(state=DISABLED)
        textbox.pack()
        
        textbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=textbox.yview)


    # =======================FRAME 2================================

    def TypeBaseSlot(self):
        self.Frame2 = Toplevel(self.AdminWindow)

        self.Frame2.title("Parking Management System")
        self.Frame2.iconbitmap(R'myimages\parko.ico')

        LeftPos = int(self.Frame2.winfo_screenwidth() - 600)/2
        TopPos = int(self.Frame2.winfo_screenheight() - 450)/2
        self.Frame2.geometry("%dx%d+%d+%d" % (500, 400, LeftPos, TopPos))
        self.Frame2["background"] = '#003e53'

        # Disabling resizable property
        self.Frame2.resizable(False, False)

        lable = Label(self.Frame2, text='Type Base Slots', width=45, height=3, font=(
            "apple-system", 14, BOLD), bg='#003e53', fg="white")
        lable.pack()

        self.img1 = Image.open(R"myimages\2wheeler1.jpg")
        self.final_img1 = ImageTk.PhotoImage(
            self.img1.resize((100, 100), Image.ANTIALIAS))

        self.img2 = Image.open(R"myimages\4wheeler.png")
        self.final_img2 = ImageTk.PhotoImage(
            self.img2.resize((100, 100), Image.ANTIALIAS))

        # Let us create a dummy button and pass the image
        button1 = Button(self.Frame2, image=self.final_img1, borderwidth=2,command=self.wheeler2)
        button2 = Button(self.Frame2, image=self.final_img2, borderwidth=2,command=self.wheeler4)
        button1.pack()
        text = Label(self.Frame2, text='2 Wheeler', bg='black', fg="white")
        text.pack()
        label2 = Label(self.Frame2, text="\n", bg='#003e53')
        label2.pack()
        button2.pack()
        text = Label(self.Frame2, text='4 Wheeler', bg='black', fg="white")
        text.pack()

    # =======================FRAME 3================================
    def slotsInfo(self):
        self.Frame3 = Toplevel(self.AdminWindow)
        LeftPos = int(self.Frame3.winfo_screenwidth() - 600)/2
        TopPos = int(self.Frame3.winfo_screenheight() - 450)/2
        self.Frame3.geometry("%dx%d+%d+%d" % (500, 400, LeftPos, TopPos))
        self.Frame3.title("Parking Management System")
        self.Frame3['background'] = '#003e53'
        self.Frame3.resizable(False, False)
        self.Frame3.iconbitmap(R"myimages\parko.ico")

        scrollbar = Scrollbar(self.Frame3)
        scrollbar.pack(side=RIGHT, fill=Y)
        textbox = Text(self.Frame3, width=64, height=24)
        label1 = Label(self.Frame3, text="        S no.                            Slot Type                               Vehicle no                          Status                           ", width=69)
        label1.pack()
        
        
        import pymysql as pm

        con = pm.connect(host="localhost", user="root", password="", db="parking management")
        
        cur = con.cursor()
        cur.execute("select Sno, Stype,Vehicleno, Status from slots")

        for rows in cur:
            k = 0
            for j in rows:
                if k==0:
                    textbox.insert(END,' ')
                textbox.insert(END,j)
                textbox.insert(END,'\t')
                k+=1
                if k==1:
                    
                    textbox.insert(END,'\t')
                if k==2:
                    textbox.insert(END,'\t')
                if k==3:
                    textbox.insert(END,'\t')


                

            textbox.insert(END,'\n')
        textbox.config(state=DISABLED)
        textbox.pack()
        
        textbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=textbox.yview)

    # ====================SUB FRAME 4===============================
    def updatenewdata(self):
        import pymysql as pm

        con = pm.connect(host="localhost", user="root", password="", db="parking management")
        a = con.cursor()    # reference     
        query1 = "update slots set Vehicleno='',Status='AVBL' where Vehicleno='{}'".format(self.Search.get().upper()) 
        a.execute(query1)
        query2 = "Select Sno from slots where Status ='AVBL' AND Stype='{}' limit 1".format(self.newVtype.get())
        a.execute(query2)
        getsno = a.fetchall()
        slotno = getsno[0][0]
        query = "update information set Name = '{}', Mobile = '{}', Vehicleno = '{}', VehicleType = '{}', Passengers = '{}',Slot='{}' where Vehicleno = '{}'".format(self.newName.get().capitalize(),self.newMob.get(),self.newVno.get().upper(),self.newVtype.get(),self.newPass.get(),str(slotno),self.Search.get().upper())
        a.execute(query)
        query3 = "UPDATE slots SET Vehicleno='{}', Status='UNAVBL' where Sno='{}'".format(self.newVno.get(),str(slotno))
        a.execute(query3)
        con.commit()
        self.subFrame4.destroy()
        messagebox.showinfo("Notice","Information stored succesfully")
        

    def UpdateNewWindow1(self):
        self.search_frame.destroy()
        self.subFrame4 = Toplevel(self.AdminWindow)
        self.subFrame4.title("Parking Management System")
        self.subFrame4['bg'] = "#003e53"
        Left = int(self.subFrame4.winfo_screenwidth() - 500) / 2
        Top = int(self.subFrame4.winfo_screenheight() - 440) / 2
        self.subFrame4.geometry("%dx%d+%d+%d" % (450, 440, Left, Top))
        self.subFrame4.iconbitmap(R"myimages\parko.ico")
        # A Label widget to show in toplevel
        label = Label(self.subFrame4, text="Update User", width=30, height=3,fg="white", bg='#003e53', font=("apple-system", 15, "bold"))
        label.pack()
        self.newName = tk.StringVar()
        self.newMob = tk.StringVar()
        self.newVno = tk.StringVar()
        self.newVtype = tk.StringVar()
        self.newPass = tk.StringVar()
        

        name = Label(self.subFrame4, text="Name        :", font=(
            "apple-system", 11, "bold"), fg="white",bg="#003e53").place(x=70, y=150)
        t_name = Entry(self.subFrame4, font=("apple-system", 12),textvariable=self.newName)
        t_name.place(x=180, y=150, width=250)
        t_name.delete(0,END)
        t_name.insert(0,self.mylist[0])


        # second row
        phone = Label(self.subFrame4, text="Mobile   :", font=(
            "apple-system", 11, "bold"), fg="white",bg="#003e53").place(x=70, y=190)
        txt_phone = Entry(
            self.subFrame4, font=("apple-system", 12),textvariable=self.newMob)
        txt_phone.place(x=180, y=190, width=250)
        txt_phone.delete(0,END)
        txt_phone.insert(0,self.mylist[1])

        # third row
        vno = Label(self.subFrame4, text="Vehicle no   :", font=(
            "apple-system", 11, "bold"), fg="white",bg="#003e53").place(x=70, y=230)
        txt_vno = Entry(
            self.subFrame4, font=("apple-system", 12),textvariable=self.newVno)
        txt_vno.place(x=180, y=230, width=250)
        txt_vno.delete(0,END)
        txt_vno.insert(0,self.mylist[2])

        # fourth row
        v_type = Label(self.subFrame4, text="Vehicle type   :", font=(
            "apple-system", 11, "bold"), fg="white",bg="#003e53").place(x=70, y=270)
        txt_vtype = Entry(
             self.subFrame4, font=("apple-system", 12),textvariable=self.newVtype)
        txt_vtype.place(x=180, y=270, width=250)
        txt_vtype.delete(0,END)
        txt_vtype.insert(0,self.mylist[3])

         # FIFTH ROW
        passengers = Label(self.subFrame4, text="Passengers  :", font=(
              "apple-system", 11, "bold"), fg="white",bg="#003e53").place(x=70, y=310)
        txt_passen = Entry(self.subFrame4, font=("apple-system", 12),textvariable=self.newPass)
        txt_passen.place(x=180, y=310, width=250)
        txt_passen.delete(0,END)
        txt_passen.insert(0,self.mylist[4])

        btn1 = Button(self.subFrame4, text="UPDATE", fg="black",bg="white",command=self.updatenewdata, width=25)
        btn1.place(x=160, y=350)
        
        
            
    # =======================SEARCH=================================
    def search_record(self):
        self.Frame4.destroy()
        self.search_frame = Toplevel(self.AdminWindow)
        self.search_frame.title("Parking Management System")
        Left = int(self.search_frame.winfo_screenwidth() - 500) / 2
        Top = int(self.search_frame.winfo_screenheight() - 450) / 2
        self.search_frame.geometry("%dx%d+%d+%d" % (500, 450, Left, Top))
        self.search_frame.iconbitmap(R'myimages\parko.ico')
        self.search_frame.resizable(False, False)
        self.search_frame['bg'] = "#003e53"
        # print(self.Search.get())
        if self.Search.get() == "":
            messagebox.showerror("Error !", "Fields are Required !")
        else:
            import pymysql as pm

            con = pm.connect(host="localhost", user="root", password="", db="parking management")
            
            cur = con.cursor()
            cur.execute("select * from information where Vehicleno = '{}'".format(self.Search.get()))
            field_names = [i[0] for i in cur.description]
            # print(field_names)
            col = 0
            allrows = cur.fetchall()

            if len(allrows)>0:
                for x in field_names:
                    e = Entry(self.search_frame, width=10, fg='black',bg="white")
                    e.grid(row=4, column=col)
                    col = col+1
                    e.insert(END, x)
                    e.configure(state="readonly")
                i=5

                self.mylist = []
                for student in allrows: 
                    for j in range(len(student)):
                        self.mylist.append(student[j])
                        e = Entry(self.search_frame, width=10, fg='blue') 
                        e.grid(row=i, column=j) 
                        e.insert(END, student[j])
                    i=i+1
                
                btn_a = Button(self.search_frame, text="UPDATE", fg="black", bg="white",width=25, command=self.UpdateNewWindow1).place(x=160, y=200)
                
            else:
                messagebox.showerror("Error","No record exists!")
                self.UpdateUser()
            
    # =======================FRAME 4================================
    def UpdateUser(self):
        
        self.Frame4 = Toplevel(self.AdminWindow)
        self.Frame4.title("Parking Management System")
        Left = int(self.Frame4.winfo_screenwidth() - 500) / 2
        Top = int(self.Frame4.winfo_screenheight() - 450) / 2
        self.Frame4.geometry("%dx%d+%d+%d" % (500, 450, Left, Top))
        self.Frame4.iconbitmap(R'myimages\parko.ico')
        self.Frame4.resizable(False, False)
        self.Frame4['bg'] = "#003e53"
        
        self.Search = tk.StringVar()

        title = Label(self.Frame4, text="UPDATE INFO ", font=(
            "apple-system", 14, "bold"), fg="white", bg="#003e53").place(x=180, y=50)

        vno = Label(self.Frame4, text="Enter Vehicle no.:", font=(
            "apple-system", 11, "bold"), fg="white", bg="#003e53").place(x=70, y=150)
        t_vno = Entry(self.Frame4, font=("apple-system", 12),textvariable=self.Search).place(x=220, y=150, width=180)
        
        # label = Label(self.Frame4, text="This is the window")

        btn = Button(self.Frame4, text="Search", fg="black", bg="white",width=25, command=self.search_record).place(x=160, y=200)


    #======================UPDATE CHARGE DBMS=======================

    def updatechargedbms(self):
        import pymysql as pm

        con = pm.connect(host="localhost", user="root", password="", db="parking management")
        
        cur = con.cursor()
        cur.execute("Update parkingcharge set TwoWheelCharge='{}', FourWheelCharge='{}' where id='admin'".format(self.twowheelcharge.get(),self.fourwheelcharge.get()))
        con.commit()
        self.subFrame5.destroy()
        messagebox.showinfo("Info","Charge Update succesfully")

    # =====================SUB FRAME 5==============================
    def updatenewcharge(self):
        self.subFrame5 = Toplevel(self.AdminWindow)
        self.subFrame5.geometry("500x300")
        self.subFrame5.title("Parking Management System")
        Left = int(self.subFrame5.winfo_screenwidth() - 500)/2
        Top = int(self.subFrame5.winfo_screenheight() - 300)/2
        self.subFrame5.geometry("%dx%d+%d+%d" % (500, 300, Left, Top))
        self.subFrame5.resizable(False, False)
        self.subFrame5['background']='#003e53'
        self.subFrame5.iconbitmap(R'myimages\parko.ico')

        self.twowheelcharge = tk.StringVar()
        self.fourwheelcharge = tk.StringVar()

        
        new_charge2 = Label(self.subFrame5, text="Enter new 2 wheel charge :", font=("Walbaum Display", 11,"bold"), fg="white",bg="#003e53").place(x=50, y=90)
        txt_new = Entry(self.subFrame5, font=("apple-system", 12),textvariable=self.twowheelcharge)
        txt_new.place(x=270, y=90, width=200)
        txt_new.delete(0,END)
        txt_new.insert(0,self.both1[0][0])
        
        new_charge4 = Label(self.subFrame5, text="Enter new 4 wheel charge :", font=("Walbaum Display", 11,"bold"), fg="white",bg="#003e53").place(x=50, y=130)
        txt_new1 = Entry(self.subFrame5, font=("apple-system", 12),textvariable=self.fourwheelcharge)
        txt_new1.place(x=270, y=130, width=200)
        txt_new1.delete(0,END)
        txt_new1.insert(0,self.both1[0][1])
        

        b1 = Button(self.subFrame5, text = "Update",width=25,command=self.updatechargedbms).place(x=270, y=170)
        
    # =======================FRAME 5================================
    def UpdateCharge(self):
        self.Frame5 = Toplevel(self.AdminWindow)
        self.Frame5.geometry("500x300")
        self.Frame5.title("Parking Management System")
        Left = int(self.Frame5.winfo_screenwidth() - 500)/2
        Top = int(self.Frame5.winfo_screenheight() - 300)/2
        self.Frame5.geometry("%dx%d+%d+%d" % (500, 300, Left, Top))
        self.Frame5.resizable(False, False)
        self.Frame5['background']='#003e53'
        self.Frame5.iconbitmap(R'myimages\parko.ico')
        
        import pymysql as pm

        con = pm.connect(host="localhost", user="root", password="", db="parking management")
        
        cur = con.cursor()
        cur.execute("select TwoWheelCharge, FourWheelCharge from parkingcharge where id='admin'")
        self.both1 = cur.fetchall()
        rupee = u"\u20B9"

        T = Text(self.Frame5, height = 7, width = 47)
        l = Label(self.Frame5, text = "Charge as per Vehicle", background = '#003e53', foreground = '#fff', font =('Courier', 18, 'bold'))
        Charge = (f"\n\n           2-Wheeler :- {self.both1[0][0]}{rupee} per hour \n           4-Wheeler :- {self.both1[0][1]}{rupee} per hour")
        b1 = Button(self.Frame5, text = "Update",command=self.updatenewcharge).place(x=240, y=170)
        b2 = Button(self.Frame5, text = "Exit", command = self.Frame5.destroy).place(x=248, y=200)
        l.pack()
        T.pack()
        T.insert(tk.END, Charge)

    #======================Change passw============================
    def changepassw(self):
        if self.input_new.get() == self.input_new1.get():
            import pymysql as pm

            con = pm.connect(host="localhost", user="root", password="", db="parking management")
        
            cur = con.cursor()
            cur.execute("Update admincred set password = '{}' where userid='admin'".format(self.input_new.get()))
            con.commit()
            # self.subFrame6.destroy()
            messagebox.showinfo("Update Password","Password Updated successfully")
        else:
            messagebox.showerror("Error","Mismatch password")
            self.subFrame6()
        

    def subForgotFrame(self):
        self.forgotframe.destroy()
        self.subForgotFrame = Toplevel(self.root)
        self.subForgotFrame.title("Parking Management System")
        Left = int(self.subForgotFrame.winfo_screenwidth() - 500)/2
        Top = int(self.subForgotFrame.winfo_screenheight() - 450)/2
        self.subForgotFrame.geometry("%dx%d+%d+%d" % (500, 450, Left, Top))
        self.subForgotFrame.iconbitmap(R'myimages\parko.ico')
        self.subForgotFrame['background']='#003e53'
        self.input_new = tk.StringVar()
        self.input_new1 = tk.StringVar()
        title = Label(self.subForgotFrame, text="Change Admin Password",height=3, font=("Walbaum Display", 18,"bold"), fg="white", bg="#003e53")
        title.pack()

        # First Row
        new_pass = Label(self.subForgotFrame, text="Enter new password :", font=("Walbaum Display", 11,"bold"), fg="white",bg="#003e53").place(x=50, y=170)
        txt_new = Entry(self.subForgotFrame,show='*', font=("apple-system", 12),textvariable=self.input_new).place(x=220, y=170, width=200)
        
        new_pass1 = Label(self.subForgotFrame, text="Enter password again:", font=("Walbaum Display", 11,"bold"), fg="white",bg="#003e53").place(x=50, y=230)
        txt_new1 = Entry(self.subForgotFrame,show='*', font=("apple-system", 12),textvariable=self.input_new1).place(x=220, y=230, width=200)

        #button
        btn = Button(self.subForgotFrame, text="Continue",font=("Walbaum Display",11,"bold"),fg="black", bg="light gray",command=self.changepassw, width=8, height=1).place(x=210,y=280)

    #======================SUB FRAME 6=============================
    def subFrame6(self):
        self.subFrame6 = Toplevel(self.AdminWindow)
        self.subFrame6.title("Parking Management System")
        Left = int(self.subFrame6.winfo_screenwidth() - 500)/2
        Top = int(self.subFrame6.winfo_screenheight() - 450)/2
        self.subFrame6.geometry("%dx%d+%d+%d" % (500, 450, Left, Top))
        self.subFrame6.iconbitmap(R'myimages\parko.ico')
        self.subFrame6['background']='#003e53'
        self.input_new = tk.StringVar()
        self.input_new1 = tk.StringVar()
        title = Label(self.subFrame6, text="Change Admin Password",height=3, font=("Walbaum Display", 18,"bold"), fg="white", bg="#003e53")
        title.pack()

        # First Row
        new_pass = Label(self.subFrame6, text="Enter new password :", font=("Walbaum Display", 11,"bold"), fg="white",bg="#003e53").place(x=50, y=170)
        txt_new = Entry(self.subFrame6,show='*', font=("apple-system", 12),textvariable=self.input_new).place(x=220, y=170, width=200)
        
        new_pass1 = Label(self.subFrame6, text="Enter password again:", font=("Walbaum Display", 11,"bold"), fg="white",bg="#003e53").place(x=50, y=230)
        txt_new1 = Entry(self.subFrame6,show='*', font=("apple-system", 12),textvariable=self.input_new1).place(x=220, y=230, width=200)

        #button
        btn = Button(self.subFrame6, text="Continue",font=("Walbaum Display",11,"bold"),fg="black", bg="light gray",command=self.changepassw, width=8, height=1).place(x=210,y=280)

        
    #======================CHECK FRAME 6=============================
    def check(self):
        if self.input_old.get() == self.passw:
            self.Frame6.destroy()
            self.subFrame6()
        else:
            self.Frame6.destroy()
            messagebox.showinfo("Note","Incorrect Old pass")
            self.ChangePass()

        
    # =======================FRAME 6================================
    def ChangePass(self):
        # self.AdminWindow.destroy()
        self.Frame6 = Toplevel(self.AdminWindow)
        self.Frame6.title("Parking Management System")
        Left = int(self.Frame6.winfo_screenwidth() - 500)/2
        Top = int(self.Frame6.winfo_screenheight() - 450)/2
        self.Frame6.geometry("%dx%d+%d+%d" % (500, 450, Left, Top))
        self.Frame6.iconbitmap(R'myimages\parko.ico')
        self.Frame6['background']='#003e53'
        self.input_old = tk.StringVar()
        title = Label(self.Frame6, text="Change Admin Password", height=4,font=("Walbaum Display", 18,"bold"), fg="white", bg="#003e53")
        title.pack()

        # First Row
        old_pass = Label(self.Frame6, text="Enter old password :", font=("Walbaum Display", 11,"bold"), fg="white",bg="#003e53").place(x=60, y=230)
        txt_old = Entry(self.Frame6, font=("apple-system", 12),textvariable=self.input_old).place(x=210, y=230, width=200)

        #button
        btn = Button(self.Frame6, text="Continue",font=("Walbaum Display",11,"bold"),fg="black", bg="light gray",command=self.check, width=8, height=1).place(x=210,y=280)

    # =====================FRAME 7====================================
    def UserFeedback(self):
        # self.AdminWindow.destroy()
        self.Frame7 = Toplevel(self.AdminWindow)
        self.Frame7.title("Parking Management System")
        Left = int(self.Frame7.winfo_screenwidth() - 500)/2
        Top = int(self.Frame7.winfo_screenheight() - 450)/2
        self.Frame7.geometry("%dx%d+%d+%d" % (500, 450, Left, Top))
        self.Frame7.iconbitmap(R'myimages\parko.ico')
        self.Frame7['background']='#003e53'
        self.Frame7.resizable(False,False)
        self.input_old = tk.StringVar()
        title = Label(self.Frame7, text="Customer Feedback", height=4,font=("Walbaum Display", 18,"bold"), fg="white", bg="#003e53")
        title.pack()
        scrollbar = Scrollbar(self.Frame7)
        scrollbar.pack(side=RIGHT, fill=Y)
        textbox = Text(self.Frame7, width=48, height=21)
        textbox.pack()
        query = "select * from information"

        import pymysql as pm

        con = pm.connect(host="localhost", user="root",
                     password="", db="parking management")

        cur = con.cursor()
        query = "Select Yfeedback from feedback"    
 
        cur.execute(query)

        # messagebox.showinfo("Notice","Information stored succesfully")
        i = 1
        for rows in cur:
            for j in rows:
                textbox.insert(END,i)
                textbox.insert(END,") ")
                textbox.insert(END,j)
            i+=1
            textbox.insert(END,'\n')
        textbox.config(state=DISABLED)
        
 
        textbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=textbox.yview)
        
                
        
    # ====================ADMIN MENU==========================
    def adminWindow(self):
        self.AdminWindow = Toplevel(self.root)

        # sets the title of the
        # Toplevel widget
        self.AdminWindow.title("Parking Management System")
        self.AdminWindow['bg'] = "#003e53"
        self.AdminWindow.iconbitmap(R"myimages\parko.ico")

        # sets the geometry of toplevel
        # Left = int(self.AdminWindow.winfo_screenwidth() - 500) / 2
        # Top = int(self.AdminWindow.winfo_screenheight() - 440) / 2
        self.AdminWindow.geometry("450x440+700+500")
        menubar = Menu(self.AdminWindow)
        self.AdminWindow.config(menu=menubar)
        admin_menu = Menu(menubar, tearoff=0)
        # # add menu item to admin menu
        admin_menu.add_command(label='Display', command=self.Display)
        admin_menu.add_command(label='Type based slots',command=self.TypeBaseSlot)
        admin_menu.add_command(label='Slots info', command=self.slotsInfo)
        admin_menu.add_command(label='Update user',command=self.UpdateUser)
        admin_menu.add_command(label='Update Charge',command=self.UpdateCharge)
        admin_menu.add_command(label='Change Password',command=self.ChangePass)
        admin_menu.add_command(label='User Feedback',command=self.UserFeedback)
        admin_menu.add_separator()
        admin_menu.add_command(label='Main Menu', command=self.AdminWindow.destroy)
        menubar.add_cascade(label="ADMIN", menu=admin_menu)
        self.raw_image1=Image.open(R"myimages\adminbg.jpg")
        self.background_image1=ImageTk.PhotoImage(self.raw_image1.resize((500, 450), Image.ANTIALIAS))
        self.background_label1 = tk.Label(self.AdminWindow, image=self.background_image1)
        self.background_label1.place(x=0, y=0, relwidth=1, relheight=1)

# ==================================================================================
#                            OPERATOR FRAMES & MENU
# ==================================================================================

    def InsertCustInfo(self):
        
        self.InTime = datetime.datetime.today().strftime("%I:%M %p")
        
        import pymysql as pm

        con = pm.connect(host="localhost", user="root", password="", db="parking management")
        a = con.cursor()    # reference     
        
        query1 = "Select Sno from slots where Status ='AVBL' AND Stype='{}' limit 1".format(self.custVtype.get())
        a.execute(query1)
        sloty = a.fetchall()
        slot1 = sloty[0][0]
        # print(slot1)
        query = "insert into information values('{}','{}','{}','{}','{}','{}','{}','{}')".format(self.custName.get().capitalize(),self.custMob.get(),self.custVno.get().upper(),self.custVtype.get(),self.custPass.get(),self.InTime,slot1,"PKD")
        a.execute(query)
        self.opFrame1.destroy()
        messagebox.showinfo("Notice","Information stored succesfully")
        query2 = "UPDATE slots SET Vehicleno='{}', Status='UNAVBL' where Sno='{}'".format(self.custVno.get().upper(),slot1)
        a.execute(query2)
        
        con.commit()        # confirm    
        self.addCustomer()
       
    # ====================OP FRAME 1=============================
    def addCustomer(self):
        self.opFrame1 = Toplevel(self.operatorWin)
        self.opFrame1.title("Parking Management System")
        Left = int(self.opFrame1.winfo_screenwidth() - 500)/2
        Top = int(self.opFrame1.winfo_screenheight() - 450)/2
        self.opFrame1.geometry("%dx%d+%d+%d" % (500, 450, Left, Top))
        self.opFrame1['background'] = '#003e53'
        self.opFrame1.iconbitmap(R'myimages\parko.ico')
        self.opFrame1.resizable(False, False)
        self.custName = tk.StringVar()
        self.custMob = tk.StringVar()
        self.custVtype = tk.IntVar()
        self.custVno = tk.StringVar()
        self.custPass = tk.StringVar()

        title = Label(self.opFrame1, text="Add Customer", font=("apple-system", 18, "bold"), fg="white", bg="black").place(x=165, y=50)

        # First row
        name = Label(self.opFrame1, text="Name        :", font=(
            "apple-system", 11, "bold",), fg="white", bg='#003e53').place(x=70, y=150)
        txt_name = Entry(self.opFrame1, font=(
            "apple-system", 12),textvariable=self.custName).place(x=180, y=150, width=250)

        # second row
        phone = Label(self.opFrame1, text="Mobile   :", font=(
            "apple-system", 11, "bold"), fg="white", bg='#003e53').place(x=70, y=190)
        txt_phone = Entry(self.opFrame1, font=(
            "apple-system", 12),textvariable=self.custMob).place(x=180, y=190, width=250)

        # third row
        Vno = Label(self.opFrame1, text="Vehicle no :", font=(
            "apple-system", 11, "bold"), fg="white", bg='#003e53').place(x=70, y=230)
        txt_add = Entry(self.opFrame1, font=("apple-system", 12),textvariable=self.custVno).place(x=180, y=230, width=250)

        # fourth row
        v_type = Label(self.opFrame1, text="Vehicle type   :", font=(
            "apple-system", 11, "bold"), fg="white", bg='#003e53').place(x=70, y=270)
        r1 = tk.Radiobutton(self.opFrame1, text='2 wheeler', variable=self.custVtype, value='2').place(x=180, y=270)  
        # self.r1.deselect()
        r2 = tk.Radiobutton(self.opFrame1, text='4 wheeler', variable=self.custVtype, value='4').place(x=260, y=270)
        # self.r2.deselect()


        # FIFTH ROW
        passengers = Label(self.opFrame1, text="Passengers  :", font=(
            "apple-system", 11, "bold"), fg="white", bg='#003e53').place(x=70, y=310)
        txt_passen = Entry(self.opFrame1,
                           font=("apple-system", 12),textvariable=self.custPass).place(x=180, y=310, width=250)

        
        btn = Button(self.opFrame1, text="REGISTER",width=25,command=self.InsertCustInfo).place(x=160, y=370)


    # ====================OP FRAME 2=============================
    def chargeAsPerVeh(self):
        self.opFrame2 = Toplevel(self.operatorWin)
        self.opFrame2.geometry("500x450+300+140")
        self.opFrame2.title("Parking Management System")
        self.opFrame2['background'] = '#003e53'
        self.opFrame2.iconbitmap(R'myimages\parko.ico')
        self.opFrame2.resizable(False, False)

        import pymysql as pm

        con = pm.connect(host="localhost", user="root", password="", db="parking management")
        
        cur = con.cursor()
        cur.execute("Select TwoWheelCharge, FourWheelCharge from parkingcharge where id='admin'")
        charge = cur.fetchall()
        
        paid2 = charge[0][0]
            
        paid4 = charge[0][1]
        rupee = u"\u20B9"
        T = Text(self.opFrame2, height=7, width=30)
        l = Label(
            self.opFrame2, text="\nCharge as per Duration\n-----------------------------------------------------------------\n")
        l.config(font=('Cambria', 14), fg='white', bg='#003e53')
        Charge = (
            f"\n 2 - Wheeler : {paid2}{rupee} per hour\n\n 4 - Wheeler : {paid4}{rupee} per hour")
        l2 = Label(self.opFrame2, text="\n--------------------------------------------------------------------------------\n\n", bg="#003e53", fg='white')
        l.config(state=DISABLED)
        b2 = Button(self.opFrame2, text="Exit",
                    command=self.opFrame2.destroy, font='Cambria')

        l.pack()
        T.pack()
        l2.pack()
        b2.pack()
        T.insert(tk.END, Charge)

    # ============SUB FRAME 3 (Slip)================
    def Slip(self):
        self.opFrame3.destroy()
        self.subFrame3 = Toplevel(self.operatorWin)
        self.subFrame3.geometry("500x450")
        self.subFrame3.title("Parking Management System")
        self.subFrame3['background'] = '#003e53'
        self.subFrame3.resizable(False, False)
        self.subFrame3.iconbitmap(R"myimages\parko.ico")

        imgFile = Image.open(R'myimages\bcimg.png')
        bcimg = ImageTk.PhotoImage(imgFile.resize((130, 50), Image.ANTIALIAS))

        T = Text(self.subFrame3, height=20, width=35)
        l = Label(self.subFrame3, text="\nSlip\n")
        l.config(font=('Cambria', 14), fg='white', bg='#003e53')

        # Uploading slip data to database
        self.date = datetime.date.today()
        self.OutTime = datetime.datetime.today().strftime("%I:%M %p")

        import pymysql as pm

        con = pm.connect(host="localhost", user="root", password="", db="parking management")
        
        cur = con.cursor()
        cur.execute("Select TwoWheelCharge, FourWheelCharge from parkingcharge where id='admin'")
        charge = cur.fetchall()
        
        if self.mylist1[3] == '2':
            paid = charge[0][0]
            vtyp = "2-wheeler"
        else:
            paid = charge[0][1]
            vtyp = "4-wheeler"

        InTime = self.mylist1[5]

        
        import pymysql as pm

        con = pm.connect(host="localhost", user="root", password="", db="parking management")
        a = con.cursor()    # reference     

        query = "select * from slip where Vehicleno = '{}'".format(self.Search1.get())
        a.execute(query)
        query1 = "update slots Set Status='AVBL',Vehicleno='' where Sno='{}'".format(self.mylist1[6])
        a.execute(query1)
        query2 = "update information Set Vstatus='UNPKD' where Vehicleno='{}'".format(self.Search1.get())
        a.execute(query2)
        data = a.fetchall()
        if not(len(data)>0):
            query1 = "insert into slip values('{}','{}','{}','{}','{}')".format(self.mylist1[2],InTime,self.OutTime,self.date,paid)
            a.execute(query1)

        
        con.commit()        # confirm    

        
        # tym = datetime.datetime.now()
        name = self.mylist1[0]
        self.rupee = u"\u20B9"
        vno = self.mylist1[2]
        Charge = (
            f"\n\t    ABC Park Ltd\n\t      Mall Road\n\n =================================\n\t  PARKING RECEIPT\n =================================\n\t\t\t{self.date}\n\n\n Name              :  \t\t{name}\n Vehicle no.       :\t\t\t{vno}\n Vehicle Type.     :\t\t\t{vtyp}\n In Time  \t\t   :    {InTime}\n Out Time \t\t   :    {self.OutTime}\n Amount paid       :  \t\t{self.rupee}{paid}")
        img_space = "\t  "
        b1 = Button(self.subFrame3, text="Exit", command=self.subFrame3.destroy,
                    font='Cambria', width=10).place(x=200, y=410)

        l.pack()
        T.pack()
        T.insert(tk.END, img_space)
        T.image_create("current", image=bcimg)
        T.insert(tk.END, Charge)

    #=====================Search record slip====================

    def search_record1(self):
        self.opFrame3.destroy()
        self.search_frame1 = Toplevel(self.operatorWin)
        self.search_frame1.title("Parking Management System")
        Left = int(self.search_frame1.winfo_screenwidth() - 500) / 2
        Top = int(self.search_frame1.winfo_screenheight() - 450) / 2
        self.search_frame1.geometry("%dx%d+%d+%d" % (500, 450, Left, Top))
        self.search_frame1.iconbitmap(R'myimages\parko.ico')
        self.search_frame1.resizable(False, False)
        self.search_frame1['bg'] = "#003e53"
        # print(self.Search1.get())
        if self.Search1.get() == "":
            messagebox.showerror("Error !", "Fields are Required !")
        else:
            import pymysql as pm

            con = pm.connect(host="localhost", user="root", password="", db="parking management")
            
            cur = con.cursor()
            cur.execute("select * from information where Vehicleno = '{}'".format(self.Search1.get()))
            field_names = [i[0] for i in cur.description]
            # print(field_names)
            col = 0
            allrows = cur.fetchall()

            if len(allrows)>0:
                for x in field_names:
                    e = Entry(self.search_frame1, width=10, fg='black',bg="white")
                    e.grid(row=4, column=col)
                    col = col+1
                    e.insert(END, x)
                    e.configure(state="readonly")
                i=5
                
                self.mylist1 = []
                for student in allrows: 
                    for j in range(len(student)):
                        self.mylist1.append(student[j])
                        e = Entry(self.search_frame1, width=10, fg='blue') 
                        e.grid(row=i, column=j) 
                        e.insert(END, student[j])
                    i=i+1
                
                
                btn_a = Button(self.search_frame1, text="Generate Slip", fg="black", bg="white",width=25, command=self.Slip).place(x=160, y=200)
                
            else:
                messagebox.showerror("Error","No record exists!")
                self.GenerateSlip()

    # ====================OP FRAME 3=============================
    def GenerateSlip(self):
        self.opFrame3 = Toplevel(self.operatorWin)
        self.opFrame3.title("Parking Management System")
        Left = int(self.opFrame3.winfo_screenwidth() - 500)/2
        Top = int(self.opFrame3.winfo_screenheight() - 450)/2
        self.opFrame3.geometry("%dx%d+%d+%d" % (500, 450, Left, Top))
        self.opFrame3.iconbitmap(R'myimages\parko.ico')
        self.opFrame3['background'] = '#003e53'
        self.opFrame3.resizable(False, False)

        self.Search1 = tk.StringVar()

        title = Label(self.opFrame3, text="Generate Slip", font=(
            "Walbaum Display", 18, "bold"), fg="white", bg="#003e53").place(x=180, y=50)

        # First Row
        vid = Label(self.opFrame3, text="Vehicle number  :", font=(
            "Walbaum Display", 11, "bold"), fg="white", bg="#003e53").place(x=70, y=150)
        txt_vid = Entry(self.opFrame3, font=("apple-system", 12),textvariable=self.Search1
                        ).place(x=210, y=150, width=200)

        btn = Button(self.opFrame3, text="Generate", font=("Walbaum Display", 11, "bold"),
                     command=self.search_record1, fg="black", bg="light gray", width=8, height=1).place(x=210, y=240)

    # ====================OP FRAME 4=============================

    def Displayop(self):
        self.opFrame1 = Toplevel(self.operatorWin)
        LeftPos = int(self.opFrame1.winfo_screenwidth() - 600)/2
        TopPos = int(self.opFrame1.winfo_screenheight() - 450)/2
        self.opFrame1.geometry("%dx%d+%d+%d" % (500, 400, LeftPos, TopPos))
        self.opFrame1.title("Parking Management System")
        self.opFrame1['background'] = '#003e53'
        self.opFrame1.resizable(False, False)
        self.opFrame1.iconbitmap(R"myimages\parko.ico")
        

        scrollbar = Scrollbar(self.opFrame1)
        scrollbar.pack(side=RIGHT, fill=Y)
        textbox = Text(self.opFrame1, width=64, height=24)
        label1 = Label(self.opFrame1, text="   V no.          V Type    Passengers               Mobile                 Slot acq.           Name                     ", width=69)
        label1.pack()
        
        
        import pymysql as pm

        con = pm.connect(host="localhost", user="root", password="", db="parking management")
        
        cur = con.cursor()
        cur.execute("select Vehicleno,VehicleType,Passengers,Mobile,Slot,Name from information")


        for rows in cur:
            k = 0
            for j in rows:
                if k==0:
                    textbox.insert(END,' ')
                textbox.insert(END,j)
                textbox.insert(END,'\t')
                k+=1
                if k==1:
                    textbox.insert(END,'  ')
                if k==4:
                    textbox.insert(END,'\t')
                

            textbox.insert(END,'\n')
        textbox.config(state=DISABLED)
        textbox.pack()
   
        textbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=textbox.yview)
    
    #=====================Search record ====================

    def search_record2(self):
        self.opFrame5.destroy()
        self.search_frame2 = Toplevel(self.operatorWin)
        self.search_frame2.title("Parking Management System")
        Left = int(self.search_frame2.winfo_screenwidth() - 500) / 2
        Top = int(self.search_frame2.winfo_screenheight() - 450) / 2
        self.search_frame2.geometry("%dx%d+%d+%d" % (500, 450, Left, Top))
        self.search_frame2.iconbitmap(R'myimages\parko.ico')
        self.search_frame2.resizable(False, False)
        self.search_frame2['bg'] = "#003e53"
        # print(self.search2.get())
        if self.search2.get() == "":
            messagebox.showerror("Error !", "Fields are Required !")
        else:
            import pymysql as pm

            con = pm.connect(host="localhost", user="root", password="", db="parking management")
            
            cur = con.cursor()
            cur.execute("select * from information where Vehicleno = '{}'".format(self.search2.get()))
            field_names = [i[0] for i in cur.description]
            # print(field_names)
            col = 0
            allrows = cur.fetchall()

            if len(allrows)>0:
                for x in field_names:
                    e = Entry(self.search_frame2, width=10, fg='black',bg="white")
                    e.grid(row=4, column=col)
                    col = col+1
                    e.insert(END, x)
                    e.configure(state="readonly")
                i=5
           
                for student in allrows: 
                    for j in range(len(student)):
                        e = Entry(self.search_frame2,width=10, fg='blue') 
                        e.grid(row=i, column=j) 
                        e.insert(END, student[j])
                    i=i+1
               
            else:
                messagebox.showerror("Error","No record exists!")
                self.SearchVehicle()

    
    # ====================OP FRAME 5=============================
    def SearchVehicle(self):
        self.opFrame5 = Toplevel(self.operatorWin)
        self.opFrame5.title("Parking Management System")
        Left = int(self.opFrame5.winfo_screenwidth() - 500)/2
        Top = int(self.opFrame5.winfo_screenheight() - 450)/2
        self.opFrame5.geometry("%dx%d+%d+%d" % (500, 450, Left, Top))
        self.opFrame5.iconbitmap(R'myimages\parko.ico')
        self.opFrame5['background'] = '#003e53'
        self.opFrame5.resizable(False, False)
        self.search2 = tk.StringVar()

        title = Label(self.opFrame5, text="Search", font=(
            "Walbaum Display", 18, "bold"), fg="white", bg="#003e53").place(x=200, y=50)

        # First Row
        v_no = Label(self.opFrame5, text="Vehicle Number  :", font=(
            "Walbaum Display", 11, "bold"), fg="white", bg="#003e53").place(x=70, y=190)
        txt_v_no = Entry(self.opFrame5, font=(
            "apple-system", 12),textvariable=self.search2).place(x=210, y=190, width=200)

        
        # button
        btn = Button(self.opFrame5, text="Display", font=("Walbaum Display", 11, "bold"),
                     fg="black", bg="light gray",command=self.search_record2, width=8, height=1).place(x=210, y=280)

    # ====================OP FRAME 6=============================
    def SlotsAvailable(self):
        self.opFrame6 = Toplevel(self.operatorWin)
        self.opFrame6.geometry("380x400+390+160")
        self.opFrame6.title("Parking Management System")
        self.opFrame6['background'] = '#003e53'
        self.opFrame6.resizable(False, False)
        self.opFrame6.iconbitmap(R"myimages\parko.ico")


        scrollbar = Scrollbar(self.opFrame6)
        scrollbar.pack(side=RIGHT, fill=Y)
        textbox = Text(self.opFrame6, width=64, height=24)
        label1 = Label(self.opFrame6, text="   S no.                               S Type                                 Status                         ", width=69)
        label1.pack()
        
        
        import pymysql as pm

        con = pm.connect(host="localhost", user="root", password="", db="parking management")
        
        cur = con.cursor()
        cur.execute("select Sno, Stype, Status from slots where Status='AVBL'")


        for rows in cur:
            k = 0
            for j in rows:
                if k==0:
                    textbox.insert(END,' ')
                textbox.insert(END,j)
                if k<2:
                    textbox.insert(END,'\t\t')
                k+=1
                
            textbox.insert(END,'\n')
        textbox.config(state=DISABLED)
        textbox.pack()
   
        textbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=textbox.yview)
        # import pymysql as pm

        # con = pm.connect(host="localhost", user="root", password="", db="parking management")
        
        # cur = con.cursor()
        # cur.execute("select Sno, Stype, Status from slots where Status='AVBL'")
        # field_names = [i[0] for i in cur.description]
        # # print(field_names)
        # col = 0
        # for x in field_names:
        #     e = Entry(self.opFrame6, width=27, fg='black',bg="white")
        #     e.grid(row=4, column=col)
        #     col = col+1
        #     e.insert(END, x)
        #     e.configure(state="readonly")
        # i=5
        # for info in cur: 
        #     for j in range(len(info)):
        #         e = Entry(self.opFrame6, width=27, fg='blue') 
        #         e.grid(row=i, column=j) 
        #         e.insert(END, info[j])
        #         e.configure(state="readonly")
        #     i=i+1


    #=====================SubmitFeed=============================
    def submitFeed(self):
        import pymysql as pm

        con = pm.connect(host="localhost", user="root", password="", db="parking management")
        a = con.cursor()    # reference     

        query = "insert into feedback values('{}','{}','{}')".format(self.name.get(),self.mail.get(),self.feed.get())
        a.execute(query)
        self.opFrame8.destroy()
        messagebox.showinfo("Feedback","Feedback recorded successfully")
        
        con.commit()        # confirm   
    # ====================OP FRAME 8=============================

    def Feedback(self):
        self.opFrame8 = Toplevel(self.operatorWin)
        self.opFrame8.geometry("500x400")
        self.opFrame8.title("Parking Management System")
        self.opFrame8.iconbitmap(R'myimages\parko.ico')
        self.opFrame8.resizable(False, False)
        self.opFrame8.configure(background='#003e53')
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#003e53')
        self.style.configure('TButton', background='#000000')
        self.style.configure('TLabel', background='#003e53',
                             foreground='#fff', font=('Arial', 8))
        self.style.configure('Header.TLabel', font=(
            'Arial', 13, 'bold', "underline"))
        self.header_frame = ttk.Frame(self.opFrame8)
        self.header_frame.pack()

        self.name = tk.StringVar()
        self.mail = tk.StringVar()
        self.feed = tk.StringVar()

        ttk.Label(self.header_frame, text='Kindly give your Feedback',
                  style='Header.TLabel').grid(row=0, column=1)
        ttk.Label(self.header_frame, wraplength=300,
                  text=(
                      '\nAdd your name, email, and comment, then click submit to add your comment. \nClick clear if you make a mistake.')).grid(
            row=1, column=1)
        self.content_in_frame = ttk.Frame(self.opFrame8)
        self.content_in_frame.pack()
        ttk.Label(self.content_in_frame, text='\n\nName:').grid(
            row=0, column=0, padx=5, sticky='sw')
        ttk.Label(self.content_in_frame, text='\n\nEmail:').grid(
            row=0, column=1, padx=5, sticky='sw')
        ttk.Label(self.content_in_frame, text='\nComments:').grid(
            row=2, column=0, padx=5, sticky='sw')
        self.comment_name = ttk.Entry(
            self.content_in_frame, width=24,textvariable=self.name, font=('Arial', 10))
        self.comment_email = ttk.Entry(
            self.content_in_frame, width=24,textvariable=self.mail, font=('Arial', 10))
        self.comments = ttk.Entry(self.content_in_frame, width=45,textvariable=self.feed, font=('Arial', 10))
        self.comment_name.grid(row=1, column=0, padx=5)
        self.comment_email.grid(row=1, column=1, padx=5)
        self.comments.grid(row=3, column=0, columnspan=2, padx=5)
        ttk.Button(self.content_in_frame, text='Submit',
                   command=self.submitFeed).grid(row=4, column=0, padx=5, pady=5, sticky='e')
        ttk.Button(self.content_in_frame, text='Clear',
                   command=self.clear).grid(row=4, column=1, padx=5, pady=5, sticky='w')


    def clear(self):
        self.comment_name.delete(0, 'end')
        self.comment_email.delete(0, 'end')
        self.comments.delete(1.0, 'end')

    # ====================OPERATOR MENU==========================

    def operatorWindow(self):

        self.operatorWin = Toplevel(self.root)
        self.operatorWin.title("Parking Management System")
        self.operatorWin['bg'] = "#003e53"

        # sets the geometry of toplevel
        Left = int(self.operatorWin.winfo_screenwidth() - 500) / 2
        Top = int(self.operatorWin.winfo_screenheight() - 440) / 2
        self.operatorWin.geometry("%dx%d+%d+%d" % (450, 440, Left, Top))
        self.menubar = Menu(self.root)
        self.operatorWin.config(menu=self.menubar)
        self.operator_menu = Menu(self.menubar, tearoff=0)
        self.operatorWin.iconbitmap(R"myimages\parko.ico")
        # add menu item to operator menu
        self.operator_menu.add_command(label='Add Customer', command=self.addCustomer)
        self.operator_menu.add_command(label='Charges as per vehicle', command=self.chargeAsPerVeh)
        self.operator_menu.add_command(label='Generate slip', command=self.GenerateSlip)
        self.operator_menu.add_command(label='Display list', command=self.Displayop)
        self.operator_menu.add_command(label='Search list', command=self.SearchVehicle)
        self.operator_menu.add_command(label='Slots Available', command=self.SlotsAvailable)
        self.operator_menu.add_command(label='Feedback', command=self.Feedback)
        self.operator_menu.add_separator()
        self.operator_menu.add_command(label='Main Menu', command=self.operatorWin.destroy)
        
        self.menubar.add_cascade(label="OPERATOR", menu=self.operator_menu)
        self.raw_image=Image.open("myimages\operator.png")
        self.background_image=ImageTk.PhotoImage(self.raw_image.resize((500, 450), Image.ANTIALIAS))
        self.background_label = tk.Label(self.operatorWin, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
     


root = Tk()
obj = PMS(root)
root.mainloop()