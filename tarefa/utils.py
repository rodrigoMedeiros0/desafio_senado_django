from math import modf

def formatar_horas(total_horas):
    horas, minutos_decimais = divmod(total_horas, 1)
    minutos = int(minutos_decimais * 60)
    
    return f'{int(horas):02}:{minutos:02}'
