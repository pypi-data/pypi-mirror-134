import pygame

from aerforge.color import *

class Line:
    def __init__(self, window, points, color = Color(240, 240, 240), add_to_objects = True):
        self.window = window
        
        self.color = color
        self.points = points

        self.scripts = []

        self.destroyed = False

        self.add_to_objects = add_to_objects

        if self.add_to_objects:
            self.window.objects.append(self)

    def _update(self):
        for script in self.scripts:
            script.update(self)

    def draw(self):
        if not self.destroyed:
            for point in self.points:
                pygame.draw.aaline(self.window.window, self.color, point[0], point[1])

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def add_points(self, points):
        self.points.append(points)

    def remove_points(self, points):
        self.points.pop(self.points.index(points))

    def destroy(self):
        self.destroyed = True

        if self.add_to_objects:
            try:
                self.window.objects.pop(self.window.objects.index(self))

            except:
                pass

    def add_script(self, script):
        self.scripts.append(script)

    def remove_script(self, script):
        self.scripts.pop(self.scripts.index(script))