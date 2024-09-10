import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    dt = 0
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    player = Player(x, y)
    
    player.add(updatable, drawable)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0,0,0))
        for item in updatable:
            item.update(dt)
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
    
if __name__ == "__main__":
    main()
