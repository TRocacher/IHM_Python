from IHM_Global import *

# === classe qui permettra d'instancier les 4 clim de la maison ===
class Climatisation:
    
    # === les attributs d'une climatisation ===
    def __init__(self,Id="Null"):
        self.id = Id # string Choix possibles : "Salon", 
        # "SalleAManger", "Entree", "Couloir"
        
        # -- date/heure dernier relevé/set --
        self.time_date = "00/00/00" # string ex 01/01/20	
        self.time_hour = "00:+00:00" # string ex 12:48:51  
        # -- données de température locale --
        self.temp_mesuree = 0.0 # float °C
        self.temp_set = 0.0 # float °C
        
        

# === classe qui regroupe les variables de la homepage ===

class DataHomePage:
    

        # ==== les attribut de la Home Page ===
    def __init__(self):
        # -- Mode --
        self.mode = HMI_Mode_Auto # string Choix possibles "Off" "Auto", "Eco", 
        # -- Tempo --
        self.tempo = Tempo_NoConnection
        self.tempostring=["Pb internet","Bleu","Blanc","Rouge"]
        self.tempobg=[COLOUR_FRAME,COLOUR_BLUE,COLOUR_WHITE,COLOUR_RED]
        # -- option --
        self.mode_opt_coupure_nuit = 0
        self.mode_opt_prioVE = 0
        self.mode_opt_repeat_set = 0
        # -- Infos puissance --
        self.pow_tot = 0.0 # float W
        self.pow_inv = 0.0 # float W
        self.pow_l1home = 0.0 # float W
        self.pow_l1 = 0.0 # float W
        self.pow_l2 = 0.0 # float W
        self.pow_l3 = 0.0 # float W
        self.pow_dispo = 0.0 # float W
        self.pow_temoin ="red"
        # -- Infos date/heure --
        self.time_date = "JourSemaine Jour mois année" 
        # string ex Monday 1 Oct 2023
        self.time_hour = "00:00:00" 
        # string ex 12:48:51

        # program, à décliner en une classe spécifique et 3 objets
        self.TempPerHour=[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18]   
        

        # hollidays 16 octets
        self.Temp_ArrRedWhiteBlue = 0x12121212  # 4 octets température arrivée/rouge/blanc/bleu = 18°C pour tous
        self.ArrivalDateSec = 0                # short int 2octets
        self.ArrivalDateMin = 0                # short int 2octets
        self.ArrivalDateHour = 0               # short int 2octets
        self.ArrivalDateDay = 1                # short int 2octets
        self.ArrivalDateMonth = 1              # short int 2octets
        self.ArrivalDateYear = 2024            # short int 2octets    
           
    
        # **Définition des 4 climatisations **
        self.ClimSalon=Climatisation("Salon")
        self.ClimSalon=Climatisation("SalleAManger")
        self.ClimSalon=Climatisation("Entree")
        self.ClimSalon=Climatisation("Couloir")


class DataParamAuto:
    def __init__(self):
        self.temp_min_ext=12
        self.pow_excess_start=500
        self.pow_excess_stop=0
        self.clim_prio=[1,2,3,4]
        self.temp_min_HC=18
        self.temp_min_HP=19
        
    def update(self,tempminext,powexcessstart,powerexcessstop, \
        tempminhc,tempminhp,climprio):
        self.temp_min_ext = tempminext
        self.pow_excess_start = powexcessstart
        self.pow_excess_stop = powerexcessstop
        self.temp_min_HC = tempminhc
        self.temp_min_HP = tempminhp
        self.clim_prio = climprio


        


# Création des datas associées à la fenêtre
data_homepage=DataHomePage()
data_automode_blue=DataParamAuto()
data_automode_white=DataParamAuto()
data_automode_red=DataParamAuto()

# =================== Test unitaire=================================  
if __name__ == "__main__" :
    MyPage=DataHomePage()
    print(MyPage.mode)
    MyPage.mode=HMI_Mode_Off
    print(MyPage.mode)
    print(MyPage.ClimSalon.id)


