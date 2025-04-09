from circleshape import CircleShape
import pygame


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius

    def draw(self, screen):
        center = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(screen, 'white', center, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
