import pygame
import math

# Base class for game objects


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def checkCollision(self, other):
        # Use the Vector2's distance_to method
        distance = self.position.distance_to(other.position)

        # Check if the distance is less than or equal to the sum of the radii
        return distance <= (self.radius + other.radius)
