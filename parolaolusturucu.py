import random
import string

def generate_password(length,level,output=[]):
    chars=string.ascii_letters
    if level>1:
        chars="{}{}".format(chars,string.digits)
    if level>2:
        chars="{}{}".format(chars,string.punctuation)
        
    for i in range(length):
        output.append(random.choice(chars))
    return "".join(output)
    
print(("-"*30)+"\n Parola Oluşturucu\n"+("-"*30))

pass_length=int(input("Uzunluk   :  "))
pass_level=int(input("Düzey     :  "))

parola=generate_password(pass_length,pass_level)
print("\nParolanız : {}\n ".format(parola))
    