
from math import ceil

from batalla_naval import Estrategia, Juego


class EstrategiaGreedy(Estrategia):

    def siguiente_turno(self, tablero, lanzaderos, barcos, turno):
        """
        """

        disparos = []
        vidas = {k: v['vida'] for k, v in barcos.items() if v['vida'] > 0}

        disparos_pendientes = lanzaderos

        while disparos_pendientes:

            barco_a_hundir = {}
            barco_a_disparar = {}
            for k, v in vidas.items():
                danio = tablero[k][barcos[k]['posicion']]
                if v <= 0 or danio <= 0:
                    continue
                disparos_necesarios = ceil(v / danio)
                if disparos_pendientes >= disparos_necesarios:
                    if not barco_a_hundir or (
                        barco_a_hundir['disparos'] > disparos_necesarios or
                        (barco_a_hundir['disparos'] == disparos_necesarios
                         and barco_a_hundir['daño'] < danio * disparos_necesarios)):
                        barco_a_hundir.update({'barco': k, 'disparos': disparos_necesarios,
                                             'daño': danio * disparos_necesarios})
                if not barco_a_disparar or barco_a_disparar['daño'] < danio:
                    barco_a_disparar.update({'barco': k, 'daño': danio})

            if barco_a_hundir:
                disparos.extend([barco_a_hundir['barco']] * barco_a_hundir['disparos'])
                disparos_pendientes -= barco_a_hundir['disparos']
                vidas[barco_a_hundir['barco']] = 0
            elif barco_a_disparar:
                disparos.append(barco_a_disparar['barco'])
                disparos_pendientes -= 1
                vidas[barco_a_disparar['barco']] -= barco_a_disparar['daño']
            else:
                # No quedan más barcos con vidas, relleno el vector de disparos con basura
                disparos.extend([0] * (lanzaderos - len(disparos)))
                break

        return disparos



if __name__ == '__main__':
    estrategia = EstrategiaGreedy()
    Juego(tablero_file='tablero2', lanzaderos=3,
          estrategia=estrategia).jugar()
