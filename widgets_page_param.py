import tkinter as tk 
from data_page import data_automode_blue, data_prog_blue, data_Hollidays 
from IHM_Global import *
from datetime import date,timedelta


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

        
        #============= La frame mode automatique ========= 
        
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
 
 
class FrameModeProg():
    LARG_FRAME = 255
    HAUT_FRAME = 360
    XFIELDSENTRY = 90
    OFFSET=105
    
    def __init__(self,window,posx=5,posy=20, texte = "couleur tempo", colour='#C0C0C0',progdata=data_prog_blue): 
        
        self.progdata=progdata
   
        #============= variables directement associées au Widget =========  
 
        self.temp_6_1 = tk.IntVar(window)        
        self.temp_6_2 = tk.IntVar(window)
        self.temp_6_3 = tk.IntVar(window)
        self.temp_6_4 = tk.IntVar(window)
        self.temp_8_1 = tk.IntVar(window)
        self.temp_8_2 = tk.IntVar(window)
        self.temp_8_3 = tk.IntVar(window)
        self.temp_8_4 = tk.IntVar(window)
        self.temp_10_1 = tk.IntVar(window) 
        self.temp_10_2 = tk.IntVar(window) 
        self.temp_10_3 = tk.IntVar(window) 
        self.temp_10_4 = tk.IntVar(window) 
        self.temp_15_1 = tk.IntVar(window) 
        self.temp_15_2 = tk.IntVar(window) 
        self.temp_15_3 = tk.IntVar(window) 
        self.temp_15_4 = tk.IntVar(window) 
        self.temp_17_1 = tk.IntVar(window) 
        self.temp_17_2 = tk.IntVar(window) 
        self.temp_17_3 = tk.IntVar(window)
        self.temp_17_4 = tk.IntVar(window) 
        self.temp_22_1 = tk.IntVar(window) 
        self.temp_22_2 = tk.IntVar(window) 
        self.temp_22_3 = tk.IntVar(window)
        self.temp_22_4 = tk.IntVar(window)
        
        self.tab_temp = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        
        #============= La frame mode programmation  ========= 
        
        # FRAME MODE PROG                   
        frame_prog = tk.Frame(window, width=self.LARG_FRAME,height=self.HAUT_FRAME,relief='sunken',bg=COLOUR_FRAME,bd=2)
        frame_prog.place(x=posx,y=posy+30)
        
        print("frame prog")
        print(frame_prog)
        
        label_prog= tk.Label(window, text=texte,bg=colour); 
        label_prog.place(x=posx, y=posy)
        # texte tourné à 90°
        canvas_salon=tk.Canvas(frame_prog, width = 160, height = 100)
        canvas_salon.place(x = self.XFIELDSENTRY+3 , y = 0)
            #texte anchor sw (sud ouest) = ref.
        canvas_salon.create_text(20,100,text = "Salon",angle = 90, anchor = "sw") 
        canvas_salon.create_text(60,100,text = "Salle à manger",angle = 90, anchor = "sw") 
        canvas_salon.create_text(100,100,text = "Entrée",angle = 90, anchor = "sw") 
        canvas_salon.create_text(140,100,text = "Couloir",angle = 90, anchor = "sw") 

        # Saisie des températures 
        templist=(0,17,18,19,20,21,22)
        label_temp_6_1 = tk.Label(frame_prog, text="Temp. 6h :", bg=COLOUR_FRAME).place(x=3, y=7+self.OFFSET)
        spinbox_t61=tk.Spinbox(frame_prog,values=templist, textvariable=self.temp_6_1, width=2).place(x=self.XFIELDSENTRY , y=5+self.OFFSET)
        spinbox_t62=tk.Spinbox(frame_prog,values=templist, textvariable=self.temp_6_2, width=2).place(x=self.XFIELDSENTRY+40 , y=5+self.OFFSET) 
        spinbox_t63=tk.Spinbox(frame_prog,values=templist, textvariable=self.temp_6_3, width=2).place(x=self.XFIELDSENTRY+80 , y=5+self.OFFSET) 
        spinbox_t64=tk.Spinbox(frame_prog,values=templist, textvariable=self.temp_6_4, width=2).place(x=self.XFIELDSENTRY+120 , y=5+self.OFFSET) 
        label_temp_8_1 = tk.Label(frame_prog, text="Temp. 8h :", bg=COLOUR_FRAME).place(x=3, y=47+self.OFFSET)
        spinbox_t81=tk.Spinbox(frame_prog,values=templist, textvariable=self.temp_8_1, width=2).place(x=self.XFIELDSENTRY , y=45+self.OFFSET) 
        spinbox_t82=tk.Spinbox(frame_prog,values=templist, textvariable=self.temp_8_2, width=2).place(x=self.XFIELDSENTRY+40 , y=45+self.OFFSET) 
        spinbox_t83=tk.Spinbox(frame_prog,values=templist, textvariable=self.temp_8_3, width=2).place(x=self.XFIELDSENTRY+80 , y=45+self.OFFSET) 
        spinbox_t84=tk.Spinbox(frame_prog,values=templist, textvariable=self.temp_8_4, width=2).place(x=self.XFIELDSENTRY+120 , y=45+self.OFFSET) 
        label_temp_10_1 = tk.Label(frame_prog, text="Temp. 10h :", bg=COLOUR_FRAME).place(x=3, y=87+self.OFFSET)
        spinbox_t101=tk.Spinbox(frame_prog,values=templist, textvariable=self.temp_10_1, width=2).place(x=self.XFIELDSENTRY , y=85+self.OFFSET) 
        spinbox_t102=tk.Spinbox(frame_prog,values=templist, textvariable=self.temp_10_2, width=2).place(x=self.XFIELDSENTRY+40 , y=85+self.OFFSET) 
        spinbox_t103=tk.Spinbox(frame_prog,values=templist, textvariable=self.temp_10_3, width=2).place(x=self.XFIELDSENTRY+80 , y=85+self.OFFSET) 
        spinbox_t104=tk.Spinbox(frame_prog,values=templist, textvariable=self.temp_10_4, width=2).place(x=self.XFIELDSENTRY+120 , y=85+self.OFFSET) 
        label_temp_15_1 = tk.Label(frame_prog, text="Temp. 15h :", bg=COLOUR_FRAME).place(x=3, y=127+self.OFFSET)
        spinbox_t151=tk.Spinbox(frame_prog,values=templist, textvariable=self.temp_15_1, width=2).place(x=self.XFIELDSENTRY , y=125+self.OFFSET) 
        spinbox_t152=tk.Spinbox(frame_prog,values=templist, textvariable=self.temp_15_2, width=2).place(x=self.XFIELDSENTRY+40 , y=125+self.OFFSET) 
        spinbox_t153=tk.Spinbox(frame_prog,values=templist, textvariable=self.temp_15_3, width=2).place(x=self.XFIELDSENTRY+80 , y=125+self.OFFSET) 
        spinbox_t154=tk.Spinbox(frame_prog,values=templist, textvariable=self.temp_15_4, width=2).place(x=self.XFIELDSENTRY+120 , y=125+self.OFFSET) 
        label_temp_17_1= tk.Label(frame_prog, text="Temp. 17h :", bg=COLOUR_FRAME).place(x=3, y=167+self.OFFSET)
        spinbox_t171=tk.Spinbox(frame_prog,values=templist, textvariable=self.temp_17_1, width=2).place(x=self.XFIELDSENTRY+0 , y=165+self.OFFSET) 
        spinbox_t172=tk.Spinbox(frame_prog,values=templist, textvariable=self.temp_17_2, width=2).place(x=self.XFIELDSENTRY+40 , y=165+self.OFFSET)
        spinbox_t173=tk.Spinbox(frame_prog,values=templist, textvariable=self.temp_17_3, width=2).place(x=self.XFIELDSENTRY+80 , y=165+self.OFFSET) 
        spinbox_t174=tk.Spinbox(frame_prog,values=templist, textvariable=self.temp_17_4, width=2).place(x=self.XFIELDSENTRY+120 , y=165+self.OFFSET)
        label_temp_22_1= tk.Label(frame_prog, text="Temp. 22h :", bg=COLOUR_FRAME).place(x=3, y=207+self.OFFSET)
        spinbox_t221=tk.Spinbox(frame_prog,values=templist, textvariable=self.temp_22_1, width=2).place(x=self.XFIELDSENTRY+0 , y=205+self.OFFSET) 
        spinbox_t222=tk.Spinbox(frame_prog,values=templist, textvariable=self.temp_22_2, width=2).place(x=self.XFIELDSENTRY+40 , y=205+self.OFFSET)
        spinbox_t223=tk.Spinbox(frame_prog,values=templist, textvariable=self.temp_22_3, width=2).place(x=self.XFIELDSENTRY+80 , y=205+self.OFFSET) 
        spinbox_t224=tk.Spinbox(frame_prog,values=templist, textvariable=self.temp_22_4, width=2).place(x=self.XFIELDSENTRY+120 , y=205+self.OFFSET) 
        
        #============= chargement des variables associées au Widget ========= 
  
        self.temp_6_1.set(self.progdata.TempPerHour[0])
        self.temp_6_2.set(self.progdata.TempPerHour[1])
        self.temp_6_3.set(self.progdata.TempPerHour[2])
        self.temp_6_4.set(self.progdata.TempPerHour[3])
        self.temp_8_1.set(self.progdata.TempPerHour[4])
        self.temp_8_2.set(self.progdata.TempPerHour[5])
        self.temp_8_3.set(self.progdata.TempPerHour[6])
        self.temp_8_4.set(self.progdata.TempPerHour[7])
        self.temp_10_1.set(self.progdata.TempPerHour[8])
        self.temp_10_2.set(self.progdata.TempPerHour[9])
        self.temp_10_3.set(self.progdata.TempPerHour[10])
        self.temp_10_4.set(self.progdata.TempPerHour[11])
        self.temp_15_1.set(self.progdata.TempPerHour[12])
        self.temp_15_2.set(self.progdata.TempPerHour[13])
        self.temp_15_3.set(self.progdata.TempPerHour[14])
        self.temp_15_4.set(self.progdata.TempPerHour[15])
        self.temp_17_1.set(self.progdata.TempPerHour[16])
        self.temp_17_2.set(self.progdata.TempPerHour[17])
        self.temp_17_3.set(self.progdata.TempPerHour[18])
        self.temp_17_4.set(self.progdata.TempPerHour[19])
        self.temp_22_1.set(self.progdata.TempPerHour[20])
        self.temp_22_2.set(self.progdata.TempPerHour[21])
        self.temp_22_3.set(self.progdata.TempPerHour[22])
        self.temp_22_4.set(self.progdata.TempPerHour[23])   
        
    def get_tab_temp(self):
        self.tab_temp[0] = self.temp_6_1.get()
        self.tab_temp[1] = self.temp_6_2.get()
        self.tab_temp[2] = self.temp_6_3.get()
        self.tab_temp[3] = self.temp_6_4.get()
        self.tab_temp[4] = self.temp_8_1.get()
        self.tab_temp[5] = self.temp_8_2.get()
        self.tab_temp[6] = self.temp_8_3.get()
        self.tab_temp[7] = self.temp_8_4.get()
        self.tab_temp[8] = self.temp_10_1.get()
        self.tab_temp[9] = self.temp_10_2.get()
        self.tab_temp[10] = self.temp_10_3.get()
        self.tab_temp[11] = self.temp_10_4.get()
        self.tab_temp[12] = self.temp_15_1.get()
        self.tab_temp[13] = self.temp_15_2.get()
        self.tab_temp[14] = self.temp_15_3.get()
        self.tab_temp[15] = self.temp_15_4.get()
        self.tab_temp[16] = self.temp_17_1.get()
        self.tab_temp[17] = self.temp_17_2.get()
        self.tab_temp[18] = self.temp_17_3.get()
        self.tab_temp[19] = self.temp_17_4.get()
        self.tab_temp[20] = self.temp_22_1.get()
        self.tab_temp[21] = self.temp_22_2.get()
        self.tab_temp[22] = self.temp_22_3.get()
        self.tab_temp[23] = self.temp_22_4.get()
        return self.tab_temp
        

