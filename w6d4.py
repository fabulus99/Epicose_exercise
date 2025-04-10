import math
valore1 = float(input("inserisci il primo vettore :\n"))
figure = {"1":"quadrato","2":"rettangolo","3":"cerchio"}

#funzione di calcolo
def calcoli_figure(figura, valore1 , valore2=0 ):
    if figura == "quadrato":
        perimetro = valore1*4
        area = valore1**2
    elif figura =="rettangolo" :
        valore2=float(input("inserisci il secondo lato:\n"))
        perimetro = (valore1+valore2)*2
        area=valore2*valore1
    elif figura == "cerchio" :
        perimetro = 2 * math.pi * valore1
        area = math.pi * (valore1 ** 2)
    else :
        print("scelta errata")

    return perimetro, area
#funzione per la scelta delle figure
def scelta():
    for i in figure.keys():
            print("seleziona", i , "per", figure[i]) 
            
#funzione main
while figure :
        scelta()
        x=input("seleziona la figura digitando il numero corrispondente\n")
        print("hai scelto",figure[x] )    
        figura = figure[x]
        perimetro, area = calcoli_figure(figura,valore1)
        print("il perimetro è:", perimetro)
        print("l'area è :", area)  
        del figure[x]