import mysql.connector


class Konekcija:
   __konekcija = None
   @staticmethod 
   def getInstance():
      if(Konekcija.__konekcija == None):
         Konekcija()
      return Konekcija.__konekcija
   def __init__(self):
      if(Konekcija.__konekcija != None):
         raise Exception("Ovo je singleton")
      else:
         Konekcija.__konekcija = mysql.connector.connect(user='root', password='stevica011',host='127.0.0.1',database='hotel')