import pygame

def awards():
    pygame.init()
    size = 800, 950
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(size)
    background = pygame.image.load("image/fon.png")
    pygame.display.set_caption("Ретро-Гонки")
    background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.blit(background, (0, 0))
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    awards()