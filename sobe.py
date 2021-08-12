from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox

from mysql.connector import cursor
from veza2 import Konekcija2

class SobeDetalji:
    def __init__(self,root):
        self.root=root
        self.root.title("   ")
        self.root.geometry("1620x770+307+300")

        self.var_brojsobe=IntVar()
        self.var_sprat=IntVar()
        self.var_tipsobe=StringVar()
        self.var_status=StringVar()
        self.var_cena=IntVar()

        lbl_title=Label(self.root,text="Hotelske Sobe",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1620,height=50)

        img1=Image.open(r"sobeFoto/room.jpg")
        img1=img1.resize((120,40),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblImage1=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblImage1.place(x=5,y=5,width=120,height=40)

        labelFrameLevo=LabelFrame(self.root,bd=2,relief=RIDGE,text="Dodavanje novih soba",font=("times new roman",12,"bold"),padx=2)
        labelFrameLevo.place(x=5,y=50,width=590,height=380)

        brojsobeLbl=Label(labelFrameLevo,text="Broj sobe",font=("times new roman",15,"bold"),padx=2,pady=6)
        brojsobeLbl.grid(row=0,column=0,sticky=W)

        brojsobeEntry=ttk.Entry(labelFrameLevo,textvariable=self.var_brojsobe, font=("times new roman",13,"bold"),width=25)
        brojsobeEntry.grid(row=0,column=1,sticky=W)

        spratLbl=Label(labelFrameLevo,text="Sprat",font=("times new roman",15,"bold"),padx=2,pady=6)
        spratLbl.grid(row=1,column=0,sticky=W)

        spratEntry=ttk.Entry(labelFrameLevo,textvariable=self.var_sprat, font=("times new roman",14,"bold"),width=25)
        spratEntry.grid(row=1,column=1,sticky=W)

        tipsobeLbl=Label(labelFrameLevo,text="Tip Sobe",font=("times new roman",14,"bold"),padx=2,pady=6)
        tipsobeLbl.grid(row=2,column=0,sticky=W)

        tipsobeEntry=ttk.Entry(labelFrameLevo,textvariable=self.var_tipsobe, font=("times new roman",14,"bold"),width=25)
        tipsobeEntry.grid(row=2,column=1,sticky=W)

        statusLbl=Label(labelFrameLevo,text="Status",font=("times new roman",14,"bold"),padx=2,pady=6)
        statusLbl.grid(row=3,column=0,sticky=W)

        statusEntry=ttk.Entry(labelFrameLevo,textvariable=self.var_status, font=("times new roman",14,"bold"),width=25)
        statusEntry.grid(row=3,column=1,sticky=W)

        cenaLbl=Label(labelFrameLevo,text="Cena",font=("times new roman",14,"bold"),padx=2,pady=6)
        cenaLbl.grid(row=4,column=0,sticky=W)

        cenaEntry=ttk.Entry(labelFrameLevo,textvariable=self.var_cena, font=("times new roman",14,"bold"),width=25)
        cenaEntry.grid(row=4,column=1,sticky=W)
    
        opisLbl=Label(labelFrameLevo,text="Opis",font=("times new roman",14,"bold"),padx=2,pady=6)
        opisLbl.grid(row=5,column=0,sticky=W)

        self.opisTekst=Text(labelFrameLevo,width=35,height=4,font=("verdana",12,"bold"))
        self.opisTekst.grid(row=5,column=1,sticky=W)

        btnFrame=Frame(labelFrameLevo)
        btnFrame.place(x=0,y=300,width=412,height=40)

        btnDodaj=Button(btnFrame,text="Dodaj",command=self.dodaj, font=("times new roman",11,"bold"),bg="black",fg="gold",width=10)
        btnDodaj.grid(row=0,column=0,padx=1)

        btnAžuriraj=Button(btnFrame,text="Ažuriraj",command=self.ažuriraj, font=("times new roman",11,"bold"),bg="black",fg="gold",width=10)
        btnAžuriraj.grid(row=0,column=1,padx=1)

        btnObriši=Button(btnFrame,text="Obriši",command=self.obriši, font=("times new roman",11,"bold"),bg="black",fg="gold",width=10)
        btnObriši.grid(row=0,column=2,padx=1)

        btnPoništi=Button(btnFrame,text="Poništi",command=self.poništi, font=("times new roman",11,"bold"),bg="black",fg="gold",width=10)
        btnPoništi.grid(row=0,column=3,padx=1)

        TablaFrame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Prikaži detalje soba",font=("times new roman",12,"bold"),padx=2)
        TablaFrame.place(x=600,y=50,width=1020,height=380)

        scrollX=ttk.Scrollbar(TablaFrame,orient=HORIZONTAL)
        scrollY=ttk.Scrollbar(TablaFrame,orient=VERTICAL)

        self.ispis=ttk.Treeview(TablaFrame,columns=("broj sobe","sprat","tip sobe","status","opis","cena"),xscrollcommand=scrollX.set,yscrollcommand=scrollY.set)
        scrollX.pack(side=BOTTOM,fill=X)
        scrollY.pack(side=RIGHT,fill=Y)
        scrollX.config(command=self.ispis.xview)
        scrollY.config(command=self.ispis.yview)

        self.ispis.heading("broj sobe",text="Broj Sobe")
        self.ispis.heading("sprat",text="Sprat")
        self.ispis.heading("tip sobe",text="Tip sobe")
        self.ispis.heading("status",text="Status")
        self.ispis.heading("opis",text="Opis")
        self.ispis.heading("cena",text="Cena")
        self.ispis['show']="headings"
        self.ispis.column("broj sobe",width=100)
        self.ispis.column("sprat",width=100)
        self.ispis.column("tip sobe",width=100)
        self.ispis.column("status",width=100)
        self.ispis.column("opis",width=100)
        self.ispis.column("cena",width=100)
        self.ispis.pack(fill=BOTH,expand=1)
        self.ispis.bind("<ButtonRelease-1>",self.podaci)

        podacibtn=Button(labelFrameLevo,text="Sobe",command=self.dohvatiPodatke,font=("times new roman",11,"bold"),bg="black",fg="gold",width=10)
        podacibtn.place(x=530,y=10,width=50,height=40)

        #ttk.Style().configure("Treeview", background="red2", foreground="white", fieldbackground="red2")

        img2=Image.open(r"sobeFoto/room.jpg")
        img2=img2.resize((810,340),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblImage2=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblImage2.place(x=0,y=430,width=810,height=340)

        img3=Image.open(r"sobeFoto/room3.jpg")
        img3=img3.resize((810,340),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblImage3=Label(self.root,image=self.photoimg3,bd=4,relief=RIDGE)
        lblImage3.place(x=810,y=430,width=810,height=340)



    def dodaj(self):
        if self.var_brojsobe.get()=="" or self.var_sprat.get()=="" or self.var_tipsobe.get()=="" or self.var_status.get()=="" or self.var_cena.get()=="":
            messagebox.showerror("Greška","Morate popuniti sva polja",parent=self.root)
        else:
            try:
                con=Konekcija2.getInstance()
                cursor=con.cursor()
                cursor.execute("INSERT INTO sobe VALUES(%s,%s,%s,%s,%s,%s)",(
                self.var_brojsobe.get(),
                self.var_sprat.get(),
                self.var_tipsobe.get(),
                self.var_status.get(),
                self.opisTekst.get("1.0",END),
                self.var_cena.get()
          ))
                con.commit()
                messagebox.showinfo("Uspešno","Nova soba je dodata",parent=self.root)
                self.poništi()
                self.dohvatiPodatke()
                
            except Exception as es:
                messagebox.showwarning("Upozorenje",f"Nešto je pošlo naopako : {es}",parent=self.root)

    def dohvatiPodatke(self):
        con=Konekcija2.getInstance()
        cursor=con.cursor()
        cursor.execute("SELECT * FROM sobe")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.ispis.delete(*self.ispis.get_children())
            for i in rows:
                self.ispis.insert("",END,values=i)
            con.commit()


    def podaci(self,event=""):
        cursor_row=self.ispis.focus()
        content=self.ispis.item(cursor_row)
        row=content['values']

        self.var_brojsobe.set(row[0])
        self.var_sprat.set(row[1])
        self.var_tipsobe.set(row[2])
        self.var_status.set(row[3])
        self.var_cena.set(row[5])
        self.opisTekst.delete("1.0",END)
        self.opisTekst.insert(END,row[4])

    def ažuriraj(self):
        if self.var_sprat.get()=="" or self.var_tipsobe.get()=="" or self.var_status.get()=="" or self.var_cena.get()=="":
            messagebox.showerror(
                "Greška", "Morate uneti sve podatke", parent=self.root)
        else:
            con=Konekcija2.getInstance()
            cursor = con.cursor()
            cursor.execute("UPDATE sobe SET sprat=%s,tip_sobe=%s,statusSobe=%s,opis=%s,cena=%s WHERE brojsobe=%s", (
                self.var_sprat.get(),
                self.var_tipsobe.get(),
                self.var_status.get(),
                self.opisTekst.get("1.0",END),
                self.var_cena.get(),
                self.var_brojsobe.get()
            ))
            con.commit()
            messagebox.showinfo("Uspešno", "Podaci o sobama su ažurirani", parent=self.root)
            self.poništi()
            self.dohvatiPodatke()
            

    def obriši(self):
        obriši=messagebox.askyesno("Hotel Sobe","Da li želite da obrišete ovu sobu?")
        if obriši>0:
            con=Konekcija2.getInstance()
            cursor=con.cursor()
            query=("DELETE FROM sobe WHERE brojsobe=%s")
            value=(self.var_brojsobe.get(),)
            cursor.execute(query,value)
        elif  not obriši:
            return
        con.commit()
        messagebox.showinfo("OK", "Soba je izbrisana", parent=self.root)
        self.poništi()
        self.dohvatiPodatke()
        

    def poništi(self):
        self.var_brojsobe.set(0)
        self.var_sprat.set(0)
        self.var_tipsobe.set("")
        self.var_status.set("")
        self.var_cena.set(0)
        self.opisTekst.delete("1.0",END)
        self.ispis.delete(*self.ispis.get_children())
       

'''root=Tk()
object=SobeDetalji(root)
root.mainloop()'''