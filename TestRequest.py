import requests
#from requests.exceptions import HTTPError

URL_FRONIUS_METER = 'http://192.168.0.11/solar_api/v1/GetMeterRealtimeData.cgi?Scope=System'
TIME_OUT_SEC = 5

try:
    res=requests.get(URL_FRONIUS_METER, timeout=TIME_OUT_SEC)
    
except Exception:
    print("exception levée")
else:
    json_brut=res.json() # json_brut est un dictionnaire...
    data_elec=json_brut["Body"]["Data"]["1"] # on vient chercher le dictionnaire '1'
    # du dictionnaire 'Data' du dictionnaire 'body' du fichier json brut...
    print(data_elec["PowerReal_P_Sum"])




