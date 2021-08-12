from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
from veza import Konekcija

class Zaposleni:
    def __init__(self,root):
        self.root=root
        self.root.title("   ")
        self.root.geometry("1620x770+307+300")

        self.var_idzaposleni=IntVar()
        self.var_ime=StringVar()
        self.var_prezime=StringVar()
        self.var_idgrad=IntVar()
        self.var_adresa=StringVar()
        self.var_telefon=IntVar()
        self.var_email=StringVar()
        self.var_idodeljenje=IntVar()
        self.var_idzanimanje=IntVar()

        self.var_pronadjiPo=StringVar()
        self.var_pronadjiTekst=StringVar()


        titleLbl=Label(self.root,text="Zaposleni",font=("times new roman",25,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        titleLbl.place(x=0,y=0,width=1620,height=50)

        img1=Image.open(r"hoteliFoto/hotel.jpg")
        img1=img1.resize((100,40),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblImage=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblImage.place(x=5,y=2,width=100,height=40)

        labelFrameLevo=LabelFrame(self.root,bd=2,relief=RIDGE,text="Detalji o zaposlenima",font=("times new roman",12,"bold"),padx=2)
        labelFrameLevo.place(x=5,y=50,width=525,height=490)

        idzaposleniLbl=Label(labelFrameLevo,text="Id zaposlenog",font=("times new roman",14,"bold"),padx=2,pady=6)
        idzaposleniLbl.grid(row=0,column=0,sticky=W)

        idzaposleniEntry=ttk.Entry(labelFrameLevo,textvariable=self.var_idzaposleni,font=("times new roman",14,"bold"),width=35,state="readonly")
        idzaposleniEntry.grid(row=0,column=1)

        imeLbl=Label(labelFrameLevo,text="Ime",font=("times new roman",14,"bold"),padx=2,pady=6)
        imeLbl.grid(row=1,column=0,sticky=W)

        imeEntry=ttk.Entry(labelFrameLevo,textvariable=self.var_ime, font=("times new roman",14,"bold"),width=35)
        imeEntry.grid(row=1,column=1)

        prezimeLbl=Label(labelFrameLevo,text="Prezime",font=("times new roman",14,"bold"),padx=2,pady=6)
        prezimeLbl.grid(row=2,column=0,sticky=W)

        prezimeEntry=ttk.Entry(labelFrameLevo,textvariable=self.var_prezime, font=("times new roman",14,"bold"),width=35)
        prezimeEntry.grid(row=2,column=1)

        idgradLbl=Label(labelFrameLevo,text="Id grada",font=("times new roman",14,"bold"),padx=2,pady=6)
        idgradLbl.grid(row=3,column=0,sticky=W)

        idgradEntry=ttk.Entry(labelFrameLevo,textvariable=self.var_idgrad, font=("times new roman",14,"bold"),width=35)
        idgradEntry.grid(row=3,column=1)

        adresaLbl=Label(labelFrameLevo,text="Adresa",font=("times new roman",14,"bold"),padx=2,pady=6)
        adresaLbl.grid(row=4,column=0,sticky=W)

        adresaEntry=ttk.Entry(labelFrameLevo,textvariable=self.var_adresa, font=("times new roman",14,"bold"),width=35)
        adresaEntry.grid(row=4,column=1)

        telefonLbl=Label(labelFrameLevo,text="Telefon",font=("times new roman",14,"bold"),padx=2,pady=6)
        telefonLbl.grid(row=5,column=0,sticky=W)

        telefonEntry=ttk.Entry(labelFrameLevo,textvariable=self.var_telefon, font=("times new roman",14,"bold"),width=35)
        telefonEntry.grid(row=5,column=1)

        emailLbl=Label(labelFrameLevo,text="Email",font=("times new roman",14,"bold"),padx=2,pady=6)
        emailLbl.grid(row=6,column=0,sticky=W)

        emailEntry=ttk.Entry(labelFrameLevo,textvariable=self.var_email, font=("times new roman",14,"bold"),width=35)
        emailEntry.grid(row=6,column=1)

        idodeljenjeLbl=Label(labelFrameLevo,text="Id odeljenje",font=("times new roman",14,"bold"),padx=2,pady=6)
        idodeljenjeLbl.grid(row=7,column=0,sticky=W)

        idodeljenjeEntry=ttk.Entry(labelFrameLevo,textvariable=self.var_idodeljenje, font=("times new roman",14,"bold"),width=35)
        idodeljenjeEntry.grid(row=7,column=1)

        idzanimanjeLbl=Label(labelFrameLevo,text="Zanimanje",font=("times new roman",14,"bold"),padx=2,pady=6)
        idzanimanjeLbl.grid(row=8,column=0,sticky=W)

        idzanimanjeEntry=ttk.Entry(labelFrameLevo,textvariable=self.var_idzanimanje, font=("times new roman",14,"bold"),width=35)
        idzanimanjeEntry.grid(row=8,column=1)

        btnFrame=Frame(labelFrameLevo)
        btnFrame.place(x=0,y=400,width=342,height=40)


        btnAžuriraj=Button(btnFrame,text="Ažuriraj",command=self.ažuriraj,font=("times new roman",12,"bold"),bg="black",fg="gold",width=10)
        btnAžuriraj.grid(row=0,column=0)

        btnObriši=Button(btnFrame,text="Obriši",command=self.obriši, font=("times new roman",12,"bold"),bg="black",fg="gold",width=10)
        btnObriši.grid(row=0,column=1,padx=1)

        btnPoništi=Button(btnFrame,text="Poništi",command=self.poništi, font=("times new roman",12,"bold"),bg="black",fg="gold",width=10)
        btnPoništi.grid(row=0,column=2,padx=1)

        TablaFrame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Pregledaj i pronadji informacije o zaposlenima",font=("times new roman",12,"bold"),padx=2)
        TablaFrame.place(x=505,y=50,width=1110,height=490)

        pronadjiLbl=Label(TablaFrame,text="Pronadji po:",font=("times new roman",15,"bold"),bg="gold",fg="black")
        pronadjiLbl.grid(row=0,column=0,sticky=W)

        pronadjiCombo=ttk.Combobox(TablaFrame,textvariable=self.var_pronadjiPo,font=("times new roman",15,"bold"),width=24,state="readonly")
        pronadjiCombo['value']=("idzaposleni","ime")
        pronadjiCombo.current()
        pronadjiCombo.grid(row=0,column=1,padx=2)

        pronadjiTekstEntry=ttk.Entry(TablaFrame,textvariable=self.var_pronadjiTekst, font=("times new roman",15,"bold"),width=24)
        pronadjiTekstEntry.grid(row=0,column=2,padx=2)

        btnPronadji=Button(TablaFrame,text="Pronadji",command=self.pronadji, font=("times new roman",15,"bold"),bg="black",fg="gold",width=9)
        btnPronadji.grid(row=0,column=3,padx=1)

        btnPrikažiSve=Button(TablaFrame,text="Prikaži sve",command=self.dohvati, font=("times new roman",15,"bold"),bg="black",fg="gold",width=9)
        btnPrikažiSve.grid(row=0,column=4,padx=1)

        detaljiTabla=Frame(TablaFrame,bd=2,relief=RIDGE)
        detaljiTabla.place(x=0,y=50,width=1100,height=420)

        scrollX=ttk.Scrollbar(detaljiTabla,orient=HORIZONTAL)
        scrollY=ttk.Scrollbar(detaljiTabla,orient=VERTICAL)

        self.podaciZaposlenih=ttk.Treeview(detaljiTabla,columns=("idzaposleni","ime","prezime","idgrad","adresa","telefon","email","idodeljenje","idzanimanje"),xscrollcommand=scrollX.set,yscrollcommand=scrollY.set)

        scrollX.pack(side=BOTTOM,fill=X)
        scrollY.pack(side=RIGHT,fill=Y)

        scrollX.config(command=self.podaciZaposlenih.xview)
        scrollY.config(command=self.podaciZaposlenih.yview)

        self.podaciZaposlenih.heading("idzaposleni",text="Id zaposlenog")
        self.podaciZaposlenih.heading("ime",text="Ime")
        self.podaciZaposlenih.heading("prezime",text="Prezime")
        self.podaciZaposlenih.heading("idgrad",text="Id grada")
        self.podaciZaposlenih.heading("adresa",text="Adresa")
        self.podaciZaposlenih.heading("telefon",text="Telefon")
        self.podaciZaposlenih.heading("email",text="Email")
        self.podaciZaposlenih.heading("idodeljenje",text="Id odeljenja")
        self.podaciZaposlenih.heading("idzanimanje",text="Id zanimanja")

        self.podaciZaposlenih['show']="headings"
        self.podaciZaposlenih.column("idzaposleni",width=100)
        self.podaciZaposlenih.column("ime",width=100)
        self.podaciZaposlenih.column("prezime",width=100)
        self.podaciZaposlenih.column("idgrad",width=100)
        self.podaciZaposlenih.column("adresa",width=100)
        self.podaciZaposlenih.column("telefon",width=100)
        self.podaciZaposlenih.column("email",width=100)
        self.podaciZaposlenih.column("idodeljenje",width=100)
        self.podaciZaposlenih.column("idzanimanje",width=100)

        self.podaciZaposlenih.pack(fill=BOTH,expand=1)
        self.podaciZaposlenih.bind("<ButtonRelease-1>",self.pokazivač)

        img2=Image.open(r"hoteliFoto/hotel.jpg")
        img2=img2.resize((1620,230),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblImage2=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblImage2.place(x=0,y=540,width=1620,height=230)


    def dohvati(self):
        con=Konekcija.getInstance()
        cursor=con.cursor()
        cursor.execute("SELECT idzaposleni,ime,prezime,idgrad,adresa,telefon,email,idodeljenje,idzanimanje FROM zaposleni")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.podaciZaposlenih.delete(*self.podaciZaposlenih.get_children())
            for i in rows:
                self.podaciZaposlenih.insert("",END,values=i)
                con.commit()
        
        
    def pokazivač(self,event=""):
        cursor_row=self.podaciZaposlenih.focus()
        content=self.podaciZaposlenih.item(cursor_row)
        row=content['values']

        self.var_idzaposleni.set(row[0]),
        self.var_ime.set(row[1]),
        self.var_prezime.set(row[2]),
        self.var_idgrad.set(row[3]),
        self.var_adresa.set(row[4]),
        self.var_telefon.set(row[5]),
        self.var_email.set(row[6]),
        self.var_idodeljenje.set(row[7]),
        self.var_idzanimanje.set(row[8])

    def pronadji(self): 
        con=Konekcija.getInstance()
        cursor=con.cursor()
        cursor.execute("SELECT idzaposleni,ime,prezime,idgrad,adresa,telefon,email,idodeljenje,idzanimanje FROM zaposleni WHERE "+str(self.var_pronadjiPo.get())+" LIKE binary '%"+self.var_pronadjiTekst.get()+"%'")
        rows = cursor.fetchall()
        if(len(rows)!=0):
            self.podaciZaposlenih.delete(*self.podaciZaposlenih.get_children())
            for i in rows: 
                self.podaciZaposlenih.insert('',END,values=i)
                con.commit()
        else:
            self.podaciZaposlenih.delete(*self.podaciZaposlenih.get_children()) 


    def ažuriraj(self):
        if self.var_idzaposleni.get()=="":
            messagebox.showerror("Greška","Molimo Vas,unesite id zaposlenog čije podatke ažurirate",parent=self.root)
        else:
            con=Konekcija.getInstance()
            cursor=con.cursor()
            cursor.execute("UPDATE zaposleni SET idgrad=%s,adresa=%s,telefon=%s WHERE idzaposleni=%s",(
                self.var_idgrad.get(),
                self.var_adresa.get(),
                self.var_telefon.get(),
                self.var_idzaposleni.get()
            ))
            con.commit()
            messagebox.showinfo("Ažuriranje","Detalji o zaposlenima su uspešno ažurirani",parent=self.root)
            self.dohvati()

    
    def obriši(self):
        obriši=messagebox.askyesno("Hotel Menadžment","Da li zaista želite da obrišete ovog zaposlenog?",parent=self.root)
        if obriši>0:
            con=Konekcija.getInstance()
            cursor=con.cursor()   
            query="DELETE FROM zaposleni WHERE idzaposleni=%s"
            value=(self.var_idzaposleni.get(),)
            cursor.execute(query,value)
        elif  not obriši:
            return
        con.commit()
        messagebox.showinfo("Brisanje","Brisanje zaposlenog uspešno",parent=self.root)
        self.dohvati()


    def poništi(self):
        self.var_idzaposleni.set(0)
        self.var_ime.set("")
        self.var_prezime.set("")
        self.var_idgrad.set(0)
        self.var_adresa.set("")
        self.var_telefon.set(0)
        self.var_email.set("")
        self.var_idodeljenje.set(0)
        self.var_idzanimanje.set(0)
        self.var_pronadjiPo.set("")
        self.var_pronadjiTekst.set("")
        self.podaciZaposlenih.delete(*self.podaciZaposlenih.get_children())


'''root=Tk()
object=Zaposleni(root)
mainloop()'''