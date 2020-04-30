from tkinter import *
from rdb import Rdb


class Options:
    def __init__(self, window, menu):
        self.window = window  # la fenetre dans laquelle seront afficher les options
        self.rdb_list = []  # liste des radiobutton
        self.menu = menu

        self.frame = Frame()
        self.frame.pack(expand=YES, side=TOP)

        # par default, on affiche les options
        self.load_opt()

    # charge l'affichage des option

    def load_opt(self):
        self.label_title()
        self.btn_retour()
        self.create_rdBtn_group()

    # créer un groupe de radiobouton
    def create_rdBtn_group(self):
        # on precharge les radiobutton
        file = open("config.cfg", "r")
        lines = file.readlines()
        file.close()
        length = len(lines)

        file = open("opt.cfg", "r")

        for line in file:
            # coupe la chaine de caractere en deux
            if line[0] != "#" and line.split("=")[0] == "level":
                lvl = line.split("=")[1].rstrip()
                break

        # on créer un radiobutton pour la generation automatique
        #self.create_radioBtn("Aléatoire", "None")
        # correspond au numero du radiobutton créer
        for i in range(length):  # pour chaque lignes
            # si la ligne comence par cfg
            if lines[i].rstrip() == lvl:
                # on créer un radiobutton
                break
        i += 1
        while (i < length):  # pour chaque lignes
            # si la ligne comence par cfg
            if lines[i][0:3] == "cfg":
                # on créer un radiobutton
                self.create_radioBtn("Grille "+lines[i][3:].rstrip(' \n'), "cfg"+lines[i][3:].rstrip(' \n'))

            if lines[i][0:3] == "lvl":
                break
            i += 1

        # on definit le bouton selectionné
        for line in file:
            # coupe la chaine de caractere en deux
            if line[0] != "#" and line.split("=")[0] == "config":
                cfg = line.split("=")[1].rstrip()
                for x in self.rdb_list:
                    if x.cfg == cfg:
                        x.select()
        file.close()

    # créer un radiobouton

    def create_radioBtn(self, name, cfg):
        # sur click appele la fonction write_opt_cfg() qui réécrit le fichier opt.cfg avec la nouvelle config
        rdb = Rdb(name, cfg, None, self.frame)

        self.rdb_list.append(rdb)  # on l'ajoute dans la liste des radiobutton

    # affiche le titre

    def label_title(self):
        label_title = Label(self.frame, text="OPTIONS",
                            font=("Courrier", 40), fg='#563535')
        label_title.pack(anchor=N)

    # recharge le menu
    def btn_retour(self):
        self.btn_back = Button(self.window, text="Menu", font=(
            "Courrier", 20), fg='#b62546', command=self.load_menu)
        self.btn_back.place(x=5, y=5, width=80, height=40)

    def load_menu(self):
        self.btn_back.destroy()
        self.frame.destroy()
        self.menu.load_menu()
