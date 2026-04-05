def costo_envio(peso,zona):
    zonas = ['local', 'regional', 'nacional']
    
    if zona not in zonas:
        return 'Zona no válida. Las zonas disponibles son: local, regional, nacional.'
    

    costo = {
        'local':     [500,  1000, 2000],
        'regional':  [1000, 2500, 5000],
        'nacional':  [2000, 4500, 8000],
    }
    
    if peso <= 1:
        return costo[zona][0]
    elif peso <= 5:
        return costo[zona][1]
    else:
        return costo[zona][2]

