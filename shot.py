from circleshape import CircleShape
from constants import SHOT_RADIUS
import pygame


class Shot(CircleShape):

    def __init__(self, position):
        super().__init__(position.x, position.y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 0)  # Will be set by Player.shoot().

    def draw(self, screen):
        center = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(screen, 'white', center, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt
