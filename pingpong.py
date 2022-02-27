import pygame

pygame.init()

window_width = 1400
window_height = 700

window_game = pygame.display.set_mode((window_width, window_height))

clock = pygame.time.Clock()

class Ball:
    def __init__(self, x, y, r, color):
        self.x = x
        self.y = y
        self.r = r
        self.color = color

    def draw(self):
        pygame.draw.circle(window_game, self.color, [self.x, self.y], self.r)


ball = Ball(window_width / 2, window_height / 2, 10, 'white')
dx = 1
dy = 0
running = True
while running:

    window_game.fill((0, 0, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    ball.draw()

    ball.x += dx
    if ball.x == window_width:
        dx = -dx

    if ball.x == 0:
        dx = dx * (-1)

    pygame.display.flip()

pygame.quit()
