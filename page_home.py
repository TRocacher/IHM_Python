from widgets_page_param import FrameModeAuto
from page_diag import *
from IHM_Global import *

from data_page import data_homepage,data_automode_blue,data_automode_white,data_automode_red
import tkinter as tk  # tk est l'alias du module tkinder 

from Serial_Interface import serial_data

class PageHome(tk.Tk):
    #frame puissance 
    LARG_FRAME_POW_PIX = 260
    HAUT_FRAME_POW_PIX = 135
    POSX_FRAME_POW_PIX = 20
    POSY_FRAME_POW_PIX = 100
    #frame mode
    LARG_FRAME_MODE_PIX = 190
    HAUT_FRAME_MODE_PIX = 37
    POSX_FRAME_MODE_PIX = 500
    POSY_FRAME_MODE_PIX = 100
    #temop couleur
    POSX_TEMPO = 300
    POSY_TEMPO = 20
    
   
    
    # =====================constructeur=================================
    def __init__(self):
        tk.Tk.__init__(self)
        # === Fenêtre principale ===
        self.geometry("800x480+0+0")  # taille en pixels
        self.resizable(width=0, height=0)
        self.title("Home") 
        
        # === Elaboration des Wdgets de la fenêtre Home ===
        #  --- la barre de menu et les menus ... --
        self.menubar=tk.Menu(self,tearoff=0) # création de contenant menubar
        
            # item Mode...
        self.mode_dictio={HMI_Mode_Off:"Arrêt",HMI_Mode_Auto:"Automatique",HMI_Mode_Program :"Programmation",HMI_Mode_Hollidays:"Vacances"}  
       
        self.menu_mode=tk.Menu(self.menubar, tearoff=0) # création du menu paramètre, fils de menubar    
        self.menubar.add_cascade(label="Mode", menu=self.menu_mode) # placement du menu fils dans la barre de menu
        self.menu_mode.add_command(label="Arrêt",command=self.updatemode_off)  # ajout des sous menus
        self.menu_mode.add_command(label="Auto",command=self.updatemode_auto)
        self.menu_mode.add_command(label="Programmation",command=self.updatemode_prog)
        self.menu_mode.add_command(label="Vacances",command=self.updatemode_hollidays)
            # item Param...
        self.menu_param=tk.Menu(self.menubar, tearoff=0) # création du menu paramètre, fils de menubar  
        self.menubar.add_cascade(label="Paramètres", menu=self.menu_param) # placement du menu fils dans la barre de menu
        self.menu_param.add_command(label="Mode Automatique",command=self.create_win_param_auto)  # ajout des sous menus
        self.menu_param.add_command(label="Mode Programmation")
        self.menu_param.add_command(label="Mode Vacances")
            # item Diagnostic...
        self.menubar.add_command(label="Diagnostic",command=self.butdiag_callback) #ajout d'un autre menu simple dans la barre de menu
            # affichage de l'ensemble du menu
        self.config(menu=self.menubar) #affichage du menu
        
        
        # label couleur tempo :
        self.label_couleurtempo=tk.Label(self,text="Couleur du jour : "+ \
                              data_homepage.tempostring[data_homepage.tempo])
        self.label_couleurtempo.place(x=self.POSX_TEMPO, y=self.POSY_TEMPO)
               
        # # --Les boutons de navigation--
        # self.button_param = tk.Button(self, text="Param.", width=13, height=1,command=self.create_win_param_auto)
        # self.button_param.place(x=5, y=300)
        # self.button_diag = tk.Button(self, text="Diagnostic", width=13, height=1,command=self.butdiag_callback)
        # self.button_diag.place(x=140, y=300)
     
        # --Labels Date and Hour--
        self.label_date = tk.Label(self, text=data_homepage.time_date,width=30, height=1)
        self.label_date.place(x=400, y=50) 
        self.label_hour = tk.Label(self, text=data_homepage.time_hour, width=30, height=1)
        self.label_hour.place(x=400, y=75) 
        
        # --Affichage infos puissance --
        self.frame_pow = tk.Frame(self, width=self.LARG_FRAME_POW_PIX, height=self.HAUT_FRAME_POW_PIX, borderwidth=3,relief='groove',bg=COLOUR_FRAME)
        self.frame_pow.place(x=self.POSX_FRAME_POW_PIX, y=self.POSY_FRAME_POW_PIX)
        self.label_powtot=tk.Label(self.frame_pow, text="Puissance totale : "+str(data_homepage.pow_tot)+"W",bg=COLOUR_FRAME)
        self.label_powtot.place(x=10, y=5)

        self.label_powinv=tk.Label(self.frame_pow, text="Puissance onduleur : "+str(data_homepage.pow_inv)+"W", bg=COLOUR_FRAME)
        self.label_powinv.place(x=10, y=25)

        self.label_powl1home=tk.Label(self.frame_pow, text="Puissance L1 maison : "+str(data_homepage.pow_l1home)+"W",bg=COLOUR_FRAME)
        self.label_powl1home.place(x=10, y=45)       

        self.label_powl1=tk.Label(self.frame_pow, text="Puissance L1  : "+str(data_homepage.pow_l1)+"W", bg=COLOUR_FRAME)
        self.label_powl1.place(x=10, y=65) 

        self.label_powl2=tk.Label(self.frame_pow, text="Puissance L2  : "+str(data_homepage.pow_l2)+"W", bg=COLOUR_FRAME)
        self.label_powl2.place(x=10, y=85) 
 
        self.label_powl3=tk.Label(self.frame_pow, text="Puissance L3  : "+str(data_homepage.pow_l3)+"W", bg=COLOUR_FRAME)
        self.label_powl3.place(x=10, y=105) 
        
        self.temoin_pow=tk.Canvas(self.frame_pow, bg=COLOUR_FRAME,height=24, width=24,highlightthickness=0)
        self.temoin_pow.place(x=220,y=5)
        self.temoin=self.temoin_pow.create_oval(2,2,22,22,fill="red")
        
        #affichage du mode
        self.frame_mode = tk.Frame(self, width=self.LARG_FRAME_MODE_PIX, height=self.HAUT_FRAME_MODE_PIX, borderwidth=3,relief='groove',bg=COLOUR_FRAME)
        self.frame_mode.place(x=self.POSX_FRAME_MODE_PIX, y=self.POSY_FRAME_MODE_PIX)
        self.label_mode=tk.Label(self.frame_mode, text=" Mode  : "+ self.mode_dictio[data_homepage.mode], bg=COLOUR_FRAME)
        self.label_mode.place(x=5, y=5) 
        # self.mode.set(data_homepage.mode)
        # self.radiobut_mode1=tk.Radiobutton(self.frame_mode,text=" Off", variable=self.mode, \
                        # value=HMI_Mode_Off, bg=COLOUR_FRAME,highlightthickness=0, command=self.update_datapage_mode).place(x=0, y=5) 
        # self.radiobut_mode2=tk.Radiobutton(self.frame_mode,text=" Auto", variable=self.mode, \
                        # value=HMI_Mode_Auto, bg=COLOUR_FRAME,highlightthickness=0, command=self.update_datapage_mode).place(x=0, y=25) 
        # self.radiobut_mode3=tk.Radiobutton(self.frame_mode,text=" Program", variable=self.mode, \
                        # value=HMI_Mode_Program, bg=COLOUR_FRAME,highlightthickness=0, command=self.update_datapage_mode).place(x=0, y=45) 
        # self.radiobut_mode4=tk.Radiobutton(self.frame_mode,text=" Hollidays", variable=self.mode, \
                        # value=HMI_Mode_Hollidays, bg=COLOUR_FRAME,highlightthickness=0, command=self.update_datapage_mode).place(x=0, y=65) 
        
    # ======================== Méthode de mise à jour des champs de la fenêtre ... ========================
    def update_time(self):
        self.label_date.config(text=data_homepage.time_date)   # .config permet de modifier les options d'un widget en cours
        self.label_hour.config(text=data_homepage.time_hour)

    def update_powdata(self):
        self.label_powtot.config(text="Puissance totale : " +str(data_homepage.pow_tot)+"W")
        self.label_powinv.config(text="Puissance onduleur : " +str(data_homepage.pow_inv)+"W")
        self.label_powl1home.config(text="Puissance L1 maison : " +str(data_homepage.pow_l1home)+"W")
        self.label_powl1.config( text="Puissance L1 : " +str(data_homepage.pow_l1)+"W")
        self.label_powl2.config( text="Puissance L2 : " +str(data_homepage.pow_l2)+"W")
        self.label_powl3.config(text="Puissance L3 : " +str(data_homepage.pow_l3)+"W")
        self.temoin_pow.itemconfig( self.temoin,fill=data_homepage.pow_temoin)

    def update_tempo(self):
        self.label_couleurtempo.config(text="Couleur du jour : "+ data_homepage.tempostring[data_homepage.tempo])
        self.label_couleurtempo.config(bg=data_homepage.tempobg[data_homepage.tempo])
  
  
    # ======================== Méthode de mise à jour de data_homepage ... ========================
    
    
    def updatemode_off(self):
        data_homepage.mode=HMI_Mode_Off #self.mode.get()
        self.label_mode.config(text=" Mode  : "+ self.mode_dictio[data_homepage.mode])
        print(data_homepage.mode)
    def updatemode_auto(self):
        data_homepage.mode=HMI_Mode_Auto
        self.label_mode.config(text=" Mode  : "+ self.mode_dictio[data_homepage.mode])
        print(data_homepage.mode)
    def updatemode_prog(self):
        data_homepage.mode=HMI_Mode_Program
        self.label_mode.config(text=" Mode  : "+ self.mode_dictio[data_homepage.mode])
        print(data_homepage.mode)
    def updatemode_hollidays(self):
        data_homepage.mode=HMI_Mode_Hollidays
        self.label_mode.config(text=" Mode  : "+ self.mode_dictio[data_homepage.mode])
        print(data_homepage.mode)










    # =============Les callbacks des widgets, méthodes==================

    def create_win_param_auto(self):
        #PageParamAuto(self)
        win_paramauto=tk.Toplevel(self)
        win_paramauto.geometry("800x480+0+0")   # taille en pixels
        win_paramauto.resizable(width=0, height=0)
        win_paramauto.title("Paramètre")

        win_paramauto.grab_set()    # permet à la fenêtre param de recevoir les évènements.
                                
        # === Elaboration des Widgets de la fenêtre win_paramauto ===
        #--top boutons--
        button_back = tk.Button(win_paramauto, text="Retour", width=13, height=1 , command=win_paramauto.destroy)
        button_back.place(x=5, y=0)
        button_confirm = tk.Button(win_paramauto, text="Confirmer", width=13, height=1 , command=self.win_paramauto_confirm)
        button_confirm.place(x=140, y=0)
        # Les 3 frames principames de saisies param auto
        self.frame_auto_blue=FrameModeAuto(win_paramauto,16,100, "Couleur Tempo bleu", COLOUR_BLUE,data_automode_blue)
        self.frame_auto_white=FrameModeAuto(win_paramauto,245+16*2,100, "Couleur Tempo blanc", COLOUR_WHITE,data_automode_white)
        self.frame_auto_red=FrameModeAuto(win_paramauto,490+16*3,100, "Couleur Tempo rouge",  COLOUR_RED,data_automode_red)

    def win_paramauto_confirm(self): 

        data_automode_blue.update(self.frame_auto_blue.get_tempminext(),      
                                self.frame_auto_blue.get_powexcess_start(),
                                self.frame_auto_blue.get_powexcess_stop(), 
                                self.frame_auto_blue.get_tempminHC(),
                                self.frame_auto_blue.get_tempminHP(),
                                self.frame_auto_blue.get_prioclim() )
                                
        data_automode_white.update(self.frame_auto_white.get_tempminext(),      
                                self.frame_auto_white.get_powexcess_start(),
                                self.frame_auto_white.get_powexcess_stop(), 
                                self.frame_auto_white.get_tempminHC(),
                                self.frame_auto_white.get_tempminHP(),
                                self.frame_auto_white.get_prioclim() ) 
                                
        data_automode_red.update(self.frame_auto_red.get_tempminext(),      
                                self.frame_auto_red.get_powexcess_start(),
                                self.frame_auto_red.get_powexcess_stop(), 
                                self.frame_auto_red.get_tempminHC(),
                                self.frame_auto_red.get_tempminHP(),
                                self.frame_auto_red.get_prioclim() )   
                                          
        serial_data.sendto_smartgateway()
        

    def butdiag_callback(self):
        win_diag_creation(self)




# =================== Test unitaire=================================

  
if __name__ == "__main__" :
    # === Genération de la fenêtre principale ===
    win_home = PageHome()
    data_homepage.time_date = "Lundi 4/07/1973"
    data_homepage.time_hour = "01:34:56"
    data_homepage.pow_tot=1500.2
    data_homepage.pow_inv=1800.2
    data_homepage.pow_l1home=2800.2
    data_homepage.pow_l1=2801.2
    data_homepage.pow_l2=2802.2
    data_homepage.pow_l3=2803.2
    win_home.update_powdata()
    win_home.update_time()
    
    
  
    win_home.temoin_pow.itemconfig(win_home.temoin,fill="green")
    
    
    win_home.mainloop()
    



	 
