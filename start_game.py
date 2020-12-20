from tools import *
from all_dialogs import show_info
from a_star_algorithm import algorithm

class StartNow:

    def __init__(self):
        pass

    def start(win, width):
        ROWS = 50
        grid = make_grid(ROWS, width)

        start = None
        end = None

        run = True
        while run:
            draw(win, grid, ROWS, width)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                # LEFT MOUSE BUTTON CLICKED
                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
                    row, col = get_clicked_pos(pos, ROWS, width)
                    node = grid[row][col]
                    if not start and node != end:
                        start = node
                        start.make_start()

                    elif not end and node != start:
                        end = node
                        end.make_end()

                    elif node != end and node != start:
                        node.make_obstacle()

                # RIGHT MOUSE BUTTON CLICKED
                elif pygame.mouse.get_pressed()[2]:
                    pos = pygame.mouse.get_pos()
                    row, col = get_clicked_pos(pos, ROWS, width)
                    node = grid[row][col]
                    node.reset_grid()
                    if node == start:
                        start = None
                    elif node == end:
                        end = None

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and start and end:
                        for row in grid:
                            for node in row:
                                node.update_neighbor_nodes(grid)

                        if algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end):
                            show_info("Shortest Path Found!", "Found The Shortest Path!!\nShown By Using Green Color!!!")
                        else:
                            show_info("No Path Found!", "All The Paths From Source Are Blocked :(")

                    if event.key == pygame.K_BACKSPACE:
                        start = None
                        end = None
                        grid = make_grid(ROWS, width)

        pygame.quit()