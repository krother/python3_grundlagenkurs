"""
Flucht aus dem Labyrinth
"""
import arcade
from arcade.draw_commands import load_texture
from arcade.key import MOTION_UP, MOTION_DOWN, MOTION_LEFT, MOTION_RIGHT
from arcade.key import ESCAPE


wand = load_texture("tiles.png", 0, 0, 32, 32)
boden = load_texture("tiles.png", 0, 32, 32, 32)
pac = load_texture("tiles.png", 0, 96, 32, 32)

LABYRINTH = """
    ##########
    #........#
    #.#.####.#
    #.#......#
    #.#....#.#
    #.#....#.#
    #......#.#
    #.####.#.#
    #........#
    ##########"""


LEVEL = []
for zeile in LABYRINTH.strip().split():
    LEVEL.append(list(zeile))


class Labyrinth(arcade.Window):

    def __init__(self):
        super().__init__(600, 600, "Labyrinth")
        self.xpos = 5
        self.ypos = 5

    def on_draw(self):
        arcade.start_render()
        for y, zeile in enumerate(LEVEL):
            for x, char in enumerate(zeile):
                if char == '#':
                    wand.draw(x * 32 + 50, y * 32 + 50, 32, 32)
        pac.draw(self.xpos * 32 + 50, self.ypos * 32 + 50, 32, 32)

    def on_key_press(self, taste, mod):
        if taste == MOTION_RIGHT:
            self.xpos += 1
        elif taste == MOTION_LEFT:
            self.xpos -= 1
        elif taste == MOTION_UP:
            self.ypos += 1
        elif taste == MOTION_DOWN:
            self.ypos -= 1
        elif taste == ESCAPE:
            arcade.window_commands.close_window()


laby = Labyrinth()
arcade.run()

'''
import random
import time


MAZE = open('level.txt').read()

class MazeGame:

    def __init__(self):
        self.game = Game()
        self.map = TiledMap(self.game)
        self.map.set_map(MAZE)
        self.fruechte = self.fruechte_zaehlen(MAZE)
        self.sprite = Sprite(self.game, 'b.pac_right', (1, 1), speed=4)
        self.geist = Sprite(self.game, 'b.ghost_center', (8, 8), speed=4)
        self.game.event_loop(figure_moves=self.move,
                             draw_func=self.draw)

    def fruechte_zaehlen(self, level):
        """Zählt die einzusammelnden Obststücke"""
        return len([c for c in level if c in "abcdefgh"])

    def draw(self):
        """
        Alles bewegen und zeichnen.
        Wird von event_loop() regelmäßig aufgerufen
        """
        self.map.draw()
        self.sprite.move()
        self.sprite.draw()
        self.geist_bewegen()
        self.geist.draw()
        self.frucht_fressen()
        self.kollision()

    def geist_bewegen(self):
        """Bewegt den Geist, aber nicht durch Wände"""
        if self.geist.finished:
            richtung = random.choice([UP, DOWN, LEFT, RIGHT])
            neues_feld = self.geist.pos + richtung
            if self.map.at(neues_feld) != '#':
                self.geist.add_move(richtung)
        self.geist.move()

    def kollision(self):
        """Prüft, ob Geist und Spieler auf dem gleichen Feld sind."""
        if self.sprite.pos == self.geist.pos:
            self.game.frame.print_text('VERLOREN!!!', (50, 400))
            pygame.display.update()
            time.sleep(5)
            self.game.exit()

    def frucht_fressen(self):
        """Mampft ein Obststück weg"""
        if self.map.at(self.sprite.pos) in 'abcdefgh':
            self.map.set_tile(self.sprite.pos, '.')
            self.fruechte -= 1
            if self.fruechte == 0:
                self.game.frame.print_text('GEWONNEN!!!', (50, 400))
                pygame.display.update()
                time.sleep(5)
                self.game.exit()

    def move(self, direction):
        """Bewegt die Spielfigur. Wird von event_loop()
        aufgerufen, wenn Pfeiltaste gedrückt"""
        neues_feld = self.sprite.pos + direction
        if self.sprite.finished and \
           not self.map.at(neues_feld) == '#':
            self.sprite.add_move(direction)


if __name__ == '__main__':  # Python-Ausdrucksweise für "Hier ist das Hauptprogramm"
    maze = MazeGame()
'''
