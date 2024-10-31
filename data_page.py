from IHM_Global import *
from datetime import date,timedelta
import struct as st 

# === classe qui permettra d'instancier les 4 clim de la maison ===
class DataClim:
    
    # === les attributs d'une climatisation ===
    def __init__(self):
        self.Temperature = 0.0              #float
        self.NewTempSet = "Arrêt"            #char
        self.LastTempSetBeforeNoCmd ="Arrêt" #char
        self.Status = "Pas de Warning"     #char
        self.BoostToken = 0                 #char
        self.time_date = "00/00/00"         # string ex 01/01/20
        self.time_hour = "00:00:00"         # string ex 12:48:51               
        self.time_Delay = "00j 00:00:00"     # string ex 03:12:48:51
                                            # pour 3jour 12h 48mn 51sec
    
        
    def Update(self,SerialList):
        #temperature
        tempStr=SerialList[0]+SerialList[1]+SerialList[2]+SerialList[3]
        self.Temperature=st.unpack("<f", tempStr)[0]
        #NexTemp, pos 4
        self.NewTempSet = TempSet2Str(st.unpack("B", SerialList[4])[0])
        
        #lasttmp cmde before nocmde, pos 5
        self.LastTempSetBeforeNoCmd = TempSet2Str(st.unpack("B", SerialList[5])[0])
        #Status, pos 6
        self.Status = Status2Str(st.unpack("B", SerialList[6])[0])
        #Status, pos 7
        self.BoostToken = st.unpack("B", SerialList[7])[0]
        #Stamp clim
        tempStr=SerialList[8]+SerialList[9];sec = st.unpack("<H", tempStr)[0]
        tempStr=SerialList[10]+SerialList[11];minute = st.unpack("<H", tempStr)[0]
        tempStr=SerialList[12]+SerialList[13]; heure = st.unpack("<H", tempStr)[0]
        tempStr=SerialList[14]+SerialList[15];jour = st.unpack("<H", tempStr)[0]
        tempStr=SerialList[16]+SerialList[17];mois = st.unpack("<H", tempStr)[0]
        tempStr=SerialList[18]+SerialList[19];annee = st.unpack("<H", tempStr)[0]
        self.time_hour=str(heure)+":"+str(minute)+":"+str(sec)
        self.time_date=str(jour)+"/"+str(mois)+"/"+str(annee)
        #intervalle 
        tempStr=SerialList[20]+SerialList[21]+SerialList[22]+SerialList[23]
        total_sec = st.unpack("<I", tempStr)[0]
        jour = total_sec // (3600*24)
        reste = total_sec  - jour*3600*24
        heure = reste //3600
        reste = reste-heure*3600
        minute = reste//60
        reste = reste-minute*60
        seconde = reste
        self.time_Delay =str(jour)+"j,"+str(heure)+":"+str(minute)+":"+str(seconde)
        
        print(self.time_hour)
        print(self.time_date)
        print(self.time_Delay)
        print(self.Temperature)
        print(self.NewTempSet)
        print(self.LastTempSetBeforeNoCmd)
        print(self.Status)
        print(self.BoostToken)


# === classe qui regroupe les variables de la homepage ===

class DataHomePage:
    

        # ==== les attribut de la Home Page ===
    def __init__(self):
        # -- Mode --
        self.mode = HMI_Mode_Program  # string Choix possibles :
        # HMI_Mode_Off , HMI_Mode_Auto ,HMI_Mode_Program ,HMI_Mode_Hollidays 
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
        
        # hollidays 16 octets
        self.Temp_ArrRedWhiteBlue = 0x12121212  # 4 octets température arrivée/rouge/blanc/bleu = 18°C pour tous
        self.ArrivalDateSec = 0                # short int 2octets
        self.ArrivalDateMin = 0                # short int 2octets
        self.ArrivalDateHour = 0               # short int 2octets
        self.ArrivalDateDay = 1                # short int 2octets
        self.ArrivalDateMonth = 1              # short int 2octets
        self.ArrivalDateYear = 2024            # short int 2octets 
       
        
        #sortie message
        self.message = " "
        


