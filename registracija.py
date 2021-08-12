from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import random
from time import strptime
from datetime import date, datetime

from mysql.connector import cursor
from veza import Konekcija

class Registracija:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Program")
        self.root.geometry("1850x1050+0+0")

        self.var_ime=StringVar()
        self.var_prezime=StringVar()
        self.var_idgrad=IntVar()
        self.var_adresa=StringVar()
        self.var_telefon=IntVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_lozinka=StringVar()
        self.var_lozinkaPotvrda=StringVar()
        self.var_idodeljenje=IntVar()
        self.var_idzanimanje=IntVar()

        self.var_check=IntVar()


        img1=Image.open(r"plažaFoto/beach3.jpg")
        img1=img1.resize((1850,1050),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblImage1=Label(self.root,image=self.photoimg1)
        lblImage1.place(x=0,y=0,relwidth=1,relheight=1)

        img2=Image.open(r"plažaFoto/beach4.jpg")
        img2=img2.resize((470,690),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblImage2=Label(self.root,image=self.photoimg2)
        lblImage2.place(x=320,y=130,width=470,height=690)

        frame=Frame(self.root,bg="white")
        frame.place(x=740,y=130,width=800,height=690)

        registracijaLbl=Label(frame,text="Registrujte se ovde",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        registracijaLbl.place(x=20,y=20)

        imeLbl=Label(frame,text="Ime",font=("times new roman",15,"bold"),bg="white")
        imeLbl.place(x=50,y=100)

        imeEntry=ttk.Entry(frame,textvariable=self.var_ime, font=("times new roman",15,"bold"))
        imeEntry.place(x=50,y=130,width=250)

        prezimeLbl=Label(frame,text="Prezime",font=("times new roman",15,"bold"),fg="black",bg="white")
        prezimeLbl.place(x=370,y=100)

        prezimeEntry=ttk.Entry(frame,textvariable=self.var_prezime, font=("times new roman",15,"bold"))
        prezimeEntry.place(x=370,y=130,width=250)

        idgradLbl=Label(frame,text="Id Grada",font=("times new roman",15,"bold"),fg="black",bg="white")
        idgradLbl.place(x=50,y=170)

        idgradEntry=ttk.Entry(frame,textvariable=self.var_idgrad, font=("times new roman",15,"bold"))
        idgradEntry.place(x=50,y=200,width=250)

        adresaLbl=Label(frame,text="Adresa",font=("times new roman",15,"bold"),fg="black",bg="white")
        adresaLbl.place(x=370,y=170)

        adresaEntry=ttk.Entry(frame,textvariable=self.var_adresa, font=("times new roman",15,"bold"))
        adresaEntry.place(x=370,y=200,width=250)

        telefonLbl=Label(frame,text="Telefon",font=("times new roman",15,"bold"),fg="black",bg="white")
        telefonLbl.place(x=50,y=240)

        telefonEntry=ttk.Entry(frame,textvariable=self.var_telefon, font=("times new roman",15,"bold"))
        telefonEntry.place(x=50,y=270,width=250)

        emailLbl=Label(frame,text="E-mail",font=("times new roman",15,"bold"),fg="black",bg="white")
        emailLbl.place(x=370,y=240)

        emailEntry=ttk.Entry(frame,textvariable=self.var_email, font=("times new roman",15,"bold"))
        emailEntry.place(x=370,y=270,width=250)

        securityQLbl=Label(frame,text="Sigurnosno Pitanje",font=("times new roman",15,"bold"),fg="black",bg="white")
        securityQLbl.place(x=50,y=310)

        securityQcombo=ttk.Combobox(frame,textvariable=self.var_securityQ, font=("times new roman",15,"bold"),state="readonly")
        securityQcombo['values']=("Biraj","Mesto rodjenja","Kućni ljubimac","Ime bake")
        securityQcombo.place(x=50,y=340,width=250)
        securityQcombo.current()

        securityALbl=Label(frame,text="Sigurnosni Odgovor",font=("times new roman",15,"bold"),fg="black",bg="white")
        securityALbl.place(x=370,y=310)

        securityAEntry=ttk.Entry(frame,textvariable=self.var_securityA, font=("times new roman",15,"bold"))
        securityAEntry.place(x=370,y=340,width=250)

        lozinkaLbl=Label(frame,text="Lozinka",font=("times new roman",15,"bold"),fg="black",bg="white")
        lozinkaLbl.place(x=50,y=370)

        lozinkaEntry=ttk.Entry(frame,textvariable=self.var_lozinka, font=("times new roman",15,"bold"))
        lozinkaEntry.place(x=50,y=410,width=250)

        lozinkaPotvrdaLbl=Label(frame,text="Potvrdite lozinku",font=("times new roman",15,"bold"),fg="black",bg="white")
        lozinkaPotvrdaLbl.place(x=370,y=370)

        lozinkaPotvrdaEntry=ttk.Entry(frame,textvariable=self.var_lozinkaPotvrda, font=("times new roman",15,"bold"))
        lozinkaPotvrdaEntry.place(x=370,y=410,width=250)

        idodeljenjeLbl=Label(frame,text="Id Odeljenja",font=("times new roman",15,"bold"),fg="black",bg="white")
        idodeljenjeLbl.place(x=50,y=440)

        idodeljenjeEntry=ttk.Entry(frame,textvariable=self.var_idodeljenje, font=("times new roman",15,"bold"))
        idodeljenjeEntry.place(x=50,y=480,width=250)

        idzanimanjeLbl=Label(frame,text="Id Zanimanja",font=("times new roman",15,"bold"),fg="black",bg="white")
        idzanimanjeLbl.place(x=370,y=440)

        idzanimanjeEntry=ttk.Entry(frame,textvariable=self.var_idzanimanje, font=("times new roman",15,"bold"))
        idzanimanjeEntry.place(x=370,y=480,width=250)

        btnCheck=Checkbutton(frame,variable=self.var_check, text="Prihvatam uslove",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        btnCheck.place(x=50,y=540)

        img3=Image.open(r"userLoginFoto/register2.png")
        img3=img3.resize((200,50),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        b1=Button(frame,image=self.photoimg3,command=self.registracija_podataka, borderwidth=0,cursor="hand2")
        b1.place(x=70,y=580,width=200)

        img4=Image.open(r"userLoginFoto/login1.png")
        img4=img4.resize((200,50),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b2=Button(frame,image=self.photoimg4,command=self.vraćanjeUlogovanje, borderwidth=0,cursor="hand2")
        b2.place(x=390,y=580,width=200)


    def registracija_podataka(self):
        if self.var_ime.get()=="" or self.var_prezime.get()=="" or self.var_idgrad.get()==0 or self.var_adresa.get()=="" or self.var_telefon.get()==0 or self.var_email.get()=="" or self.var_securityQ.get()=="Biraj" or self.var_securityA.get()=="" or self.var_lozinka.get()=="" or self.var_lozinkaPotvrda.get()=="" or self.var_idodeljenje.get()==0 or self.var_idzanimanje.get()==0:
            messagebox.showerror("Greška","Morate popuniti sva polja")
        elif self.var_lozinka.get()!= self.var_lozinkaPotvrda.get():
            messagebox.showerror("Greška","Potvrda lozinke se ne poklapa sa lozinkom")
        elif self.var_check.get()==0:
            messagebox.showerror("Greška","Molimo Vas,prihvatite uslove")
        else:
            con=Konekcija.getInstance()
            cursor=con.cursor()
            query=("SELECT * FROM zaposleni WHERE email=%s")
            value=(self.var_email.get(),)
            cursor.execute(query,value)
            row=cursor.fetchone()
            if row!=None:
                messagebox.showerror("Greška","Pogrešna lozinka,pokušajte ponovo")
            else:
                cursor.execute("INSERT INTO zaposleni(ime,prezime,idgrad,adresa,telefon,email,security_question,security_answer,lozinka,idodeljenje,idzanimanje) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            self.var_ime.get(),
            self.var_prezime.get(),
            self.var_idgrad.get(),
            self.var_adresa.get(),
            self.var_telefon.get(),
            self.var_email.get(),
            self.var_securityQ.get(),
            self.var_securityA.get(),
            self.var_lozinka.get(),
            self.var_idodeljenje.get(),
            self.var_idzanimanje.get(),
                ))
                con.commit()
                messagebox.showinfo("Uspešno","Registracija uspešna")

    def vraćanjeUlogovanje(self):
        self.root.destroy()


'''root=Tk()
object=Registracija(root)
mainloop()'''