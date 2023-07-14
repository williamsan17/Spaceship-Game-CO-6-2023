import pygame
from game.utils.constants import SPACESHIP, SCREEN_WIDTH


class Spaceship:
    WITH = 40
    HEIGHT = 60
    X_POS = (SCREEN_WIDTH // 2) - WITH
    Y_POS = 500
    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.WITH, self.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS

    def update(self, game_speed, user_input):
        if user_input[pygame.K_LEFT]:
            self.move_left(game_speed)

        if user_input[pygame.K_RIGHT]:
            self.move_right(game_speed)
        
        if user_input[pygame.K_UP]:
            self.move_up(game_speed)

        if user_input[pygame.K_DOWN]:
            self.move_down(game_speed)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move_left(self, game_speed):
    #    if self.rect.left > 0:
    #        self.rect.x -= game_speed
 
        self.rect.x -= game_speed
        if self.rect.left < 0:
           self.rect.right = SCREEN_WIDTH 
    def move_right(self, game_speed):
     #   if self.rect.right < SCREEN_WIDTH:
      #      self.rect.x += game_speed
    
        self.rect.x += game_speed
        if self.rect.right > SCREEN_WIDTH:
            self.rect.left = 0
    def move_up(self, game_speed):
        if self.rect.y > 250:
            self.rect.y -= game_speed

    def move_down(self, game_speed):
        if self.rect.y < 500:
            self.rect.y += game_speed
