import math
import numpy as np
from random import randint, random
from code_pipeline.tests_generation import RoadTestFactory
from code_pipeline.visualization import RoadTestVisualizer


class RoadtitionBase():
    def __init__(self, executor=None, map_size=None):
        self.executor = executor  # attributo che definisce il tipo di esecutore
        self.map_size = map_size  # dimensione della mappa
        self.visualize = RoadTestVisualizer(self.map_size)  # per visualizzare le strade a video

    def execute_test(self, road_points):
        '''
        Metodo usato per generare test

        :param road_points: cartesian points of the road
        :return: the result of the test [Pass, Fail, Invalid or Error]
        '''

        # trasformo la strada in un formato necessario per il testing
        test = RoadTestFactory.create_road_test(road_points)

        # Con execute_tes si testa la strada precedentemente creata
        test_outcome, description, execution_data = self.executor.execute_test(test)
        print("\033[1;34m test_outcome= \033[1;31m", test_outcome, "\033[1;30m")
        self.visualize.visualize_road_test(test)

        return test_outcome

    def initial_population_generator(self, time_spent=1 / 4):
        '''
        Genera la popolazione iniziale

        :param time_spent: part of the total time that are spent for generate the starting population

        :return: list of road seen as initial population
        '''
        i = 0
        strade_da_unire = []

        while self.executor.time_budget.get_remaining_real_time() > self.executor.time_budget.time_budget * (1 - time_spent) :
            if (i % 2 == 0): #se i è pari allora genero un arco di ellisse in senso antiorario Sx <--
                road_points = self.bow(c_x0=randint(60, 120), c_y0=randint(60, 100), radius=randint(40, 70),
                                       interpolation_points=randint(4, 5), Angle_init=randint(295, 360),
                                       Angle_final=randint(180, 245))

            else: # se i è dispari allora genero un arco di ellisse in senso orario --> Dx
                road_points = self.bow(c_x0=randint(60, 120), c_y0=randint(60, 100), radius=randint(40, 70),
                                       interpolation_points=randint(4, 5), Angle_init=randint(0, 65),
                                       Angle_final=randint(115, 180))

            test_outcome = self.execute_test(road_points)

            if test_outcome != "ERROR":
                strade_da_unire.append(road_points)

            i = i + 1

        return strade_da_unire

    def hebi_generator(self, strade_da_unire):

        for i in range(0, len(strade_da_unire)):
            for j in range(0, len(strade_da_unire)):

                if i != j:
                    x1, y1 = self.roadpoint_to_xy(strade_da_unire[i])  # trasformo le prime 2 in coordinate x,y
                    x2, y2 = self.roadpoint_to_xy(strade_da_unire[j])  # trasformo le prime 2 in coordinate x,y
                    x_unione, y_unione = self.crossover(x1, y1, x2, y2)  # crossover tra le 2 strade
                    x_reframe, y_reframe = self.reframe(x_unione, y_unione)
                    new_road_point = self.xy_to_roadpoint(x_reframe, y_reframe)
                    self.execute_test(new_road_point)
        return None

    def bow(self, c_x0, c_y0, radius, interpolation_points, Angle_init, Angle_final):
        # Generatore di strade modellate come archi di spirali
        raggio_v = radius
        random_coef= randint(3,4)
        road_points = []

        center_x = c_x0
        center_y = c_y0

        angles_in_deg = np.linspace(Angle_init, Angle_final, num=interpolation_points)

        for angle_in_rads in [math.radians(a) for a in angles_in_deg]:
            raggio_v = raggio_v + random() * random_coef#  # RAGGIO_VARIABILE, potresti giocare con quel *2 e mettere un randint(iniziale,finale)
            x = math.sin(angle_in_rads) * raggio_v + center_x
            y = math.cos(angle_in_rads) * raggio_v + center_y
            road_points.append((x, y))


        return road_points

    def crossover(self, x1, y1, x2, y2):
        x_temp = []
        x_diff = x2[0] - x1[-1]  # differenza tra il primo del secondo e l'ultimo del primo
        y_temp = []
        y_diff = y2[0] - y1[-1]
        for t in range(0, len(x2)):
            x_temp.append(x2[t] - x_diff)  # vado a sottrarre il valore differenza per unire le 2 strade e crearne una sola

        for i in range(0, len(y2)):  # devo traslare tutti i valori di y2
            y_temp.append(y2[i] - y_diff)  # vado a togliere la differenza di altezza tra i 2 valori, in modo da rendere la curva continua

        # quando unisco le due strade nel punto di congiunzione ci sono 2 punti consecutivi (x,y) uguali e il programma genera errore.
        # quindi li elimino entrambi
        del x_temp[0]
        del y_temp[0]

        del x1[-1]
        del y1[-1]

        x_unione = [*x1, *x_temp]  # unione delle ascisse
        y_unione = [*y1, *y_temp]  # unione delle ordinate

        return x_unione, y_unione

    def xy_to_roadpoint(self, x, y):
        road_point = []
        for i in range(0, len(x)):
            road_point.append((x[i], y[i]))
        return road_point

    def roadpoint_to_xy(self, road_point):
        x = [x for x, y in road_point]
        y = [y for x, y in road_point]
        return x, y

    def reframe(self, x_unione, y_unione):
        x_reframe = x_unione
        y_reframe = y_unione

        if (min(x_unione) < 10 or max(x_unione) > 180) and (max(x_unione) - min(x_unione)) < 180:
            if (min(x_unione) < 10):
                inc_x = 10 - min(x_unione)
                for i in range(0, len(x_unione)):
                    t = x_unione[i]
                    x_reframe[i] = t + inc_x
            elif (max(x_unione) > 180):
                dec_x = 180 - max(x_unione)
                for i in range(0, len(x_unione)):
                    t = x_unione[i]
                    x_reframe[i] = t + dec_x

        if (min(y_unione) < 10 or max(y_unione) > 180) and (max(y_unione) - min(y_unione)) < 180:
            if (min(y_unione) < 10):
                inc_y = 10 - min(y_unione)
                for i in range(0, len(y_unione)):
                    t = y_unione[i]
                    y_reframe[i] = t + inc_y
            elif (max(y_unione) > 180):
                dec_y = 180 - max(y_unione)
                for i in range(0, len(y_unione)):
                    t = y_unione[i]
                    y_reframe[i] = t + dec_y

        if (max(x_unione) - min(x_unione)) > 180 or (max(y_unione) - min(y_unione)) > 180:
            x_d, y_d = self.halve(x_reframe, y_reframe)
            x_reframe, y_reframe = self.reframe(x_d, y_d)

        return x_reframe, y_reframe

    def halve(self, x, y):

        slice_x = len(x) // 4           # voglio togliere 1/2 dei punti x, quindi:
        del x[0:slice_x]                # tolgo 1/4 dei punti all'inizio
        del x[len(x) - slice_x:len(x)]  # tolgo 1/4 dei punti alla fine

        slice_y = len(y) // 4           # stessa cosa faccio con l'ordiante
        del y[0:slice_y]
        del y[len(y) - slice_y:len(y)]

        return x, y
