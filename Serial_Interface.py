# === classes de données directement liées au µC ===

from IHM_Global import *
from time import strftime
import time as _time
from datetime import date,timedelta
import serial
from data_page import data_homepage, data_automode_blue,\
                        data_automode_white, data_automode_red,\
                        data_prog_blue, data_prog_white,\
                        data_prog_red, data_Hollidays,\
                        Data_Clim_Salon,Data_Clim_SaM,\
                        Data_Clim_Entree,Data_Clim_Couloir,Data_Ext
                        
import struct as st # pour envoyer float, cad d'abord passer en byte

           
                
class DFH_CentralData:
    def __init__(self): 
        self.SerialStatus = Serial_NoError
        # 92 octets en tout
        # Time struct 12 octets
        self.Sec = 0                # short int 2octets
        self.Min = 0                # short int 2octets
        self.Hour = 0               # short int 2octets
        self.Day = 1                # short int 2octets
        self.Month = 1              # short int 2octets
        self.Year = 2024            # short int 2octets      
        # HMI mode 4 octets
        self.mode = HMI_Mode_Auto   # int 4octets   
        # mode auto 20 octets
        self.TempMinExt = 7.0       # float 4 octets
        self.PowExcessStart = 500.0 # float 4 octets
        self.PowExcessStop = 0.0    # float 4 octets
        self.ClimPrio = [1,2,3,4]   # 4 octets
        self.TempMinHC = 18         #short int 2 octets
        self.TempMinHP = 18         #short int 2 octets
        # mode program 24 bytes
        self.TempPerHour=[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18]
        # hollidays 16 octets
        self.hollymode = HMI_Mode_Auto
        self.TempHG_bleu = 10
        self.TempHG_blanc = 10
        self.TempHG_rouge = 10
        self.ArrivalDateSec = 0                # short int 2octets
        self.ArrivalDateMin = 0                # short int 2octets
        self.ArrivalDateHour = 0               # short int 2octets
        self.ArrivalDateDay = 1                # short int 2octets
        self.ArrivalDateMonth = 1              # short int 2octets
        self.ArrivalDateYear = 2024            # short int 2octets   
        #power and options 16 octets2
        self.PowExcess = 0.0                   # float 4 octets
        self.PowL1_Home = 0.0                  # float 4 octets
        self.PowInverter = 0.0                 # float 4 octets    
        self.Option = [0x1,0x2,0x3,0x4]     #  4 octets 
 
        # 92 octets en tout
        
        self.serial_dataparamauto = data_automode_blue
        self.serial_dataparamprog = data_prog_blue
 
    def update_bufferdata(self):
        # Time struct 12 octets
        self.Sec = int(strftime('%S'))
        self.Min = int(strftime('%M'))
        self.Hour = int(strftime('%H'))
        self.Day = int(strftime('%d'))
        self.Month = int(strftime('%m'))
        self.Year = int(strftime('%Y'))
            
        # HMI mode 4 octets
        self.mode = data_homepage.mode
            
        # mode auto 20 octets
        # si la couleur n'est pas définie (non accès internet), on evoie une couleur rouge
        if data_homepage.tempo == Tempo_Bleu:
            self.serial_dataparamauto = data_automode_blue
            self.serial_dataparamprog = data_prog_blue
        elif data_homepage.tempo == Tempo_Blanc:
            self.serial_dataparamauto = data_automode_white
            self.serial_dataparamprog = data_prog_white
        else :
            self.serial_dataparamauto=data_automode_red
            self.serial_dataparamprog = data_prog_red
                
        self.TempMinExt = float(self.serial_dataparamauto.temp_min_ext)       # float 4 octets
        self.PowExcessStart = float(self.serial_dataparamauto.pow_excess_start)  # float 4 octets
        self.PowExcessStop = float(self.serial_dataparamauto.pow_excess_stop)  # float 4 octets
        self.ClimPrio = self.serial_dataparamauto.clim_prio  # 4 octets
        self.TempMinHC = self.serial_dataparamauto.temp_min_HC            #short int 2 octets
        self.TempMinHP = self.serial_dataparamauto.temp_min_HP               #short int 2 octets
        
        # mode program 24 bytes
        self.TempPerHour = self.serial_dataparamprog.TempPerHour

        # hollidays 16 octets
        self.hollymode = data_Hollidays.hollyarrival_mode
        self.TempHG_bleu = data_Hollidays.hollytempmin_blue 
        self.TempHG_blanc = data_Hollidays.hollytempmin_white 
        self.TempHG_rouge = data_Hollidays.hollytempmin_red 
        self.ArrivalDateSec = 0             # short int 2octets
        self.ArrivalDateMin = 0               # short int 2octets
        self.ArrivalDateHour = data_Hollidays.arrivalhour               # short int 2octets
        self.ArrivalDateDay = data_Hollidays.arrivaldate.day                # short int 2octets
        self.ArrivalDateMonth = data_Hollidays.arrivaldate.month              # short int 2octets
        self.ArrivalDateYear = data_Hollidays.arrivaldate.year           # short int 2octets  
        
    
  
  
        #power and options 16 octets
        self.PowExcess = -data_homepage.pow_tot      # float 4 octets signe - pour singifier que
                                                        # si PowExcess > 0 c'est bon ! 
        self.PowL1_Home = data_homepage.pow_l1home                # float 4 octets
        self.PowInverter = data_homepage.pow_inv              # float 4 octets    
        self.Option[0] = data_homepage.mode_opt_repeat_set            # Tab 4 octets 
        self.Option[1] = data_homepage.mode_opt_prioVE  
        self.Option[2] = data_homepage.mode_opt_coupure_nuit
        self.Option[3] = data_homepage.tempo

    def sendto_smartgateway(self):
        ser = serial.Serial(port='/dev/serial0',baudrate=9600, timeout=1)
        ser.flushInput(); #vider le buffer 
        _time.sleep(0.5); #????
        
        self.update_bufferdata()
        # Time struct 12 octets
        trame = st.pack("<HHH",self.Sec,self.Min,self.Hour)
        trame = trame+st.pack("<HHH",self.Day,self.Month,self.Year)
      
        # HMI mode 4 octets
        trame = trame+st.pack("<i",self.mode)
        
        # mode auto 20 octets
        trame = trame+st.pack("<f",self.TempMinExt)
        trame = trame+st.pack("<f",self.PowExcessStart)
        trame = trame+st.pack("<f",self.PowExcessStop)
        trame = trame+st.pack("B",self.ClimPrio[0])
        trame = trame+st.pack("B",self.ClimPrio[1])
        trame = trame+st.pack("B",self.ClimPrio[2])
        trame = trame+st.pack("B",self.ClimPrio[3])
        trame = trame+st.pack("<H",self.TempMinHC)
        trame = trame+st.pack("<H",self.TempMinHP)        

        # mode program 24 bytes
        for i in range(0,24):
            trame=trame+st.pack("B",self.TempPerHour[i])
       
        # hollidays 16 octets
        trame = trame+st.pack("B",self.hollymode)
        trame = trame+st.pack("B",self.TempHG_bleu)
        trame = trame+st.pack("B",self.TempHG_blanc)
        trame = trame+st.pack("B",self.TempHG_rouge)
        trame = trame+st.pack("<HHH",self.ArrivalDateSec,self.ArrivalDateMin,self.ArrivalDateHour) 
        trame = trame+st.pack("<HHH",self.ArrivalDateDay,self.ArrivalDateMonth,self.ArrivalDateYear) 
       
        #power and options 16 octets
        trame = trame+st.pack("<f",self.PowExcess)
        trame = trame+st.pack("<f",self.PowL1_Home)
        trame = trame+st.pack("<f",self.PowInverter)
        trame = trame+st.pack("B",self.Option[0]) 
        trame = trame+st.pack("B",self.Option[1]) 
        trame = trame+st.pack("B",self.Option[2]) 
        trame = trame+st.pack("B",self.Option[3]) 

        
        
        # encapsulaiton longueur    
        l=len(trame)+1 # on inclut le checksum
        trame_l=st.pack("<B",l)
        trame=trame_l+trame # Trame =|L|...data...|
                    #        |0  ....  L-1|
                     
        #calcul checksum
        checksum=0
        for i in range(0,l): # de 0 à L exclu
            checksum=checksum+trame[i]
        checksum=checksum%256
        trame_sum=st.pack("<B",checksum)
        trame=trame+trame_sum
        
        #emission...
        ser.write(trame)
        #pause pour laisser le tps SGw de calculer la réponse
        _time.sleep(0.5);
        
        
        
        #Lecture du buffer série (liste)
        TabSerialIn=[]
        IsRx=0
        while (ser.inWaiting()>0): #tant qu'il y a des octets ds le buffer
            TabSerialIn.append(ser.read())
            IsRx=1
        
        if (IsRx==1):
            self.SerialStatus=Serial_NoError;
            #test de longueur (premier octet est la longueur, mais il faut 
            #ajouter +1 (le byte de checksum) 
        
            longueur=st.unpack("B",TabSerialIn[0])[0] #attention unpack
                                                #renvoie un tuple donc
                                                #on cherche le premier élt [0]
            if (len(TabSerialIn)==longueur+1):
                self.SerialStatus=Serial_NoError;
            else :
                self.SerialStatus=Serial_ReceiveLongFail ;
         
            #test checksum    
            if (self.SerialStatus==Serial_NoError):
                CS_Sum=0
                CS_Val = st.unpack("B",TabSerialIn[longueur])[0] 
                #calcul du checksum
                for i in range(0,longueur):
                    CS_Sum=CS_Sum+st.unpack("B",TabSerialIn[i])[0]
                    CS_Sum=CS_Sum&255 
                if  (CS_Sum!= CS_Val):
                    self.SerialStatus=Serial_ReceiveCheckSumFail
            
            #Mise à jour des clim data   
            # ex 0x5 'T','o','t','o',CS
            #     0   1   2   3   4   5
            if (self.SerialStatus==Serial_NoError):
                longueur=longueur-1  # longueur contient maintennt le nbre 
                                        #d'octetes dela payload exemple 24*4+21
                longExt=24     
                long_DataClim=(longueur-longExt)//4; #exemple long_DataClim=24
                ClimList=TabSerialIn[1:long_DataClim+1] # dernier élt exclu
                Data_Clim_Salon.Update(ClimList)
                
                ClimList=TabSerialIn[(1+long_DataClim):(2*long_DataClim+1)] # dernier élt exclu
                Data_Clim_SaM.Update(ClimList)
                
                ClimList=TabSerialIn[(1+2*long_DataClim):(3*long_DataClim+1)] # dernier élt exclu
                Data_Clim_Entree.Update(ClimList)
                
                ClimList=TabSerialIn[(1+3*long_DataClim):(4*long_DataClim+1)] # dernier élt exclu
                Data_Clim_Couloir.Update(ClimList)
                
                ClimList=TabSerialIn[(4*long_DataClim+1):(4*long_DataClim+1+longExt)] # dernier élt exclu
                Data_Ext.Update(ClimList)

        
        else: # Rx ne renvoie rien
            self.SerialStatus=Serial_NoMssgFromSGw;
        
# création de la variable serial_data pour exploitation 
# via d'autres modules
serial_data = DFH_CentralData()



# =================== Test unitaire=================================  
if __name__ == "__main__" :
    MyTimeStamp = TimeStampTypedef()
    MyTimeStamp.update
    print(type(MyTimeStamp.Sec))
    print(MyTimeStamp.Min)    
    print(MyTimeStamp.Hour)
    print(MyTimeStamp.Day)
    print(MyTimeStamp.Month)
    print(MyTimeStamp.Year)
