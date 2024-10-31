import tkinter as tk 
from IHM_Global import *
from data_page import Clim_Salon,Clim_SaM,Clim_Entree,Clim_Couloir

class FrameClim():
    LARG_FRAME_PIX = 380
    HAUT_FRAME_PIX = 140

    
    def __init__(self,window,posx=5,posy=20, RmDvData=Clim_Salon): 
         
        # ==========    FRAME climatisation     ============        
        self.frame_RmDv = tk.Frame(window, width=self.LARG_FRAME_PIX , height=self.HAUT_FRAME_PIX, borderwidth=3,relief='groove',bg=COLOUR_FRAME)
        self.frame_RmDv.place(x=posx, y=posy)
        
        self.label_temp=tk.Label(self.frame_RmDv, text="Température : "+str(round(RmDvData.Temperature,1))+"°C",bg=COLOUR_FRAME)
        self.label_temp.place(x=5, y=5)
        
        self.label_NewTempSet=tk.Label(self.frame_RmDv, text="Cmde Actuelle : "+RmDvData.NewTempSet ,bg=COLOUR_FRAME)
        self.label_NewTempSet.place(x=5, y=25)
 
        self.label_TempSetBefore=tk.Label(self.frame_RmDv, text="Cmde non répétée : "+RmDvData.LastTempSetBeforeNoCmd ,bg=COLOUR_FRAME)
        self.label_TempSetBefore.place(x=5, y=45)       

        self.label_BoostToken=tk.Label(self.frame_RmDv, text="Boost Token : "+ str(RmDvData.BoostToken) ,bg=COLOUR_FRAME)
        self.label_BoostToken.place(x=5, y=65)  

        self.label_BoostToken=tk.Label(self.frame_RmDv, text="Stamp :"+ RmDvData.time_date + " " + RmDvData.time_hour,bg=COLOUR_FRAME)
        self.label_BoostToken.place(x=5, y=85)  
        
        self.label_BoostToken=tk.Label(self.frame_RmDv, text="Intervalle prochain :"+ RmDvData.time_Delay ,bg=COLOUR_FRAME)
        self.label_BoostToken.place(x=5, y=105)  
        
        # self.label_powl1home=tk.Label(self.frame_pow, text="Puissance L1 maison : "+str(data_homepage.pow_l1home)+"W",bg=COLOUR_FRAME)
        # self.label_powl1home.place(x=10, y=45)       

        # self.label_powl1=tk.Label(self.frame_pow, text="Puissance L1  : "+str(data_homepage.pow_l1)+"W", bg=COLOUR_FRAME)
        # self.label_powl1.place(x=10, y=65) 

        # self.label_powl2=tk.Label(self.frame_pow, text="Puissance L2  : "+str(data_homepage.pow_l2)+"W", bg=COLOUR_FRAME)
        # self.label_powl2.place(x=10, y=85) 
 
        # self.label_powl3=tk.Label(self.frame_pow, text="Puissance L3  : "+str(data_homepage.pow_l3)+"W", bg=COLOUR_FRAME)
        # self.label_powl3.place(x=10, y=105) 
        
        # self.temoin_pow=tk.Canvas(self.frame_pow, bg=COLOUR_FRAME,height=24, width=24,highlightthickness=0)
        # self.temoin_pow.place(x=220,y=5)
        # self.temoin=self.temoin_pow.create_oval(2,2,22,22,fill="red")




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

	frame_ClimSalon=FrameClim(win_clim,5,50,Clim_Salon)
	frame_ClimSalon=FrameClim(win_clim,400,50,Clim_SaM)
	frame_ClimSalon=FrameClim(win_clim,5,200,Clim_Entree)
	frame_ClimSalon=FrameClim(win_clim,400,200,Clim_Couloir)
