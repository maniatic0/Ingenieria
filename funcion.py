'''
Created on Jan 23, 2017

@author: alexander
@author: christian
'''

from datetime import *
#from exceptions import *
from math import *

class Tarifa:
    _semana = 0.0
    _finde = 0.0
    def __init__(self, sem, fin):
        self._semana = sem
        self._finde = fin
        
    def getSemana(self):
        return self._semana
    
    def getFinde(self):
        return self._finde
    

def calcularPrecio(tarifa, tiempoDeServicio):
    if tiempoDeServicio[1] < tiempoDeServicio[0]:
        raise Exception('No puedes ir al pasado')
    resta = tiempoDeServicio[1] - tiempoDeServicio[0]
    if  resta < timedelta(minutes = 15):
        raise Exception('No puede ser menor a 15 minutos')
    if resta > timedelta(days = 7):
        raise Exception('No puede ser mayor a 7 dias')
    
    # Pasar todo fin de semana. TO DO falta mas 
    if tiempoDeServicio[1].weekday() < tiempoDeServicio[0].weekday():
        deltaTiempoSemana = (resta - timedelta(hours = 48)).total_seconds()
        deltaTiempoFinde = timedelta(hours = 48).total_seconds()
    # Iniciar Semana y LLegar a Fin de semana
    elif tiempoDeServicio[0].weekday() < 5 and tiempoDeServicio[1].weekday() >= 5:
        deltaTiempoFinde = timedelta(hours=tiempoDeServicio[1].hour(), minutes=tiempoDeServicio[1].minute(), 
                                         seconds=tiempoDeServicio[1].second(), microseconds=tiempoDeServicio[1].microsecond())
        if tiempoDeServicio[1].weekday() == 6:
            deltaTiempoFinde = deltaTiempoFinde + timedelta(days=1)
        deltaTiempoSemana = (resta - deltaTiempoFinde).total_seconds()
        deltaTiempoFinde = deltaTiempoFinde.total_seconds()
    # Inicio Fin de Semana a Semana
    elif tiempoDeServicio[0].weekday() >= 5 and tiempoDeServicio[1].weekday() < 5:
        deltaTiempoFinde = timedelta(hours=tiempoDeServicio[0].hour(), minutes=tiempoDeServicio[1].minute(), 
                                         seconds=tiempoDeServicio[0].second(), microseconds=tiempoDeServicio[0].microsecond())
        if tiempoDeServicio[0].weekday() == 6:
            deltaTiempoFinde = deltaTiempoFinde + timedelta(days=1)
        deltaTiempoSemana = (resta - deltaTiempoFinde).total_seconds()
        deltaTiempoFinde = deltaTiempoFinde.total_seconds()
    # Inicio Sabado a Domingo
    elif tiempoDeServicio[0].weekday() == 5 and tiempoDeServicio[1].weekday() == 6:
        deltaTiempoFinde = resta.total_seconds()
        deltaTiempoSemana = timedelta(0).total_seconds()
    # Inicio Semana a Semana
    elif tiempoDeServicio[0].weekday() < 5 and tiempoDeServicio[1].weekday() < 5:        
        deltaTiempoSemana = resta.total_seconds()
        deltaTiempoFinde = timedelta(0).total_seconds()
    # Inicio Domingo a Sabado
    elif tiempoDeServicio[0].weekday() == 6 and tiempoDeServicio[1].weekday() == 5:
        deltaSabado = timedelta(hours=24) - timedelta(hours=tiempoDeServicio[0].hour())
        deltaDomingo = timedelta(hours=tiempoDeServicio[1].hour()) - deltaSabado
        deltaTiempoFinde = deltaSabado + deltaDomingo
        deltaTiempoSemana = (resta - deltaTiempoFinde).total_seconds()
        deltaTiempoFinde = deltaTiempoFinde.total_seconds()
        
    # Calcular Precio
    deltaTiempoFinde = round(((deltaTiempoFinde / 24) / 24)+0.5)
    deltaTiempoSemana = round(((deltaTiempoSemana / 24) / 24)+0.5)
    precio = deltaTiempoFinde*tarifa.getFinde() + deltaTiempoSemana*tarifa.getSemana()
    return precio

if __name__ == '__main__':
    a = Tarifa(1,1)
    print(a.getFinde())
    calcularPrecio(a, [datetime.today(), datetime(2017, 1, 25)])
    calcularPrecio(a, [datetime.today(), datetime(2017, 2, 23)])
# csm con palma
    