# === classes de données directement liées au µC ===
from time import strftime

class TimeStampTypedef:
    def __init__(self): 
        self.Sec = 0
        self.Min = 0
        self.Hour = 0
        self.Day = 1
        self.Month = 1
        self.Year = 2024
    
    def update(self):
        self.Sec = int(strftime('%S'))
        self.Min = int(strftime('%M'))
        self.Hour = int(strftime('%H'))
        self.Day = int(strftime('%d'))
        self.Month = int(strftime('%m'))
        self.Year = int(strftime('%Y'))

class DFH_HMIMode:
    def __init__(self): 
        self.Mode = 0 # voir data_page.py pour les valeurs précises, int

    
    def update(self, mode):
        self.Mode = mode


class DFH_AutoModeDataTypedef:
    
    def __init__(self):
        self.TempMinExt = 7.0
        self.PowExcessStart = 500.0
        self.PowExcessStop = 0.0
        self.ClimPrio = [1,2,3,4]
        self.TempMinHC = 18 #short int !
        self.TempMinHP = 18 #short int !
      
    def update(self,tempminext,powexcessstart,powexcessstop,climprio,tempminhc,tempminhp):
        self.TempMinExt = float(tempminext)
        self.PowExcessStart = float(powexcessstart)
        self.PowExcessStop = float(powexcessstop)
        self.ClimPrio = climprio
        self.TempMinHC = tempminhc #short int !
        self.TempMinHP = tempminhp #short int !
        
        


class DFH_ProgramModeDataTypedef:

    def __init__(self):
        self.TempPerHour=[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,1818,18,18,18,18,18]

    def update(self,tmpperhour):
        self.TempPerHour=tmpperhour

        
class DFH_HollidaysModeDataTypedef:

    def __init__(self):
        self.Temp_ArrRedWhiteBlue = 0x12121212 # température arrivée/rouge/blanc/bleu = 18°C pour tous
        self.ArrivalDate # objet de type TimeStampTypedef
                


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
