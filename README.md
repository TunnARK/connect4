# Connect 4

TP n°1 de Conception Orientée Objet pour le M2 auro.

## Objectifs

1. commenter le décorateur `skip` pour `tests.test_game.TestGame.test_dumb_6` et implémenter
   `connect4.dump_ia.DumbIA.play` jusqu’à ce que `python -m unittest` fonctionne à nouveau
2. commenter le décorateur `skip` pour `tests.test_game.TestGame.test_column_win` et améliorer
   `connect4.game.Grid.win` jusqu’à ce que `python -m unittest` fonctionne à nouveau
3. commenter le décorateur `skip` pour `tests.test_game.TestGame.test_tie` et implémenter
   `connect4.game.Grid.tie` jusqu’à ce que `python -m unittest` fonctionne à nouveau. `python -m connect4` devrait
   également fonctionner.
4. implémenter `connect4.console_player.ConsolePlayer.play` jusqu’à ce que que le jeu soit utilisable avec
   `python -m connect4 --player-a ConsolePlayer`


--- 

> Notes du 2022/09/30 - Start





# Informations utiles

[Repo GitHub pour le TP1 Connect4](https://github.com/nim65s/connect4)

> N.B.:
    - Python fait croire que c'est un code interpreté (i.e. qui n'a pas besoin de compilation) alors quil conserve un cache de compilation en interne
    - Pypy lui est un code interpreté car il exécute directement

# Presentation du projet

## Class Cell
```python
class Cell(Enum):
    EMPTY = "."
    A = "X"
    B = "O"
```
## Class Grid

> Toute les méthodes de toutes les classes continnent des `self` ! (Hors exception)

```python
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
```

## Class Player

```python
class Player:
    # fonction qui necessite de savoir l etat de la grille (donc en parametre)
    def play(self, grid: Grid) -> int:
        raise NotImplementedError
```

## Class Game

```python
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
```

# Execution

- [__main__.py]()

Fichier qui crée un instance du jeu game avec un player A et B pour ensuite lancer le `game.main`

Lancer ce fichier ne fonctionnera pas plustot lancer les tests

## test_game.py

- [lien vers le fichier test_game.py](https://github.com/nim65s/connect4/blob/main/tests/test_game.py)

1. Lancer la commande `python3 -m unittest`
    Retourne:
    ```
    ssss..ss
    ----------------------------------------------------------------------
    Ran 8 tests in 0.001s

    OK (skipped=6)
    ```
2. Vérifier que le test fonctionne réellement en y créant une erreur voulue
    - Enlever une ligne de la grille
    - Relancer le test
    Retourne:
    ```
    ssssF.ss
    ======================================================================
    FAIL: test_grid_str (tests.test_game.TestGame)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
    File "/home/tunn/Documents/GitHub/connect4/tests/test_game.py", line 20, in test_grid_str
        self.assertEqual("\n" + str(grid), GRID_DUMB_6)
    AssertionError: '\n|.[23 chars].....|\n|.......|\n|.......|\n|XOXOXO.|\n+-------+\n 0123456\n' != '\n|.[23 chars].....|\n|.......|\n|XOXOXO.|\n+-------+\n 0123456\n'
    
    - |.......|
    |.......|
    |.......|
    |.......|
    |.......|
    |XOXOXO.|
    +-------+
    0123456


    ----------------------------------------------------------------------
    Ran 8 tests in 0.001s

    FAILED (failures=1, skipped=6)
    ```

# Travail à faire

1. commenter le décorateur `skip` pour `tests.test_game.TestGame.test_dumb_6` et implémenter
   `connect4.dump_ia.DumbIA.play` jusqu’à ce que `python -m unittest` fonctionne à nouveau
    - L'IA doit simplement jouer une colonne si celle-ci est vide
    - Faire en sorte que l'on obtienne cette grille
    ```
    |.......|
    |.......|
    |.......|
    |.......|
    |.......|
    |XOXOXO.|
    +-------+
    0123456
    ```
2. commenter le décorateur `skip` pour `tests.test_game.TestGame.test_column_win` et améliorer
   `connect4.game.Grid.win` jusqu’à ce que `python -m unittest` fonctionne à nouveau
   - Completer la section `vertical` de `connect4.game.Grid.win` jusqu'à ce que l'unittest fonctionne
3. commenter le décorateur `skip` pour `tests.test_game.TestGame.test_tie` et implémenter
   `connect4.game.Grid.tie` jusqu’à ce que `python -m unittest` fonctionne à nouveau. `python -m connect4` devrait
   également fonctionner.
4. implémenter `connect4.console_player.ConsolePlayer.play` jusqu’à ce que que le jeu soit utilisable avec
   `python -m connect4 --player-a ConsolePlayer`



> Notes du 2022/09/30 - End

---