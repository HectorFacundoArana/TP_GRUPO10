from TADCentroImpresion import *
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

centro=crearCentro()

# Agregamos trabajos 

agregarTrabajo(centro,[0, "Pedro", "PDF", 25, "baja", "20/05/2026", "12:30"])
agregarTrabajo(centro,[1, "Ana", "WORD", 15, "media", "20/05/2026", "13:00"])
agregarTrabajo(centro,[2, "Carlos", "EXCEL", 5, "alta", "20/05/2026", "14:00"])
agregarTrabajo(centro,[3, "Elena", "PDF", 6, "baja", "20/05/2026", "15:00"])
agregarTrabajo(centro,[4, "Luis", "WORD", 12, "media", "20/05/2026", "16:00"])
agregarTrabajo(centro,[5, "Maria", "EXCEL", 5, "alta", "20/05/2026", "17:00"])


t=1
while(t!=0):
	print(f'''
	1-Recepcion de documentos
	2-Cambio de prioridad individual
	3-Procesar impresion ({tamanio(centro)} En cola)
	4-Visualizacion de la cola de impresion
	5-Reajuste por fecha
	6-Filtrado por formato (eliminar)
	7-Filtrado por franja horaria
	0-Cerrar menu''')

	t=int(input())
	#1°: Recepcion de Documentos
	if(t==1):
		s = 'S'
		while (s=='S'):
			trabajo=crearTrabajo()
			jidValido=False
			while(jidValido==False):
				jid=int(input("Ingrese JobID: "))
				if(centroVacio(centro)==False):
					for i in range (tamanio(centro)):
						aux=recuperarTrabajo(centro,i)
						if(jid==verJobid(aux)):
							print("JobID ya usado. Por favor ingrese otro.")
							break
						if(i==(tamanio(centro)-1)):
							print("JobID valido.")
							jidValido=True
				else:
					print("JobID valido.")
					jidValido=True
			nom=input("Ingrese nombre del documento: ").lower()
			form=pedir_formato()
			pag=int(input("Ingrese cantidad de paginas: "))
			prio=pedir_prioridad()
			fech=input("")
			hora=input("")

			cargarTrabajo(trabajo,jid,nom,form,pag,prio,fech,hora)
			print("Trabajo cargado correctamente")
			print(verJobid(trabajo))
			print(verNombre(trabajo))
			print(verFormato(trabajo))
			print(verPaginas(trabajo))
			print(verPrioridad(trabajo))
			print(verFecha(trabajo))
			print(verHora(trabajo))
			agregarTrabajo(centro,trabajo)

			s=input("¿Desea agregar mas trabajos a la cola de impresion?(S/N)").upper()

	#2°: Cambio de Prioridad Individual
	elif(t==2):
		print("Cambio de prioridad a un trabajo")
		jobid=int(input("Ingrese el JobID del trabajo para modificar su prioridad: "))
		print("Ingrese nueva prioridad del trabajo")
		nuevaPrio=pedir_prioridad()
		encontrado=False
		for i in range(tamanio(centro)):
			aux=recuperarTrabajo(centro,i)
			if (jobid==verJobid(aux)):
				modPrioridad(aux,nuevaPrio)
				print("Se ha modificado la prioridad del trabajo a ",nuevaPrio)
				encontrado=True
		if (encontrado==False):
			print("No se ha encontrado un trabajo con JobID ",jobid)
	#3°: Procesar Impresion (Atencion de la Cola)
	elif(t == 3):
		procesarImpresion = True

		while procesarImpresion:

			if centroVacio(centro):
				print("No hay trabajos en la cola de impresion. Volviendo al menu.")
				break

			for prioridad in PRIORIDADES_VALIDAS:
				if not procesarImpresion:
					break  # Corta el for de prioridades cuando el usuario decide no continuar

				for i in range(tamanio(centro)):
					aux = recuperarTrabajo(centro, i)
					if verPrioridad(aux) == prioridad:
						print(f'''
						JobID: {verJobid(aux)}
						Nombre: {verNombre(aux)}
						Formato: {verFormato(aux)}
						Cantidad de paginas: {verPaginas(aux)}
						Nivel de prioridad: {verPrioridad(aux)}
						Fecha: {verFecha(aux)}
						Hora: {verHora(aux)}
						''')
						eliminarTrabajo(centro, aux)

						continuar = input("¿Desea continuar con las impresiones?(S/N): ").upper()
						if continuar == "N":
							procesarImpresion = False
						break


	#4°: Visualizacion de la Cola de Impresion
	elif(t==4):
		print("Visualizacion de la cola de impresion")
		if (centroVacio(centro)==False):
			for i in range(tamanio(centro)):
				aux=recuperarTrabajo(centro,i)
				if(verPrioridad(aux)=='alta'):
					print(f'''
					JobID: {verJobid(aux)}
					Nombre: {verNombre(aux)}
					Formato: {verFormato(aux)}
					Cantidad de paginas: {verPaginas(aux)}
					Nivel de prioridad: {verPrioridad(aux)}
					Fecha: {verFecha(aux)}
					Hora: {verHora(aux)}
					''')
			for j in range(tamanio(centro)):
				aux=recuperarTrabajo(centro,j)
				if(verPrioridad(aux)=='media'):
					print(f'''
					JobID: {verJobid(aux)}
					Nombre: {verNombre(aux)}
					Formato: {verFormato(aux)}
					Cantidad de paginas: {verPaginas(aux)}
					Nivel de prioridad: {verPrioridad(aux)}
					Fecha: {verFecha(aux)}
					Hora: {verHora(aux)}
					''')
			for k in range(tamanio(centro)):
				aux=recuperarTrabajo(centro,k)
				if(verPrioridad(aux)=='baja'):
					print(f'''
					JobID: {verJobid(aux)}
					Nombre: {verNombre(aux)}
					Formato: {verFormato(aux)}
					Cantidad de paginas: {verPaginas(aux)}
					Nivel de prioridad: {verPrioridad(aux)}
					Fecha: {verFecha(aux)}
					Hora: {verHora(aux)}
					''')
		else:
			print("No hay trabajos en la cola de impresion. Volviendo al menu.")

	#5°: Reajuste Masivo por Fecha
	elif(t==5):
		print("Reajuste de prioridad a Baja de los trabajos de un mes")
		nuevaPrio='baja'
		mesInput=input("Ingrese mes(MM): ")
		#Uso de try para asegurar el formato correcto del input de mes
		try:
			#Transformo el input que es un string a un formato fecha
			mes_comp=datetime.strptime(mesInput,"%m").month
			for i in range(tamanio(centro)):
				aux=recuperarTrabajo(centro,i)
				if(mes_comp==verFecha(aux).month):
					modPrioridad(aux,nuevaPrio)
		except ValueError:
			print("Error: el mes ingreado no es valido. Ingresar de 01 a 12")

	#6: Filtrado por Formato (eliminacion)
	elif(t==6):
		print("Eliminacion por formato de trabajo")
		i=0
		form=pedir_formato()
		while(i<(tamanio(centro))):
			aux=recuperarTrabajo(centro,i)
			if(form==verFormato(aux)):
				print(f'''
				JobID: {verJobid(aux)}
				Nombre: {verNombre(aux)}
				Formato: {verFormato(aux)}
				Cantidad de paginas: {verPaginas(aux)}
				Nivel de priorirdad: {verPrioridad(aux)}
				Fecha: {verFecha(aux)}
				Hora: {verHora(aux)}
				Trabajo eliminado.
				''')
				eliminarTrabajo(centro,aux)
			else:
				i=i+1

	#7: Filtrado por Franja Horaria (nueva cola)
	elif(t==7):
		print("Listado de trabajos dentro de una franja horaria")
		i=0
		colaFranja=crearCola()
		min=input("Ingrese inicio de franja horaria(HH:MM): ")
		hora_min=datetime.strptime(min,"%H:%M").time()
		max=input("Ingrese final de franja horaria(HH:MM): ")
		hora_max=datetime.strptime(max,"%H:%M").time()
		for i in range(tamanio(centro)):
			aux=recuperarTrabajo(centro,i)
			if(hora_min<=verHora(aux)<=hora_max):
				print(f'''
				JobID: {verJobid(aux)}
				Nombre: {verNombre(aux)}
				Formato: {verFormato(aux)}
				Cantidad de paginas: {verPaginas(aux)}
				Nivel de priorirdad: {verPrioridad(aux)}
				Fecha: {verFecha(aux)}
				Hora: {verHora(aux)}
				''')
				encolar(colaFranja,aux)

	#8: Cierre de Menu
	elif(t==0):
		print("Saliendo del menu...")

	#8:Fuera de parametro
	else:
		print("No ha ingresado una opcion correcta, pruebe otra vez...")
