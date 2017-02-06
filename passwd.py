#!/usr/bin/python3

# 13.4 Ficheros y listas

fich = open("/etc/passwd","r")
usuarios = fich.readlines()
users = {} 	#diccionario con los usuarios

for usuario in usuarios:
	nick = usuario.split(':')[0]
	shell = usuario.split(':')[-1][:-1]
	users[nick] = shell

try:	

	print('User root: ',users['root'])	#imprime el value de la key root
	print('User imaginario',users['imaginario'])

except KeyError:	#Si no encuentra un usuario, elevamos la excepcion
	print("User not found")

fich.close()
