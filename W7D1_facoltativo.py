#genera password
import random
lista = ["a","b","c","d","e","f","g","h","i","l","m","n","o","p","q","r","s","t","u","v","z","1","2","3","4","5","6","7","8","9","0","!","$","&"]
lunghezza = int(input("inserisci:\n1 per una password di 8 caratteri\n2 per una di 20 caratteri:\n"))
passw = ""
if lunghezza == 1:
    while len(passw) < 8 :    
        passw = passw + random.choice(lista)

elif lunghezza == 2:
    while len(passw) < 20:
        passw = passw + random.choice(lista)

else : 
    print("scelta errata")

print("questa è la tua nuova password:\n" , passw)