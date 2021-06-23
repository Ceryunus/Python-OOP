#classlar ile örnek Inheritance - Kalıtım(Not : Javada daha iyi :) )
import time
zaman=time.localtime()

class teacher():
    def __init__(self,name,surname,birthday):
        self.name=name
        self.surname=surname
        self.birthday=birthday


    def ageCalculator(self):
        age=zaman.tm_year-self.birthday
        return age


    def sayHello(self):
        print("Merhaba benim adım "+self.name)


class student(teacher): #teacher classının özelliklerini miras aldı bu class

    def __init__(self,name,surname,birthday,schoolNumber):
        teacher.__init__(self,name,surname,birthday) # burada da miras aldığı şeyleri cağırıyorum ki kullanabileyim
        self.schoolnumber=schoolNumber


t1=teacher("Thecapsiz", "hoca", 1965)
print(f"öğretmen isim : {t1.name} soyisim : {t1.surname} doğum yılı : {t1.birthday} yaşı : {t1.ageCalculator()}")
s1=student("yunus","mersinli",2001,616099)
print(f"ögrenci ismi : {s1.name} soyisim : {s1.surname} doğum yılı : {s1.birthday} yaşı : {s1.ageCalculator()}")
s1.sayHello()
