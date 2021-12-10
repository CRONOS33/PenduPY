###Ce programme vise à créer un pendu avec interface graphique###
#Guillot_Antony 10/12/2021
#ce qui est améliorable:

##Importation modules
import tkinter as tk

##Variables

##Fonctions

def creation_main_window():
    main_window = tk.Tk()
    main_window.title("Pendu")
    main_window.geometry('1000x500+450+100')

    top_canvas= tk.Canvas(main_window,width=500,height=300)
    top_canvas.place(x=0,y=0)

    title_chose_lettre=tk.Label(main_window,text = "Entrez ce qu'on vous demande")
    title_chose_lettre.place(x=30,y=401)

    chose_lettre= tk.Entry(main_window)
    chose_lettre.place(x=180,y=401)

    mot_courrent=tk.Label(main_window,text = "Entrez ce qu'on vous demande")

    start_button=tk.Button(main_window,text="start")
    start_button.place(x=800,y=401)

    main_window.mainloop()

creation_main_window()  