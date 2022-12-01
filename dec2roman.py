import math


def DectoRoman(A) :
    deger={
    	1 : 'I',
    	5 : 'V',
    	10 : 'X',
    	50 : 'L',
    	100 : 'C',
    	500 : 'D',
    	1000 : 'M' ,
    	}

    div = 1
    while A>=div:
        div*=10
    div//=10
    res=""
    
    while A:
        lastnum=(A//div)
        
        if lastnum<=3:
            res+=(deger[div]*lastnum)
        elif lastnum==4:
            res+=(deger[div]+deger[div*5])
        elif 5 <= lastnum <=8:
            res+=(deger[div*5]+(deger[div]*(lastnum-5)))
        elif lastnum==9:
            res+=(deger[div]+deger[div*10])
            
        A=math.floor(A%div)
        div//=10
    return res
sayi=int(input("Decimal Sayı Giriniz: "))
print(sayi," Sayısı Roma Rakamı olarak: ", str(DectoRoman(sayi)))
