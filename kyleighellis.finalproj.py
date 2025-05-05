# kyleigh ellis
# 4th period


import pygame
import random

# Initialize PyGame
pygame.init()

# Game Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (255, 255, 255)
CHARACTER_SIZE = 80

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('moving color square')

# Define Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PINK = (255, 203, 232)
GREEN = (161, 232, 163)

# Character Class
class Character:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = CHARACTER_SIZE
        self.height = CHARACTER_SIZE
        self.color = PINK
        self.speed = 3

    def move(self, keys, mouse_pos):
        # keyboard move
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

        # Mouse movement
        self.x, self.y = mouse_pos

    def change_color_on_click(self, mouse_pos, mouse_click):
        # mouse click is within the character
        if self.rect().collidepoint(mouse_pos) and mouse_click:
            # change color between pink & green
            if self.color == PINK:
                self.color = GREEN
            else:
                self.color = PINK

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

# class game
class Game:
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.character = Cutecharacter(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)

    def handle_input(self):
        keys = pygame.key.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()[0]  # leftclick
        self.character.move(keys, mouse_pos)
        self.character.change_color_on_click(mouse_pos, mouse_click)

    def update(self):
        pass

    def draw(self):
        screen.fill(BACKGROUND_COLOR)
        self.character.draw(screen)

    def run(self):
        while self.running:
            self.handle_input()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.update()
            self.draw()

            pygame.display.flip()
            self.clock.tick(40)  # 40 fps
        pygame.quit()

# main
def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
