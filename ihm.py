# ATTENTION PLANTAGE si erreur d'adressage IP 10 et pas 11 ou l'inverse
# le try catch doit être amélioré

from IHM_Global import *
from page_home import PageHome
from data_page import data_homepage
from time import strftime
import tkinter as tk
import requests

UPDATE_TIME_PER = 1000
UPDATE_POW_PER = 60000
URL_FRONIUS_METER = 'http://192.168.0.10/solar_api/v1/GetMeterRealtimeData.cgi?Scope=System'
URL_FRONIUS_INVERTER= 'http://192.168.0.10/solar_api/v1/GetInverterRealtimeData.cgi?Scope=System&DataCollection=CumulationInverterData'
URL_EDFTEMPO = 'https://www.api-couleur-tempo.fr/api/jourTempo/today'
TIME_OUT_SEC = 5
TIME_OUT_SEC_TEMPO = 10


      

def updatepowdata(): # requête vers inverter avec gestion exeption\
                       # au cas où échec de connection. \
                       # timout configurable
    win_home.after(UPDATE_POW_PER ,updatepowdata)
    try:
        res=requests.get(URL_FRONIUS_METER, timeout=TIME_OUT_SEC)
        res_inv=requests.get(URL_FRONIUS_INVERTER,timeout=TIME_OUT_SEC)
        res_tempo=requests.get(URL_EDFTEMPO,timeout=TIME_OUT_SEC_TEMPO)
    except Exception:
        data_homepage.pow_tot=50000.0
        data_homepage.pow_inv=-50000.0
        data_homepage.pow_l1home=50000.0
        
    else:
     
        json_brut=res.json() # json_brut est un dictionnaire...
        data_elec=json_brut["Body"]["Data"]["1"] # on vient chercher \
        #le dictionnaire '1' du dictionnaire 'Data' du dictionnaire \
        #'body' du fichier json brut...
        json_brut=res_inv.json()
        fronius_inverter_power=json_brut["Body"]["Data"]["PAC"]\
                                        ["Values"]["1"]
        data_homepage.pow_tot=data_elec["PowerReal_P_Sum"] 
        data_homepage.pow_inv=fronius_inverter_power
        data_homepage.pow_l1=data_elec["PowerReal_P_Phase_1"] 
        data_homepage.pow_l1home=round((data_homepage.pow_l1+data_homepage.pow_inv),1)
        if data_homepage.pow_tot > 2000.0:
            data_homepage.pow_temoin = "#ff0000" #rouge
        elif data_homepage.pow_tot > 0.0 :
            data_homepage.pow_temoin = "#ff9933" #orange
        elif data_homepage.pow_tot > -2000.0 :
            data_homepage.pow_temoin = "#ccff99" #vert pâle
        else : 
             data_homepage.pow_temoin = "#00994c" #vert foncé
        
        # arrondi à une décimale dans la soustraction
        data_homepage.pow_l2=data_elec["PowerReal_P_Phase_2"] 
        data_homepage.pow_l3=data_elec["PowerReal_P_Phase_3"] 

    finally:
        win_home.update_powdata()
        

def updatelabel_tempoEDF():
    win_home.after(UPDATE_POW_PER ,updatelabel_tempoEDF) # modifier la période 
    try:
        res_tempo=requests.get(URL_EDFTEMPO,timeout=TIME_OUT_SEC_TEMPO)
    except Exception:
        data_homepage.tempo = Tempo_NoConnection 
    else:  
        json_brut=res_tempo.json()
        data_homepage.tempo =json_brut["codeJour"]
        win_home.update_tempo()
        print(data_homepage.tempo) 
        print(data_homepage.tempostring[data_homepage.tempo]  )
        

def transaction_SGw():
    pass
    
def UpdateLabel_Clim():
    pass

def updatetimedata():
    win_home.after(UPDATE_TIME_PER ,updatetimedata)
    data_homepage.time_hour=strftime('%H:%M:%S')
    data_homepage.time_date=strftime('%A %d %b %Y')
    data_homepage.time_dateSTM32=strftime("%d/%m/%Y")
    win_home.update_time()





# === Code principal ===

# Genération de la fenêtre principale
win_home = PageHome()


updatepowdata()
updatelabel_tempoEDF()
# Lancement Horloge
updatetimedata()


# entrée dans la boucle infinie. Attente des évènements souris
win_home.mainloop() 
