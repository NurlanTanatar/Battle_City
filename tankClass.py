import pygame
from enum import Enum
from globalVars import screen, Direction

class Tank:
    def __init__(self,name, u, x, y, speed, color,lives,d_right=pygame.K_RIGHT, d_left=pygame.K_LEFT, d_up=pygame.K_UP, d_down=pygame.K_DOWN):
        self.u = u
        self.x = x
        self.y = y
        self.speed = speed
        self.color = color
        self.width = 40
        self.direction = Direction.RIGHT
        self.lives = lives
        self.name = name
        self.KEY  = {d_right: Direction.RIGHT, d_left: Direction.LEFT,
                    d_up: Direction.UP, d_down: Direction.DOWN}

    def draw(self):
        tank_c = (self.x + int(self.width / 2), self.y + int(self.width / 2))
        pygame.draw.rect(screen, self.color,
                         (self.x, self.y, self.width, self.width), 2)
        pygame.draw.circle(screen, self.color, tank_c, int(self.width / 2))

        if self.direction == Direction.RIGHT:
            pygame.draw.line(screen, self.color, tank_c, (self.x + self.width + int(self.width / 2), self.y + int(self.width / 2)), 4)
        
        if self.direction == Direction.LEFT:
            pygame.draw.line(screen, self.color, tank_c, (
            self.x - int(self.width / 2), self.y + int(self.width / 2)), 4)
            
        if self.direction == Direction.UP:
            pygame.draw.line(screen, self.color, tank_c, (self.x + int(self.width / 2), self.y - int(self.width / 2)), 4)
           
        if self.direction == Direction.DOWN:
            pygame.draw.line(screen, self.color, tank_c, (self.x + int(self.width / 2), self.y + self.width + int(self.width / 2)), 4)
    

    def change_direction(self, direction):
        self.direction = direction
    def move(self):
            if self.direction == Direction.LEFT:
                if self.x + self.width < 0:
                    self.x = 1200 
                else:
                    self.x -= self.speed
            if self.direction == Direction.RIGHT:
                if self.x > 1200:
                    self.x = 0
                else:
                    self.x += self.speed
            if self.direction == Direction.UP:
                if self.y < 0 - self.width:
                    self.y = 600
                else:
                    self.y -= self.speed
            if self.direction == Direction.DOWN:
                if self.y > 600:
                    self.y = 0-self.width
                else:
                    self.y += self.speed
            self.draw()
    def chances(self):
        font = pygame.font.SysFont("Calibri", 30, True)
        score = font.render("lives: " + str(self.lives), True, (self.color))
        screen.blit(score, (1050, self.u))
    def dead(self):
            font = pygame.font.SysFont("Calibri", 30)
            text = font.render(str(self.name) + ' destructed ', True, (255,255,255))
            screen.blit(text, (450,500))