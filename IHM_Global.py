#VALEURS POSSIBLES DE LA VARIABLE Mode
HMI_Mode_Off = 0xA0
HMI_Mode_Auto = 0xA1
HMI_Mode_Program = 0xA2
HMI_Mode_Hollidays = 0xA3

MODE_DICTIO = {HMI_Mode_Off:"Arrêt",HMI_Mode_Auto:"Automatique",HMI_Mode_Program :"Programmation",HMI_Mode_Hollidays:"Vacances"} 

#VALEURS POSSIBLES DE LA VARIABLE CouleurTempo
Tempo_Bleu = 1
Tempo_Blanc = 2
Tempo_Rouge = 3
Tempo_NoConnection = 0

# COULEURS POUR BACKGROUND
COLOUR_FRAME = '#C0C0C0'
COLOUR_BLUE = '#4065DE'
COLOUR_WHITE = '#FFFFFF'
COLOUR_RED = '#FF0000'

#Valeur possible Diagnostic
Serial_NoError =  0
Serial_ReceiveCheckSumFail = 1
Serial_ReceiveLongFail = 2
Serial_NoMssgFromSGw=3

#liste des cmdes téléco IR
Chaud_18_VanBas_FanAuto = 193
Chaud_19_VanBas_FanAuto = 194
Chaud_20_VanBas_FanAuto = 195
Chaud_21_VanBas_FanAuto = 196
Chaud_22_VanBas_FanAuto = 197
Chaud_23_VanBas_FanAuto = 198
NoCommandToSend = 199
Stop = 192

#liste des warning RmDv
Status_NoWarning =1
Status_Trial_2 = 2
Status_Trial_3 = 3
Status_Error_TempI2C = 20
Status_Error_NewTempSetNotReceived = 21
Status_NoStatusReceived = 22
