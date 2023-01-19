from base import RoadtitionBase


class Roadtition(RoadtitionBase):
    def __init__(self, executor=None, map_size=None):
        self.executor=executor
        super().__init__(executor=executor, map_size=map_size)

    def start(self):

        while self.executor.time_budget.get_remaining_real_time() > 0:

            #print("\nSono nella popolazione iniziale")
            initial_roads_population = self.initial_population_generator(n_max_of_road = 5)

            #print("\nComincio a fare il crossover")
            heir_population_1 , oob = self.hebi_generator(initial_roads_population)
            heir_population , fitness = self.fitness_of_one_population(heir_population_1 , oob, len(heir_population_1))
            #print("\nheir_population: ", heir_population)

            #print("\n--------------Entro nella fitness function-----------------------")
            self.fitness_generator(heir_population = heir_population ,fitness_parent = fitness, oob = oob)

        return None

