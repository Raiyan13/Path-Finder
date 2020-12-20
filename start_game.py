from tools import *

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