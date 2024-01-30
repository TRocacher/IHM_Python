import serial
import json # pour passer un string à partir d'un dico
import struct as st # pour envoyer float, cad d'abord passer en byte
from time import strftime

# Tx = GPIO14 cad pin externe n°4 en partant du haut
# Rx = GPIO15 cad pin externe n°5 en partant du haut
# GND = pin externe n°3

ser = serial.Serial(port='/dev/serial0',baudrate=9600, timeout=1)

Hour=int(strftime('%H'))
Min=int(strftime('%M'))
Sec=int(strftime('%S'))
Year=int(strftime('%Y'))
Month=int(strftime('%m'))
Day=int(strftime('%d'))
print(8)
print(Sec)
print(Min)
print(Hour)
print(Day)
print(Month)
print(Year)


#élaboration trame byte sans checksum
Trame_H = st.pack("<HHH",Sec,Min,Hour)
Trame_D = st.pack("<HHH",Day,Month,Year)
Trame=Trame_H+Trame_D

L=len(Trame)+1 # on inclut le checksum
Trame_L=st.pack("<B",L)
Trame=Trame_L+Trame # Trame =|L|...data...|
                    #        |0  ....  L-1|
#calcul checksum
Sum=0
for i in range(0,L): # de 0 à L exclu
    Sum=Sum+Trame[i]

    
    
print(Sum)
Sum=Sum%256
print(Sum)
Trame_Sum=st.pack("<B",Sum)
Trame=Trame+Trame_Sum
ser.write(Trame) 




# Ref doc pySerial API
# timeout est en secondes, c'est un float
# on peut tout paramétrer ici, parité, stop bit...

# les méthodes 
# -- ouverture et fermeture du port --
# .open(), exemple ser.open()
# .close()
# remarque lorsque le port est passé lors de l'instanciation, il est 
# immédiatement ouvert



# ------------important String / byte --------------
#mes_bytes=bytes([0x3,0x48,0x65,0x6C,0x6C,0x6F])
#ser.write(mes_bytes) # envoie physiquement la suite de bytes précédents
#ser.write("Hello") génère une erreur car ce n'est pas la suite de 
# code ascii