class DataParamAuto:
    def __init__(self):
        self.temp_min_ext=12
        self.pow_excess_start=100
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



class DataParamProg:
    def __init__(self):

        
        #self.TempPerHour = {"6h":temp_6h,"8h":temp_8h,"10h":temp_10h,"15h":temp_10h,"17h":temp_10h,"22h":temp_22h} 
        self.TempPerHour =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        # 17 10 24 modifié 17 par 19 en état init
    def update(self,temp_per_hour):
        for i in range(0,24):
            self.TempPerHour[i]=temp_per_hour[i]
            
        
class DataParamHollidays:
    def __init__(self):
        
        self.hollyarrival_mode = HMI_Mode_Auto
        self.hollytempmin_blue = 10
        self.hollytempmin_white = 10
        self.hollytempmin_red = 10
        self.arrivaldate = date.today()  
        self.arrivalhour = 0   
        
    def update(self, arrivaldate, arrivalhour, hollyarrival_mode, \
                hollytempmin_blue, hollytempmin_white, hollytempmin_red ):
                    
        self.arrivaldate = arrivaldate
        self.arrivalhour= arrivalhour
        self.hollyarrival_mode = hollyarrival_mode
        self.hollytempmin_blue = hollytempmin_blue
        self.hollytempmin_white = hollytempmin_white
        self.hollytempmin_red = hollytempmin_red    

def TempSet2Str(cmde):
    LocalStr=""
    if (cmde == Chaud_18_VanBas_FanAuto) :LocalStr="18°C Volets Bas, Fan auto"
    elif  (cmde == Chaud_19_VanBas_FanAuto) :LocalStr="19°C Volets Bas, Fan auto"
    elif  (cmde == Chaud_20_VanBas_FanAuto) :LocalStr="20°C Volets Bas, Fan auto"
    elif  (cmde == Chaud_21_VanBas_FanAuto) :LocalStr="21°C Volets Bas, Fan auto"
    elif  (cmde == Chaud_22_VanBas_FanAuto) :LocalStr="22°C Volets Bas, Fan auto"
    elif  (cmde == Chaud_23_VanBas_FanAuto) :LocalStr="23°C Volets Bas, Fan auto"
    elif  (cmde == NoCommandToSend) :LocalStr="Pas de nouvelle commande..."
    elif  (cmde == Stop) :LocalStr="Arrêt"
    else : LocalStr="Code cmde erroné"
    return LocalStr

def Status2Str(status):
    LocalStr=""
    if (status == Status_NoWarning) :LocalStr="Pas de Warning"
    elif  (status == Status_Trial_2 ) :LocalStr="Transmission au 2eme essai"
    elif  (status == Status_Trial_3 ) :LocalStr="Transmission au 3eme essai"
    elif  (status == Status_Error_TempI2C) :LocalStr="Erreur capteur I2C"
    elif  (status == Status_Error_NewTempSetNotReceived ) :
        LocalStr="La téléco n'a pas reçu la cmde"
    elif  (status == Status_NoStatusReceived) :LocalStr="SmGw n'a pas reçu le statut teleco"
    else : LocalStr="Code status erroné"                
    return LocalStr



# Création des datas associées à la fenêtre
data_homepage=DataHomePage()
data_automode_blue=DataParamAuto()
data_automode_white=DataParamAuto()
data_automode_red=DataParamAuto()
data_prog_blue = DataParamProg()
data_prog_white = DataParamProg()
data_prog_red = DataParamProg()
data_Hollidays = DataParamHollidays()

#les clim
Clim_Salon=DataClim()
Clim_SaM=DataClim()
Clim_Entree=DataClim()
Clim_Couloir=DataClim()

# =================== Test unitaire=================================  
if __name__ == "__main__" :
    MyPage=DataHomePage()
    print(MyPage.mode)
    MyPage.mode=HMI_Mode_Off
    print(MyPage.mode)
    print(MyPage.ClimSalon.id)


