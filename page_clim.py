import tkinter as tk 
from IHM_Global import *
from data_page import Data_Clim_Salon,Data_Clim_SaM, Data_Clim_Entree, \
                      Data_Clim_Couloir,Data_Ext

class FrameClim():
    LARG_FRAME_PIX = 380
    HAUT_FRAME_PIX = 140

    
    def __init__(self,window,posx=5,posy=20, RmDvData=Data_Clim_Salon): 
                  
        # ==========    FRAME climatisation     ============        
        self.frame_RmDv = tk.Frame(window, width=self.LARG_FRAME_PIX , height=self.HAUT_FRAME_PIX, borderwidth=3,relief='groove',bg=COLOUR_FRAME)
        self.frame_RmDv.place(x=posx, y=posy)
        
        self.label_temp=tk.Label(self.frame_RmDv, text="Température : "+str(round(RmDvData.Temperature,1))+"°C",bg=COLOUR_FRAME)
        self.label_temp.place(x=5, y=5)
        
        self.label_NewTempSet=tk.Label(self.frame_RmDv, text="Cmde Actuelle : "+RmDvData.NewTempSet ,bg=COLOUR_FRAME)
        self.label_NewTempSet.place(x=5, y=25)
 
        self.label_Repcmde=tk.Label(self.frame_RmDv, text="Cmde non répétée : "+RmDvData.LastTempSetBeforeNoCmd ,bg=COLOUR_FRAME)
        self.label_Repcmde.place(x=5, y=45)       

        self.label_BoostToken=tk.Label(self.frame_RmDv, text="Boost Token : "+ str(RmDvData.BoostToken) ,bg=COLOUR_FRAME)
        self.label_BoostToken.place(x=5, y=65)  

        self.label_Status=tk.Label(self.frame_RmDv, text="Status : "+ str(RmDvData.Status) ,bg=COLOUR_FRAME)
        self.label_Status.place(x=140, y=65)  


        self.label_Stamp=tk.Label(self.frame_RmDv, text="Stamp : "+ RmDvData.time_date + " " + RmDvData.time_hour,bg=COLOUR_FRAME)
        self.label_Stamp.place(x=5, y=85)  
        
        self.label_NextInt=tk.Label(self.frame_RmDv, text="Prochaine transmission : "+ RmDvData.time_Delay ,bg=COLOUR_FRAME)
        self.label_NextInt.place(x=5, y=105)  
        

class FrameExt():
    LARG_FRAMEEXT_PIX = 630
    HAUT_FRAMEEXT_PIX = 50
    
    def __init__(self,window,posx=5,posy=20): 
        # ==========    FRAME RmDvExt    ============        
        self.frame_RmDv = tk.Frame(window, width=self.LARG_FRAMEEXT_PIX , height=self.HAUT_FRAMEEXT_PIX, borderwidth=3,relief='groove',bg=COLOUR_FRAME)
        self.frame_RmDv.place(x=posx, y=posy)
        
        self.label_temp=tk.Label(self.frame_RmDv, text="Température : "+str(round(Data_Ext.Temperature,1))+"°C",bg=COLOUR_FRAME)
        self.label_temp.place(x=5, y=3)
        
        self.label_Stamp=tk.Label(self.frame_RmDv, text="Stamp : "+ Data_Ext.time_date + " " + Data_Ext.time_hour,bg=COLOUR_FRAME)
        self.label_Stamp.place(x=300, y=3) 
        
        self.label_NextInt=tk.Label(self.frame_RmDv, text="Prochaine transmission :" + Data_Ext.time_Delay ,bg=COLOUR_FRAME)
        self.label_NextInt.place(x=300, y=23)  
        
        self.label_Status=tk.Label(self.frame_RmDv, text="Status : "+ str(Data_Ext.Status) ,bg=COLOUR_FRAME)
        self.label_Status.place(x=5, y=23) 


def win_clim_creation(root_win):
	win_clim=tk.Toplevel(root_win)
	win_clim.geometry("800x480+0+0")  # taille en pixels
	win_clim.resizable(width=0, height=0)
	win_clim.title("Informations climatisations :")
	# --top boutons--
	button_exit = tk.Button(win_clim, text="Back", width=13,
                          height=1 , command=win_clim.destroy)
	button_exit.place(x=5, y=0)
	win_clim.grab_set() 

    #les titres 
	label_Salon=tk.Label(win_clim, text="Salon :",bg=COLOUR_WHITE)
	label_Salon.place(x=300, y= 40-20)
	label_SaM=tk.Label(win_clim, text="Salle à manger :",bg=COLOUR_WHITE)
	label_SaM.place(x=650, y= 40-20)
	label_Entree=tk.Label(win_clim, text="Entrée :",bg=COLOUR_WHITE)
	label_Entree.place(x=300, y= 210-20)
	label_Couloir=tk.Label(win_clim, text="Couloir :",bg=COLOUR_WHITE)
	label_Couloir.place(x=650, y= 210-20)
	label_Ext=tk.Label(win_clim, text="Module extérieur :",bg=COLOUR_WHITE)
	label_Ext.place(x=5, y= 370)
	
	#frames 
	frame_ClimSalon=FrameClim(win_clim,5,40,Data_Clim_Salon)
	frame_ClimSaM=FrameClim(win_clim,400,40,Data_Clim_SaM)
	frame_ClimEntree=FrameClim(win_clim,5,210,Data_Clim_Entree)
	frame_ClimCouloir=FrameClim(win_clim,400,210,Data_Clim_Couloir)
	frame_Ext = FrameExt(win_clim,150,360)
