import serial
import json # pour passer un string à partir d'un dico
import struct # pour envoyer float, cad d'abord passer en byte

# Tx = GPIO14 cad pin externe n°4 en partant du haut
# Rx = GPIO15 cad pin externe n°5 en partant du haut
# GND = pin externe n°3

ser = serial.Serial(port='/dev/serial0',baudrate=9600, timeout=1)
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
mes_bytes=bytes([0x3,0x48,0x65,0x6C,0x6C,0x6F])
ser.write(mes_bytes) # envoie physiquement la suite de bytes précédents
#ser.write("Hello") génère une erreur car ce n'est pas la suite de 
# code ascii




