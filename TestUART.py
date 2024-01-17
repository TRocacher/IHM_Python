import serial

# Tx = GPIO14 cad pin externe n°4 en partant du haut
# Rx = GPIO15 cad pin externe n°5 en partant du haut
# GND = pin externe n°3

ser = serial.Serial(port='/dev/serial0',baudrate=9600, timeout=5)
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

# CONCLUSION : avant d'envoyer un message string "on l'encode" cad qu'on
# reconstruit la suite de code ASCII
# on peut le faire aussi avec b" "



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




