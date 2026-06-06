from TADCentroImpresion import *
from TADCentroImpresionCola import *
from TADTrabajo import *
from TADCola import *
from datetime import datetime,date,time

# Defino una lista con las prioridades validas
PRIORIDADES_VALIDAS = ["alta", "media", "baja"]

# Creo una funcion llamada pedir_prioridad para validar lo que escribe el usuario
def pedir_prioridad():
	# Inicio un ciclo que se repite hasta que el usuario escriba algo correcto
	while True:
		prio = input("Prioridad (Alta, Media, Baja): ").lower()
		# Comparo en minuscula con .lower() para que no importe si escribe "ALTA" o "alta"
		if prio in PRIORIDADES_VALIDAS:
			# Si es valida, la retorno y el ciclo se corta
			return prio
		else:
			# Si no es valida, aviso y el while vuelve a pedir el input
			print("-> Prioridad invalida. Solo se permite: Alta, Media o Baja.")

# Defino una lista con los formatos validos
FORMATOS_VALIDOS = ["pdf", "imagen", "texto"]

# Creo una funcion llamada pedir_formato para validar lo que escribe el usuario
def pedir_formato():
	# Inicio un ciclo que se repite hasta que el usuario escriba algo correcto
	while True:
		form = input("Formato (PDF, Imagen, Texto): ").lower()
		# Comparo en minuscula con .lower() para que no importe si escribe "ALTA" o "alta"
		if form in FORMATOS_VALIDOS:
			# Si es valida, la retorno y el ciclo se corta
			return form
		else:
			# Si no es valida, aviso y el while vuelve a pedir el input
			print("-> Formato invalida. Solo se permite: PDF, Imagen o Texto.")

def existejid(centro, jid):
	if(centroVacio(centro)==False):
		for i in range(tamanio(centro)):
			aux = desencolarTrabajo(centro)
			if (verJobid(aux) == jid):
				return True
			encolarTrabajo(centro,aux)
		return False

centro = crearColaCentro()

# Agregamos trabajos

t0 = crearTrabajo()
cargarTrabajo(t0, 0, "pedro", "pdf", 25, "baja", "20/05/2026", "12:30")
encolarTrabajo(centro, t0)

t1 = crearTrabajo()
cargarTrabajo(t1, 1, "ana", "imagen", 15, "media", "20/05/2026", "13:00")
agregarTrabajo(centro, t1)

t2 = crearTrabajo()
cargarTrabajo(t2, 2, "carlos", "texto", 5, "alta", "20/05/2026", "14:00")
encolarTrabajo(centro, t2)

t3 = crearTrabajo()
cargarTrabajo(t3, 3, "elena", "pdf", 6, "baja", "20/05/2026", "15:00")
encolarTrabajo(centro, t3)

t4 = crearTrabajo()
cargarTrabajo(t4, 4, "luis", "imagen", 12, "media", "20/05/2026", "16:00")
encolarTrabajo(centro, t4)

t5 = crearTrabajo()
cargarTrabajo(t5, 5, "maria", "texto", 5, "alta", "20/05/2026", "17:00")
encolarTrabajo(centro, t5)

t6 = crearTrabajo()
cargarTrabajo(t6, 6, "jose", "pdf", 8, "baja", "21/05/2026", "09:15")
encolarTrabajo(centro, t6)

t7 = crearTrabajo()
cargarTrabajo(t7, 7, "lucia", "imagen", 20, "media", "21/05/2026", "10:30")
encolarTrabajo(centro, t7)

t8 = crearTrabajo()
cargarTrabajo(t8, 8, "marcos", "texto", 10, "alta", "22/05/2026", "11:45")
encolarTrabajo(centro, t8)

t9 = crearTrabajo()
cargarTrabajo(t9, 9, "sofia", "pdf", 3, "media", "22/05/2026", "14:20")
encolarTrabajo(centro, t9)



