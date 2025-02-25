import pygame

class Shape: 
    def __init__(self, x, y, dx, dy, colour):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.colour = colour

    def bounce_if_needed(self, xl, yt, xr, yb):
        if self.x > xr or self.x <= xl:
            self.dx = -self.dx

        if self.y > yb or self.y <= yt:
            self.dy = -self.dy

    def move(self):
        self.x += self.dx
        self.y += self.dy

class Circle(Shape):
    def __init__(self, x, y, dx, dy, colour, radius):
        Shape.__init__(self, x, y, dx, dy, colour)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.radius)


class Square(Shape):
    def __init__(self, x, y, dx, dy, colour, edge_length):
        Shape.__init__(self, x, y, dx, dy, colour)
        self.edge_length = edge_length

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.edge_length, self.edge_length))

# class Circle: 
#     def __init__(self, x, y, dx, dy, colour, size):
#         self.x = x
#         self.y = y
#         self.dx = dx
#         self.dy = dy
#         self.colour = colour
#         self.size = size

#     def bounce_if_needed(self, xl, yt, xr, yb):
#         if self.x > xr or self.x <= xl:
#             self.dx = -self.dx

#         if self.y > yb or self.y <= yt:
#             self.dy = -self.dy

#     def move(self):
#         self.x += self.dx
#         self.y += self.dy


max_x = 500
max_y = 500

##--------------
# n = 2

# x = [10, 40]
# y = [10, 40]

# dx = [1, 2]
# dy = [2, 3]

# colour = ["blue", "red"]
# size = [10, 20]
##---------------

shapes = [
    Circle(10, 10, 1, 2, "red", 10),
    Circle(15, 20, 2, 3, "blue", 15),
    Circle(5, 5, 3, 1, "yellow", 20),
    Circle(35, 5, 6, 5, "purple", 8),
    Circle(15, 5, 2, 1, "green", 30),
    Square(10, 10, 2, 2, "purple", 40)
]

c1 = Circle(10, 10, 1, 2, "red", 10)
c2 = Circle(15, 20, 2, 3, "blue", 15)
c3 = Circle(5, 5, 3, 1, "yellow", 20)
c4 = Circle(35, 5, 6, 5, "purple", 8)
c5 = Circle(15, 5, 2, 1, "green", 30)
sq1 = Square(10, 10, 2, 2, "purple", 40)


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
    screen.fill("cyan")

    ##----------------------
    # for i in range(n):
        
        # pygame.draw.circle(screen, colour[i], (x[i], y[i]), size[i])

        # x[i] += dx[i]
        # y[i] += dy[i]

        # if x[i] > max_x or x[i] <= 0:
        #     dx[i] = -dx[i]

        # if y[i] > max_y or y[i] <= 0:
        #     dy[i] = -dy[i]
        ##--------------------

    # pygame.draw.circle(screen, c1.colour, (c1.x, c1.y), c1.radius)
    # pygame.draw.circle(screen, c2.colour, (c2.x, c2.y), c2.radius)
    # pygame.draw.circle(screen, c3.colour, (c3.x, c3.y), c3.radius)
    # pygame.draw.circle(screen, c4.colour, (c4.x, c4.y), c4.radius)
    # pygame.draw.circle(screen, c5.colour, (c5.x, c5.y), c5.radius)
    # pygame.draw.rect(screen, sq1.colour, (sq1.x, sq1.y, sq1.edge_length, sq1.edge_length))


    # flip() the display to put your work on screen
    pygame.display.flip()

    c1.move()
    c1.bounce_if_needed(0, 0, max_x, max_y)
    c2.move()
    c2.bounce_if_needed(0, 0, max_x, max_y)
    c3.move()
    c3.bounce_if_needed(0, 0, max_x, max_y)
    c4.move()
    c4.bounce_if_needed(0, 0, max_x, max_y)
    c5.move()
    c5.bounce_if_needed(0, 0, max_x, max_y)
    sq1.move()
    sq1.bounce_if_needed(0, 0, max_x, max_y)

    clock.tick(60)  # limits FPS to 60


pygame.quit()