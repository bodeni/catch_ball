import pygame
from random import randint


SCR_RES = (800, 600)
FPS = 2

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

TOTAL_BALLS = 60


class Ball:
    def __init__(self):
        self.x = randint(100, SCR_RES[0] - 100)
        self.y = randint(150, SCR_RES[1] - 100)
        self.r = randint(10, 100)
        self.color = COLORS[randint(0, 5)]


class GameManager:
    def __init__(self):
        pygame.init()
        self._screen = pygame.display.set_mode(SCR_RES)
        pygame.display.set_caption("Catch Ball")
        self._clock = pygame.time.Clock()
        self._fnt = pygame.font.SysFont(None, 24)

    def show_score(self, score_count=0):
        self._score_count = score_count
        self._score_surf = self._fnt.render(str(self._score_count), 1, RED)                  
        self._screen.blit(self._score_surf, (10, 10))

    def hide_score(self):
        self._score_surf.fill(BLACK)
        self._screen.blit(self._score_surf, (10, 10))

    def show_timer(self, current_time=TOTAL_BALLS):
        self._current_time = current_time
        self._timer_surf = self._fnt.render(str(self._current_time), 1, BLUE)
        self._screen.blit(self._timer_surf, (770, 10))

    def hide_timer(self):
        self._timer_surf.fill("BLACK")
        self._screen.blit(self._timer_surf, (770, 10))

    def show_pspace(self):
        self._pspace_surf = self._fnt.render("PRESS SPACE", 1, YELLOW)
        self._pos_pspace = self._pspace_surf.get_rect(center=(SCR_RES[0] // 2,
                                                              SCR_RES[1] // 2))
        self._screen.blit(self._pspace_surf,self._pos_pspace)

    def hide_pspace(self):
        self._pspace_surf.fill(BLACK)
        self._screen.blit(self._pspace_surf,self._pos_pspace)

    def start_menu(self, first_iter: bool):
        self.show_pspace()

        if first_iter:
            self.show_score()
            self.show_timer()

        pygame.display.update()

        started = False
        while not started:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.hide_pspace()
                            started = True

        if not first_iter:
            self.hide_score()
            self.hide_timer()
            self.show_score()
            self.show_timer()


    def main_loop(self):
        first_iter = True
        while True:
            __current_time = TOTAL_BALLS
            __score_count = 0
            self._finished = False
            self.start_menu(first_iter)

            while not self._finished: 

                ball = Ball()
                pygame.draw.circle(
                    self._screen, ball.color, (ball.x, ball.y), ball.r)
                pygame.display.update()
                old_r = ball.r

                self._clock.tick(FPS)

                self.hide_timer()
                self.show_timer(__current_time)
                __current_time -= 1 
                
                if __current_time == -1:
                    self._finished = True
                    if first_iter:
                        first_iter = False

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if ((event.pos[0] - ball.x)**2 +
                            (event.pos[1] - ball.y)**2)**0.5 <= ball.r:
                            old_r = ball.r
                            ball.r = 0
                            __score_count += 1
                            self.hide_score()
                            self.show_score(__score_count)
                
                pygame.draw.circle(
                    self._screen, BLACK, (ball.x, ball.y), old_r)


def main():
    game = GameManager()
    game.main_loop()


if __name__ == "__main__":
    main()
