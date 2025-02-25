import pygame

max_x = 500
max_y = 500

x = 10
y = 10

dx = 1
dy = 2

x2 = 40
y2 = 40

dx2 = 2
dy2 = 3

# pygame setup
pygame.init()
screen = pygame.display.set_mode((max_x, max_y))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "yellow", (x, y), 10)
    pygame.draw.circle(screen, "green", (x2, y2), 20)

    # flip() the display to put your work on screen
    pygame.display.flip()

    x += dx
    y += dy

    if x > max_x or x <= 0:
        dx = -dx

    if y > max_y or y <= 0:
        dy = -dy
     
    x2 += dx2
    y2 += dy2

    if x2 > max_x or x2 <= 0:
        dx2 = -dx2

    if y2 > max_y or y2 <= 0:
        dy2 = -dy2


    clock.tick(60)  # limits FPS to 60


pygame.quit()