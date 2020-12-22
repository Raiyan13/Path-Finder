import pygame
from colors import *

HEIGHT = 650
WIDTH = 900

class Vertex:
	def __init__(self, row, col, width, total_rows):
		self.row = row
		self.col = col
		self.color = GRID
		self.width = width
		self.neighbors = []
		self.x = row * width
		self.y = col * width
		self.total_rows = total_rows

	def get_current_position(self):
		return self.row, self.col

	def make_start(self):
		self.color = CYAN

	def make_closed(self):
		self.color = WHITE

	def make_open(self):
		self.color = GRAY

	def make_obstacle(self):
		self.color = RED

	def make_end(self):
		self.color = MAGENTA

	def make_shortest_path(self):
		self.color = LIME

	def is_start(self):
		return self.color == CYAN

	def is_closed(self):
		return self.color == WHITE

	def is_open(self):
		return self.color == GRAY

	def is_obstacle(self):
		return self.color == RED

	def is_end(self):
		return self.color == MAGENTA

	def reset_grid(self):
		self.color = GRID

	def draw(self, win):
		pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

	def update_neighbor_nodes(self, grid):
		self.neighbors = []
		# DOWN
		if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_obstacle():
			self.neighbors.append(grid[self.row + 1][self.col])

		# UP
		if self.row > 0 and not grid[self.row - 1][self.col].is_obstacle():
			self.neighbors.append(grid[self.row - 1][self.col])

		# RIGHT
		if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_obstacle():
			self.neighbors.append(grid[self.row][self.col + 1])

		# LEFT
		if self.col > 0 and not grid[self.row][self.col - 1].is_obstacle():
			self.neighbors.append(grid[self.row][self.col - 1])

	def __lt__(self, other):
		return False

def make_grid(rows, width):
	grid = []
	gap = width // rows
	for i in range(rows):
		grid.append([])
		for j in range(rows):
			vertex = Vertex(i, j, gap, rows)
			grid[i].append(vertex)

	return grid


def draw_grid(win, rows, width):
	gap = width // rows
	for i in range(rows):
		pygame.draw.line(win, DARK_GRAY, (0, i * gap), (width, i * gap))
		for j in range(rows):
			pygame.draw.line(win, DARK_GRAY, (j * gap, 0), (j * gap, width))

def get_clicked_pos(pos, rows, width):
	gap = width // rows
	y, x = pos

	row = y // gap
	col = x // gap

	return row, col

def draw(win, grid, rows, width):
	win.fill(GRID)

	for row in grid:
		for node in row:
			node.draw(win)

	draw_grid(win, rows, width)
	pygame.display.flip()


