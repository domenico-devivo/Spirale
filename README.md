# Spirale at Cyber-Physical Systems Testing Competition

Spirale is a program made for participate at [SBST](https://sbst21.github.io/tools/) competition.

In particular in the branch of CPS testing competition, based on the generation of random roads as input in a self-driving cars simulation environment.

### What is the structure of Spirale?

The program use a genetic approach which generate sets of roads modeled as arcs of spirals.
- Initially generating a random starting population of roads
- Subsequently this inizial population is crossed with itself for generate a set of offsping roads

### What are the goals ?

- Minimize the invalid tests. This is done framed, define a intervall of values in which specify the inizial end the final points, and build bow that non intersect
- Maximize the tests that outcome as "Fail". Discarding the test that are falg as "Error", and crossed randomically the roads

### How it works?

![A single road](https://user-images.githubusercontent.com/108838837/211591654-c62199c8-abfb-4670-a79e-a2e403217710.png)

![A single crossover](https://user-images.githubusercontent.com/108838837/211593200-c45bdaf3-5112-4f08-98e7-a58d4e1c5206.png)
