from matplotlib import pyplot as plt
import numpy as np
import csv

class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

class Operation:
    def __init__(self):
        self.TargetList = []
        self.Obstacles = []
        self.TargetNameList = []
        self.Target = self.ReadTargetCoordinates("parameters/Targets.csv")
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

class MazeMap(Operation):
    def __init__(self):
        super().__init__()
        self.barriers = []
        [(self.barriers.append(self.ObstacleGenerator(obstacle_iteration[0],obstacle_iteration[1],obstacle_iteration[2],obstacle_iteration[3]))) for obstacle_iteration in self.ObstaclesList]
    
    def MazeGenerator(self, x1, x2):
        self.maze = np.zeros((x1,x2))
        for i in self.barriers:
            for x,y in i:
                self.maze[x][y] = 8
        return self.maze
        
    def MazeUpdate(self,path,maze):
        for x, y in path[:(len(path)-1)]:
            if (x,y) != (0,0):
                self.maze[x][y] = 1
        return self.maze

def astar(maze, start, end):
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0
    open_list = []
    closed_list = []
    open_list.append(start_node)

    while len(open_list) > 0:
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index
        open_list.pop(current_index)
        closed_list.append(current_node)

        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] 

        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue
            if maze[node_position[0]][node_position[1]] != 0:
                continue
            new_node = Node(current_node, node_position)
            children.append(new_node)

        for child in children:
            for closed_child in closed_list:
                if child == closed_child:
                    continue
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue
            open_list.append(child)


if __name__ == "__main__":
    maze_map = MazeMap()
    maze = maze_map.MazeGenerator(21,21)
    route = []
    start = (0, 0)
    for x, y in maze_map.Target[0]:
        end = (x, y)
        path = astar(maze, start, end)
        maze = maze_map.MazeUpdate(path,maze)
        start =(x, y)
        route.append(path)
    [print("Target:{} | TraveledRoute:{}".format(maze_map.Target[1][i],route[i])) for i in range(0,len(route))]
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.canvas.set_window_title('A* Algorithm')
    fig.set_size_inches(10.5, 4.0)
    ax1.plot([x for xroute in route for x,y in xroute], [y for yroute in route for x,y in yroute], "b",
    [barrier[0] for q in maze_map.barriers for barrier in q],[barrier[1] for q in maze_map.barriers for barrier in q], "ro",
    [x for x, y in maze_map.Target[0]],[y for x, y in maze_map.Target[0]],"bo")
    ax2.imshow(np.rot90(maze), interpolation='nearest', cmap="RdGy", extent=[0, 20, 0, 20])
    plt.show()