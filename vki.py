

from math import fabs


boycm=int(input("Boyunuz CM? : "))
kilo=float(input("Kilonuz KG? : "))

"""
18,5 küçükse zayıf
25 altı normal
30 altı şişman
40 üstü obez
"""
boy=boycm/100
vki=round(kilo/((boy)**2),2)
print(")("*15,"\n")

if vki < 18.5 :
    
    print("VKİ : {} Zayıfsınız...".format(vki))
    print("{} KG Alabilirsiniz.\n".format(round(24*(boy**2)-kilo),2))
    print(")("*15,"\n")
elif vki < 25 :
        print("VKİ : {} Normalsiniz...\n".format(vki))
        print(")("*15,"\n")
elif vki < 30 :
        print("VKİ : {} Fazla Kilolusunuz...".format(vki))
        print("{} KG Vermelisiniz.\n".format(round(kilo-(24.9*(boy**2)),2)))
        print(")("*15,"\n")
elif vki < 40 :
        print("VKİ : {} Obezsiniz...".format(vki))
        print("{} KG Vermelisiniz.\n".format(round(kilo-(24.9*(boy**2)),2)))
        print(")("*15,"\n")
else:
        print("VKİ : {} Aşırı Obezsiniz...".format(vki))
        print("{} KG Vermelisiniz.\n".format(round(kilo-(24.9*(boy**2)),2)))
        print(")("*15,"\n")