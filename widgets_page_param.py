import tkinter as tk 
from data_page import data_automode_blue
from IHM_Global import *


class FrameModeAuto():
    LARG_FRAME = 245
    HAUT_FRAME = 300
    XFIELDSENTRY = 190
    prioclim=(1,1,1,1)
    
    def __init__(self,window,posx=5,posy=20, texte = "couleur tempo", colour='#C0C0C0',automodedata=data_automode_blue): 
        
        self.automodedata=automodedata
        #============= variables directement associées au Widget =========  
        self.tempminHP = tk.IntVar(window) 
        self.tempminHC = tk.IntVar(window) 
        self.prioclim_salon = tk.IntVar(window) 
        self.prioclim_sam = tk.IntVar(window) 
        self.prioclim_entree = tk.IntVar(window)
        self.prioclim_couloir = tk.IntVar(window)  
        self.tempext = tk.IntVar(window)
        self.powexcess_start = tk.IntVar(window) 
        self.powexcess_stop = tk.IntVar(window)
        #============= chargement des variables associées au Widget ========= 
        self.tempminHP.set(self.automodedata.temp_min_HP) 
        self.tempminHC.set(self.automodedata.temp_min_HC)
        self.prioclim_salon.set(self.automodedata.clim_prio[0])
        self.prioclim_sam.set(self.automodedata.clim_prio[1])
        self.prioclim_entree.set(self.automodedata.clim_prio[2])
        self.prioclim_couloir.set(self.automodedata.clim_prio[3])
        self.tempext.set(self.automodedata.temp_min_ext)
        self.powexcess_start.set(self.automodedata.pow_excess_start)
        self.powexcess_stop.set(self.automodedata.pow_excess_stop)

        
     
        
        # FRAME MODE AUTOMATIQUE                            
        frame_Auto = tk.Frame(window, width=self.LARG_FRAME,height=self.HAUT_FRAME,relief='sunken',bg=COLOUR_FRAME,bd=2)
        frame_Auto.place(x=posx,y=posy+30)
        label_Auto= tk.Label(window, text=texte,bg=colour); 
        label_Auto.place(x=posx, y=posy)
    
        # Saisie des températures min HP
        label_tempHP= tk.Label(frame_Auto, text="Température min HP :", bg=COLOUR_FRAME)
        label_tempHP.place(x=10, y=5)
        spinbox_HP=tk.Spinbox(frame_Auto,from_ = 17, to =22, width =2, textvariable=self.tempminHP)
        spinbox_HP.place(x=self.XFIELDSENTRY , y=5)    
    
        # Saisie des températures min HC
        label_tempHC= tk.Label(frame_Auto, text="Température min HC :", bg=COLOUR_FRAME)
        label_tempHC.place(x=10, y=25)
        spinbox_HC=tk.Spinbox(frame_Auto,from_ = 17, to =22, width =2,textvariable=self.tempminHC)
        spinbox_HC.place(x=self.XFIELDSENTRY , y=25)   
    
        # les priorité des climatiseurs ...
        label_Salon= tk.Label(frame_Auto, text="Priorité Clim Salon :", bg=COLOUR_FRAME)
        label_Salon.place(x=10, y=55)
        spinbox_Salon=tk.Spinbox(frame_Auto,from_ = 1, to =4, width =1,textvariable=self.prioclim_salon )
        spinbox_Salon.place(x=self.XFIELDSENTRY+10 , y=55)
        
        label_SaM= tk.Label(frame_Auto, text="Priorité clim Salle à manger:", bg=COLOUR_FRAME)
        label_SaM.place(x=10, y=75)
        spinbox_SaM=tk.Spinbox(frame_Auto,from_ = 1, to =4, width = 1, textvariable=self.prioclim_sam)
        spinbox_SaM.place(x=self.XFIELDSENTRY+10 , y=75)
        
        label_Entree= tk.Label(frame_Auto, text="Priorité clim entrée :",bg=COLOUR_FRAME)
        label_Entree.place(x=10, y=95)
        spinbox_Entree=tk.Spinbox(frame_Auto,from_ = 1, to =4, width = 1,textvariable=self.prioclim_entree)
        spinbox_Entree.place(x=self.XFIELDSENTRY+10 , y=95)
    
        label_Couloir= tk.Label(frame_Auto, text="Priorité clim couloir :", bg=COLOUR_FRAME)
        label_Couloir.place(x=10, y=115)
        spinbox_Couloir=tk.Spinbox(frame_Auto,from_ = 1, to =4, width = 1, textvariable=self.prioclim_couloir )
        spinbox_Couloir.place(x=self.XFIELDSENTRY+10 , y=115)	
        
        # Saisie des températures exterieure cut off
        tk.Label(frame_Auto, text="Température extérieure ",bg=COLOUR_FRAME).place(x=10, y=145)
        tk.Label(frame_Auto, text="de coupure clim la nuit : ", bg=COLOUR_FRAME).place(x=10, y=165)
        spinbox_tempext_cut=tk.Spinbox(frame_Auto,from_ = 0, to =30, width =2, textvariable=self.tempext)
        spinbox_tempext_cut.place(x=self.XFIELDSENTRY , y=155)  
        
         # Saisie de la puissance de démarrage
        tk.Label(frame_Auto, text="Excès de puissance pour ", bg=COLOUR_FRAME).place(x=10, y=190)
        tk.Label(frame_Auto, text="démarrer surchauffe ", bg=COLOUR_FRAME).place(x=10, y=210)
        spinbox_pow_start=tk.Spinbox(frame_Auto,from_ = 0, to =2000,increment=100, width =4, textvariable=self.powexcess_start)  
        spinbox_pow_start.place(x=self.XFIELDSENTRY-10 , y=200)  
        
        # Saisie de la puissance d'arrêt
        tk.Label(frame_Auto, text="Excès de puissance pour ", bg=COLOUR_FRAME).place(x=10, y=235)
        tk.Label(frame_Auto, text="arrêter surchauffe ", bg=COLOUR_FRAME).place(x=10, y=255)
        spinbox_pow_stop=tk.Spinbox(frame_Auto,from_ = 0, to =2000, increment=100, width =4, textvariable=self.powexcess_stop)  
        spinbox_pow_stop.place(x=self.XFIELDSENTRY-10 , y=245) 
     
       
    

    def get_tempminHP(self):
        return(self.tempminHP.get()) 
        
    def get_tempminHC(self):
        return(self.tempminHC.get()) 
        
    def get_tempminext(self):
        return(self.tempext.get()) 
        
    def get_powexcess_start(self):
        return(self.powexcess_start.get()) 
        
    def get_powexcess_stop(self):
        return(self.powexcess_stop.get()) 
        
    def get_prioclim(self):
        self.prioclim=(self.prioclim_salon.get(),self.prioclim_sam.get(),
                    self.prioclim_entree.get(),self.prioclim_couloir.get())
        return self.prioclim
        
