import re
def additionviaphrase(phrase):
    a = b = 0
    if re.search("(somme)\s{1,}[A-Za-z]{1,}\s{1,}\d{1,}\s{1,}[A-Za-z]{1,}\s{1,}\d{1,}", phrase) is not None:
        liste = re.findall("\d{1,}\.?\d{0,}",phrase)
        for i in range(len(liste)):
            a = liste[i]
            a = float(a)
            b += a
        print ("Cette somme est égale à: \n", b)
            
    else:
        print("Je ne peux rien faire")


#additionviaphrase("la somme de 13 et 30")
