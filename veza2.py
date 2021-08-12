import mysql.connector


class Konekcija2:
   __konekcija = None
   @staticmethod 
   def getInstance():
      if(Konekcija2.__konekcija == None):
         Konekcija2()
      return Konekcija2.__konekcija
   def __init__(self):
      if(Konekcija2.__konekcija != None):
         raise Exception("Ovo je singleton")
      else:
         Konekcija2.__konekcija = mysql.connector.connect(user='root', password='stevica011',host='127.0.0.1',database='hotel')