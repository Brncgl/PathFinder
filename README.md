# Pathfinder A * Algorithm

I built path finding  algorithm which given from parameters. I based on A* algorithm. Two pathfinder reads the targets and obstacles parameters from the parameter file. It creates the first obstacles and goes to the targets one by one.

## Testing
``` python PathFinder.py ```
<p align="center">
  <img src="https://github.com/Brncgl/PathFinder-Astar-Algorithm/blob/master/image/test_image/PathFinder.png" alt="https://github.com/Brncgl/PathFinder-Astar-Algorithm/blob/master/image/test_image/PathFinder.png" width="400" />
</p>

```
Target:1 | StepCost:6 | TraveledRoute:[(1, 0), (2, 1), (3, 2), (4, 2), (5, 1), (6, 0), (7, 1)]
Target:2 | StepCost:6 | TraveledRoute:[(7, 1), (7, 2), (7, 3), (8, 4), (9, 4), (10, 4), (11, 3)]
Target:3 | StepCost:7 | TraveledRoute:[(11, 3), (11, 2), (12, 1), (13, 1), (14, 0), (15, 1), (16, 2), (17, 2)]
Target:4 | StepCost:9 | TraveledRoute:[(17, 2), (16, 3), (15, 4), (15, 5), (15, 6), (15, 7), (15, 8), (15, 9), (16, 10), (17, 10)]
Target:5 | StepCost:6 | TraveledRoute:[(17, 10), (16, 11), (15, 10), (14, 11), (13, 11), (12, 10), (11, 10)]
Target:6 | StepCost:6 | TraveledRoute:[(11, 10), (11, 11), (11, 12), (11, 13), (11, 14), (12, 15), (12, 16)]
Target:7 | StepCost:8 | TraveledRoute:[(12, 16), (13, 16), (14, 17), (15, 18), (16, 17), (17, 16), (18, 15), (19, 15), (20, 14)]
Target:8 | StepCost:10 | TraveledRoute:[(20, 14), (20, 15), (19, 16), (18, 17), (17, 18), (16, 18), (15, 19), (14, 19), (13, 20), (12, 20), (11, 19)]
Target:9 | StepCost:11 | TraveledRoute:[(11, 19), (10, 18), (9, 17), (8, 16), (7, 15), (6, 14), (6, 13), (5, 12), (4, 12), (3, 12), (2, 12), (1, 13)]
Target:10 | StepCost:3 | TraveledRoute:[(1, 13), (1, 12), (0, 11), (0, 10)]
Target:11 | StepCost:8 | TraveledRoute:[(0, 10), (1, 10), (2, 10), (3, 10), (4, 9), (4, 8), (3, 7), (2, 6), (1, 7)]
Target:RETURN | StepCost:7 | TraveledRoute:[(1, 7), (0, 6), (1, 5), (1, 4), (1, 3), (1, 2), (1, 1), (0, 0)]
```

``` python PathFinder1.py ```
<p align="center">
  <img src="image\test_image\PathFinder1.png" alt="image\test_image\PathFinder1.png" width="600" />
</p>

```
Target:1 | TraveledRoute:[(0, 0), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
Target:2 | TraveledRoute:[(7, 1), (7, 2), (7, 3), (8, 4), (9, 4), (10, 4), (11, 3)]
Target:3 | TraveledRoute:[(11, 3), (11, 2), (12, 1), (13, 1), (14, 1), (15, 2), (16, 2), (17, 2)]
Target:4 | TraveledRoute:[(17, 2), (17, 3), (16, 4), (15, 5), (15, 6), (15, 7), (15, 8), (15, 9), (16, 10), (17, 10)]
Target:5 | TraveledRoute:[(17, 10), (16, 11), (15, 10), (14, 10), (13, 10), (12, 10), (11, 10)]
Target:6 | TraveledRoute:[(11, 10), (12, 11), (11, 12), (11, 13), (11, 14), (12, 15), (12, 16)]
Target:7 | TraveledRoute:[(12, 16), (13, 15), (14, 15), (15, 15), (16, 15), (17, 15), (18, 15), (19, 15), (20, 14)]
Target:8 | TraveledRoute:[(20, 14), (20, 15), (19, 16), (18, 17), (17, 18), (16, 19), (15, 19), (14, 19), (13, 19), (12, 19), (11, 19)]
Target:9 | TraveledRoute:[(11, 19), (10, 18), (9, 17), (8, 16), (7, 15), (6, 14), (5, 15), (4, 15), (3, 15), (2, 15), (1, 14), (1, 13)]
Target:10 | TraveledRoute:[(1, 13), (0, 12), (0, 11), (0, 10)]
Target:11 | TraveledRoute:[(0, 10), (1, 10), (2, 10), (3, 10), (4, 9), (4, 8), (3, 7), (2, 7), (1, 7)]
Target:RETURN | TraveledRoute:[(1, 7), (0, 6), (0, 5), (0, 4), (0, 3), (0, 2), (0, 1), (0, 0)]
```
## Setup Specs
> * Ubuntu 18.04
> * Python 3.6
> * Matplotlib 3.1.1
> * Numpy 1.16.5
> * Pandas 0.25.1

## Parameter Files
### Target:
<p align="center">
  <img src="image\parameters_image\Target_CSV.png" alt="image\parameters_image\Target_CSV.png" width="300" />
</p>

### Obstacles (x1,y1)(x2,y2):
<p align="center">
  <img src="image\parameters_image\Obstacles_CSV.png" alt="image\parameters_image\Obstacles_CSV.png" width="300" />
</p>

## Reference Codes
- PathFinder A* Algorithm
  - https://rosettacode.org/wiki/A*_search_algorithm#Python

- PathFinder1 A* Algorithm
  - https://gist.github.com/dhavalptl630007/40b61e91ddf3538af095f768d6e0dcc4
