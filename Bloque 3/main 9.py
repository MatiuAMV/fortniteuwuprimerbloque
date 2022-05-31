
while True:
	print("cual es tu calificacion")
	calificacion=int(input("calificacion: "))
	calificacion2=int(input("calificacion: "))
	calificacion3=int(input("calificacion: "))


	calificacionll=calificacion+calificacion2+calificacion3/3
	print("promedio:",calificacionll)

	
	
	if(calificacionll<6):
		print("reprobaste")

	else:
		print('pasaste *le da una medalla*')
		print("🎖")