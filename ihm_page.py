from ihm_page_fields import *
import tkinter as tk  # tk est l'alias du module tkinder 
# TK est la classe permettant de faire une fenêtre
# tk.TK est le moyen d'accéder à cette classe via l'alias tk
# Pour éviter d'utiliser tk.Tk (utiliser simplement Tk),
# on aurait pu faire "from tkinder import Tk".
# Tk est la classe permettant de faire des fenêtres

   



class HomePage(tk.Tk): 
    LARG_FRAME_POW_PIX = 200
    HAUT_FRAME_POW_PIX = 100
    POSX_FRAME_POW_PIX = 20
    POSY_FRAME_POW_PIX = 100
    COULOUR_FRAME = '#B9C8DF'
    
    # =====================constructeur=================================
    def __init__(self):
        tk.Tk.__init__(self)
        # --Fenêtre principale--
        self.geometry("800x480+0+0")  # taille en pixels
        self.resizable(width=0, height=0)
        self.title("Home") 
        # ===Elaboration des Wdgets de la fenêtre Home===       
        # --Les boutons de navigation--
        self.button_param = tk.Button(self, text="Param.", width=13,\
                                      height=1,\
                                      command=self.butparam_callback)
                                      # taille en multiple de la font
                                      # par défaut de tkinter 
                                      # (pas en pixel !)
        self.button_param.place(x=5, y=0)
        self.button_diag = tk.Button(self, text="Diagnostic",
                                     width=13, 
                                     height=1, 
                                     command=self.butdiag_callback)
        self.button_diag.place(x=140, y=0)
     
        # --Labels Date and Hour--
        self.label_date = tk.Label(self, text=PageData.time_date, 
                                   width=30, height=1)
        self.label_date.place(x=400, y=50) 
        self.label_hour = tk.Label(self, text=PageData.time_hour,
                                   width=30, height=1)
        self.label_hour.place(x=400, y=100) 
        
        # --Affichage infos puissance --
        self.frame_pow = tk.Frame(self, width=self.LARG_FRAME_POW_PIX, \
        height=self.HAUT_FRAME_POW_PIX, borderwidth=3,  \
        bg=self.COULOUR_FRAME)
        self.frame_pow.place(x=self.POSX_FRAME_POW_PIX,\
        y=self.POSY_FRAME_POW_PIX)
        self.label_powtot=tk.Label(self.frame_pow, \
        text="Puissance totale : "+str(PageData.pow_tot)+"W")
        self.label_powtot.pack()
 
 
 
 
 
 
        
    # ========================Méthode d'instance========================
    def update_time(self):
        self.label_date.config(text=PageData.time_date)
        # .config permet de modifier les options d'un widget en cours
        self.label_hour.config(text=PageData.time_hour)

    def update_powdata(self):
        self.label_powtot.config(\
        text="Puissance totale : "+str(PageData.pow_tot)+"W")
















    # =============Les callbacks des widgets, méthodes==================

    def butparam_callback(self):
        win_param=tk.Toplevel(self)
        win_param.geometry("800x480+0+0")   # taille en pixels
        win_param.resizable(width=0, height=0)
        win_param.title("Paramètre")
        #--top boutons--
        button_exit = tk.Button(win_param, text="Back", width=13,
                                height=1 , command=win_param.destroy)
        button_exit.place(x=5, y=0)
        win_param.grab_set()    # permet à la fenêtre param 
                                # de recevoir les évènements.

    def butdiag_callback(self):
        win_diag=tk.Toplevel(self)
        win_diag.geometry("800x480+0+0")  # taille en pixels
        win_diag.resizable(width=0, height=0)
        win_diag.title("Diagnostic")
        # --top boutons--
        button_exit = tk.Button(win_diag, text="Back", width=13,
                                height=1 , command=win_diag.destroy)
        button_exit.place(x=5, y=0)
        win_diag.grab_set() 




    # =================== Test unitaire=================================

  
if __name__ == "__main__" :
    # === Genération de la fenêtre principale ===
    win_home = HomePage()
    PageData.time_date = "Lundi 4/07/1973"
    PageData.time_hour = "01:34:56"
    PageData.pow_tot=1500.2
    win_home.update_powdata()
    win_home.update_time()
    win_home.mainloop()
    



	 
