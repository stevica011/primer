from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
from počasniGost import PredikcijaGosta
from veza import Konekcija

class Gosti:
    def __init__(self,root):
        self.root=root
        self.root.title("   ")
        self.root.geometry("1620x770+307+300")


        self.var_idgost=IntVar()
        x=random.randint(1000,4999)
        self.var_idgost.set(int(x))
        self.var_ime=StringVar()
        self.var_prezime=StringVar()
        self.var_pol=StringVar()
        self.var_godine=IntVar()
        self.var_telefon=IntVar()
        self.var_email=StringVar()
        self.var_brojdokumenta=IntVar()
        self.var_iddokument=IntVar()
        self.var_brojrezervacija=IntVar()
        self.var_bodovi=IntVar()
        self.var_rezident=StringVar()
        self.var_počasnigost=IntVar()

        self.PronadjiPo=StringVar()
        self.PronadjiTekst=StringVar()



        lbl_title=Label(self.root,text="Baza gostiju",font=("times new roman",25,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1620,height=50)

        img1=Image.open(r"hoteliFoto/hotel.jpg")
        img1=img1.resize((100,40),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblImage=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblImage.place(x=5,y=2,width=100,height=40)

        labelFrameLevo=LabelFrame(self.root,bd=2,relief=RIDGE,text="Detalji gostiju",font=("times new roman",12,"bold"),padx=2)
        labelFrameLevo.place(x=5,y=50,width=502,height=530)

        idgostLbl=Label(labelFrameLevo,text="ID gosta",font=("times new roman",14,"bold"),padx=2,pady=6)
        idgostLbl.grid(row=0,column=0,sticky=W)

        idgostEntry=ttk.Entry(labelFrameLevo,textvariable=self.var_idgost,font=("times new roman",14,"bold"),width=20,state="readonly")
        idgostEntry.grid(row=0,column=1)

        imeLbl=Label(labelFrameLevo,text="Ime",font=("times new roman",14,"bold"),padx=2,pady=6)
        imeLbl.grid(row=1,column=0,sticky=W)

        imeEntry=ttk.Entry(labelFrameLevo,textvariable=self.var_ime, font=("times new roman",14,"bold"),width=20)
        imeEntry.grid(row=1,column=1,padx=30)

        btnML=Button(labelFrameLevo,text="Predikcija",command=self.predikcija, font=("times new roman",12,"bold"),bg="black",fg="gold",width=9)
        btnML.grid(row=1,column=3,padx=1)

        prezimeLbl=Label(labelFrameLevo,text="Prezime",font=("times new roman",14,"bold"),padx=2,pady=6)
        prezimeLbl.grid(row=2,column=0,sticky=W)

        prezimeEntry=ttk.Entry(labelFrameLevo,textvariable=self.var_prezime, font=("times new roman",14,"bold"),width=20)
        prezimeEntry.grid(row=2,column=1)

        polLbl=Label(labelFrameLevo,text="Pol",font=("times new roman",14,"bold"),padx=2,pady=6)
        polLbl.grid(row=3,column=0,sticky=W)

        polCombo=ttk.Combobox(labelFrameLevo,textvariable=self.var_pol,font=("times new roman",13,"bold"),width=18,state="readonly")
        polCombo.current()
        polCombo['value']=("Muški","Ženski")
        polCombo.grid(row=3,column=1,padx=1)

        godineLbl=Label(labelFrameLevo,text="Godine",font=("times new roman",14,"bold"),padx=2,pady=6)
        godineLbl.grid(row=4,column=0,sticky=W)

        godineEntry=ttk.Entry(labelFrameLevo,textvariable=self.var_godine, font=("times new roman",14,"bold"),width=20)
        godineEntry.grid(row=4,column=1)

        telefonLbl=Label(labelFrameLevo,text="Telefon",font=("times new roman",14,"bold"),padx=2,pady=6)
        telefonLbl.grid(row=5,column=0,sticky=W)

        telefonEntry=ttk.Entry(labelFrameLevo,textvariable=self.var_telefon, font=("times new roman",14,"bold"),width=20)
        telefonEntry.grid(row=5,column=1)

        emailLbl=Label(labelFrameLevo,text="Email",font=("times new roman",14,"bold"),padx=2,pady=6)
        emailLbl.grid(row=6,column=0,sticky=W)

        emailEntry=ttk.Entry(labelFrameLevo,textvariable=self.var_email, font=("times new roman",14,"bold"),width=20)
        emailEntry.grid(row=6,column=1)

        brojdokumentaLbl=Label(labelFrameLevo,text="Broj dokumenta",font=("times new roman",14,"bold"),padx=2,pady=6)
        brojdokumentaLbl.grid(row=7,column=0,sticky=W)

        brojdokumentaEntry=ttk.Entry(labelFrameLevo,textvariable=self.var_brojdokumenta, font=("times new roman",14,"bold"),width=20)
        brojdokumentaEntry.grid(row=7,column=1)

        iddokumentLbl=Label(labelFrameLevo,text="Dokument",font=("times new roman",14,"bold"),padx=2,pady=6)
        iddokumentLbl.grid(row=8,column=0,sticky=W)

        iddokumentCombo=ttk.Combobox(labelFrameLevo,textvariable=self.var_iddokument,font=("times new roman",13,"bold"),width=18,state="readonly")
        iddokumentCombo.current()
        iddokumentCombo['value']=(1,2,3)
        iddokumentCombo.grid(row=8,column=1,padx=1)

        brojrezervacijaLbl=Label(labelFrameLevo,text="Broj rezervacija",font=("times new roman",14,"bold"),padx=2,pady=6)
        brojrezervacijaLbl.grid(row=9,column=0,sticky=W)

        brojrezervacijaEntry=ttk.Entry(labelFrameLevo,textvariable=self.var_brojrezervacija, font=("times new roman",14,"bold"),width=20)
        brojrezervacijaEntry.grid(row=9,column=1)

        bodoviLbl=Label(labelFrameLevo,text="Bodovi",font=("times new roman",14,"bold"),padx=2,pady=6)
        bodoviLbl.grid(row=10,column=0,sticky=W)

        bodoviEntry=ttk.Entry(labelFrameLevo,textvariable=self.var_bodovi, font=("times new roman",14,"bold"),width=20)
        bodoviEntry.grid(row=10,column=1)

        btnML2=Button(labelFrameLevo,text="Promena statusa",command=self.statusGosta, font=("times new roman",12,"bold"),bg="black",fg="gold",width=11)
        btnML2.grid(row=10,column=3,padx=1)

        počasnigostLbl=Label(labelFrameLevo,text="Rezident",font=("times new roman",14,"bold"),padx=2,pady=6)
        počasnigostLbl.grid(row=11,column=0,sticky=W)

        počasnigostEntry=ttk.Entry(labelFrameLevo,textvariable=self.var_rezident, font=("times new roman",14,"bold"),width=20)
        počasnigostEntry.grid(row=11,column=1)

        rezidentLbl=Label(labelFrameLevo,text="Počasni gost",font=("times new roman",14,"bold"),padx=2,pady=6)
        rezidentLbl.grid(row=12,column=0,sticky=W)

        rezidentEntry=ttk.Entry(labelFrameLevo,textvariable=self.var_počasnigost, font=("times new roman",14,"bold"),width=20)
        rezidentEntry.grid(row=12,column=1)

        btnFrame=Frame(labelFrameLevo)
        btnFrame.place(x=0,y=470,width=448,height=36)

        btnRegistruj=Button(btnFrame,text="Registruj",command=self.registracija, font=("times new roman",12,"bold"),bg="black",fg="gold",width=10)
        btnRegistruj.grid(row=0,column=0,padx=1)

        btnPromeni=Button(btnFrame,text="Promeni",command=self.ažuriraj, font=("times new roman",12,"bold"),bg="black",fg="gold",width=10)
        btnPromeni.grid(row=0,column=1,padx=1)

        btnObriši=Button(btnFrame,text="Obriši",command=self.obriši, font=("times new roman",12,"bold"),bg="black",fg="gold",width=10)
        btnObriši.grid(row=0,column=2,padx=1)

        btnPoništi=Button(btnFrame,text="Poništi",command=self.poništi, font=("times new roman",12,"bold"),bg="black",fg="gold",width=10)
        btnPoništi.grid(row=0,column=3,padx=1)


        TablaFrame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Pogledajte i potražite detalje o gostima",font=("times new roman",12,"bold"),padx=2)
        TablaFrame.place(x=505,y=50,width=1110,height=530)

        lblPronadji=Label(TablaFrame,text="Pronadji po:",font=("times new roman",15,"bold"),bg="gold",fg="black")
        lblPronadji.grid(row=0,column=0,sticky=W)

        
        comboPronadji=ttk.Combobox(TablaFrame,textvariable=self.PronadjiPo,font=("times new roman",15,"bold"),width=24,state="readonly")
        comboPronadji['value']=("ime","prezime")
        comboPronadji.current()
        comboPronadji.grid(row=0,column=1,padx=2)

        tekstPronadji=ttk.Entry(TablaFrame,textvariable=self.PronadjiTekst, font=("times new roman",15,"bold"),width=24)
        tekstPronadji.grid(row=0,column=2,padx=2)

        btnPronadji=Button(TablaFrame,text="Pronadji",command=self.pronadji, font=("times new roman",15,"bold"),bg="black",fg="gold",width=9)
        btnPronadji.grid(row=0,column=3,padx=1)

        btnPrikažiSve=Button(TablaFrame,text="ShowAll",command=self.prikažiGoste, font=("times new roman",15,"bold"),bg="black",fg="gold",width=9)
        btnPrikažiSve.grid(row=0,column=4,padx=1)


        detaljiTabla=Frame(TablaFrame,bd=2,relief=RIDGE)
        detaljiTabla.place(x=0,y=50,width=1100,height=460)

        scrollX=ttk.Scrollbar(detaljiTabla,orient=HORIZONTAL)
        scrollY=ttk.Scrollbar(detaljiTabla,orient=VERTICAL)

        self.detaljiTabla=ttk.Treeview(detaljiTabla,columns=("idgost","ime","prezime","pol","godine","telefon","email","brojdokumenta","iddokument","brojrezervacija","bodovi","rezident","počasnigost"),xscrollcommand=scrollX.set,yscrollcommand=scrollY.set)

        scrollX.pack(side=BOTTOM,fill=X)
        scrollY.pack(side=RIGHT,fill=Y)

        scrollX.config(command=self.detaljiTabla.xview)
        scrollY.config(command=self.detaljiTabla.yview)

        self.detaljiTabla.heading("idgost",text="ID gosta")
        self.detaljiTabla.heading("ime",text="Ime")
        self.detaljiTabla.heading("prezime",text="Prezime")
        self.detaljiTabla.heading("pol",text="Pol")
        self.detaljiTabla.heading("godine",text="Godine")
        self.detaljiTabla.heading("telefon",text="telefon")
        self.detaljiTabla.heading("email",text="Email")
        self.detaljiTabla.heading("brojdokumenta",text="Broj dok.")
        self.detaljiTabla.heading("iddokument",text="ID dok.")
        self.detaljiTabla.heading("brojrezervacija",text="Broj rezerv.")
        self.detaljiTabla.heading("bodovi",text="Bodovi")
        self.detaljiTabla.heading("rezident",text="Rezident")
        self.detaljiTabla.heading("počasnigost",text="Počasni")
        self.detaljiTabla['show']="headings"
        self.detaljiTabla.column("idgost",width=100)
        self.detaljiTabla.column("ime",width=100)
        self.detaljiTabla.column("prezime",width=100)
        self.detaljiTabla.column("pol",width=100)
        self.detaljiTabla.column("godine",width=100)
        self.detaljiTabla.column("telefon",width=100)
        self.detaljiTabla.column("email",width=100)
        self.detaljiTabla.column("brojdokumenta",width=100)
        self.detaljiTabla.column("iddokument",width=100)
        self.detaljiTabla.column("brojrezervacija",width=100)
        self.detaljiTabla.column("bodovi",width=100)
        self.detaljiTabla.column("rezident",width=100)
        self.detaljiTabla.column("počasnigost",width=100)
        

        self.detaljiTabla.pack(fill=BOTH,expand=1)
        self.detaljiTabla.bind("<ButtonRelease-1>",self.pokazivač)


        img2=Image.open(r"hoteliFoto/hotel.jpg")
        img2=img2.resize((1620,200),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblImage2=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblImage2.place(x=0,y=577,width=1620,height=200)


    def registracija(self):
        if self.var_idgost.get()==0 or self.var_ime.get()=="" or self.var_prezime.get()=="" or self.var_pol.get()=="" or self.var_godine.get()==0 or self.var_telefon.get()==0 or self.var_email.get()=="" or self.var_brojdokumenta.get()==0 or self.var_iddokument.get()==0 or self.var_rezident.get()=="":
            messagebox.showerror("Greška","Sva polja morate popuniti",parent=self.root)
        else:
            try:
                con=Konekcija.getInstance()
                cursor=con.cursor()
                cursor.execute("INSERT INTO gosti VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            self.var_idgost.get(),
            self.var_ime.get(),
            self.var_prezime.get(),
            self.var_pol.get(),
            self.var_godine.get(),
            self.var_telefon.get(),
            self.var_email.get(),
            self.var_brojdokumenta.get(),
            self.var_iddokument.get(),
            self.var_brojrezervacija.get(),
            self.var_bodovi.get(),
            self.var_rezident.get(),
            self.var_počasnigost.get()))
                con.commit()
                messagebox.showinfo("Uspešno","Gost je uspešno registrovan",parent=self.root)
                self.poništi()
                self.prikažiGoste()
            except Exception as es:
                messagebox.showwarning("Upozorenje",f"Nešto je pošlo loše:{es}",parent=self.root)

    def ažuriraj(self):
        if self.var_idgost.get()==0:
            messagebox.showerror("Greška","Molimo Vas,unesite ID gosta",parent=self.root)
        else:
            con=Konekcija.getInstance()
            cursor=con.cursor()
            cursor.execute("UPDATE gosti SET telefon=%s,email=%s WHERE idgosti=%s",(
                self.var_telefon.get(),
                self.var_email.get(),
                self.var_idgost.get()
            ))
            con.commit()
            messagebox.showinfo("Uspešno","Podaci o gostu su uspešno izmenjeni",parent=self.root)
            self.poništi()
            self.prikažiGoste()

    def statusGosta(self):
            con=Konekcija.getInstance()
            cursor=con.cursor()
            cursor.execute("UPDATE gosti SET počasnigost=4 WHERE bodovi<1000")
            cursor.execute("UPDATE gosti SET počasnigost=3 WHERE bodovi>1000 and bodovi<2000" )
            cursor.execute("UPDATE gosti SET počasnigost=2 WHERE bodovi>2000 and bodovi<4000")
            cursor.execute("UPDATE gosti SET počasnigost=1 WHERE bodovi>4000")
            con.commit()
            messagebox.showinfo("Uspešno","Status gostiju je ažuriran",parent=self.root)
            self.poništi()
            self.prikažiGoste()
            
    def obriši(self):
        obriši=messagebox.askyesno("Hotel Menadžment Sistem","Da li zaista želite da obrišete gosta?")
        if obriši>0:
            con=Konekcija.getInstance()
            cursor=con.cursor()
            query=("DELETE FROM gosti WHERE idgosti=%s")
            value=(self.var_idgost.get(),)
            cursor.execute(query,value)
        elif  not obriši:
            return
        con.commit()
        messagebox.showinfo("OK","Uspešno obrisani podaci o gostu",parent=self.root)
        self.poništi()
        self.prikažiGoste()
        

    def poništi(self):
        self.var_ime.set("")
        self.var_prezime.set("")
        self.var_pol.set("")
        self.var_godine.set(0)
        self.var_telefon.set(0)
        self.var_email.set("")
        self.var_brojdokumenta.set(0)
        self.var_iddokument.set(0)
        self.var_brojrezervacija.set(0)
        self.var_bodovi.set(0)
        self.var_rezident.set("")
        self.var_počasnigost.set(0)
        x=random.randint(1000,9999)
        self.var_idgost.set(str(x))
        self.detaljiTabla.delete(*self.detaljiTabla.get_children())


    def pronadji(self): 
        con=Konekcija.getInstance()
        cur=con.cursor()
        cur.execute("SELECT * FROM gosti WHERE "+str(self.PronadjiPo.get())+" like binary '%"+self.PronadjiTekst.get()+"%'") 
        rows = cur.fetchall()
        if(len(rows)!=0):
            self.detaljiTabla.delete(*self.detaljiTabla.get_children())
            for i in rows: 
                self.detaljiTabla.insert('',END,values=i)
                con.commit()
        else:
            self.detaljiTabla.delete(*self.detaljiTabla.get_children()) 

    def prikažiGoste(self):
        con=Konekcija.getInstance()
        cursor=con.cursor()
        cursor.execute("SELECT * FROM gosti")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.detaljiTabla.delete(*self.detaljiTabla.get_children())
            for i in rows:
                self.detaljiTabla.insert("",END,values=i)
        con.commit()

    
    def pokazivač(self,event=""):
        cursor_row=self.detaljiTabla.focus()
        content=self.detaljiTabla.item(cursor_row)
        row=content['values']

        self.var_idgost.set(row[0]),
        self.var_ime.set(row[1]),
        self.var_prezime.set(row[2]),
        self.var_pol.set(row[3]),
        self.var_godine.set(row[4]),
        self.var_telefon.set(row[5]),
        self.var_email.set(row[6]),
        self.var_brojdokumenta.set(row[7]),
        self.var_iddokument.set(row[8]),
        self.var_brojrezervacija.set(row[9])
        self.var_bodovi.set(row[10])
        self.var_rezident.set(row[11])
        self.var_počasnigost.set(row[12])
        

    def predikcija(self):
        self.new_window=Toplevel(self.root)
        self.app=PredikcijaGosta(self.new_window)



'''root=Tk()
object=Gosti(root)
mainloop()'''