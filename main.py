from base import RoadtitionBase

'''
Road generator:
    1)I generate the initial population, seen as a set of spiral arcs
    2)I generate the heir population ,joining the arcs with the Cartesian product between the inital set with itself ( excluding equal indices )
    
    i.e: 
    1) initial population=[S1, S2, S3]
    2) heir population=[S1+S2, S1+S3, S2+S1, S2+S3, S3+S1, S3+S2]
'''

class Roadtition(RoadtitionBase):
    def __init__(self, executor=None, map_size=None):
        super().__init__(executor=executor, map_size=map_size)

    def start(self):

        initial_roads_population = self.initial_population_generator(time_spent=1 / 4)
        self.hebi_generator(initial_roads_population)

        return None
