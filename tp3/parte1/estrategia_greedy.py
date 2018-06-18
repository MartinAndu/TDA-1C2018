
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

            barco_a_matar = {}
            mejor_barco_a_disparar = {}
            for k, v in vidas.items():
                danio = tablero[k][barcos[k]['posicion']]
                if v <= 0 or danio <= 0:
                    continue
                disparos_necesarios = ceil(v / danio)
                if disparos_pendientes >= disparos_necesarios:
                    if not barco_a_matar or (
                        barco_a_matar['disparos'] > disparos_necesarios or
                        (barco_a_matar['disparos'] == disparos_necesarios
                         and barco_a_matar['daño'] < danio * disparos_necesarios)):
                        barco_a_matar.update({'barco': k, 'disparos': disparos_necesarios,
                                             'daño': danio * disparos_necesarios})
                if not mejor_barco_a_disparar or mejor_barco_a_disparar['daño'] < danio:
                    mejor_barco_a_disparar.update({'barco': k, 'daño': danio})

            if barco_a_matar:
                disparos.extend([barco_a_matar['barco']] * barco_a_matar['disparos'])
                disparos_pendientes -= barco_a_matar['disparos']
                vidas[barco_a_matar['barco']] = 0
            elif mejor_barco_a_disparar:
                disparos.append(mejor_barco_a_disparar['barco'])
                disparos_pendientes -= 1
                vidas[mejor_barco_a_disparar['barco']] -= mejor_barco_a_disparar['daño']
            else:
                # No quedan más barcos con vidas, relleno el
                disparos.extend([0] * (lanzaderos - len(disparos)))
                break

        return disparos



if __name__ == '__main__':
    estrategia = EstrategiaGreedy()
    Juego(tablero_file='tablero3', lanzaderos=3,
          estrategia=estrategia).jugar()
