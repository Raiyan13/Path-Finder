import pygame
from colors import *

HEIGHT = 650
WIDTH = 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Path Finder...")

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

	def update_neighbors(self, grid):
		pass

	def __lt__(self, other):
		return False


