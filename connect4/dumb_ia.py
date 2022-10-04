from .game import Cell, Game, Grid, Player


class DumbIA(Player):
    """IA which play on the column of the first possible empty cell it finds."""

    # Doit retourner la column a jouer (ici la premiere colonne libre)
    def play(self, grid: Grid) -> int:
        # Parcours des colonnes pour trouver la premiere colonne libre
        for line in range(grid.lines): 
            for column in range(grid.columns):
            # test si cell empty
                if grid.grid[line][column] == Cell.EMPTY:
                    return column
        raise ValueError(f"Grid is full")