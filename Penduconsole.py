###Ce programme vise à créer un pendu dans la console###
#Guillot_Antony 10/12/2021
#ce qui est améliorable:

##Modules
import random as rd


##Variables
#alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
dictionnaire=["dragon","marmitte","joueur","violet","camion","chaise"]

##Fonctions

def choix(liste_mots):
    #cette fontion renvoi un élément aléatoir d'une liste.
    return rd.choice(liste_mots)
    
def liste_mots():
    #cration des mots avec un fichier txt
    mots=open("Mots.txt","r")
    dictionnaire=mots.readlines()
    n=len(dictionnaire)
    for i in range(n) :
        element=dictionnaire[i]
        element=element.lower()
        element=list(element)
        for lettre in element:
            if lettre=="\n":
                 element.remove("\n")
        mot=""
        for lettre in element:
            mot=mot+lettre
        
        dictionnaire[i]=mot
    mots.close()

    return dictionnaire


def choix_lettres(mot):
    #creation du mot à trouver
    n=len(mot)
    liste_lettre=list(mot)
    nb_lettre_visible= n//7 +1
    lettres_visibles=[]
    boucle=True
    while boucle:
        try :
            difficulte=int(input("Entrez une version 0 (lettre du debut) ou 1 (une lettre pour 7 lettre dans le mot) "))
            if difficulte==1 or difficulte==0:
                boucle=False
            else:
                print("Vous devez rentrez 0 ou 1")


        except  ValueError:
            print("Entrez un chiffre (0 ou 1)")


    if difficulte==1:
        for i in range(nb_lettre_visible):
            lettre=choix(liste_lettre)
            if lettre not in lettres_visibles:
                lettres_visibles.append(lettre)

        
    elif difficulte==0:
        lettres_visibles=liste_lettre[0]
    else:
        print("Choissisez entre 0 et 1 pas autre chose merci:        ")  
        return choix_lettres(mot)

    for i in range(n):
            if liste_lettre[i] not in lettres_visibles:
                liste_lettre[i]=" _ "      

    return liste_lettre


def pendu():
    #cette fonction affiche une version du jeu en console
    alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    erreurs=8
    mot=choix(dictionnaire)
    liste_lettre=choix_lettres(mot)
    n=len(mot)
    lettres_tester=[]
    for lettre in liste_lettre:
        if lettre in alphabet and lettre not in lettres_tester:
            lettres_tester=lettres_tester +[lettre]
 
    while erreurs!=0 and " _ " in liste_lettre:
        print()
        print(liste_lettre)
        print("Il vous reste {a} possibilité ".format(a=erreurs))
        print("Voici les lettres que vous avez essayé {a} ".format(a=lettres_tester))
        boucle=True
        while boucle:
            try:
                essai=str(input("Entrer une lettre 'en minusule'  à essayer:     "))

                if essai in alphabet:
                    boucle=False
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
                            print("Rater cette lettre n'y est pas essaye encore")                    
                            erreurs=erreurs-1
                            
                    else:
                        print("ATTENTION vous avez déjà tester cette lettre ")
                else:
                    print("Rentrez une lettre en minuscules")

            except ValueError:
                print("Entrez ce que je vous demande svp , une lettre en minuscule")

    if erreurs==0:
        print("La reponse était {a} le pendu est mort try again".format(a=mot))
        return erreurs
        
    else:
        print("Vous avez trouvé {a} GG".format(a=liste_lettre))
        return erreurs



def boucle_jeu():
    boucle=True
    meilleur_score=0
    while boucle:
        try:
            volonte=int(input("Pour jouer entre 1 sinon entrez 0: "))
            if volonte==0 or volonte==1:
                boucle=False
            else:
                print("J'ai dit 0 OU 1")
        except  ValueError:
            print("Non mais entrez un nombre au moins")
        
    volonte=1
    while volonte==1:
        x=pendu()
        if x!=0:
            meilleur_score=8-pendu()
            print("Lors de votre meilleur essai vous avez fait {a} erreurs ".format(a=meilleur_score))
        boucle=True
        
        while boucle:
            try:
                volonte=int(input("Pour retry taper 1 /0 pour arreter:    "))
                if volonte == 0 or volonte==1:
                    boucle=False
                else:
                    print("0 ou 1 !!")
            except  ValueError:
                print("Non mais entrez un nombre au moins")
           

            
    print("BY BY")
    return
    
dictionnaire=liste_mots()
boucle_jeu()