from circleshape import *
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color("white"), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius > ASTEROID_MIN_RADIUS:
            angle = random.uniform(20.0, 50.0)
            asteroid_a = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            asteroid_a.velocity = self.velocity.rotate(angle) * 1.2
            asteroid_b = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            asteroid_b.velocity = self.velocity.rotate(-angle) * 1.2
