
def calcular_puntaje_ronda (scores):
    return {
                participante: sum(jueces.values())
                for participante,jueces in scores.items()
    }

def calcular_valores (puntaje_ronda,total_acumulado, mejor_puntaje):
    for participante, puntaje in puntaje_ronda.items():
        total_acumulado[participante] += puntaje
        if puntaje > mejor_puntaje[participante]:
            mejor_puntaje[participante] = puntaje

def calcular_ganador(puntaje_ronda):
    return max(puntaje_ronda, key=puntaje_ronda.get)