import socket
import json

#Variables a enviar al Tia Portal por UDP
id_unidad = 'sur'
id_frente = "cx530"
gas_type = "CH4"
ppm_value = 20
LMP = True

msgToSendTiaPortal = {"id_unidad": id_unidad, "id_frente":id_frente, "gas_type":gas_type, "ppm_value":ppm_value, "LMP":False}
msgJson = json.dumps(msgToSendTiaPortal)

bytesToSend         = str.encode(msgJson)
serverAddressPort   = ("192.168.0.21", 2021)
bufferSize          = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket
UDPClientSocket.sendto(bytesToSend, serverAddressPort)

