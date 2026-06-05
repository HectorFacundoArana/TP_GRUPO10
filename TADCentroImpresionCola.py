from TADTrabajo import *
from TADCola import *

def crearColaCentro():
	#Crea un centro de impresion vacio
	return []

def encolarTrabajo(centro,trabajo):
	#Agrega un trabajo al centro de impresion
	centro.append(trabajo)

def desencolarTrabajo(centro):
	#Elimina el primer trabajo de la cola
	desencolar(centro)

def tamanio(centro):
	#Retorna cantidad de trabajos
	return len(centro)

def existeTrabajo(centro,trabajo):
	#Comprueba si existe una venta
	return trabajo in centro

def centroVacio(centro):
	#Retorna True si centro no tiene elementos
	return esVacia(centro)

def copiarColaCentro(centro,cola):
	#Copia los trabajos del centro de impresion a una cola
	copiarCola(centro,cola)
