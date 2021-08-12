from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import random
from time import strftime
from datetime import date, datetime
from veza import Konekcija

class CeneNabavka:
    def __init__(self,root):
        self.root=root
        self.root.title("    ")
        self.root.geometry("1850x1050+0+0")

        self.root.protocol('WM_DELETE_WINDOW',self.zatvoriProzor)

        self.var_idnormativi=IntVar()
        self.var_naziv=StringVar()
        self.var_cena=StringVar()
        self.var_količina=StringVar()
        self.var_idArtikla=IntVar()

        self.var_idartikli=IntVar()
        self.var_naziv2=StringVar()
        self.var_stanje=StringVar()
        self.var_nabavka=IntVar()
        self.var_limit=IntVar()

        self.var_pronadjiPo1=StringVar()
        self.var_pronadjiTekst1=StringVar()
        self.var_pronadjiPo2=StringVar()
        self.var_pronadjiTekst2=StringVar()



        img1=Image.open(r"restoraniFoto/restoran5.jpg")
        img1=img1.resize((620,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblImage=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblImage.place(x=0,y=0,width=620,height=140)

        img2=Image.open(r"restoraniFoto/restoran3.jpg")
        img2=img2.resize((620,140),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblImage2=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblImage2.place(x=620,y=0,width=620,height=140)

        img3=Image.open(r"restoraniFoto/restoran4.jpg")
        img3=img3.resize((610,140),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblImage3=Label(self.root,image=self.photoimg3,bd=4,relief=RIDGE)
        lblImage3.place(x=1240,y=0,width=610,height=140)

        titleLbl=Label(self.root,text="Postavljanje cena i nabavka robe",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        titleLbl.place(x=0,y=140,width=1850,height=70)

        self.lbl = Label(self.root, font = ('calibri', 15, 'bold'),
        foreground = 'gold',background="black")
        self.lbl.place(x=10,y=160,width=300)
        self.datum()


        frameCene=LabelFrame(self.root,bd=2,relief=RIDGE,text="Proveri i postavi cene",font=("times new roman",15,"bold"),padx=2)
        frameCene.place(x=10,y=210,width=920,height=800)

        idnormativiLbl=Label(frameCene,text="ID stavke",font=("times new roman",12,"bold"),padx=2,pady=3,width=10)
        idnormativiLbl.grid(row=0,column=0)

        idnormativiEntry=ttk.Entry(frameCene,textvariable=self.var_idnormativi, font=("times new roman",12,"bold"))
        idnormativiEntry.grid(row=0,column=1)

        nazivLbl=Label(frameCene,text="Naziv",font=("times new roman",12,"bold"),padx=2,pady=3,width=10)
        nazivLbl.grid(row=1,column=0)

        nazivEntry=ttk.Entry(frameCene,textvariable=self.var_naziv, font=("times new roman",12,"bold"))
        nazivEntry.grid(row=1,column=1)

        cenaLbl=Label(frameCene,text="Cena",font=("times new roman",12,"bold"),padx=2,pady=3,width=10)
        cenaLbl.grid(row=2,column=0)

        cenaEntry=ttk.Entry(frameCene,textvariable=self.var_cena, font=("times new roman",12,"bold"))
        cenaEntry.grid(row=2,column=1)

        količinaLbl=Label(frameCene,text="Količina",font=("times new roman",12,"bold"),padx=2,pady=3,width=10)
        količinaLbl.grid(row=3,column=0)

        količinaEntry=ttk.Entry(frameCene,textvariable=self.var_količina, font=("times new roman",12,"bold"))
        količinaEntry.grid(row=3,column=1)

        idArtikalLbl=Label(frameCene,text="ID Artikla",font=("times new roman",12,"bold"),padx=2,pady=3,width=10)
        idArtikalLbl.grid(row=4,column=0)

        idArtikalEntry=ttk.Entry(frameCene,textvariable=self.var_idArtikla, font=("times new roman",12,"bold"))
        idArtikalEntry.grid(row=4,column=1)

        btnFrame=Frame(frameCene)
        btnFrame.place(x=0,y=200,width=480,height=40)

        btnDodajStavku=Button(btnFrame,text="Dodaj Stavku",command=self.upisNoveStavke, font=("times new roman",12,"bold"),bg="black",fg="gold",width=11)
        btnDodajStavku.grid(row=0,column=0,padx=1)

        btnPromeniStavku=Button(btnFrame,text="Izmeni Stavku",command=self.izmeniStavku, font=("times new roman",12,"bold"),bg="black",fg="gold",width=11)
        btnPromeniStavku.grid(row=0,column=1,padx=1)

        btnObrišiStavku=Button(btnFrame,text="Obriši Stavku",command=self.obrišiStavku, font=("times new roman",12,"bold"),bg="black",fg="gold",width=11)
        btnObrišiStavku.grid(row=0,column=2,padx=1)

        btnPoništiStavku=Button(btnFrame,text="Poništi",command=self.poništi, font=("times new roman",12,"bold"),bg="black",fg="gold",width=11)
        btnPoništiStavku.grid(row=0,column=3,padx=1)

        TablaFrame=Frame(frameCene,bd=2,relief=RIDGE)
        TablaFrame.place(x=0,y=300,width=915,height=500)

        pronadjiLbl=Label(TablaFrame,text="Pronadji po:",font=("times new roman",14,"bold"),bg="black",fg="yellow")
        pronadjiLbl.grid(row=1,column=0,sticky=W)

        pronadjiCombo=ttk.Combobox(TablaFrame,textvariable=self.var_pronadjiPo1,font=("times new roman",12,"bold"),width=14,state="readonly")
        pronadjiCombo['value']=("idnormativi","nazivArtikla")
        pronadjiCombo.current()
        pronadjiCombo.grid(row=1,column=1,padx=2)
   
        pronadjiTekst=ttk.Entry(TablaFrame,textvariable=self.var_pronadjiTekst1, font=("times new roman",12,"bold"),width=14)
        pronadjiTekst.grid(row=1,column=2,padx=2)

        btnPronadji=Button(TablaFrame,text="Pronadji",command=self.pronadjiStavke, font=("times new roman",12,"bold"),bg="black",fg="gold",width=7)
        btnPronadji.grid(row=1,column=3,padx=1)

        btnPrikaži=Button(TablaFrame,text="Prikaži Sve",command=self.prikažiStavke, font=("times new roman",12,"bold"),bg="black",fg="gold",width=7)
        btnPrikaži.grid(row=1,column=4,padx=1)

        detaljiTabla=Frame(TablaFrame)
        detaljiTabla.place(x=0,y=70,width=910,height=400)
        
        scroll_x = Scrollbar(detaljiTabla,orient=HORIZONTAL)
        scroll_y = Scrollbar(detaljiTabla,orient=VERTICAL)
        self.ispis=ttk.Treeview(detaljiTabla,columns=("idnormativi","nazivArtikla","cena","količina","idArtikla"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.ispis.xview) 
        scroll_y.config(command=self.ispis.yview)
        self.ispis.heading("idnormativi",text="ID stavke")
        self.ispis.heading("nazivArtikla",text="Naziv")
        self.ispis.heading("cena",text="Cena")
        self.ispis.heading("količina",text="Količina")
        self.ispis.heading("idArtikla",text="ID artikla")
        self.ispis['show']='headings' 
        self.ispis.column("idnormativi",width=100) 
        self.ispis.column("nazivArtikla",width=100)
        self.ispis.column("cena",width=100)
        self.ispis.column("količina",width=100)
        self.ispis.column("idArtikla",width=100)
        self.ispis.bind("<ButtonRelease-1>",self.pokazivač)
        self.ispis.pack(fill=BOTH,expand=1)

        frameNabavka=LabelFrame(self.root,bd=2,relief=RIDGE,text="Nabavka robe",font=("times new roman",15,"bold"),padx=2)
        frameNabavka.place(x=930,y=210,width=910,height=800)

        idartikliLbl=Label(frameNabavka,text="ID artikla",font=("times new roman",12,"bold"),padx=2,pady=3,width=10)
        idartikliLbl.grid(row=0,column=0)

        idartikliEntry=ttk.Entry(frameNabavka,textvariable=self.var_idartikli, font=("times new roman",12,"bold"))
        idartikliEntry.grid(row=0,column=1)

        naziv2Lbl=Label(frameNabavka,text="Naziv",font=("times new roman",12,"bold"),padx=2,pady=3,width=10)
        naziv2Lbl.grid(row=1,column=0)

        naziv2Entry=ttk.Entry(frameNabavka,textvariable=self.var_naziv2, font=("times new roman",12,"bold"))
        naziv2Entry.grid(row=1,column=1)

        stanjeLbl=Label(frameNabavka,text="Stanje",font=("times new roman",12,"bold"),padx=2,pady=3,width=10)
        stanjeLbl.grid(row=2,column=0)

        stanjeEntry=ttk.Entry(frameNabavka,textvariable=self.var_stanje, font=("times new roman",12,"bold"))
        stanjeEntry.grid(row=2,column=1,padx=5)

        nabavkaLbl=Label(frameNabavka,text="Nabavka",font=("times new roman",12,"bold"),padx=2,pady=3,width=10)
        nabavkaLbl.grid(row=2,column=2)

        nabavkaEntry=ttk.Entry(frameNabavka,textvariable=self.var_nabavka, font=("times new roman",12,"bold"))
        nabavkaEntry.grid(row=2,column=3)

        limitLbl=Label(frameNabavka,text="Limit",font=("times new roman",12,"bold"),padx=2,pady=3,width=10)
        limitLbl.grid(row=3,column=0)

        limitEntry=ttk.Entry(frameNabavka,textvariable=self.var_limit, font=("times new roman",12,"bold"))
        limitEntry.grid(row=3,column=1)

        btnFrame2=Frame(frameNabavka)
        btnFrame2.place(x=0,y=200,width=480,height=40)

        btnDodajStavku=Button(btnFrame2,text="Dodaj Artikal",command=self.upisNovogArtikla, font=("times new roman",12,"bold"),bg="black",fg="gold",width=11)
        btnDodajStavku.grid(row=0,column=0,padx=1)

        btnPromeniStavku=Button(btnFrame2,text="Nabavka",command=self.dodajNaStanje, font=("times new roman",12,"bold"),bg="black",fg="gold",width=11)
        btnPromeniStavku.grid(row=0,column=1,padx=1)

        btnObrišiStavku=Button(btnFrame2,text="Obriši Artikal",command=self.obrišiArtikal, font=("times new roman",12,"bold"),bg="black",fg="gold",width=11)
        btnObrišiStavku.grid(row=0,column=2,padx=1)

        TablaFrame2=Frame(frameNabavka,bd=2,relief=RIDGE)
        TablaFrame2.place(x=0,y=300,width=905,height=500)

        pronadjiLbl2=Label(TablaFrame2,text="Pronadji po:",font=("times new roman",14,"bold"),bg="black",fg="yellow")
        pronadjiLbl2.grid(row=1,column=0,sticky=W)

        pronadjiCombo2=ttk.Combobox(TablaFrame2,textvariable=self.var_pronadjiPo2,font=("times new roman",12,"bold"),width=14,state="readonly")
        pronadjiCombo2['value']=("idartikli","naziv")
        pronadjiCombo2.current()
        pronadjiCombo2.grid(row=1,column=1,padx=2)
   
        pronadjiTekst2=ttk.Entry(TablaFrame2,textvariable=self.var_pronadjiTekst2, font=("times new roman",12,"bold"),width=14)
        pronadjiTekst2.grid(row=1,column=2,padx=2)

        btnPronadji2=Button(TablaFrame2,text="Pronadji",command=self.pronadjiArtikle, font=("times new roman",12,"bold"),bg="black",fg="gold",width=7)
        btnPronadji2.grid(row=1,column=3,padx=1)

        btnPrikaži2=Button(TablaFrame2,text="Prikaži Sve",command=self.prikažiArtikle, font=("times new roman",12,"bold"),bg="black",fg="gold",width=7)
        btnPrikaži2.grid(row=1,column=4,padx=1)

        detaljiTabla2=Frame(TablaFrame2)
        detaljiTabla2.place(x=0,y=70,width=900,height=400)
        
        scroll_x2 = Scrollbar(detaljiTabla2,orient=HORIZONTAL)
        scroll_y2 = Scrollbar(detaljiTabla2,orient=VERTICAL)
        self.ispis2=ttk.Treeview(detaljiTabla2,columns=("idartikli","naziv","stanje","limit"),xscrollcommand=scroll_x2.set,yscrollcommand=scroll_y2.set)
        scroll_x2.pack(side=BOTTOM,fill=X)
        scroll_y2.pack(side=RIGHT,fill=Y)
        scroll_x2.config(command=self.ispis2.xview) 
        scroll_y2.config(command=self.ispis2.yview)
        self.ispis2.heading("idartikli",text="ID artikla")
        self.ispis2.heading("naziv",text="Naziv")
        self.ispis2.heading("stanje",text="Stanje")
        self.ispis2.heading("limit",text="Limit")
        self.ispis2['show']='headings' 
        self.ispis2.column("idartikli",width=100) 
        self.ispis2.column("naziv",width=100)
        self.ispis2.column("stanje",width=100)
        self.ispis2.column("limit",width=100)
        self.ispis2.bind("<ButtonRelease-1>",self.pokazivač2)
        self.ispis2.pack(fill=BOTH,expand=1)


    def prikažiStavke(self):
        con=Konekcija.getInstance()
        cur=con.cursor()
        cur.execute("SELECT * FROM normativi")
        rows=cur.fetchall()
        if(len(rows)!=0):
            self.ispis.delete(*self.ispis.get_children())
            for row in rows:
                self.ispis.insert('',END,values=row)
            con.commit()

    def pokazivač(self,event):
        cursor_row = self.ispis.focus()
        contents = self.ispis.item(cursor_row)
        row = contents['values']

        self.var_idnormativi.set(row[0])
        self.var_naziv.set(row[1])
        self.var_cena.set(row[2])
        self.var_količina.set(row[3])
        self.var_idArtikla.set(row[4])

    def pronadjiStavke(self):
        con=Konekcija.getInstance()
        cur=con.cursor()
        cur.execute("SELECT * FROM normativi WHERE "+str(self.var_pronadjiPo1.get())+" LIKE binary '%"+self.var_pronadjiTekst1.get()+"%'") 
        rows = cur.fetchall()
        if(len(rows)!=0):
            self.ispis.delete(*self.ispis.get_children())
            for i in rows: 
                self.ispis.insert('',END,values=i)
                con.commit()
        else:
            self.ispis.delete(*self.ispis.get_children()) 
    
    def prikažiArtikle(self):
        con=Konekcija.getInstance()
        cur=con.cursor()
        cur.execute("SELECT * FROM artikli")
        rows=cur.fetchall()
        if(len(rows)!=0):
            self.ispis2.delete(*self.ispis2.get_children())
            for row in rows:
                self.ispis2.insert('',END,values=row)
            con.commit()


    def pokazivač2(self,event):
        cursor_row = self.ispis2.focus()
        contents = self.ispis2.item(cursor_row)
        row = contents['values']

        self.var_idartikli.set(row[0])
        self.var_naziv2.set(row[1])
        self.var_stanje.set(row[2])
        self.var_limit.set(row[3])

    def pronadjiArtikle(self):
        con=Konekcija.getInstance()
        cur=con.cursor()
        cur.execute("SELECT * FROM artikli WHERE "+str(self.var_pronadjiPo2.get())+" LIKE binary '%"+self.var_pronadjiTekst2.get()+"%'") 
        rows = cur.fetchall()
        if(len(rows)!=0):
            self.ispis2.delete(*self.ispis2.get_children())
            for i in rows: 
                self.ispis2.insert('',END,values=i)
                con.commit()
        else:
            self.ispis2.delete(*self.ispis2.get_children()) 


    def upisNoveStavke(self):
        if self.var_naziv.get()=="" or self.var_cena.get()=="" or self.var_količina.get()=="" or self.var_idArtikla.get()==0 :
            messagebox.showerror("Greška","Sva polja morate popuniti",parent=self.root)
        else:
            try:
                con=Konekcija.getInstance()
                cursor=con.cursor()
                cursor.execute("INSERT INTO normativi(nazivArtikla,cena,količina,idartikli) VALUES(%s,%s,%s,%s)",(
            self.var_naziv.get(),
            float(self.var_cena.get()),
            float(self.var_količina.get()),
            self.var_idArtikla.get()))
                con.commit()
                messagebox.showinfo("OK","Stavka je uspešno upisana",parent=self.root)
                self.poništi()
                self.prikažiStavke()
            except Exception as es:
                messagebox.showwarning("Upozorenje",f"Nešto je pošlo loše:{es}",parent=self.root)

    def izmeniStavku(self):
        if self.var_idnormativi.get()==0:
            messagebox.showerror("Greška","Molimo Vas,unesite ID normativa",parent=self.root)
        else:
            con=Konekcija.getInstance()
            cursor=con.cursor()
            cursor.execute("UPDATE normativi SET cena=%s,količina=%s  WHERE idnormativi=%s",(
                float(self.var_cena.get()),
                float(self.var_količina.get()),
                self.var_idnormativi.get()
            ))
            con.commit()
            messagebox.showinfo("Uspešno","Uspešno izmenjene cene i količina",parent=self.root)
            self.poništi()
            self.prikažiStavke()


    def obrišiStavku(self):
        obriši=messagebox.askyesno("Restoran","Da li zaista želite da obrišete stavku?")
        if obriši>0:
            con=Konekcija.getInstance()
            cursor=con.cursor()
            query=("DELETE FROM normativi WHERE idnormativi=%s")
            value=(self.var_idnormativi.get(),)
            cursor.execute(query,value)
        elif  not obriši:
            return
        con.commit()
        messagebox.showinfo("Uspešno","Uspešno obrisana stavka",parent=self.root)
        self.poništi()
        self.prikažiStavke()


    def poništi(self):
        self.var_idnormativi.set(0)
        self.var_naziv.set("")
        self.var_cena.set(0)
        self.var_količina.set(0)
        self.var_idArtikla.set(0)
        self.var_pronadjiPo1.set("")
        self.var_pronadjiTekst1.set(0)
        self.var_idartikli.set(0)
        self.var_naziv2.set("")
        self.var_stanje.set(0)
        self.var_limit.set(0)
        self.var_nabavka.set(0)
        self.var_pronadjiPo2.set("")
        self.var_pronadjiTekst2.set(0)
        self.ispis.delete(*self.ispis.get_children()),
        self.ispis2.delete(*self.ispis2.get_children())
    
    def upisNovogArtikla(self):
        if self.var_naziv2.get()=="" or self.var_stanje.get()==0 or self.var_limit.get()==0:
            messagebox.showerror("Greška","Sva polja morate popuniti",parent=self.root)
        else:
            try:
                con=Konekcija.getInstance()
                cursor=con.cursor()
                cursor.execute("INSERT INTO artikli(naziv,stanjeKgLiKom,nabavkaRobe) VALUES(%s,%s,%s)",(
            self.var_naziv2.get(),
            self.var_stanje.get(),
            self.var_limit.get()
            ))
                con.commit()
                messagebox.showinfo("OK","Artikal je uspešno upisan",parent=self.root)
                self.poništi()
                self.prikažiArtikle()

            except Exception as es:
                messagebox.showwarning("Upozorenje",f"Nešto je pošlo loše:{es}",parent=self.root)

    def dodajNaStanje(self):
        if self.var_idartikli.get()==0:
            messagebox.showerror("Greška","Molimo Vas,unesite ID artikla",parent=self.root)
        else:
            con=Konekcija.getInstance()
            cursor=con.cursor()
            cursor.execute("UPDATE artikli SET stanjeKgLiKom=%s,nabavkaRobe=%s WHERE idartikli=%s",(
                float(self.var_stanje.get())+(self.var_nabavka.get()),
                self.var_limit.get(),
                self.var_idartikli.get()
            ))
            self.var_stanje.set(float(self.var_stanje.get())+(self.var_nabavka.get()))
            self.var_nabavka.set(0)
            con.commit()
            messagebox.showinfo("OK","Nabavka uspešna",parent=self.root)
            self.prikažiArtikle()

    
    def obrišiArtikal(self):
        obriši=messagebox.askyesno("Restoran","Da li zaista želite da obrišete artikal?")
        if obriši>0:
            con=Konekcija.getInstance()
            cursor=con.cursor()
            query=("DELETE FROM artikli WHERE idartikli=%s")
            value=(self.var_idartikli.get(),)
            cursor.execute(query,value)
        elif  not obriši:
            return
        con.commit()
        messagebox.showinfo("Uspešno","Uspešno obrisan artikal",parent=self.root)
        self.poništi()
        self.prikažiArtikle()


    def datum(self):
        now = strftime("%Y-%m-%d %H:%M:%S")
        self.lbl.config(text = now)
        self.lbl.after(1000, self.datum)


    def zatvoriProzor(self):
        response=messagebox.askyesno('Izlaz','Da li ste sigurni da želite da izadjete?',parent=self.root)
        if response:
            self.root.destroy()

'''root=Tk()
object=CeneNabavka(root)
mainloop()'''

