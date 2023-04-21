__author__ = "Konrad Ceglarski"

import pygame, random

class food:
    def __init__(self, map_size, snake, food_type):
        self.spawn(map_size, snake)
        self.type = food_type

    def spawn(self, map_size, snake):
        # spawn loop to avoid spawning in the snake
        self.pos = [random.randint(0, map_size-1), random.randint(0, map_size-1)]
        if self.pos in snake:
            self.spawn(map_size, snake)
        self.type = random.randint(0,5)

    def display(self, app, colors, element_size):
        # display food
        if self.type == 0:
            pygame.draw.rect(app, colors[4], [self.pos[0]*element_size+1, self.pos[1]*element_size+1, element_size-2, element_size-2])
        else:
            pygame.draw.rect(app, colors[3], [self.pos[0]*element_size+1, self.pos[1]*element_size+1, element_size-2, element_size-2])