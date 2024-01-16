from ihm_page import HomePage
from ihm_page_fields import *
from time import strftime
import tkinter as tk

UPDATE_TIME_PER = 1000
URL_FRONIUS_METER = 'http://192.168.0.11/solar_api/v1/GetMeterRealtimeData.cgi?Scope=System'
TIME_OUT_SEC = 5


def UpdateLabel_PowInfos():
	pass
	
def UpdateLabel_TempoEDF():
	pass
	
def UpdateSystemManager():
	pass
	
def UpdateLabel_Clim():
	pass

def UpdateTime():
	win_home.after(UPDATE_TIME_PER ,UpdateTime)
	PageData.time_hour=strftime('%H:%M:%S')
	PageData.time_date=strftime('%A %d %b %Y')
	PageData.time_dateSTM32=strftime("%d/%b/%Y")
	win_home.label_date.config(text=PageData.time_date) # .config permet de modifier
	# les options d'un widget, indispensable donc !
	win_home.label_hour.config(text=PageData.time_hour)


	   


# === Code principal ===

# Genération de la fenêtre principale
win_home = HomePage()


# Lancement Horloge
UpdateTime()


# entrée dans la boucle infinie. Attente des évènements souris
win_home.mainloop() 
