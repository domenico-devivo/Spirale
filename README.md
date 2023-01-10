# Spirale at Cyber-Physical Systems Testing Competition

**_Spirale_** is a program made for participate at [SBST](https://sbst21.github.io/tools/) competition.

In particular in the branch of CPS testing competition, based on the generation of random roads as input in a self-driving cars simulation environment.

### What is the structure of Spirale?

The program use a genetic approach which generate sets of roads modeled as arcs of spirals.
- Initially generating a random starting population of roads
- Subsequently this inizial population is crossed with itself for generate a set of offsping roads

### What are the goals ?

- Minimize the invalid tests. This is done framed, define a intervall of values in which specify the inizial end the final points, and build bow that non intersect.
- Maximize the tests that outcome as "Fail". Discarding the test that are falg as "Error", and crossed randomically the roads.

### How it works?
The run of Spirale depends on the pipeline of the [CPS too competition](https://github.com/sbft-cps-tool-competition/cps-tool-competition).
The minimum number of input values to start it are:
> python competition.py --time-budget 180 --executor mock --map-size 200 --module-path ../Spirale --module-name main --class-name Roadtition

The _competition.py_ expects to find the start() method that must be implemented in the Roadtition class ( placed in the _main_ module ).

1) The first method called inside start() is initial_population_generator() , in which the roads are created whose curvatures are derived from spiral arcs.
 In the below image there is an example of tested valid road of initial population:

![A single road](https://user-images.githubusercontent.com/108838837/211591654-c62199c8-abfb-4670-a79e-a2e403217710.png)

2)The second method called inside start() is hebi_generator(initial_population_of_roads) in which takes place the crossover between two different roads of the initial population. Hebi means snake in japanee like the new road in the image:

![A single crossover](https://user-images.githubusercontent.com/108838837/211593200-c45bdaf3-5112-4f08-98e7-a58d4e1c5206.png)

3) For every valid road the competition.py calls also some mathods for validate the road. At the end of the time_budget the result of the program is a 
![A result](https://user-images.githubusercontent.com/108838837/211600193-dad3c582-94fa-478a-a4f1-b460c5ddb0ca.png)
