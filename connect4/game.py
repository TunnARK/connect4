from enum import Enum
from random import randrange

from sympy import true


class Cell(Enum):
    """Enumeration representing a Connect4 Cell."""

    EMPTY = "."
    A = "X"
    B = "O"


class Grid:
    """Grid of 42 Cells."""

    lines = 6
    columns = 7

    def __init__(self):
        """Initialize a "self.grid" member: a list of list of Cells."""
        self.grid = [[Cell.EMPTY] * self.columns for _ in range(self.lines)]

    def __str__(self) -> str:
        """Reprensent this Grid as an ASCII image."""
        ret = ""
        for line in range(self.lines - 1, -1, -1):
            ret += "|"
            for column in range(self.columns):
                ret += self.grid[line][column].value
            ret += "|\n"
        ret += "+" + "-" * self.columns + "+\n"
        ret += " " + "".join(str(i) for i in range(self.columns)) + "\n"
        return ret

    # Place le jeton dans une colonne en le stoppant sur la premiere ligne libre (si elle existe)
    def place(self, column: int, cell: Cell) -> int:
        """Put one Cell into one of the 7 columns of this grid. Return the line where
        the token stops."""
        for line in range(self.lines):
            if self.grid[line][column] == Cell.EMPTY:
                self.grid[line][column] = cell
                return line
        raise ValueError(f"Column {column} is full.")

    # Verifier si 4 jetons sont alignees horizentalement, verticalement ou diagmt
    def win(self, line: int, column: int) -> bool:
        """Check if the Cell at "line" / "column" is part of 4 Cells from the same
        player in a horizontal / vertical / diagonal line."""

        adjacent = 0 # compteur
        color = self.grid[line][column]
        
        # Horizontal
        for cell in self.grid[line]:
            if cell == color:
                adjacent += 1
                if adjacent == 4:
                    return True
            else:
                adjacent = 0

        # Vertical
        for c in range(self.columns):
            for l in range(self.lines):
                if self.grid[l][c] == color:
                    adjacent += 1
                    if adjacent == 4:
                        return True
                else:
                    adjacent = 0
            
        # TODO: Diagonal
        return False

    # Condition d arret en cas de match nul
    def tie(self) -> bool:
        """Check if the grid is full."""

        # verifier si toutes les cases sont deja remplis
        for c in range(self.columns):
            for l in range(self.lines):
                if self.grid[l][c] == Cell.EMPTY:
                    return False
        return True


class Player:
    # fonction qui necessite de savoir l etat de la grille (donc en parametre)
    """Abstract base class for Players in this game."""

    def play(self, grid: Grid) -> int:
        """Main method for the player: show them the current grid, and ask them on which
        column they want to play."""
        raise NotImplementedError


class Game:
    """Main class of this project."""

    def __init__(self, player_a: Player, player_b: Player):
        """Initialize a new game with 2 Players and a Grid."""
        self.player_a = player_a
        self.player_b = player_b
        self.grid = Grid()

    def main(self):
        """Let players play until one of the win or the grid is full."""
        while True:
            if self.play(self.player_a, Cell.A):
                print(self.grid)
                print("A wins !")
                break
            if self.grid.tie():
                print(self.grid)
                print("Tie.")
                break
            if self.play(self.player_b, Cell.B): # Attention different de player.play
                print(self.grid)
                print("B wins !")
                break
            if self.grid.tie():
                print(self.grid)
                print("Tie.")
                break

    def play(self, player: Player, cell: Cell) -> bool:
        """Process one turn for one player.

        Ask the player  on which column they want to play, ask the grid on which line
        the token stops, and check if this was a winning move."""
        column = player.play(self.grid)
        line = self.grid.place(column, cell)
        return self.grid.win(line, column)
