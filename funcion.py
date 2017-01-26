'''
Created on Jan 23, 2017

@author: alexander
@author: christian
'''

from datetime import datetime, timedelta
from math import ceil

class Tarifa:
    # Dominio Clase Tarifa
    # (0,1e308) (1e308 es el máximo número representado por Python)

    _semana = 0.0
    _finde = 0.0
    def __init__(self, sem, fin):
        if sem < 0 or fin < 0:
            raise Exception('No existen las Tarifas Negativas')
        self._semana = sem
        self._finde = fin
        
    def getSemana(self):
        return self._semana
    
    def getFinde(self):
        return self._finde
    

def calcularPrecio(tarifa, tiempoDeServicio):
    # Domimio tiempoDeServicio: 
    # año = [1,9999], mes = [1,12], hora = [0,23], minuto = [0,59], segundo = [0,59], microsegundo = [0,999999] 
    # Para toda la función calcularPrecio el dominio de datos corresponde al dominio de ambas funciones, 
    # por ejemplo en un año cualquiera el dominio es del primero de enero a las 0 horas 0 minutos 1 segundos 
    # hasta el 31 de diciembre a las 23 horas 59 minutos 59 segundos. Los segundos no se toman en cuenta para 
    # el cálculo de la función. El rango de la función si corresponde a cualesquiera dos fechas mientras la
    #  diferencia sea mayor a quince minutos y menor a 7 dias, es decir: 0 dias 00:15 < TiempoDeServicio < 07 dias 00:00
    if tiempoDeServicio[1] < tiempoDeServicio[0]:
        raise Exception('No puedes ir al pasado')
    resta = tiempoDeServicio[1] - tiempoDeServicio[0]
    if  resta < timedelta(minutes = 15):
        raise Exception('No puede ser menor a 15 minutos')
    if resta > timedelta(days = 7):
        raise Exception('No puede ser mayor a 7 dias')
    
    
    iterador = tiempoDeServicio[0]
    
    if iterador.weekday() >= 5:
        semana = False
    else:
        semana = True
    
        
    deltaTiempoSemana = 0
    deltaTiempoFinde = 0
    acumuladorMinutosSemana = timedelta()
    acumuladorMinutosFinde = timedelta()
    
    while iterador + timedelta(hours=1) < tiempoDeServicio[1]:
        old_iterador = iterador
        iterador = iterador + timedelta(hours=1)
        if iterador.weekday() >= 5:
            # Se toma que, si se pasan algunos minutos en la semana antes de llegar al fin de semana,
            # entonces consumio una hora de semana
            if semana:
                # Reiniciamos las horas de fin de semana como si contaramos desde 0
                aux = datetime.combine(iterador.date(), datetime.min.time())
                acumuladorMinutosFinde = acumuladorMinutosFinde + (iterador - aux)
                acumuladorMinutosSemana = acumuladorMinutosSemana + (aux - old_iterador)
                iterador = aux
            else:
                deltaTiempoFinde = deltaTiempoFinde + 1
            semana = False
        else:
            # Se toma que, si se pasan algunos minutos en el fin semana antes de llegar a la semana,
            # entonces consumio una hora de fin de semana
            if semana:
                deltaTiempoSemana = deltaTiempoSemana + 1
            else:
                # Reiniciamos las horas de semana como si contaramos desde 0
                aux = datetime.combine(iterador.date(), datetime.min.time())
                acumuladorMinutosFinde = acumuladorMinutosFinde + (aux - old_iterador)
                acumuladorMinutosSemana = acumuladorMinutosSemana + (iterador - aux)
                iterador = datetime.combine(iterador.date(), datetime.min.time())
            semana = True
            
    # Sobraron tiempo
    if tiempoDeServicio[1] - iterador > timedelta():
        # Falto una hora de fin de semana
        if tiempoDeServicio[1].weekday() >= 5 and iterador.weekday() >= 5:
            acumuladorMinutosFinde = acumuladorMinutosFinde + (tiempoDeServicio[1] - iterador)
        # Falto una hora de semana
        elif tiempoDeServicio[1].weekday() < 5 and iterador.weekday() < 5:
            acumuladorMinutosSemana = acumuladorMinutosSemana + (tiempoDeServicio[1] - iterador)
        # De semana llega a fin de semana
        elif tiempoDeServicio[1].weekday() < 5 and iterador.weekday() >= 5:
            aux = datetime.combine(tiempoDeServicio.date(), datetime.min.time())
            acumuladorMinutosFinde = acumuladorMinutosFinde + (tiempoDeServicio[1] - aux)
            acumuladorMinutosSemana = acumuladorMinutosSemana + (aux - iterador)
        # De fin de semana llega a semana
        elif tiempoDeServicio[1].weekday() >= 5 and iterador.weekday() < 5:
            aux = datetime.combine(tiempoDeServicio.date(), datetime.min.time())
            acumuladorMinutosFinde = acumuladorMinutosFinde + (aux - iterador)
            acumuladorMinutosSemana = acumuladorMinutosSemana + (tiempoDeServicio[1] - aux)
            
    semanaHorasParciales = ceil(acumuladorMinutosSemana / timedelta(hours=1))
    findeHorasParciales = ceil(acumuladorMinutosFinde / timedelta(hours=1))
    precio = (deltaTiempoFinde + findeHorasParciales)*tarifa.getFinde() + (deltaTiempoSemana + semanaHorasParciales)*tarifa.getSemana()
    return precio
