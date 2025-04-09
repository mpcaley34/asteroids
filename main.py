import pygame
import sys
from constants import *
from player import *
from asteroids import *
from asteroidfield import *


def main():
    pygame.init()
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()
    Shot.containers = (shots_group, updatable, drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots_group)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        dt = clock.tick(60) / 1000
        # Make sure close button works
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill('black')
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.checkCollision(player):
                sys.exit('Game over!')

            for bullet in shots_group:
                if bullet.checkCollision(asteroid):
                    bullet.kill()
                    asteroid.split()

        for i in drawable:
            i.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
