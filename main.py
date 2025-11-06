import pygame
import sys
from logger import log_state, log_event
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        screen.fill((0, 0, 0))
        for drawing in drawable:
            drawing.draw(screen)
        for roid in asteroids:
            if roid.collision_check(player):
                print("Game over!")
                sys.exit()
        for roid in asteroids:
            for shot in shots:
                if roid.collision_check(shot):
                    log_event("asteroid_shot")
                    roid.split()
                    shot.kill()
                    
        pygame.display.flip()


        dt = clock.tick(60) / 1000

    
if __name__ == "__main__":
    main()
