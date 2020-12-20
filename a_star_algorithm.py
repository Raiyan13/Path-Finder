from queue import PriorityQueue
from tools import *

def h(p1, p2):
	x1, y1 = p1
	x2, y2 = p2
	return abs(x1 - x2) + abs(y1 - y2)


def find_shortest_path(came_from, current, draw, start):
	while current in came_from:
		current = came_from[current]
		if current == start:
			break
		current.make_shortest_path()
		draw()


def algorithm(draw, grid, start, end):
	cost = 0
	priority_queue = PriorityQueue()
	priority_queue.put((0, cost, start))
	came_from = {}

	g_cost = {node: float("inf") for row in grid for node in row}
	g_cost[start] = 0

	f_cost = {node: float("inf") for row in grid for node in row}
	f_cost[start] = h(start.get_current_position(), end.get_current_position())

	priority_queue_track = {start}

	while not priority_queue.empty():

        #need to check event here

		current = priority_queue.get()[2]
        #add related code when start from 45

		if current == end:
			find_shortest_path(came_from, end, draw, start)
			end.make_end()
			return True

        # need to check and traverse and update other things here

	return False