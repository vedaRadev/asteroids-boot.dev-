import pygame
import constants
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    containers = None

    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0


    def draw(self, screen):
        pygame.draw.polygon(screen, pygame.Color(255, 255, 255), self.triangle(), 2)


    def update(self, dt):
        if self.shot_timer > 0:
            self.shot_timer -= dt
            if self.shot_timer < 0:
                self.shot_timer = 0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            if self.shot_timer == 0:
                self.shoot()


    def shoot(self):
        self.shot_timer = constants.PLAYER_SHOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y, constants.SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity *= constants.PLAYER_SHOT_SPEED


    def rotate(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt


    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius           # type: ignore
        b = self.position - forward * self.radius - right   # type: ignore
        c = self.position - forward * self.radius + right   # type: ignore
        return [a, b, c]
