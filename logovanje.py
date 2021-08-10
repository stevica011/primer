from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import random
from mysql.connector import cursor
from registracija import Registracija
from hotel import Hotel
from veza import Konekcija


def main():
    win = Tk()
    app = LoginWindow(win)
    win.mainloop()


class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Program")
        self.root.geometry("1850x1050+0+0")

        self.root.protocol('WM_DELETE_WINDOW', self.izlaz)

        self.var_email = StringVar()
        self.var_lozinka = StringVar()

        img1 = Image.open(r"plažaFoto/beach.png")
        img1 = img1.resize((1850, 1050), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblImage1 = Label(self.root, image=self.photoimg1)
        lblImage1.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="blue")
        frame.place(x=760, y=220, width=340, height=450)

        img2 = Image.open(r"userLoginFoto/user1.png")
        img2 = img2.resize((100, 100), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblImage2 = Label(image=self.photoimg2, bg="blue", borderwidth=0)
        lblImage2.place(x=880, y=225, width=100, height=100)

        naslovLbl = Label(frame, text="Prijavljivanje", font=("times new roman", 20, "bold"), fg="white", bg="blue")
        naslovLbl.place(x=90, y=100)

        emailLbl = Label(frame, text="E-mail", font=("times new roman", 15, "bold"), fg="white", bg="blue")
        emailLbl.place(x=70, y=155)

        self.textEmail = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15, "bold"))
        self.textEmail.place(x=40, y=180, width=280)

        lozinkaLbl = Label(frame, text="Lozinka", font=("times new roman", 15, "bold"), fg="white", bg="blue")
        lozinkaLbl.place(x=70, y=225)

        self.textLozinka = ttk.Entry(frame, textvariable=self.var_lozinka, show="*", font=("times new roman", 15, "bold"))
        self.textLozinka.place(x=40, y=250, width=270)

        img3 = Image.open(r"userLoginFoto/user1.png")
        img3 = img3.resize((35, 35), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblImage3 = Label(image=self.photoimg3, bg="blue", borderwidth=0)
        lblImage3.place(x=767, y=367, width=35, height=35)

        img4 = Image.open(r"userLoginFoto/user1.png")
        img4 = img4.resize((35, 35), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblImage4 = Label(image=self.photoimg4, bg="blue", borderwidth=0)
        lblImage4.place(x=767, y=439, width=35, height=35)

        btnLogin = Button(frame, text="Logovanje", command=self.logovanje, font=("times new roman", 15, "bold"),bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="green", activebackground="yellow")
        btnLogin.place(x=110, y=300, width=120, height=35)

        btnRegister = Button(frame, text="Registracija novog korisnika", command=self.registracija_prozor, font=("times new roman", 10, "bold"), borderwidth=0, fg="white", bg="blue", activeforeground="white", activebackground="brown")
        btnRegister.place(x=15, y=350, width=160)

        btnRegister2= Button(frame, text="Zaboravljena lozinka", command=self.zaboravljena_lozinka, font=("times new roman", 10, "bold"), borderwidth=0, fg="white", bg="blue", activeforeground="white", activebackground="brown")
        btnRegister2.place(x=15, y=380, width=160)


    def registracija_prozor(self):
        self.new_window = Toplevel(self.root)
        self.app = Registracija(self.new_window)

    def logovanje(self):
        if self.textEmail.get() == "" or self.textLozinka.get() == "":
            messagebox.showerror("Greška", "Popunite sva polja!")
        else:
            con=Konekcija.getInstance()
            cursor = con.cursor()
            cursor.execute("SELECT * FROM zaposleni WHERE email=%s and lozinka=%s", (
                self.var_email.get(),
                self.var_lozinka.get()
            ))
            row = cursor.fetchone()
            if row == None:
                messagebox.showerror(
                    "Greška", "Pogrešno uneti podaci,pokušajte ponovo")
            else:
                open_main = messagebox.askyesno("Da Ne", "Pristup glavnom programu")
                self.var_email.set("")
                self.var_lozinka.set("")
                if open_main:   # a moze i "if open_main>0:"
                    self.new_window = Toplevel(self.root)
                    self.app = Hotel(self.new_window)
                else:
                    if not open_main:
                        return
            con.commit()

    def promena_lozinke(self):
        if self.combo_security_Q.get() == "Biraj":
            messagebox.showerror("Greška", "Izaberite sigurnosno pitanje", parent=self.root2)
        elif self.security_A.get() == "":
            messagebox.showerror("Greška", "Molimo Vas,unesite odgovor", parent=self.root2)
        elif self.txt_novaLozinka.get() == "":
            messagebox.showerror("Greška", "Unesite novu lozinku", parent=self.root2)
        else:
            con=Konekcija.getInstance()
            cursor = con.cursor()
            query = ("SELECT * FROM zaposleni WHERE email=%s and security_question=%s and security_answer=%s")
            value = (self.textEmail.get(),self.combo_security_Q.get(), self.security_A.get())
            cursor.execute(query, value)
            row = cursor.fetchone()
            if row == None:
                messagebox.showerror("Greška", "Molimo Vas,unesite tačan odgovor", parent=self.root2)
            else:
                query = ("UPDATE zaposleni SET lozinka=%s WHERE email=%s")
                value = (self.txt_novaLozinka.get(), self.textEmail.get())
                cursor.execute(query, value)
                con.commit()
                messagebox.showinfo("Info", "Vaša lozinka je promenjena,molimo Vas ulogujte se ponovo", parent=self.root2)
                self.root2.destroy()
                self.var_email.set("")
                self.var_lozinka.set("")

    def zaboravljena_lozinka(self):
        if self.textEmail.get() == "":
            messagebox.showerror("Greška", "Molimo Vas,unesite Vaš e-mail i Vašu lozinku")
        else:
            con=Konekcija.getInstance()
            cursor = con.cursor()
            query = ("SELECT * FROM zaposleni WHERE email=%s")
            value = (self.textEmail.get(),)
            cursor.execute(query, value)
            row = cursor.fetchone()
            if row == None:
                messagebox.showerror("Greška", "Molimo Vas unesite ispravnu lozinku")
            else:
                self.root2 = Toplevel()
                self.root2.title("Zaboravljena Lozinka")
                self.root2.geometry("340x450+830+270")

                lbL = Label(self.root2, text="Zaboravljena Lozinka", font=("times new roman", 20, "bold"), fg="blue", bg="white")
                lbL.place(x=0, y=10, relwidth=1)

                security_Q = Label(self.root2, text="Sigurnosno pitanje", font=("times new roman", 15, "bold"), fg="black", bg="white")
                security_Q.place(x=50, y=80)

                self.combo_security_Q = ttk.Combobox(self.root2, font=("times new roman", 15, "bold"), state="readonly")
                self.combo_security_Q['values'] = ("Biraj", "Mesto rodjenja", "Kućni ljubimac", "Ime bake")
                self.combo_security_Q.place(x=50, y=110, width=250)
                self.combo_security_Q.current()

                security_A = Label(self.root2, text="Sigurnosni odgovor", font=("times new roman", 15, "bold"), fg="black", bg="white")
                security_A.place(x=50, y=150)

                self.security_A = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
                self.security_A.place(x=50, y=180, width=250)

                novaLozinka = Label(self.root2, text="Nova Lozinka", font=("times new roman", 15, "bold"), fg="black", bg="white")
                novaLozinka.place(x=50, y=220)

                self.txt_novaLozinka = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
                self.txt_novaLozinka.place(x=50, y=250, width=250)

                btn = Button(self.root2, text="Promeni", command=self.promena_lozinke, font=("times new roman", 15, "bold"), fg="white", bg="blue")
                btn.place(x=130, y=290)

    def izlaz(self):
        response = messagebox.askyesno("Izlaz", "Da li ste sigurni da želite da izadjete?",parent=self.root)
        if response:
            self.root.destroy()





main()
