###Ce programme vise à créer un pendu dans la console###
#Guillot_Antony 10/12/2021
#ce qui est améliorable:

##Modules
import random as rd
from tkinter.constants import N

##Variables
#alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
dictionnaire=["dragon","marmitte","joueur","violet","camion","chaise"]

##Fonctions

def choix(liste_mots):
    #cette fontion renvoi un élément aléatoir d'une liste.

    return rd.choice(liste_mots)
    
def choix_lettres(mot):
    n=len(mot)
    liste_lettre=list(mot)
    nb_lettre_visible= n//7 +1
    lettres_visibles=[]

    for i in range(nb_lettre_visible):
        lettre=choix(liste_lettre)
        if lettre not in lettres_visibles:
            lettres_visibles.append(lettre)

    for i in range(n):
        if liste_lettre[i] not in lettres_visibles:
            liste_lettre[i]=" _ "

    return liste_lettre


def pendu():
    alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    erreurs=8
    mot=choix(dictionnaire)
    liste_lettre=choix_lettres(mot)
    n=len(mot)
    lettres_tester=[]
 
    while erreurs!=0 and " _ " in liste_lettre:
        print()
        print(liste_lettre)
        print("voici les lettres que vous avez essayé   ")
        print(lettres_tester)
        essai=str(input("entrer une lettre 'en minusule'  à essayer:     "))
        if essai in alphabet:
            if essai not in lettres_tester:
                 lettres_tester.append(essai)
           
            if essai in mot and essai not in liste_lettre:
                liste_indice=[]
                for i in range(n):
                    if essai==mot[i]:
                        liste_indice.append(i)
                for indice in (liste_indice):
                    liste_lettre[indice]=essai
            else:
                print("Rater essaye encore")
               
                erreurs=erreurs-1
                print("il vous reste")
                print(erreurs)
                print("possibilités") 
        else:
            print("rentrer une lettre en minuscules")
    if erreurs==0:
        print("la reponse était")
        print(mot)
        print("le pendu est mort")
        return None
        
    else:
        print("vous avez trouvez")
        print(liste_lettre)
        print("GG")
        return None

pendu()