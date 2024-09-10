import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    dt = 0
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()
    
    player = Player(x, y)
    
    player.add(updatable, drawable)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.fill((0,0,0))
        for item in updatable:
            item.update(dt)
        for obj in asteroids:
            for bullet in shots:
                if bullet.col_check(obj):
                    obj.split()
                    bullet.kill()
        for obj in asteroids:
            if obj.col_check(player):
                print("Game over!")
                sys.exit()
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
    
if __name__ == "__main__":
    main()
