import matplotlib.pyplot as plt
import sys
import csv

class Barrier:
    def __init__(self):
        self.TargetList = []
        self.Obstacles = []
        self.TargetNameList = []
        global Target 
        Target = self.ReadTargetCoordinates("parameters/Targets.csv")
        self.ObstaclesList = self.ReadObstacleCoordinates("parameters/Obstacles.csv")

    def ReadTargetCoordinates(self, file):
        with open(file) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            [(self.TargetList.append([int(row[0]), int(row[1])]),self.TargetNameList.append(row[2])) for row in readCSV]
        return self.TargetList, self.TargetNameList

    def ReadObstacleCoordinates(self,file):
        with open(file) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            [(self.Obstacles.append([int(row[0]),int(row[1]),int(row[2]),int(row[3])])) for row in readCSV] #[[x1,x2,y1,y2],[x1,x2,y1,y2],...]
        return self.Obstacles

    def ObstacleGenerator(self,x1,x2,y1,y2):
        set_of_obstacles = set()
        [(set_of_obstacles.add((i,y1)),set_of_obstacles.add((i,y2))) for i in range(x1,x2+1)]
        [(set_of_obstacles.add((x1,i)),set_of_obstacles.add((x2,i))) for i in range(y1,y2+1)]
        self.obstacles_list = list(set_of_obstacles)
        return self.obstacles_list

class AStarGraph(Barrier):
    def __init__(self):
        super().__init__()
        self.barriers = []
        self.barriers_grap = []
        [(self.barriers.append(self.ObstacleGenerator(obstacle_iteration[0],obstacle_iteration[1],obstacle_iteration[2],obstacle_iteration[3])),self.barriers_grap.append(self.ObstacleGenerator(obstacle_iteration[0],obstacle_iteration[1],obstacle_iteration[2],obstacle_iteration[3]))) for obstacle_iteration in self.ObstaclesList]
    
    def heuristic(self, start, goal):
        D = 1
        D2 = 1
        dx = abs(start[0] - goal[0])
        dy = abs(start[1] - goal[1])
        return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)

    def get_vertex_neighbours(self, pos):
        n = []
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
            x2 = pos[0] + dx
            y2 = pos[1] + dy
            if x2 < 0 or x2 > 20 or y2 < 0 or y2 > 20:
                continue
            n.append((x2, y2))
        return n

    def move_cost(self, a, b):
        for barrier in self.barriers:
            if b in barrier:
                return 100
        return 1

    def barrier_update(self, traveledroute):
        #[(self.barriers.append([v])) for route in traveled_route for v in route]
        self.barriers.append(traveledroute)
        #index = []
        #[(index.append((i,j))) for i in range(len(self.barriers)) for j in range(len(self.barriers[i])) if (0, 0) == self.barriers[i][j]]
        #[(self.barriers[i].pop(j)) for i,j in index]
        return self.barriers

def AStarSearch(start, end, graph):
    G = {}
    F = {} 
    G[start] = 0
    F[start] = graph.heuristic(start, end)
    closedVertices = set()
    openVertices = set([start])
    cameFrom = {}

    while len(openVertices) > 0:
        current = None
        currentFscore = None
        for pos in openVertices:
            if current is None or F[pos] < currentFscore:
                currentFscore = F[pos]
                current = pos

        if current == end:
            path = [current]
            while current in cameFrom:
                current = cameFrom[current]
                path.append(current)
            path.reverse()
            return path, F[end], path

        openVertices.remove(current)
        closedVertices.add(current)

        for neighbour in graph.get_vertex_neighbours(current):
            if neighbour in closedVertices:
                continue
            candidateG = G[current] + graph.move_cost(current, neighbour)
            if neighbour not in openVertices:
                openVertices.add(neighbour)
            elif candidateG >= G[neighbour]:
                continue

            cameFrom[neighbour] = current
            G[neighbour] = candidateG
            H = graph.heuristic(neighbour, end)
            F[neighbour] = G[neighbour] + H
    raise RuntimeError("A* failed to find a solution")

if __name__ == "__main__":
    graph = AStarGraph()
    traveled_route = []
    step_cost = []
    start = (1,0)
    for x, y in Target[0]:
        result, cost ,path = AStarSearch(start, (x,y), graph)
        traveled_route.append(path)
        step_cost.append(cost)
        graph.barrier_update(result)
        start =(x,y)
        
    [print("Target:{} | StepCost:{} | TraveledRoute:{}".format(Target[1][i],step_cost[i],traveled_route[i])) for i in range(0,len(Target[1]))]
    plt.plot([v[0] for route in traveled_route for v in route], [v[1] for route in traveled_route for v in route],'b',
    [obs[0] for i in graph.barriers_grap for obs in i],[obs[1] for i in graph.barriers_grap for obs in i],"rs",
    1,0,"bo",[target[0] for target in Target[0]],[target[1] for target in Target[0]],"bo")
    plt.show()