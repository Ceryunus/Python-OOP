#classlaı oluşturma ve 1 örnek updateing
import time
zaman=time.localtime()

#person adında bir class oluşturdum
class Person:

    #class attributes buraya yazılır
    adress="no information"


    #constructor (yapıcı metod)
    def __init__(self,name,year):
        self.name = name
        self.year = year
        print("constructor metodu calıştırıldı")


        #object attributes



    #instance methods
    def selam(self):
        print(f"Merhaba benim adım {self.name}")
    def ageCalculator(self):

        return print(f"{zaman.tm_year-self.year} yasındasınız" )


#object (instance)

p1=Person("yunus",2001)
p2=Person(name="kadir",year=1993)

#update
p1.name="Yunus Emre"
p1.adress="Trabzon"
#oluşan objeleri yazdırdım
print(p1.name)
print(f"name :{p1.name}  birthyear :{p1.year} adress :{p1.adress}")
print(f"name :{p2.name}  birthyear :{p2.year} adress :{p1.adress}")

#selamlama ve yaş hesapmama fonlsiyonlarını çalıştırdım.
p1.selam()
p1.ageCalculator()