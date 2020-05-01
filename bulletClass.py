import pygame
from enum import Enum
from globalVars import screen, Direction


class Bullet:
    def __init__(self,x,y,color,drop = False):
        self.x = x
        self.y = y
        self.color = color
        self.speed = 1
        self.radius = 5
        self.dx, self.dy =0 ,0
        self.drop = drop
    def draw(self):
        pygame.draw.circle(screen, self.color,(self.x,self.y),self.radius)
    def start(self,x,y):
        if self.drop == True:
            self.x += self.dx
            self.y += self.dy
            self.draw()
    def shoot(self,Tank):
        if Tank.direction == Direction.RIGHT:
            self.x, self.y = Tank.x + int(Tank.width / 2), Tank.y + int(Tank.width / 2)
            self.dx, self.dy = 15, 0
        if Tank.direction == Direction.LEFT:
            self.x, self.y = Tank.x + int(Tank.width / 2), Tank.y + int(Tank.width / 2)
            self.dx, self.dy = -15, 0
        if Tank.direction == Direction.UP:
            self.x, self.y = Tank.x + int(Tank.width / 2), Tank.y + int(Tank.width / 2)
            self.dx, self.dy = 0, -15
        if Tank.direction == Direction.DOWN:
            self.x, self.y = Tank.x + int(Tank.width / 2), Tank.y + int(Tank.width / 2)
            self.dx, self.dy = 0, 15
    def out(self):
        if self.x >= 1200 or self.x <= 0 or self.y >= 600 or self.y <= 0:
            return True
        return False
    def colission(self,Tank):
        if Tank.direction == Direction.RIGHT and self.drop == True:
            if(self.x > Tank.x and self.x < Tank.x + 60) and (self.y > Tank.y and self.y < Tank.y + 40):
                return True
        if Tank.direction == Direction.LEFT and self.drop == True:
            if(self.x > Tank.x - 20 and self.x < Tank.x + 40) and (self.y > Tank.y and self.y < Tank.y + 40):
                return True
        if Tank.direction == Direction.UP and self.drop == True:
            if(self.y > Tank.y - 20 and self.y < Tank.y + 40) and (self.x > Tank.y and self.x < Tank.x + 40):
                return True
        if Tank.direction == Direction.DOWN and self.drop == True:
            if(self.y > Tank.y and self.y < Tank.y + 60) and (self.x > Tank.x and self.x < Tank.x + 40):
                return True 