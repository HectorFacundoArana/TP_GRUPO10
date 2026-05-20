from TADTrabajo import *
from TADCola import *

def crearCentro():
	#Crea un centro de impresion vacio
	return []

def agregarTrabajo(centro,trabajo):
	#Agrega un trabajo al centro de impresion
	centro.append(trabajo)

def eliminarTrabajo(centro,trabajo):
	#Elimina un trabajo especifico
	centro.remove(trabajo)

def recuperarTrabajo(centro,i):
	#Retorna el trabajo de la posicion iesima
	return centro[i]

def tamanio(centro):
	#Retorna cantidad de trabajos
	return len(centro)

def existeTrabajo(centro,trabajo):
	#Comprueba si existe una venta
	return trabajo in centro

def centroVacio(centro):

	#Retorna True si centro no tiene elementos
	return len(centro)==0
