
# coding: utf-8

import random
import os
import pprint


def gale_shapley(M, W):
    """
    Dados dos sets M y W, devuelve un matching estable entre ellos.

    M y W deben ser diccionarios, donde cada clave es el elemento del
    set y su valor es una lista con ranking sobre cada uno de los
    elementos del otro set.
    """

    total = len(M)

    matching = {}
    inverse_matching = {}

    def _match(m, w):
        # print('matching ', m, ' y ', w)
        matching[m] = w
        inverse_matching[w] = m

    def _unmatch(m, w):
        # print('Unmatching ', m, ' y ', w)
        del matching[m]
        del inverse_matching[w]

    def _rank(prefs, k):
        return -prefs.index(k)

    while len(matching) < total:
        for m, preferences in M.items():
            # print('Starting with ', m)

            if m in matching:
                continue

            for w in preferences:
                if w not in inverse_matching:
                    _match(m, w)
                    break

                m1 = inverse_matching[w]

                if _rank(W[w], m) > _rank(W[w], m1):
                    _unmatch(m1, w)
                    _match(m, w)
                    break

    return matching


class TPSolver:
    sep = '|'

    def __init__(self, players=20, teams=2, path='preferencias', seed=1337):
        """
        players: numero de jugadores
        teams: numero de equipos
        path: ruta, en la que se van a generar archivos de preferencias
        seed: semilla para inicializar el random
        """
        self.players = players
        self.teams = teams
        self.path = path
        random.seed(seed)

    def generate_set_for_tp(self):
        """
        Genera y retorna sets P (jugadores) y T (equipos), con preferencias
        randomizadas sobre el otro set
        """
        players_l = list(range(1, self.players + 1))
        teams_l = list(range(1, self.teams + 1))
        p_prefs = {i: random.sample(teams_l, self.teams) for i in players_l}
        t_prefs = {i: random.sample(players_l, self.players) for i in teams_l}
        return p_prefs, t_prefs

    def wrap_prefs(self, prefs, n):
        return [str(i) + self.sep + str(j) for i in prefs for j in range(1, n + 1)]

    def adapt_set_for_gs(self, players, teams):
        """
        Convierte sets de preferencias de PxT jugadores y TxP equipos a PxP para
        que se le pueda aplicar gale shapley. Para ello extiende la cantidad de
        equipos a P, y cambia las preferencias de los jugadores.
        """
        n = len(players) // len(teams)

        players_adapted = {}
        teams_adapted = {}

        for p, prefs in players.items():
            players_adapted[p] = self.wrap_prefs(prefs, n)

        for t, prefs in teams.items():
            for t_adapted in self.wrap_prefs([t], n):
                teams_adapted[t_adapted] = prefs

        return players_adapted, teams_adapted

    def unwrap_set_after_gs(self, matching):
        """
        Convierte el matching retornado por gale shapley a las dimensiones PxT
        iniciales.
        """
        matching_players = {}

        for k, v in matching.items():
            matching_players[k] = int(v.split(self.sep)[0])
        return matching_players

    def write_set_as_files(self, players, teams):
        """
        Escribe el set generado como archivos en formato, pedido por el tp
        """
        if not os.path.exists(self.path):
            os.makedirs(self.path)

        for s, n in [(players, 'jugador_{}.prf'), (teams, 'equipo_{}.prf')]:
            for k, v in s.items():
                path = os.path.join(self.path, n.format(str(k)))
                with open(path, 'w') as f:
                    f.write('\n'.join(map(str, v)))

    def read_set_from_files(self, path=None):
        """
        Lee los sets de jugadores y equipos desde una ruta especificada.
        """
        players, teams = {}, {}

        for s, k, n in [(players, self.players, 'jugador_{}.prf'),
                        (teams, self.teams, 'equipo_{}.prf')]:
            for i in range(1, k + 1):
                with open(os.path.join(path, n.format(str(i)))) as f:
                    s[i] = list(map(int, f.read().split('\n')))
        return players, teams

    def reverse_match(self, m):
        """ Invierte el matching de jugador->equipo a equipo->jugador """
        r = {v: [] for v in set(m.values())}
        for k, v in m.items():
            r[v].append(k)
        return r

    def solve_tp(self, generate_files=True):
        """
        Resuelve el tp. Si generate_files está en False, va a  leer los
        sets desde la ruta especificada
        """
        if generate_files:
            players, teams = self.generate_set_for_tp()
            self.write_set_as_files(players, teams)
        else:
            players, teams = self.read_set_from_files(self.path)

        M, W = self.adapt_set_for_gs(players, teams)
        m = gale_shapley(M, W)
        return self.unwrap_set_after_gs(m)


def main():
    s = TPSolver(players=200, teams=20)
    m = s.solve_tp()
    print('Equipo: [jugador1...jugadorN]\n')
    pprint.pprint(s.reverse_match(m))


if __name__ == '__main__':
    main()
