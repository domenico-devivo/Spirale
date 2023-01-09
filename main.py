from base import RoadtitionBase

'''
Generatore di strade:
    1)Genero la popolazione iniziale, vista come insieme di archi di spirali
    2)Genero la popolazione erede ,unendo gli archi con il prodotto cartesiano tra l'insieme inziale con se stesso ( escludendo indici uguali )
    
    Es: 
    1) strade_valide=[S1, S2, S3]
    2) strade_unite=[S1+S2, S1+S3, S2+S1, S2+S3, S3+S1, S3+S2]
'''


class Roadtition(RoadtitionBase):
    def __init__(self, executor=None, map_size=None):
        super().__init__(executor=executor, map_size=map_size)

    def start(self):

        initial_roads_population = self.initial_population_generator(time_spent=1 / 4)
        self.hebi_generator(initial_roads_population)

        return None
