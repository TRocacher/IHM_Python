import tkinter as tk 
from ihm_page_fields import AutoModeDataBlue,AutoModeDataWhite,AutoModeDataRed

class FrameModeAuto():
    LARG_FRAME = 245
    HAUT_FRAME = 300
    COLOUR_FRAME = '#C0C0C0'
    XFIELDSENTRY = 190
    
    def __init__(self,window,posx=5,posy=20, texte = "couleur tempo", colour='#C0C0C0',AutomodeData=AutoModeDataBlue): 
        #============= variables directement associées au Widget =========  
        tempminHP = tk.IntVar(window) 
        tempminHC = tk.IntVar(window) 
        prioclim_salon = tk.IntVar(window) 
        prioclim_sam = tk.IntVar(window) 
        prioclim_entree = tk.IntVar(window)
        prioclim_couloir = tk.IntVar(window)  
        tempext = tk.IntVar(window)
        powexcess_start = tk.IntVar(window) 
        powexcess_stop = tk.IntVar(window)
        #============= chargement des variables associées au Widget ========= 
        #tempext.set(AutomodeData.temp_min_ext)
        tempminHP.set(AutomodeData.temp_min_HP) 
        tempminHC.set(AutomodeData.temp_min_HC)
        prioclim_salon.set(AutomodeData.clim_prio[0])
        prioclim_sam.set(AutomodeData.clim_prio[1])
        prioclim_entree.set(AutomodeData.clim_prio[2])
        prioclim_couloir.set(AutomodeData.clim_prio[3])
        tempext.set(AutomodeData.temp_min_ext)
        powexcess_start.set(AutomodeData.pow_excess_start)
        powexcess_stop.set(AutomodeData.pow_excess_stop)

        
     
        
        # FRAME MODE AUTOMATIQUE                            
        frame_Auto = tk.Frame(window, width=self.LARG_FRAME,height=self.HAUT_FRAME,relief='sunken',bg=self.COLOUR_FRAME,bd=2)
        frame_Auto.place(x=posx,y=posy+30)
        label_Auto= tk.Label(window, text=texte,bg=colour); 
        label_Auto.place(x=posx, y=posy)
    
        # Saisie des températures min HP
        label_tempHP= tk.Label(frame_Auto, text="Température min HP :", bg=self.COLOUR_FRAME)
        label_tempHP.place(x=10, y=5)
        spinbox_HP=tk.Spinbox(frame_Auto,from_ = 17, to =22, width =2, textvariable=tempminHP)
        spinbox_HP.place(x=self.XFIELDSENTRY , y=5)    
    
        # Saisie des températures min HC
        label_tempHC= tk.Label(frame_Auto, text="Température min HC :", bg=self.COLOUR_FRAME)
        label_tempHC.place(x=10, y=25)
        spinbox_HC=tk.Spinbox(frame_Auto,from_ = 17, to =22, width =2,textvariable=tempminHC)
        spinbox_HC.place(x=self.XFIELDSENTRY , y=25)   
    
        # les priorité des climatiseurs ...
        label_Salon= tk.Label(frame_Auto, text="Priorité Clim Salon :", bg=self.COLOUR_FRAME)
        label_Salon.place(x=10, y=55)
        spinbox_Salon=tk.Spinbox(frame_Auto,from_ = 1, to =4, width =1,textvariable=prioclim_salon )
        spinbox_Salon.place(x=self.XFIELDSENTRY+10 , y=55)
        
        label_SaM= tk.Label(frame_Auto, text="Priorité clim Salle à manger:", bg=self.COLOUR_FRAME)
        label_SaM.place(x=10, y=75)
        spinbox_SaM=tk.Spinbox(frame_Auto,from_ = 1, to =4, width = 1, textvariable=prioclim_sam)
        spinbox_SaM.place(x=self.XFIELDSENTRY+10 , y=75)
        
        label_Entree= tk.Label(frame_Auto, text="Priorité clim entrée :",bg=self.COLOUR_FRAME)
        label_Entree.place(x=10, y=95)
        spinbox_Entree=tk.Spinbox(frame_Auto,from_ = 1, to =4, width = 1,textvariable=prioclim_entree)
        spinbox_Entree.place(x=self.XFIELDSENTRY+10 , y=95)
    
        label_Couloir= tk.Label(frame_Auto, text="Priorité clim couloir :", bg=self.COLOUR_FRAME)
        label_Couloir.place(x=10, y=115)
        spinbox_Couloir=tk.Spinbox(frame_Auto,from_ = 1, to =4, width = 1, textvariable=prioclim_couloir )
        spinbox_Couloir.place(x=self.XFIELDSENTRY+10 , y=115)	
        
        # Saisie des températures exterieure cut off
        tk.Label(frame_Auto, text="Température extérieure ",bg=self.COLOUR_FRAME).place(x=10, y=145)
        tk.Label(frame_Auto, text="de coupure clim la nuit : ", bg=self.COLOUR_FRAME).place(x=10, y=165)
        spinbox_tempext_cut=tk.Spinbox(frame_Auto,from_ = 0, to =30, width =2, textvariable=tempext)
        spinbox_tempext_cut.place(x=self.XFIELDSENTRY , y=155)  
        
         # Saisie de la puissance de démarrage
        tk.Label(frame_Auto, text="Excès de puissance pour ", bg=self.COLOUR_FRAME).place(x=10, y=190)
        tk.Label(frame_Auto, text="démarrer surchauffe ", bg=self.COLOUR_FRAME).place(x=10, y=210)
        spinbox_pow_start=tk.Spinbox(frame_Auto,from_ = 0, to =2000,increment=100, width =4, textvariable=powexcess_stop)  
        spinbox_pow_start.place(x=self.XFIELDSENTRY-10 , y=200)  
        
        # Saisie de la puissance d'arrêt
        tk.Label(frame_Auto, text="Excès de puissance pour ", bg=self.COLOUR_FRAME).place(x=10, y=235)
        tk.Label(frame_Auto, text="arrêter surchauffe ", bg=self.COLOUR_FRAME).place(x=10, y=255)
        spinbox_pow_stop=tk.Spinbox(frame_Auto,from_ = 0, to =2000, increment=100, width =4, textvariable=powexcess_start)  
        spinbox_pow_stop.place(x=self.XFIELDSENTRY-10 , y=245) 
        

def win_param_creation(root_win):
    COLOUR_BLUE = '#4065DE'
    COLOUR_WHITE = '#FFFFFF'
    COLOUR_RED = '#FF0000'
    win_param=tk.Toplevel(root_win)
       
    
    win_param.geometry("800x480+0+0")   # taille en pixels
    win_param.resizable(width=0, height=0)
    win_param.title("Paramètre")
    #--top boutons--
    button_exit = tk.Button(win_param, text="Back", width=13,
                                height=1 , command=win_param.destroy)
    button_exit.place(x=5, y=0)
    win_param.grab_set()    # permet à la fenêtre param 
                                # de recevoir les évènements.
    
    FramAutoBlue=FrameModeAuto(win_param,16,100, "Couleur Tempo bleu", COLOUR_BLUE,AutoModeDataBlue)
    FramAutoWhite=FrameModeAuto(win_param,245+16*2,100, "Couleur Tempo blanc", COLOUR_WHITE,AutoModeDataWhite)
    FramAutoRed=FrameModeAuto(win_param,490+16*3,100, "Couleur Tempo rouge",  COLOUR_RED,AutoModeDataRed)
    
		#trouver comment associer les variables associées à chaque widget.
		#Conrôler valeur int pout temp et valeur float pour . 		
	