while True:
	print("1-Recepcion de documentos")
	print("2-Cambio de prioridad individual")
	print(f"3-Procesar impresion ({tamanio(centro)} en cola)")
	print("4-Visualizacion de la cola de impresion")
	print("5-Reajuste por fecha")
	print("6-Filtrado por formato (eliminar)")
	print("7-Filtrado por franja horaria")
	print("0-Cerrar menu")
	try:
		opcion = int(input("Ingrese una opcion: "))
	except ValueError:
		print("Error, debe ingresar un numero entero")
		continue

		#1: Recepcion de Documentos
	#Verificacion de ID
	if opcion == 1:
		while True:
			trabajo = crearTrabajo()
			while True:
				try:
					jid = int(input("Ingrese ID del trabajo: "))
					if existejid(centro, jid):
						print("ID ya utilizado, ingresar otro")
					else:
						print("ID valido")
						break
				except ValueError:
					print("Error: El ID debe ser un numero entero")

			#Carga de los demas datos
			nombre = input("Ingrese nombre del documento: ").lower()
			formato = pedir_formato()
			while True:
				try:
					paginas = int(input("Ingrese cantidad de paginas: "))
					if paginas > 0:
						break
					else:
						print("La cantidad de paginas debe ser mayor a 0")
				except ValueError:
					print("Error: Debe ingresar un numero entero")

			prioridad = pedir_prioridad()
			while True:
				try:
					fecha = input("Ingrese fecha (DD/MM/AAAA): ")
					datetime.strptime(fecha, "%d/%m/%Y")
					break
				except ValueError:
					print("Error: Formato de fecha invalido. Debe ser DD/MM/AAAA")

			while True:
				try:
					hora = input("Ingrese hora (HH:MM): ")
					datetime.strptime(hora, "%H:%M")
					break
				except ValueError:
					print("Error: Formato de hora invalido. Debe ser HH:MM")

			cargarTrabajo(trabajo, jid, nombre, formato, paginas, prioridad, fecha, hora)

			#Muestra los datos cargados para verificar que sea correcto
			print("Cargado correctamente")
			print(verJobid(trabajo))
			print(verNombre(trabajo))
			print(verFormato(trabajo))
			print(verPaginas(trabajo))
			print(verPrioridad(trabajo))
			print(verFecha(trabajo))
			print(verHora(trabajo))
			encolarTrabajo(centro, trabajo)

			#Consulta para seguir cargando trabajo
			continuar = input("Desea cargar mas trabajo? S/N: ").upper()
			if continuar != "S":
				break


	#2: Cambio de Prioridad Individual
	elif opcion == 2:
		print("Cambio de Prioridad")
		while True:
			try:
				jid = int(input("Ingrese ID del trabajo: "))
				if existejid(centro, jid):
					nuevaPrio = pedir_prioridad()
					for i in range(tamanio(centro)):
						aux = desencolarTrabajo(centro)
						if verJobid(aux) == jid:
							modPrioridad(aux, nuevaPrio)
							print("Se modifico correctamente")
						encolarTrabajo(centro,aux)
					break

				else:
						print("ID valido")
			except ValueError:
				print("Error: El ID debe ser un numero entero")
				continue


	#3: Procesar Impresion (Atencion de la Cola)
	elif(opcion == 3):
		while True:
			if (centroVacio(centro)==True):
				print("No hay trabajos en la cola de impresion. Volviendo al menu.")
				break
			aux = desencolarTrabajo(centro)
			print(f"\nJobID: {verJobid(aux)}")
			print(f"Nombre: {verNombre(aux)}")
			print(f"Formato: {verFormato(aux)}")
			print(f"Cantidad de paginas: {verPaginas(aux)}")
			print(f"Nivel de prioridad: {verPrioridad(aux)}")
			print(f"Fecha: {verFecha(aux)}")
			print(f"Hora: {verHora(aux)}")
			continuar = input("¿Desea continuar con las impresiones?(S/N): ").upper()
			if continuar != "S":
				break

	#4: Visualizacion de la Cola de Impresion
	elif(opcion==4):
		print("Visualizacion de la cola de impresion")
		if(centroVacio(centro)==True):
			print("No hay trabajos en la cola de impresion. Volviendo al menu.")
		for i in range (tamanio(centro)):
			aux = desencolarTrabajo(centro)
			print(f"\nJobID: {verJobid(aux)}")
			print(f"Nombre: {verNombre(aux)}")
			print(f"Formato: {verFormato(aux)}")
			print(f"Cantidad de paginas: {verPaginas(aux)}")
			print(f"Nivel de prioridad: {verPrioridad(aux)}")
			print(f"Fecha: {verFecha(aux)}")
			print(f"Hora: {verHora(aux)}")
			encolarTrabajo(centro,aux)

	#5: Reajuste Masivo por Fecha
	elif(opcion==5):
		print("Reajuste de prioridad a Baja de los trabajos de un mes")
		nuevaPrio='baja'
		mesInput=input("Ingrese mes(MM): ")
		try:
			mes_comp=datetime.strptime(mesInput,"%m").month
			for i in range(tamanio(centro)):
				aux=desencolarTrabajo(centro)
				fecha_obj=datetime.strptime(verFecha(aux),"%d/%m/%Y")
				if(mes_comp==fecha_obj.month):
					modPrioridad(aux,nuevaPrio)
				encolarTrabajo(centro,aux)
		except ValueError:
			print("Error: el mes ingreado no es valido. Ingresar de 01 a 12")

	#6: Filtrado por Formato (eliminar)
	elif(opcion==6):
		print("Eliminacion por formato de trabajo")
		form=pedir_formato()
		#Este i va a controlar la cantidad de operaciones que se hacen en la cola
		i=1
		ini=tamanio(centro)
		while(True):
			if(esVacio(centro)==True):
				print("No hay trabajos en la cola de trabajo. Volviendo al menu...")
				break
			if(i==ini):
				break
			else:
				aux=desencolarTrabajo(centro)
				if(form==verFormato(aux).lower()):
					print(f"\nJobID: {verJobid(aux)}")
					print(f"Nombre: {verNombre(aux)}")
					print(f"Formato: {verFormato(aux)}")
					print(f"Cantidad de paginas: {verPaginas(aux)}")
					print(f"Nivel de prioridad: {verPrioridad(aux)}")
					print(f"Fecha: {verFecha(aux)}")
					print(f"Hora: {verHora(aux)}")
					print("Trabajo eliminado.")
					eliminarTrabajo(centro,aux)
					i=i+1
				else:
					encolarTrabajo(centro,aux)
					i=i+1

	#7: Filtrado por Franja Horaria (nueva cola)
	elif(opcion==7):
		print("Listado de trabajos dentro de una franja horaria")
		colaFranja=crearCola()
		try:
			min=input("Ingrese inicio de franja horaria(HH:MM): ")
			hora_min=datetime.strptime(min,"%H:%M").time()
			max=input("Ingrese final de franja horaria(HH:MM): ")
			hora_max=datetime.strptime(max,"%H:%M").time()

			for i in range(tamanio(centro)):
				aux=desencolarTrabajo(centro)
				hora_obj=datetime.strptime(verHora(aux),"%H:%M").time()
				if(hora_min<=hora_obj<=hora_max):
					encolar(colaFranja,aux)
				encolarTrabajo(centro,aux)
			while not esVacia(colaFranja):
				aux=desencolar(colaFranja)
				print(f"\nJobID: {verJobid(aux)}")
				print(f"Nombre: {verNombre(aux)}")
				print(f"Formato: {verFormato(aux)}")
				print(f"Cantidad de paginas: {verPaginas(aux)}")
				print(f"Nivel de prioridad: {verPrioridad(aux)}")
				print(f"Fecha: {verFecha(aux)}")
				print(f"Hora: {verHora(aux)}")
		except ValueError:
			print("Error: Formato de hora invalido")

	#8: Cierre de Menu
	elif(opcion==0):
		print("Saliendo del menu...")
		break

	#9:Fuera de parametro
	else:
		print("No ha ingresado una opcion correcta, pruebe otra vez...")
