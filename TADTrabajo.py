def crearTrabajo():
	#Crea un trabajo vacio
	return [0, "", "", 0, 0, 0, 0]

def cargarTrabajo(trabajo,jobid,nomdoc,formato,paginas,lvlprio,fecha,hora):
	#Carga los datos de un trabajo por parametro
	trabajo[0]= jobid
	trabajo[1]= nomdoc
	trabajo[2]= formato
	trabajo[3]= paginas
	trabajo[4]= lvlprio
	trabajo[5]= fecha
	trabajo[6]= hora

def verJobid(trabajo):
	#Retorna el ID de Trabajo
	return trabajo[0]
def verNombre(trabajo):
	#Retorna el Nombre del Documento
	return trabajo[1]
def verFormato(trabajo):
	#Retorna el Tipo de Formato
	return trabajo[2]
def verPaginas(trabajo):
	#Retorna la cantidad de paginas
	return trabajo[3]
def verPrioridad(trabajo):
	#Retorna el nivel de prioridad
	return trabajo[4]
def verFecha(trabajo):
	#Retorna la fecha de envio
	return trabajo[5]
def verHora(trabajo):
	#Retorna la hora de envio
	return trabajo[6]

def modJobid(trabajo,nuevoJobid):
	#Modifica el ID de trabajo
	trabajo[0]=nuevoJobid
def modNombre(trabajo,nuevoNombre):
	#Modifica el nombre de un trabajo
	trabajo[1]=nuevoNombre
def modFormato(trabajo,nuevoFormato):
	#Modifica el formato de un trabajo
	trabajo[2]=nuevoFormato
def modPaginas(trabajo,nuevaPaginas):
	#Modifica la cantidad de paginas de un trabajo
	trabajo[3]=nuevaPaginas
def modPrioridad(trabajo,nuevaPrioridad):
	#Modifica el nivel de prioridad de un trabajo
	trabajo[4]=nuevaPrioridad
def modFecha(trabajo,nuevaFecha):
	#Modifica la fecha de envio de un trabajo
	trabajo[5]=nuevaFecha
def modHora(trabajo,nuevaHora):
	#Modifica la hora de envio de un trabajo
	trabajo[6]=nuevaHora

def asignarTrabajo(trabajo1,trabajo2):
	#Asigna los datos de un trabajo en otro
	#trabajo1[0]=trabajo2[0],...
	modJobid(trabajo1,verJobid(trabajo2))
	modNombre(trabajo1,verNombre(trabajo2))
	modFormato(trabajo1,verFormato(trabajo2))
	modPaginas(trabajo1,verPaginas(trabajo2))
	modPrioridad(trabajo1,verPrioridad(trabajo2))
	modFecha(trabajo1,verFecha(trabajo2))
	modHora(trabajo1,verHora(trabajo2))
