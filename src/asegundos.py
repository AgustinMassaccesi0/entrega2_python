def a_segundos(cancion):
    partes = cancion["duration"].split(":")
    return int(partes[0]) * 60 + int(partes[1])



