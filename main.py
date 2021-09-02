from src.functions import createMaze
from src.motoreGrafico import game
cols    = 10
rows    = 10
w       = 30
grid = createMaze(cols, rows, w)
game(grid, cols, rows, w, mode=False)
