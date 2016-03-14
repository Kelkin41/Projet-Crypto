def sansPonctuation(chaine):
    i = 32
    for i in range(32,48,1):
        chaine = chaine.replace(chr(i),"")
    
    chaine = chaine.replace(" ","")
    chaine = chaine.replace("È","e")
    chaine = chaine.replace("‡","a")
    chaine = chaine.replace("Ë","e")
    chaine = chaine.replace("Í","e")
    chaine = chaine.replace("Ù","o")
    chaine = chaine.upper()
    print(chaine)
    

    
chaine = input("Entrer une chaine de caractere : ")
sansPonctuation(chaine)