class FrameModeHollydaysDate():
    LARG_FRAME = 260
    HAUT_FRAME = 80
    XFIELDSENTRY = 130
    XSHIFT_FRAMETEMP = 0
    YSHIFT_FRAMETEMP = 150
    XFIELDSENTRYTEMP = 250
    def __init__(self,window,posx = 5,posy = 20, hollydays_data = data_Hollidays): 
        
        # =========  FRAME  ============== 
        label_frame= tk.Label(window, text="saisir le jour de rentrée de vacances : ").place(x=posx, y=posy)                  
        frame = tk.Frame(window, width=self.LARG_FRAME,height=self.HAUT_FRAME,relief='sunken',bg=COLOUR_FRAME,bd=2)
        frame.place(x=posx,y=posy+30)
        
        # ============ variables directement associées au Widget ==== 
        
        self.deltaday = tk.IntVar(window)
        self.holly_hour = tk.IntVar(window)
  
        self.holly_mode = tk.StringVar(window) 
        self.holly_tempminblue = tk.IntVar(window) 
        self.holly_tempminwhite = tk.IntVar(window)
        self.holly_tempminred = tk.IntVar(window)
        
        #gestion du temps
        self.today = date.today()
        self.arrival = date.today()
        self.date_arrivee_str=str(self.arrival)
        
        #============= La frame vacance date arrivée ========= 
        tk.Label(frame, text="jour d'arrivée :", bg=COLOUR_FRAME).place(x=5, y=10)
        spinbox_arrival=tk.Spinbox(frame,values=(-1,+1), textvariable=self.deltaday , width=2,\
                    bg=COLOUR_FRAME, command = self.update_arrival)
        spinbox_arrival.place(x=self.XFIELDSENTRY+83 , y=10)
        self.label_arrivaldate = tk.Label(frame, text="   cliquer sur ...", width=11,bg="white")
        self.label_arrivaldate.place(x=self.XFIELDSENTRY, y=11)
        tk.Label(frame, text="Heure d'arrivée :", bg=COLOUR_FRAME).place(x=5, y=35)
        spinbox_arrival=tk.Spinbox(frame,from_ =0, to_ = 23, textvariable=self.holly_hour , width=2)
        spinbox_arrival.place(x=self.XFIELDSENTRY , y=35)
        tk.Label(frame, text="h", bg=COLOUR_FRAME).place(x=self.XFIELDSENTRY+40, y=37)
        

    
        #============= La frame vacance températures d'arrivée ========= 
        templist=(0,10,11,12,13,14,15,16,17)
        # =========  FRAME  ============== 
        tk.Label(window, text="saisir les températures d'arrivées : ").place(x=posx+self.XSHIFT_FRAMETEMP, y=posy+self.YSHIFT_FRAMETEMP)                  
        frame_temp = tk.Frame(window, width=self.LARG_FRAME*2,height=self.HAUT_FRAME*2,relief='sunken',bg=COLOUR_FRAME,bd=2)
        frame_temp.place(x=posx+self.XSHIFT_FRAMETEMP,y=posy+self.YSHIFT_FRAMETEMP+30)
        tk.Label(frame_temp, text="Mode journée veille d'arrivée :", bg=COLOUR_FRAME).place(x=5, y=10)
        tk.Spinbox(frame_temp,values=(MODE_DICTIO[HMI_Mode_Auto],MODE_DICTIO[HMI_Mode_Program]), textvariable=self.holly_mode ,width=12).place(x=self.XFIELDSENTRYTEMP,y=10)      
        tk.Label(frame_temp, text="Température hors gel bleu :", bg=COLOUR_FRAME).place(x=5, y=35)
        tk.Spinbox(frame_temp,values=templist, textvariable=self.holly_tempminblue , width=2).place(x=self.XFIELDSENTRYTEMP,y=35)
        tk.Label(frame_temp, text="Température hors gel blanc :", bg=COLOUR_FRAME).place(x=5, y=60)
        tk.Spinbox(frame_temp,values=templist, textvariable=self.holly_tempminwhite , width=2).place(x=self.XFIELDSENTRYTEMP,y=60)
        tk.Label(frame_temp, text="Température hors gel rouge :", bg=COLOUR_FRAME).place(x=5, y=85)  
        tk.Spinbox(frame_temp,values=templist, textvariable=self.holly_tempminred , width=2).place(x=self.XFIELDSENTRYTEMP,y=85)      
    
        #============= chargement des variables associées au Widget ========= 
        if hollydays_data.arrivaldate <= date.today() : # rien n'a été modifié ou la date d'arrivée anciennement écrite n'est plus valide
            self.label_arrivaldate.config(text=   "cliquer sur ...")
        else :
            self.arrival=hollydays_data.arrivaldate           
            self.label_arrivaldate.config(text=str(self.arrival))
            self.holly_hour.set(hollydays_data.arrivalhour)
        
        self.holly_mode.set(MODE_DICTIO[hollydays_data.hollyarrival_mode])
        self.holly_tempminblue.set(hollydays_data.hollytempmin_blue)
        self.holly_tempminwhite.set(hollydays_data.hollytempmin_white)
        self.holly_tempminred.set(hollydays_data.hollytempmin_red)
    
    
    
    def update_arrival(self):   
        td= timedelta(self.deltaday.get())
        self.today = date.today() #réactualisation pour éviter les 12 coups de minuits...
        
        self.arrival = self.arrival + td
        if self.arrival<self.today :
            self.arrival=self.today
         
        self.label_arrivaldate.config(text=str(self.arrival))
   
        
    def get_arrivaldate(self):
        return(self.arrival) 
        
    def get_arrivalhour(self):
        return(self.holly_hour.get()) 

    def get_hollymode(self):
        value = HMI_Mode_Auto
        if self.holly_mode.get() == MODE_DICTIO[HMI_Mode_Program]:
            value = HMI_Mode_Program
        return(value) 
        
    def get_holly_tempminblue(self):
        return(self.holly_tempminblue.get())
        
    def get_holly_tempminwhite(self):
        return(self.holly_tempminwhite.get())

    def get_holly_tempminred(self):
        return(self.holly_tempminred.get())

        
        
