#bandera o centinela

nombre=" "
bandera= False

while nombre != "fin":
	nombre = input("Ingrese un nombre: ")
	if nombre == "adrian":
		bandera= True

if bandera:
	print("entro Adrian ")
else:
	print("no entro Adrian")