deger={
	'I' : 1,
	'V' : 5,
	'X' : 10,
	'L' : 50,
	'C' : 100,
	'D' : 500,
	'M' : 1000,
	}

def RomenToDecimal(romaRakam) :
	sum = 0
	for i in range(len(romaRakam) -1) :
		left = romaRakam[i]
		right = romaRakam[i+1]
		if deger[left]<deger[right] :
			sum -=deger[left]
		else :
			sum += deger[left]
	sum += deger[romaRakam[-1]]
	print(romaRakam," === ",sum)
	return sum
	
romaRakam=input('Romen Rakamı Gir : ')
romaRakam=romaRakam.upper()
RomenToDecimal(romaRakam)
