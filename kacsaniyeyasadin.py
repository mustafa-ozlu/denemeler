from datetime import *

dogum=datetime.strptime(input("Doğum Tarihin (g.a.Y) :\t"),"%d.%m.%Y")
now=datetime.today()
yas=now-dogum
bugun=now.strftime("%d.%m.%Y")
print("Bugün :\t\t ",bugun) #,"%d.%m.%Y"))
print("{}\t Saniye Yaşadın".format(round(yas.total_seconds(),2)))
print("{}\t\t Gün Yaşadın".format(yas.days))
