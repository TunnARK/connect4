from enum import Enum


class Cell(Enum):
    EMPTY = "."
    A = "X"
    B = "O"


class Grid:
    lines = 6
    columns = 7

    def __init__(self):
        self.grid = [[Cell.EMPTY] * self.columns for _ in range(self.lines)]

    def __str__(self) -> str:
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
        for line in range(self.lines):
            if self.grid[line][column] == Cell.EMPTY:
                self.grid[line][column] = cell
                return line
        raise ValueError(f"Column {column} is full.")

    # Verifier si 4 jetons sont alignees horizentalement, verticalement ou diagmt
    def win(self, line: int, column: int) -> bool:
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

        # TODO: Vertical
        # TODO: Diagonal
        return False

    # Condition d arret en cas de match nul
    def tie(self) -> bool:
        # TODO
        # verifier si toutes les cases sont deja remplis
        return False


class Player:
    # fonction qui necessite de savoir l etat de la grille (donc en parametre)
    def play(self, grid: Grid) -> int:
        raise NotImplementedError


class Game:
    def __init__(self, player_a: Player, player_b: Player):
        self.player_a = player_a
        self.player_b = player_b
        self.grid = Grid()

    def main(self):
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
        column = player.play(self.grid)
        line = self.grid.place(column, cell)
        return self.grid.win(line, column)
