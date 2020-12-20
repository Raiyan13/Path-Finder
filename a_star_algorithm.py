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

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		current = priority_queue.get()[2]
		priority_queue_track.remove(current)

		if current == end:
			find_shortest_path(came_from, end, draw, start)
			end.make_end()
			return True

		for neighbor in current.neighbors:
			temp_g_cost = g_cost[current] + 1

			if temp_g_cost < g_cost[neighbor]:
				came_from[neighbor] = current
				g_cost[neighbor] = temp_g_cost
				f_cost[neighbor] = temp_g_cost + h(neighbor.get_current_position(), end.get_current_position())

				if neighbor not in priority_queue_track:
					cost += 1
					priority_queue.put((f_cost[neighbor], cost, neighbor))
					priority_queue_track.add(neighbor)
					neighbor.make_open()

		draw()

		if current != start:
			current.make_closed()
			
	return False