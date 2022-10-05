from .game import Game, Grid, Player, Cell
from connect4 import game


class CheaterB(Player):
    """This IA cheats and modify the grid to ensure player B wins."""

    def play(self, grid: Grid) -> int:
        #print(grid)
        cell = Cell.B
        Grid.place(grid, 1, cell)
        Grid.place(grid, 2, cell)
        Grid.place(grid, 3, cell)
        #print(grid)
        return 4
