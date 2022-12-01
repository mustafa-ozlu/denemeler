sayi=int(input("Sayı Giriniz :  "))

toplam=0

for i in range(1,sayi):
    if sayi%i==0:
        toplam+=i
        
if sayi==toplam:
    print("*"*30)
    print("{} sayısı mükemmel sayıdır".format(sayi))
    print("*"*30)
        
else:
    print("{} sayısı mükemmel değil.".format(sayi))
        