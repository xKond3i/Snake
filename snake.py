__author__ = "Konrad Ceglarski"

import pygame

class snake:
    def __init__(self, elements):
        super().__init__()
        self.lenght = len(elements)
        self.elements = elements
        self.head = self.elements[0]
        self.dir = 'E'
        self.key_lock = False
        self.reserve = [[],[]]  # two reserve spots
        self.dead = False

    def display(self, app, colors, element_size, map_size, borders):
        # display snake elements
        for element in self.elements[1:]:
            pygame.draw.rect(app, colors[2], [element[0]*element_size+1, element[1]*element_size+1, element_size-2, element_size-2])
        # display head
        pygame.draw.rect(app, colors[1], [self.head[0]*element_size+1, self.head[1]*element_size+1, element_size-2, element_size-2])

    def move(self):
        # take position of next element in the list
        self.reserve[1] = self.reserve[0]
        self.reserve[0] = self.elements[-1]
        for i in range(self.lenght-1, 0, -1):
            self.elements[i] = self.elements[i-1]
        # move head based on the dir
        if self.dir == 'E':
            self.elements[0] = [self.elements[0][0]+1, self.elements[0][1]]
        elif self.dir == 'S':
            self.elements[0] = [self.elements[0][0], self.elements[0][1]+1]
        elif self.dir == 'W':
            self.elements[0] = [self.elements[0][0]-1, self.elements[0][1]]
        elif self.dir == 'N':
            self.elements[0] = [self.elements[0][0], self.elements[0][1]-1]
        # set the head
        self.head = self.elements[0]
        self.key_lock = False

    def check_collision(self, map_size, borders, food):
        # checking for self collisions
        for i in range(self.lenght-1, 0, -1):
            if self.elements[i] == self.head:
                self.dead = True
        # check for collision with the wall
        if not borders:
            if self.head[0] >= map_size:
                self.head[0] = 0
            elif self.head[0] < 0:
                self.head[0] = map_size
            elif self.head[1] >= map_size:
                self.head[1] = 0
            elif self.head[1] < 0:
                self.head[1] = map_size
            self.elements[0] = self.head
        else:
            if self.head[0] >= map_size or self.head[0] < 0 or self.head[1] >= map_size or self.head[1] < 0:
                self.dead = True
        # checking for collision with food - when they have the same position
        if self.head == food.pos:
            if food.type == 0:
                self.grow(2)    # golden apple
            else:
                self.grow(1)    # normal apple
            food.spawn(map_size, self.elements)

    def grow(self, amount):
        self.lenght += amount
        for i in range(0, amount):
            self.elements.append(self.reserve[i])

    def restart(self, elements):
        self.lenght = len(elements)
        self.elements = elements
        self.head = self.elements[0]
        self.dir = 'E'
        self.key_lock = False
        self.reserve = [[],[]]
        self.dead = False