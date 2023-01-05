from base import RoadtitionBase

'''
Generatore di strade:
    1)Genero la popolazione iniziale, vista come insieme di archi di spirali
    2)Genero la prole ,unendo gli archi con il prodotto cartesiano tra l'insieme inziale con se stesso ( escludendo indici uguali )
    
    Es: 
    1) strade_valide=[S1, S2, S3]
    2) strade_unite=[S1+S2, S1+S3, S2+S1, S2+S3, S3+S1, S3+S2]
   
'''


class Roadtition(RoadtitionBase):  # Roadtition() l'unione tra road e competition proprio quello che fa la classe
    def __init__(self, executor=None, map_size=None): #questi paramentri li prendo dalla stringa di comanda
        super().__init__(executor=executor, map_size=map_size) #inizializzatore della superclasse

    def start(self):
        #Metodo chiamato da competition.py al fine di generare i test

        strade_da_unire = self.initial_population_generator(choice=True, i_value=3,
                                                            time_spent=1 / 4)  # genero la popolazione iniziale

        self.hebi_generator(strade_da_unire)  # incrocio le strade della popolazione iniziale per generarne di nuove

        return None


'''
Come avviare il programma a linea di comando?

python competition.py 
--time-budget 180 
--executor mock 
--beamng-home C:/Users/Dexter/Desktop/BeamNG.tech.v0.26.1.0 
--beamng-user C:/Users/Dexter/Desktop 
--map-size 200 
--module-path C:/Users/Dexter/Desktop/CompetiMio 
--module-name main 
--class-name Roadtition
'''