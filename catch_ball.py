import pygame
from random import randint


SCREEN_RESOLUTION = (1024, 768)
FPS = 2

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


class Ball:
    def __init__(self):
        self.x = randint(100, 924)
        self.y = randint(100, 668)
        self.r = randint(10, 100)
        self.color = COLORS[randint(0, 5)]


class GameManager:
    def __init__(self):
        pygame.init()
        self._screen = pygame.display.set_mode(SCREEN_RESOLUTION)

    def main_loop(self):
        finished = False
        clock = pygame.time.Clock()
        while not finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
            ball = Ball()
            pygame.draw.circle(
                self._screen, ball.color, (ball.x, ball.y), ball.r)
            pygame.display.update()
            clock.tick(FPS)


def main():
    game = GameManager()
    game.main_loop()


if __name__ == "__main__":
    main()
