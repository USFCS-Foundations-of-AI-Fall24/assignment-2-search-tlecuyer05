import math
from queue import PriorityQueue

from Graph import *


class map_state() :
    ## f = total estimated cost
    ## g = cost so far
    ## h = estimated cost to goal
    def __init__(self, location, mars_graph="MarsMap",
                 prev_state=None, g=0,h=0):
        self.location = location
        self.mars_graph = read_mars_graph(mars_graph)
        self.prev_state = prev_state
        self.g = g
        self.h = h
        self.f = self.g + self.h

    def __eq__(self, other):
        return self.location == other.location

    def __hash__(self):
        return hash(self.location)

    def __repr__(self):
        return "(%s)" % (self.location)

    def __lt__(self, other):
        return self.f < other.f

    def __le__(self, other):
        return self.f <= other.f

    def is_goal(self):
        return self.location == '1,1'


def a_star(start_state, heuristic_fn, goal_test, use_closed_list=True) :
    search_queue = PriorityQueue()
    closed_list = {}
    search_queue.put(start_state)
    ## you do the rest.
    while not search_queue.empty():
        current_state = search_queue.get()
        if goal_test(current_state):
            goal_path = []
            while current_state:
                goal_path.append(current_state.location)
                current_state = current_state.prev_state
            print("Total states generated: ", len(closed_list))
            return goal_path[::-1] #Reverse the list order to show the start from '8,8'

        if use_closed_list:
            closed_list[current_state] = current_state.f
        neighbors = current_state.mars_graph.get_edges(current_state.location)
        for neighbor in neighbors:
            neighbor_state = map_state(neighbor.dest, prev_state=current_state,
                                       g=(current_state.g + 1), h=heuristic_fn(neighbor.dest))
            if neighbor_state not in closed_list or neighbor_state.f < closed_list[neighbor_state]:
                search_queue.put(neighbor_state)
    return None

def goal(state) :
    return state.location == "1,1"

## default heuristic - we can use this to implement uniform cost search
def h1(state) :
    return 0

## you do this - return the straight-line distance between the state and (1,1)
def sld(location):
    p1x, p1y = map(int, location.split(','))
    p2x, p2y = 1, 1
    return math.sqrt((p1x - p2x) ** 2 + (p1y - p2y) ** 2)

## you implement this. Open the file filename, read in each line,
## construct a Graph object and assign it to self.mars_graph().
def read_mars_graph(filename):
    mars_graph = Graph()  # Create and assign a new Graph object

    with open(filename, 'r') as file:
        for line in file:
            node, neighbors = line.split(":")
            node = node.strip()
            mars_graph.add_node(node)

            for neighbor in neighbors.strip().split():
                neighbor = neighbor.strip()
                edge = Edge(node, neighbor)
                mars_graph.add_edge(edge)
    return mars_graph


if __name__ == "__main__":
    s = map_state(location="8,8", g=0, h=sld("8,8"))
    a = a_star(s, sld, goal)
    print(len(a))
    print(a)
    s2 = map_state(location="8,8")
    b = a_star(s2, h1, goal)
    print(len(b))
    print(b)