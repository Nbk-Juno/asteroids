import pygame
from logger import log_event
import random
from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)
            v1 = self.velocity.rotate(random_angle) * 1.2
            v2 = self.velocity.rotate(-random_angle) * 1.2
            self.radius -= ASTEROID_MIN_RADIUS
            roid1 = Asteroid(self.position.x, self.position.y, self.radius)
            roid2 = Asteroid(self.position.x, self.position.y, self.radius)
            roid1.velocity = v1
            roid2.velocity = v2
