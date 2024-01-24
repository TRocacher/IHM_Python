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
mes_bytes=bytes([0x48,0x65,0x6C,0x6C,0x6F])
ser.write(mes_bytes) # envoie physiquement la suite de bytes précédents
#ser.write("Hello") génère une erreur car ce n'est pas la suite de 
# code ascii


mssg="Bonjour monsieur !"
mes_bytes_2=mssg.encode()
ser.write(mes_bytes_2)
ser.write(b"Au revoir")

ser.write(b"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")



# CONCLUSION : avant d'envoyer un message string "on l'encode" cad qu'on
# reconstruit la suite de code ASCII
# on peut le faire aussi avec b" "


# ci dessous un dictionnaire passé en string à la liaison série
# le STM32 va recevoir le dico en caractère ASCII


MyDic={"Power":"145.4","Tempo":"Rouge"}
MyDic_Str=json.dumps(MyDic)
print(MyDic) # MyDic est un string ...
MyDic_Bytes=MyDic_Str.encode('utf-8')
ser.write(MyDic_Bytes)


#envoyer directement un float par liaons série 
myfloat=3.14

floatbytes = struct.pack('!f',myfloat) # permet de convertir en byte

print(myfloat)
print(floatbytes )
ser.write(floatbytes)


# ci dessous des exemles de lectures
# les prints ne sont pas bons car ce sont des bytes.
# il faut les convertir

Rep_1=ser.read(size=5)
print(Rep_1)
Rep_2=ser.readline()
print(Rep_2)

mssg_1=Rep_1.decode()
print(mssg_1)
mssg_2=Rep_2.decode()
print(mssg_2)

#CONCLUSION : avant de printer, on fait un decode. Cela permet de trans
#former la suite de bytes en un string pour python.




