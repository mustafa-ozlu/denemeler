from ast import main
import sys

def baslik():
    print("-"*30)
    print("1. Santigrat Fahreneit ")
    print("2. Fahreneit Santigrat")
    print("3. Çıkış")
    print("-"*30)


def santitofah():
    #f-32/1,8
    derece=float(input("Santigrat Dereceyi Gir : "))
    fahreneit=round((derece*1.8)+32,2)
    print(derece,"Santigrat = " ,fahreneit, " Fahreneit")
    
def fahtosanti():
    derece=float(input("Fahreneit Dereceyi Gir : "))
    santi=round((derece-32)/1.8,2)
    
    print(derece, "Fahreneit = ",santi," Santigrat")
    
while True :
    baslik()
    secim=input("Secimini Yap : ")

    if secim =="1":
        santitofah()
    elif secim == "2":
        fahtosanti()
    elif secim == "3":
        print("By By")
        sys.exit()
    else:
        print("Hatali Giris\n")