###Ce programme vise à créer un pendu avec interface graphique###
#Guillot_Antony 10/12/2021
#ce qui est améliorable:

##Importation modules
import tkinter as tk
import random as rd
from typing import Text





##Variables testes
#alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#dictionnaire=["dragon","marmitte","joueur","violet","camion","chaise"]

##Fonctions

def creation_main_window():
    #creation fenetre
    print(1)
    main_window = tk.Tk()
    main_window.title("Pendu")
    main_window.geometry('1000x500+450+100')

    image1 = tk.PhotoImage(file="bonhomme1.gif") 
    image2 = tk.PhotoImage(file="bonhomme2.gif") 
    image3 = tk.PhotoImage(file="bonhomme3.gif") 
    image4 = tk.PhotoImage(file="bonhomme4.gif") 
    image5 = tk.PhotoImage(file="bonhomme5.gif") 
    image6 = tk.PhotoImage(file="bonhomme6.gif") 
    image7 = tk.PhotoImage(file="bonhomme7.gif") 
    image8 = tk.PhotoImage(file="bonhomme8.gif") 
    top_canvas= tk.Canvas(main_window,width=500,height=300)
    
    top_canvas.place(x=0,y=0)


    title_chose_lettre=tk.Label(main_window,text = "Entrez ce qu'on vous demande")
    title_chose_lettre.place(x=30,y=401)
    top_canvas.create_image(0,0, anchor = "nw", image=image1)


    chose_lettre= tk.Entry(main_window)
    chose_lettre.place(x=180,y=450)

    txt_demande=tk.StringVar()
    txt_demande.set("test")
    demande=tk.Label(main_window,textvariable= txt_demande)
    demande.place(x=500,y=1)

    txt_mot_courrant=tk.StringVar()
    txt_mot_courrant.set("test")
    mot_courrent=tk.Label(main_window,textvariable= txt_mot_courrant)
    mot_courrent.place(x=500,y=100)

    txt_lettre_utilises=tk.StringVar()
    txt_lettre_utilises.set("test")
    lettre_utilises=tk.Label(main_window,textvariable=txt_lettre_utilises)
    lettre_utilises.place(x=500,y=200)

    txt_chance=tk.StringVar()
    txt_chance.set(8)
    nb_chance=tk.Label(main_window,textvariable= txt_chance)
    nb_chance.place(x=500,y=300)

    


    def get_entry():
        x=chose_lettre.get()
        alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        erreurs=txt_chance
        lettres_tester=(list(txt_lettre_utilises))
        try:
            essai=str(x)
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
                        print("Rater cette lettre n'y est pas essaye encore")                    
                        erreurs=erreurs-1
                        
                else:
                    print("ATTENTION vous avez déjà tester cette lettre ")
            else:
                print("Rentrez une lettre en minuscules")

        except ValueError:
            print("Entrez ce que je vous demande svp , une lettre en minuscule")

        return x



    def choix(liste_mots):
        #cette fontion renvoi un élément aléatoir d'une liste.
        return rd.choice(liste_mots)
        
    def liste_mots():
        #creation des mots avec un fichier txt
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
        for i in range(nb_lettre_visible):
            lettre=choix(liste_lettre)
            if lettre not in lettres_visibles:
                lettres_visibles.append(lettre)
        for i in range(n):
                if liste_lettre[i] not in lettres_visibles:
                    liste_lettre[i]=" _ "      

        return liste_lettre


    def pendu():
        #cette fonction affiche une version du jeu en console
        dictionnaire=liste_mots()
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
                txt_demande.set("Pour jouer entre 1 sinon entrez 0: ")
                volonte=int(chose_lettre.get())
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
    def boucle_jeu2():
        alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        dictionnaire=liste_mots()
        mot=choix(dictionnaire)
        liste_lettre=choix_lettres(mot)
        n=len(mot)
        lettres_tester=[]
        for lettre in liste_lettre:
            if lettre in alphabet and lettre not in lettres_tester:
                lettres_tester=lettres_tester +[lettre]
        txt_mot_courrant.set(str(liste_lettre))
        txt_demande.set("Entrez une lettre")
        txt_lettre_utilises.set(lettres_tester)
        return

    start_button=tk.Button(main_window,text="start",command=boucle_jeu2)
    start_button.place(x=800,y=401)

    test_entre=tk.Button(main_window,text="test2",command=get_entry)
    test_entre.place(x=30,y=450)

    

    
    main_window.mainloop()
    return 0
    

creation_main_window() 