from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
from mysql.connector import cursor
from veza2 import Konekcija2

class RezervacijaSoba:
    def __init__(self,root):
        self.root=root
        self.root.title("   ")
        self.root.geometry("1620x770+307+300")


        self.var_brojračuna=IntVar()
        self.var_idgosti=IntVar()
        self.var_brojsobe=IntVar()
        self.var_prijava=StringVar()
        self.var_odjava=StringVar()
        self.var_dostupnesobe=StringVar()
        self.var_tip_sobe=StringVar()
        self.var_brojdana=IntVar()
        self.var_cenaSobe=IntVar()
        self.var_cena=IntVar()
        self.var_dodatacena=IntVar()
        self.var_račun=IntVar()
        self.var_status=StringVar()
        self.var_rezervacijaDan=IntVar()

        self.var_pazar=IntVar()
        self.var_dan=IntVar()
        self.var_statusD=StringVar()

        self.var_pronadjiPo=StringVar()
        self.var_pronadjiTekst=StringVar()
        
        lbltitle=Label(self.root,text="Rezervacija soba",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbltitle.place(x=0,y=0,width=1620,height=50)

        img1=Image.open(r"sobeFoto/room.jpg")
        img1=img1.resize((100,40),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblImage=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblImage.place(x=5,y=3,width=100,height=42)

        self.labelFrameLevo=LabelFrame(self.root,bd=2,relief=RIDGE,text="Detalji rezervacije",font=("times new roman",12,"bold"),padx=2)
        self.labelFrameLevo.place(x=5,y=50,width=505,height=490)

        brojračunaLbl=Label(self.labelFrameLevo,text="Broj računa",font=("times new roman",12,"bold"),padx=2,pady=6)
        brojračunaLbl.grid(row=0,column=0,sticky=W)

        brojračunaEntry=ttk.Entry(self.labelFrameLevo,textvariable=self.var_brojračuna, font=("times new roman",13,"bold"),width=15,state="readonly")
        brojračunaEntry.grid(row=0,column=1)

        idgostLbl=Label(self.labelFrameLevo,text="Id gosta",font=("times new roman",12,"bold"),padx=2,pady=6)
        idgostLbl.grid(row=1,column=0,sticky=W)

        idgostEntry=ttk.Entry(self.labelFrameLevo,textvariable=self.var_idgosti, font=("times new roman",13,"bold"),width=15)
        idgostEntry.grid(row=1,column=1)

        btnPokažiGosta=Button(self.labelFrameLevo,command=self.pokažiGosta, text="Prikaži gosta",font=("arial",8,"bold"),bg="black",fg="gold",width=8)
        btnPokažiGosta.place(x=390,y=35)

        brojsobeLbl=Label(self.labelFrameLevo,text="Broj sobe",font=("times new roman",12,"bold"),padx=2,pady=6)
        brojsobeLbl.grid(row=2,column=0,sticky=W)

        brojsobeEntry=ttk.Entry(self.labelFrameLevo,textvariable=self.var_brojsobe, font=("times new roman",13,"bold"),width=15)
        brojsobeEntry.grid(row=2,column=1)

        prijavaLbl=Label(self.labelFrameLevo,text="Prijava",font=("times new roman",12,"bold"),padx=2,pady=6)
        prijavaLbl.grid(row=3,column=0,sticky=W)

        prijavaEntry=ttk.Entry(self.labelFrameLevo,textvariable=self.var_prijava, font=("times new roman",13,"bold"),width=15)
        prijavaEntry.grid(row=3,column=1)

        odjavaLbl=Label(self.labelFrameLevo,text="Odjava",font=("times new roman",12,"bold"),padx=2,pady=6)
        odjavaLbl.grid(row=4,column=0,sticky=W)

        odjavaEntry=ttk.Entry(self.labelFrameLevo,textvariable=self.var_odjava, font=("times new roman",13,"bold"),width=15)
        odjavaEntry.grid(row=4,column=1)

        dostupneSobeLbl=Label(self.labelFrameLevo,text="Dostupne sobe",font=("times new roman",12,"bold"),padx=2,pady=6)
        dostupneSobeLbl.grid(row=5,column=0,sticky=W)
        
        self.dostupneSobe()

        btndostupneSobe=Button(self.labelFrameLevo,text="Soba",command=self.čitaj, font=("arial",8,"bold"),bg="black",fg="gold",width=8)
        btndostupneSobe.place(x=300,y=168)

        btnRefresh=Button(self.labelFrameLevo,text="Refresh",command=self.dostupneSobe, font=("arial",8,"bold"),bg="black",fg="gold",width=8)
        btnRefresh.place(x=400,y=167)

        tipsobeLbl=Label(self.labelFrameLevo,text="Tip sobe",font=("times new roman",12,"bold"),padx=2,pady=6)
        tipsobeLbl.grid(row=6,column=0,sticky=W)

        tipsobeEntry=ttk.Entry(self.labelFrameLevo,textvariable=self.var_tip_sobe, font=("times new roman",13,"bold"),width=15)
        tipsobeEntry.grid(row=6,column=1)

        brojdanaLbl=Label(self.labelFrameLevo,text="Broj dana",font=("times new roman",12,"bold"),padx=2,pady=6)
        brojdanaLbl.grid(row=7,column=0,sticky=W)

        brojdanaEntry=ttk.Entry(self.labelFrameLevo,textvariable=self.var_brojdana, font=("times new roman",13,"bold"),width=15)
        brojdanaEntry.grid(row=7,column=1)

        cenaSobeLbl=Label(self.labelFrameLevo,text="Cena sobe",font=("times new roman",12,"bold"),padx=2,pady=6)
        cenaSobeLbl.grid(row=8,column=0,sticky=W)

        cenaSobeEntry=ttk.Entry(self.labelFrameLevo,textvariable=self.var_cenaSobe, font=("times new roman",13,"bold"),width=15)
        cenaSobeEntry.grid(row=8,column=1)

        btnZaduženje=Button(self.labelFrameLevo,text="Cena",command=self.naplata, font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnZaduženje.grid(row=9,column=0,padx=1,sticky=W)

        cenaEntry=ttk.Entry(self.labelFrameLevo,textvariable=self.var_cena, font=("times new roman",13,"bold"),width=15)
        cenaEntry.grid(row=9,column=1)

        btnZaduženje2=Button(self.labelFrameLevo,text="Dodaj cenu",command=self.naplata2, font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnZaduženje2.grid(row=9,column=2,padx=1,sticky=W)

        cenaDodajEntry=ttk.Entry(self.labelFrameLevo,textvariable=self.var_dodatacena, font=("times new roman",13,"bold"),width=15)
        cenaDodajEntry.grid(row=9,column=3)

        btnRačun=Button(self.labelFrameLevo,text="Naplata",command=self.naplatiRačun, font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnRačun.grid(row=10,column=0,padx=1,sticky=W)

        totalEntry=ttk.Entry(self.labelFrameLevo,textvariable=self.var_račun, font=("times new roman",13,"bold"),width=15)
        totalEntry.grid(row=10,column=1)

        statusRačunaLbl=Label(self.labelFrameLevo,text="Status računa",font=("times new roman",12,"bold"),padx=2,pady=6)
        statusRačunaLbl.grid(row=11,column=0,sticky=W)

        statusRačunaEntry=ttk.Entry(self.labelFrameLevo,textvariable=self.var_status, font=("times new roman",13,"bold"),width=15)
        statusRačunaEntry.grid(row=11,column=1)

        rezervacijaDanLbl=Label(self.labelFrameLevo,text="DanR",font=("times new roman",12,"bold"),padx=2,pady=6)
        rezervacijaDanLbl.grid(row=12,column=0,sticky=W)

        rezervacijaDanEntry=ttk.Entry(self.labelFrameLevo,textvariable=self.var_rezervacijaDan, font=("times new roman",13,"bold"),width=15)
        rezervacijaDanEntry.grid(row=12,column=1)


        btnFrame=Frame(self.labelFrameLevo)
        btnFrame.place(x=0,y=430,width=448,height=36)

        btnRezerviši=Button(btnFrame,text="Rezerviši",command=self.dodajRezervaciju, font=("times new roman",12,"bold"),bg="black",fg="gold",width=10)
        btnRezerviši.grid(row=0,column=0,padx=1)

        btnPromeni=Button(btnFrame,text="Promeni",command=self.izmeniRezervaciju, font=("times new roman",12,"bold"),bg="black",fg="gold",width=10)
        btnPromeni.grid(row=0,column=1,padx=1)

        btnObriši=Button(btnFrame,text="Obriši",command=self.obriši, font=("times new roman",12,"bold"),bg="black",fg="gold",width=10)
        btnObriši.grid(row=0,column=2,padx=1)

        btnPoništi=Button(btnFrame,text="Poništi",command=self.poništi, font=("times new roman",12,"bold"),bg="black",fg="gold",width=10)
        btnPoništi.grid(row=0,column=3,padx=1)


        img2=Image.open(r"sobeFoto/room.jpg")
        img2=img2.resize((700,230),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblImage2=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblImage2.place(x=900,y=55,width=700,height=230)


        TablaFrame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Pogledaj detalje i pretraži rezervacije",font=("times new roman",12,"bold"),padx=2)
        TablaFrame.place(x=505,y=280,width=1110,height=260)

        pronadjiLbl=Label(TablaFrame,text="Pronadji:",font=("times new roman",15,"bold"),bg="gold",fg="black")
        pronadjiLbl.grid(row=0,column=0,sticky=W)

        pronadjiCombo=ttk.Combobox(TablaFrame,textvariable=self.var_pronadjiPo, font=("times new roman",15,"bold"),width=24,state="readonly")
        pronadjiCombo['value']=("idgosti","brojsobe")
        pronadjiCombo.current()
        pronadjiCombo.grid(row=0,column=1,padx=2)

        pronadjiTekstEntry=ttk.Entry(TablaFrame,textvariable=self.var_pronadjiTekst, font=("times new roman",15,"bold"),width=24)
        pronadjiTekstEntry.grid(row=0,column=2,padx=2)

        btnPotraži=Button(TablaFrame,text="Potraži",command=self.traži, font=("times new roman",15,"bold"),bg="black",fg="gold",width=8)
        btnPotraži.grid(row=0,column=3,padx=1)

        btnPrikažiSve=Button(TablaFrame,text="Prikaži sve",command=self.pokažiRezervacije, font=("times new roman",15,"bold"),bg="black",fg="gold",width=8)
        btnPrikažiSve.grid(row=0,column=4,padx=1)


        detaljiTabla=Frame(TablaFrame,bd=2,relief=RIDGE)
        detaljiTabla.place(x=0,y=50,width=1100,height=180)

        scrollX=ttk.Scrollbar(detaljiTabla,orient=HORIZONTAL)
        scrollY=ttk.Scrollbar(detaljiTabla,orient=VERTICAL)

        self.sobeTabla=ttk.Treeview(detaljiTabla,columns=("brojračuna","idgosti","brojsobe","prijava","odjava","trenutnacena","total","status","dan"),xscrollcommand=scrollX.set,yscrollcommand=scrollY.set)
        scrollX.pack(side=BOTTOM,fill=X)
        scrollY.pack(side=RIGHT,fill=Y)
        scrollX.config(command=self.sobeTabla.xview)
        scrollY.config(command=self.sobeTabla.yview)

        self.sobeTabla.heading("brojračuna",text="Broj računa")
        self.sobeTabla.heading("idgosti",text="ID gosta")
        self.sobeTabla.heading("brojsobe",text="Broj sobe")
        self.sobeTabla.heading("prijava",text="Prijava")
        self.sobeTabla.heading("odjava",text="Odjava")
        self.sobeTabla.heading("trenutnacena",text="Zaduženje")
        self.sobeTabla.heading("total",text="Račun total")
        self.sobeTabla.heading("status",text="Status računa")
        self.sobeTabla.heading("dan",text="Dan")
        self.sobeTabla['show']="headings"
        self.sobeTabla.column("brojračuna",width=100)
        self.sobeTabla.column("idgosti",width=100)
        self.sobeTabla.column("brojsobe",width=100)
        self.sobeTabla.column("prijava",width=100)
        self.sobeTabla.column("odjava",width=100)
        self.sobeTabla.column("trenutnacena",width=100)
        self.sobeTabla.column("total",width=100)
        self.sobeTabla.column("status",width=100)
        self.sobeTabla.column("dan",width=100)
     
        self.sobeTabla.pack(fill=BOTH,expand=1)
        self.sobeTabla.bind("<ButtonRelease-1>",self.pokazivač)


        framePazar=Frame(self.root)
        framePazar.place(x=10,y=550,width=400,height=200)

        pazarLbl=Label(framePazar,text="Pazar",font=("times new roman",12,"bold"),pady=6,width=6)
        pazarLbl.grid(row=1,column=0)

        pazarEntry=ttk.Entry(framePazar,textvariable=self.var_pazar)
        pazarEntry.grid(row=1,column=1,padx=20)

        danLbl=Label(framePazar,text="Dan",font=("times new roman",12,"bold"),pady=6,width=6)
        danLbl.grid(row=2,column=0)

        danEntry=ttk.Entry(framePazar,textvariable=self.var_dan)
        danEntry.grid(row=2,column=1,padx=20)

        statusDlbl=Label(framePazar,text="Status",font=("times new roman",12,"bold"),pady=6,width=6)
        statusDlbl.grid(row=3,column=0)

        statusEntry=ttk.Entry(framePazar,textvariable=self.var_statusD)
        statusEntry.grid(row=3,column=1)

        dugmePazar=Button(framePazar,text="Upiši račun",command=self.upiširačun,font=("arial",10,"bold"),bg="black",fg="gold",width=8)
        dugmePazar.grid(row=1,column=3,padx=1)

        dugmeDani=Button(framePazar,text="Dani",command=self.prikažiSveDane, font=("times new roman",10,"bold"),bg="black",fg="gold",width=8)
        dugmeDani.grid(row=2,column=3,padx=1)

        dugmeDanas=Button(framePazar,text="Danas",command=self.prikažiDanas, font=("times new roman",10,"bold"),bg="black",fg="gold",width=8)
        dugmeDanas.grid(row=3,column=3,padx=1)


        detaljiTabla2=Frame(self.root)
        detaljiTabla2.place(x=390,y=550,width=300,height=200)

        scroll_x2 = Scrollbar(detaljiTabla2,orient=HORIZONTAL)
        scroll_y2 = Scrollbar(detaljiTabla2,orient=VERTICAL)
        self.ispis2=ttk.Treeview(detaljiTabla2,columns=("dan","kasa","status"),xscrollcommand=scroll_x2.set,yscrollcommand=scroll_y2.set)
        scroll_x2.pack(side=BOTTOM,fill=X)
        scroll_y2.pack(side=RIGHT,fill=Y)
        scroll_x2.config(command=self.ispis2.xview) 
        scroll_y2.config(command=self.ispis2.yview)
        self.ispis2.heading("dan",text="Dan")
        self.ispis2.heading("kasa",text="Kasa")
        self.ispis2.heading("status",text="Status")
        self.ispis2['show']='headings'  
        self.ispis2.column("dan",width=100)
        self.ispis2.column("kasa",width=100)
        self.ispis2.column("status",width=100)
        self.ispis2.bind("<ButtonRelease-1>",self.pokazivač2)
        self.ispis2.pack(fill=BOTH,expand=1)

        dugmeOff=Button(self.root,text="Ugasi konekciju",command=self.off, font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        dugmeOff.place(x=1490,y=735,width=130,height=30)


    def prikažiSveDane(self):
        con=Konekcija2.getInstance()
        cur=con.cursor()
        cur.execute("SELECT * FROM pazar")
        rows=cur.fetchall()
        if(len(rows)!=0):
            self.ispis2.delete(*self.ispis2.get_children())
            for row in rows:
                self.ispis2.insert('',END,values=row)
                con.commit()

    def prikažiDanas(self):
        con=Konekcija2.getInstance()
        cur=con.cursor()
        cur.execute("SELECT * FROM pazar WHERE status='otvoren'")
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

        self.var_dan.set(row[0])
        self.var_pazar.set(row[1])
        self.var_statusD.set(row[2])

    def upiširačun(self):
        if self.var_statusD.get()!="otvoren":
            messagebox.showerror("Greška", "Ovaj dan je završen,izaberite tekući dan!", parent=self.root)
        elif self.var_rezervacijaDan.get()==0:
            messagebox.showerror("Greška", "Ova rezervacija nije naplaćena!", parent=self.root)
        else:
            if self.var_status.get()=="naplaćen":
                con=Konekcija2.getInstance()
                cur=con.cursor()
                cur.execute("UPDATE pazar SET kasa=%s WHERE dan=%s",(self.var_pazar.get()+self.var_račun.get(),self.var_dan.get(),))
                cur.execute("UPDATE rezervacija SET status='upisan u kasu' WHERE brojračuna=%s",(self.var_brojračuna.get(),))
                con.commit()
                messagebox.showinfo("OK","Uspešno uvećan pazar",parent=self.root)
                self.poništi()
                self.prikažiDanas()
                self.pokažiRezervacije()           
            elif self.var_status.get()=="upisan u kasu":
                messagebox.showerror("Greška", "Račun je već upisan u kasu", parent=self.root)
            else:
                messagebox.showerror("Greška", "Račun nije naplaćen", parent=self.root)


    def dodajRezervaciju(self):
        if self.var_idgosti.get()==0 or self.var_brojsobe.get()==0 or self.var_prijava.get()=="" or self.var_odjava.get()=="" or self.var_cena.get()==0:
            messagebox.showerror("Greška","Sva polja morate popuniti",parent=self.root)
        else:
            try:
                con=Konekcija2.getInstance()
                cursor=con.cursor()
                self.var_status.set("otvoren")
                cursor.execute("INSERT INTO rezervacija(idgosti,brojsobe,prijava,odjava,trenutnacena,total,status,dan) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.var_idgosti.get(),
                self.var_brojsobe.get(),
                self.var_prijava.get(),
                self.var_odjava.get(),
                self.var_cena.get(),
                self.var_račun.get(),
                self.var_status.get(),
                self.var_rezervacijaDan.get()
          ))
                cursor.execute("UPDATE sobe SET statusSobe='zauzeta' WHERE brojsobe=%s",(self.var_brojsobe.get(),))
                con.commit()
                messagebox.showinfo("Uspešno","Soba je rezervisana",parent=self.root)
                self.poništi()
                self.pokažiRezervacije() 
            except Exception as es:
                messagebox.showwarning("Upozorenje",f"Nešto je krenulo loše:{es}",parent=self.root)

    def izmeniRezervaciju(self):
        if self.var_status.get()!="otvoren":
            messagebox.showerror("Greška", "Ne možete izmeniti rezervaciju,račun je već naplaćen!", parent=self.root)
        elif self.var_prijava.get()=="" or self.var_odjava.get()=="":
            messagebox.showerror("Greška", "Unesite datume", parent=self.root)
        else:
            con=Konekcija2.getInstance()
            cursor = con.cursor()
            cursor.execute("UPDATE rezervacija SET prijava=%s,odjava=%s,trenutnacena=%s  WHERE brojračuna=%s", (
                self.var_prijava.get(),
                self.var_odjava.get(),
                self.var_cena.get(),
                self.var_brojračuna.get()
            ))
            con.commit()
            messagebox.showinfo("Promena", "Rezervacija je uspešno izmenjena", parent=self.root)
            self.poništi()
            self.pokažiRezervacije()
            

    
    def obriši(self):
        if self.var_račun.get()!=0:
            messagebox.showerror("Greška", "Račun je već naplaćen", parent=self.root)
        else:
            obriši=messagebox.askyesno("Hotel Menadžment","Da li zaista želite da obrišete rezervaciju?")
            if obriši>0:
                con=Konekcija2.getInstance()
                cursor=con.cursor()
                query="DELETE FROM rezervacija WHERE brojračuna=%s"
                value=(self.var_brojračuna.get(),)
                cursor.execute(query,value)
                cursor.execute("UPDATE sobe SET statusSobe='slobodna' WHERE brojsobe=%s",(self.var_brojsobe.get(),))
            else:
                return
            con.commit()
            messagebox.showinfo("Uspešno","Uspešno obrisana rezervacija",parent=self.root)
            self.poništi()
            self.pokažiRezervacije()

    def poništi(self):
        self.var_idgosti.set(0)
        self.var_brojsobe.set(0)
        self.var_prijava.set("")
        self.var_odjava.set("")
        self.var_dostupnesobe.set("")
        self.var_tip_sobe.set("")
        self.var_brojdana.set(0)
        self.var_cenaSobe.set(0)
        self.var_dodatacena.set(0)
        self.var_cena.set(0)
        self.var_račun.set(0)
        self.var_status.set("")
        self.var_brojračuna.set(0)
        if self.var_statusD.get()!="otvoren":
            self.var_pazar.set(0)
            self.var_dan.set(0)
            self.var_statusD.set("")
        self.var_rezervacijaDan.set(0)
        self.sobeTabla.delete(*self.sobeTabla.get_children())

    def poništi2(self):
        self.var_idgosti.set(0)
        self.var_prijava.set("")
        self.var_odjava.set("")
        self.var_dostupnesobe.set("")
        self.var_brojdana.set(0)
        self.var_dodatacena.set(0)
        self.var_cena.set(0)
        self.var_račun.set(0)
        self.var_status.set("")
        self.var_brojračuna.set(0)
        if self.var_statusD.get()!="otvoren":
            self.var_pazar.set(0)
            self.var_dan.set(0)
            self.var_statusD.set("")
        self.var_rezervacijaDan.set(0)
        self.sobeTabla.delete(*self.sobeTabla.get_children())

    def naplata(self):
        self.var_cena.set(self.var_cenaSobe.get()*self.var_brojdana.get())

    def naplata2(self):
        con=Konekcija2.getInstance()
        cursor=con.cursor()
        cursor.execute("SELECT tip_sobe,cena FROM sobe WHERE brojsobe=%s",(self.var_brojsobe.get(),))
        soba=cursor.fetchone()
        self.var_tip_sobe.set(soba[0])
        self.var_cenaSobe.set(soba[1])
        self.var_dodatacena.set(self.var_brojdana.get()*self.var_cenaSobe.get())
        self.var_cena.set(self.var_cena.get()+self.var_dodatacena.get())
        con.commit()

    def naplatiRačun(self):
        if self.var_cena.get()==0:
            messagebox.showerror("Greška","Nema zaduženja trenutnog",parent=self.root)
        elif self.var_račun.get()!=0:
            messagebox.showerror("Greška", "Račun je već naplaćen", parent=self.root)
        elif self.var_statusD.get()!="otvoren":
            messagebox.showerror("Greška", "Dan je već završen,birajte današnji dan!", parent=self.root)
        else:
            con=Konekcija2.getInstance()
            cursor=con.cursor()
            cursor.execute("UPDATE rezervacija SET total=%s,dan=%s,status='naplaćen' WHERE brojračuna=%s",(self.var_cena.get(),self.var_dan.get(),self.var_brojračuna.get()))
            cursor.execute("UPDATE sobe SET statusSobe='slobodna' WHERE brojsobe=%s",(self.var_brojsobe.get(),))
            if self.var_cena.get()>15000:
                cursor.execute("UPDATE gosti SET bodovi=bodovi+200,brojrezervacija=brojrezervacija+1  WHERE idgosti=%s",(self.var_idgosti.get(),))
                con.commit()
                messagebox.showinfo("Naplata", "Račun je uspešno naplaćen", parent=self.root)
                self.poništi()
                self.pokažiRezervacije()
            elif self.var_cena.get()>10000 and self.var_cena.get()<=15000:
                cursor.execute("UPDATE gosti SET bodovi=bodovi+100,brojrezervacija=brojrezervacija+1  WHERE idgosti=%s",(self.var_idgosti.get(),))
                con.commit()
                messagebox.showinfo("Naplata", "Račun je uspešno naplaćen", parent=self.root)
                self.poništi()
                self.pokažiRezervacije()
            else:
                cursor.execute("UPDATE gosti SET bodovi=bodovi+50,brojrezervacija=brojrezervacija+1  WHERE idgosti=%s",(self.var_idgosti.get(),))
                con.commit()
                messagebox.showinfo("Naplata", "Račun je uspešno naplaćen", parent=self.root)
                self.poništi()
                self.pokažiRezervacije()
                
            
    def traži(self): 
        con=Konekcija2.getInstance()
        cur=con.cursor()
        cur.execute("SELECT * FROM rezervacija WHERE "+str(self.var_pronadjiPo.get())+" = "+self.var_pronadjiTekst.get())
        rows = cur.fetchall()
        if(len(rows)!=0):
            self.sobeTabla.delete(*self.sobeTabla.get_children())
            for i in rows: 
                self.sobeTabla.insert('',END,values=i)
                con.commit()
        else:
            self.sobeTabla.delete(*self.sobeTabla.get_children())    

    def pokažiRezervacije(self):
        con=Konekcija2.getInstance()
        cursor=con.cursor()
        cursor.execute("SELECT * FROM rezervacija")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.sobeTabla.delete(*self.sobeTabla.get_children())
            for i in rows:
                self.sobeTabla.insert("",END,values=i)
            con.commit()

    def pokazivač(self,event=""):
        cursor_row=self.sobeTabla.focus()
        content=self.sobeTabla.item(cursor_row)
        row=content['values']

        self.var_brojračuna.set(row[0]),
        self.var_idgosti.set(row[1]),
        self.var_brojsobe.set(row[2]),
        self.var_prijava.set(row[3]),
        self.var_odjava.set(row[4]),
        self.var_cena.set(row[5]),
        self.var_račun.set(row[6]),
        self.var_status.set(row[7])
        self.var_rezervacijaDan.set(row[8])

        con=Konekcija2.getInstance()
        cursor=con.cursor()
        cursor.execute("SELECT tip_sobe,cena FROM sobe WHERE brojsobe=%s",(self.var_brojsobe.get(),))
        soba=cursor.fetchone()
        self.var_tip_sobe.set(soba[0])
        self.var_cenaSobe.set(soba[1])
        con.commit()

    def čitaj(self):
        self.var_brojsobe.set(self.var_dostupnesobe.get()[0:4])
        if self.var_dostupnesobe.get()[5:13]=="Apartman":
            self.var_tip_sobe.set(self.var_dostupnesobe.get()[5:13])
            self.var_cenaSobe.set(self.var_dostupnesobe.get()[14:])
        elif self.var_dostupnesobe.get()[5:9]=="Dubl":
            self.var_tip_sobe.set(self.var_dostupnesobe.get()[5:9])
            self.var_cenaSobe.set(self.var_dostupnesobe.get()[10:])
        else:
            self.var_tip_sobe.set(self.var_dostupnesobe.get()[5:10])
            self.var_cenaSobe.set(self.var_dostupnesobe.get()[11:])
        self.poništi2()
    
    def pokažiGosta(self):
        if self.var_idgosti.get()==0:
            messagebox.showerror("Greška","Molimo Vas unesite ID gosta",parent=self.root)
        else:
            con=Konekcija2.getInstance()
            cur=con.cursor()
            query=("SELECT ime FROM gosti WHERE idgosti=%s")
            value=(self.var_idgosti.get(),)
            cur.execute(query,value)
            row=cur.fetchone()
            if row==None:
                messagebox.showerror("Greška","Ovaj ID ne postoji",parent=self.root)
            else:

                prikazFrame=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                prikazFrame.place(x=515,y=60,width=320,height=210)

                lblIme=Label(prikazFrame,text="Ime:",font=("arial",12,"bold"))
                lblIme.place(x=0,y=0)

                lbl=Label(prikazFrame,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)

                query=("SELECT  prezime FROM gosti WHERE idgosti=%s")
                value=(self.var_idgosti.get(),)
                cur.execute(query,value)
                row=cur.fetchone()

                lblPrezime=Label(prikazFrame,text="Prezime:",font=("arial",12,"bold"))
                lblPrezime.place(x=0,y=30)

                lbl2=Label(prikazFrame,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=30)

                query=("SELECT  email FROM gosti WHERE idgosti=%s")
                value=(self.var_idgosti.get(),)
                cur.execute(query,value)
                row=cur.fetchone()

                lblEmail=Label(prikazFrame,text="Email:",font=("arial",12,"bold"))
                lblEmail.place(x=0,y=60)

                lbl3=Label(prikazFrame,text=row,font=("arial",12,"bold"))
                lbl3.place(x=90,y=60)

                query=("SELECT  telefon FROM gosti WHERE idgosti=%s")
                value=(self.var_idgosti.get(),)
                cur.execute(query,value)
                row=cur.fetchone()

                lblTelefon=Label(prikazFrame,text="Telefon:",font=("arial",12,"bold"))
                lblTelefon.place(x=0,y=90)

                lbl4=Label(prikazFrame,text=row,font=("arial",12,"bold"))
                lbl4.place(x=90,y=90)

                query=("SELECT  godine FROM gosti WHERE idgosti=%s")
                value=(self.var_idgosti.get(),)
                cur.execute(query,value)
                row=cur.fetchone()
           
                lblGodine=Label(prikazFrame,text="Godine:",font=("arial",12,"bold"))
                lblGodine.place(x=0,y=120)

                lbl5=Label(prikazFrame,text=row,font=("arial",12,"bold"))
                lbl5.place(x=90,y=120)

                query=("SELECT  bodovi FROM gosti WHERE idgosti=%s")
                value=(self.var_idgosti.get(),)
                cur.execute(query,value)
                row=cur.fetchone()

                lblGodine=Label(prikazFrame,text="Bodovi:",font=("arial",12,"bold"))
                lblGodine.place(x=0,y=150)

                lbl5=Label(prikazFrame,text=row,font=("arial",12,"bold"))
                lbl5.place(x=90,y=150)

                con.commit()

    def dostupneSobe(self):
        con=Konekcija2.getInstance()
        cursor=con.cursor()
        cursor.execute("SELECT brojsobe,tip_sobe,cena FROM sobe WHERE statusSobe='slobodna'")
        soba=cursor.fetchall()
        dostupneSobeCombo=ttk.Combobox(self.labelFrameLevo,textvariable=self.var_dostupnesobe,font=("times new roman",13,"bold"),width=18,state="readonly")
        dostupneSobeCombo.current()
        dostupneSobeCombo['value']=soba
        dostupneSobeCombo.grid(row=5,column=1,padx=1,sticky=W)
        con.commit()

    def off(self):
        con=Konekcija2.getInstance()
        messagebox.showinfo("off","Odjavljivanje uspelo!")
        con.close()

    def ponovo(self):
        self.root.destroy()
        root=Tk()
        object=RezervacijaSoba(root)
        mainloop()


'''root=Tk()
object=RezervacijaSoba(root)
mainloop()'''

