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
        if sem < 0 or fin < 0:
            raise Exception('No existen las Tarifas Negativas')
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
    
    
    iterador = tiempoDeServicio[0]
    
    if tiempoDeServicio[0].weekday() >= 5:
        semana = False
    else:
        semana = True
        
    deltaTiempoSemana = 0
    deltaTiempoFinde = 0
    while iterador + timedelta(hours=1) < tiempoDeServicio[1]:
        iterador = iterador + timedelta(hours=1)
        if iterador.weekday() >= 5:
            # Se toma que, si se pasan algunos minutos en la semana antes de llegar al fin de semana,
            # entonces consumio una hora de semana
            if semana:
                deltaTiempoSemana = deltaTiempoSemana + 1
            else:
                deltaTiempoFinde = deltaTiempoFinde + 1
            # Reiniciamos las horas de fin de semana como si contaramos desde 0
            iterador = datetime.combine(iterador.date(), datetime.min.time())
            semana = False
        else:
            # Se toma que, si se pasan algunos minutos en el fin semana antes de llegar a la semana,
            # entonces consumio una hora de fin de semana
            if not semana:
                deltaTiempoSemana = deltaTiempoSemana + 1
            else:
                deltaTiempoFinde = deltaTiempoFinde + 1
            # Reiniciamos las horas de semana como si contaramos desde 0
            iterador = datetime.combine(iterador.date(), datetime.min.time())
            semana = True
            
    # Sobraron tiempo
    if tiempoDeServicio[1] - iterador > timedelta():
        # Falto una hora de fin de semana
        if tiempoDeServicio[1].weekday() >= 5 and iterador.weekday() >= 5:
            deltaTiempoFinde = deltaTiempoFinde + 1
        # Falto una hora de semana
        elif tiempoDeServicio[1].weekday() < 5 and iterador.weekday() < 5:
            deltaTiempoSemana = deltaTiempoSemana + 1
        # Hay horas de fin de semana y semana como recargo
        else:
            deltaTiempoSemana = deltaTiempoSemana + 1
            deltaTiempoFinde = deltaTiempoFinde + 1
    
    """
    # Pasar todo fin de semana.
    if tiempoDeServicio[1].weekday() <= tiempoDeServicio[0].weekday() and tiempoDeServicio[0].weekday() < 5:
        deltaTiempoSemana = (resta - timedelta(hours = 48)).total_seconds()
        deltaTiempoFinde = timedelta(hours = 48).total_seconds()
    # Iniciar Semana y LLegar a Fin de semana
    elif tiempoDeServicio[0].weekday() < 5 and tiempoDeServicio[1].weekday() >= 5:
        deltaTiempoFinde = timedelta(hours=tiempoDeServicio[1].hour(), minutes=tiempoDeServicio[1].minute(), 
                                         seconds=tiempoDeServicio[1].second(), microseconds=tiempoDeServicio[1].microsecond())
        # Como se que fue a sabado o domingo, se que si fue a domingo pase todo sabado
        if tiempoDeServicio[1].weekday() == 6:
            deltaTiempoFinde = deltaTiempoFinde + timedelta(days=1)
        deltaTiempoSemana = (resta - deltaTiempoFinde).total_seconds()
        deltaTiempoFinde = deltaTiempoFinde.total_seconds()
    # Inicio Fin de Semana a Semana
    elif tiempoDeServicio[0].weekday() >= 5 and tiempoDeServicio[1].weekday() < 5:
        deltaTiempoFinde = timedelta(hours=tiempoDeServicio[0].hour(), minutes=tiempoDeServicio[1].minute(), 
                                         seconds=tiempoDeServicio[0].second(), microseconds=tiempoDeServicio[0].microsecond())
        # Como llegue a la semana e inicie el sabado, se que pase el domingo
        if tiempoDeServicio[0].weekday() == 5:
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
    """
    print(deltaTiempoFinde)
    print(deltaTiempoSemana)
    precio = deltaTiempoFinde*tarifa.getFinde() + deltaTiempoSemana*tarifa.getSemana()
    return precio

if __name__ == '__main__':
    a = Tarifa(1,0.01)
    print(a.getFinde())
    print(calcularPrecio(a, [datetime.today(), datetime(2017, 1, 25, 2)]))
    print(calcularPrecio(a, [datetime.today(), datetime(2017, 1, 25)]))
    print(calcularPrecio(a, [datetime.today(), datetime(2017, 1, 27)]))
    calcularPrecio(a, [datetime.today(), datetime(2017, 2, 23)])
# csm con palma
    