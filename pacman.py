import pygame

import pygame.gfxdraw

from maze import Maze
from eventloop import EventLoop
from player import Player
from settings import Settings


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((735, 800))
        pygame.display.set_caption("Pac-man")
        self.settings = Settings()

        self.maze = Maze(self.screen, 'images/maze.txt', 'images/cube0.png', 'images/gate0.png', 'images/dot0.png')

        self.player = Player(self.settings, self.screen, self.maze)

    def play(self):
        clock = pygame.time.Clock()
        eloop = EventLoop(finished=False)

        while not eloop.finished:
            eloop.check_events(self.settings, self.player, self.maze)

            self.player.update(self.maze)

            self.display_game()
            clock.tick(20)

    def display_game(self):
        self.screen.fill((0, 0, 0))
        self.maze.blitme()
        self.player.blitme()

        pygame.display.flip()


game = Game()
game.play()
