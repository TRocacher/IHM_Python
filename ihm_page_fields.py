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

class HomePageData:
    

        # ==== les attribut de la Home Page ===
    def __init__(self):
        # -- Mode --
        self.mode = "Off" # string Choix possibles "Off" "Auto", "Eco", 
        # "Vacances"
        self.mode_opt_coupure_nuit = "0" # string Choix  : "0", "1"
        self.mode_opt_prioVE = "0" # string Choix : "0", "1"
        self.mode_opt_repeat_set = "0" # string Choix  : "0", "1"
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
        self.time_dateSTM32 = "00/00/00" # string ex 01/01/20	
        self.time_date = "JourSemaine Jour mois année" 
        # string ex Monday 1 Oct 2023
        self.time_hour = "00:00:00" 
        # string ex 12:48:51
        # -- Infos enedis, météo, temp exterieur--
        self.edf_tempo = "Bleu"
        # string Choix possibles "Bleu" "Blanc", "Rouge"
        self.prev_meteo = "degage" 
        # string Choix possibles "degage", "couvert"
        self.temp_ext = 0.0 # float °C
        # -- Warning stème --
        self.warning = "RAS" 
        # string Choix possibles "RAS" "Avertissement" "Erreur"
    
        # ** les attribut de la page vacances **
        self.vac_dep_date =  "00/00/00" # string ex 01/01/20	
        self.vac_dep_hour = "00:00:00" # string ex 12:48:51 
        self.vac_ret_date =  "00/00/00" # string ex 01/01/20	
        self.vac_ret_hour = "00:00:00" # string ex 12:48:51 
        self.set_temp_min = 15.0 # float °C
        self.set_temp_ret = 19.0 # float °C  

        # **Définition des 4 climatisations **
        self.ClimSalon=Climatisation("Salon")
        self.ClimSalon=Climatisation("SalleAManger")
        self.ClimSalon=Climatisation("Entree")
        self.ClimSalon=Climatisation("Couloir")


class ParamPageAutoModeData:
    def __init__(self):
        self.temp_min_ext=12
        self.pow_excess_start=500
        self.pow_excess_stop=0
        self.clim_prio=[1,2,3,4]
        self.temp_min_HC=18
        self.temp_min_HP=19
        
    def update(self,tempminext,powexcessstart,powerexcessstop, \
        climprio,tempminhc,tempminhp):
        self.temp_min_ext = tempminext
        self.pow_excess_start = powexcessstart
        self.pow_excess_stop = powerexcessstop
        self.clim_prio = climprio
        self.temp_min_HC = tempminhc
        self.temp_min_HP = tempminhp


        
        

# Création des datas associées à la fenêtre
PageData=HomePageData()
AutoModeDataBlue=ParamPageAutoModeData()
AutoModeDataWhite=ParamPageAutoModeData()
AutoModeDataRed=ParamPageAutoModeData()

# =================== Test unitaire=================================  
if __name__ == "__main__" :
    MyPage=HomePageData()
    print(MyPage.mode)
    MyPage.mode="Auto"
    print(MyPage.mode)
    print(MyPage.ClimSalon.id)


