import pygame
import math
import sys

clock = pygame.time.Clock()

from pygame.locals import *
pygame.init()

pygame.display.set_caption("Inverse Kinematics")


WINDOW_SIZE = (800,400)

screen = pygame.display.set_mode(WINDOW_SIZE,0,32)
class Vector2:

    def __init__(self, x : float, y : float):
        self.x = x
        self.y = y

    def heading(self, point):
        # For this function y is entered first. This is not a mistake
        return math.atan2(point.y - self.y, point.x - self.x) 

    def add(self, b ):
        fx = self.x + b.x 
        fy = self.x + b.y
        return Vector2(fx, fy)

    def sub(self, b ):
        fx = self.x - b.x 
        fy = self.y - b.y
        return Vector2(fx, fy)

    def mult(self, b : float):
        fx = self.x * b 
        fy = self.y * b 
        return Vector2(fx, fy)
    
    def magnitude(self):
        return (math.sqrt(self.x**2 + self.y **2))

    def normalized(self):
        fx = self.x / self.magnitude()
        fy = self.y / self.magnitude()
        return Vector2(fx, fy)


    def __repr__(self):
        return f"({self.x}, {self.y})"

ZERO_V = Vector2(0,0)


class Segment:

    def __init__ (self, a : Vector2, b : Vector2, length : float, angle : float):
        # angle in radians
        self.a = a 
        self.b = b
        self.length = length
        self.angle = angle

    def draw(self, surface):
        pygame.draw.line(surface, pygame.Color(255,255,255), (self.a.x, self.a.y), (self.b.x, self.b.y), width = 4)

    def calculateB(self):
        fx = self.a.x + self.length * math.cos(self.angle)
        fy = self.a.y + self.length * math.sin(self.angle)
        return Vector2(fx, fy)
    
    def update(self):
        self.b = self.calculateB()

    def follow(self, target : Vector2):
        self.angle = self.a.heading(target)

        self.a.x = target.x - self.length * math.cos(self.angle)
        self.a.y = target.y - self.length * math.sin(self.angle)







def main():
    running = True

    seg = Segment(Vector2(400, 200), Vector2(400,200), 50, 0)
    while running:
        screen.fill(pygame.Color(0,0,0))

        mx, my = pygame.mouse.get_pos() 

        mouse_coords = Vector2(mx, my)

        seg.update()
        seg.follow(mouse_coords)
        seg.draw(screen)
        

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    pass
                if event.key == K_DOWN:
                    pass


        pygame.display.update()
        clock.tick(60)

main()


def test():
    a = Vector2(0,0)
    b = Vector2(10, 10)

    print(a)
    print(a.add(b))
    print(a)
    print(b.add(a))
    print(b.mult(-1))
    print(b.add(b))

