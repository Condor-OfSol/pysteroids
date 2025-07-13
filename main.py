import pygame
import sys
from constants import * 
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from shot import Shot


def main():
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    Player.containers = (updateable, drawables)
    Asteroid.containers = (asteroids, updateable, drawables)
    AsteroidField.containers = (updateable)
    Shot.containers = (bullets, updateable, drawables)


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(pygame.Color("black"))
        updateable.update(dt)
        for asteroid in asteroids:
            if asteroid.check_collisions(player):
                print("Game over!")
                sys.exit(0)
        for drawable in drawables:
            drawable.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    


if __name__ == "__main__":
    main()
