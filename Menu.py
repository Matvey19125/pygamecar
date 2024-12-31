import pygame
import sys
from osnovscene import Shoes

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
background = pygame.image.load("image/fon.png")
background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
WHITE = (255, 255, 255)
font = pygame.font.Font(None, 74)
play_button = font.render('Играть', True, WHITE)
shop_button = font.render('Магазин', True, WHITE)
exit_button = font.render('Выход', True, WHITE)
play_button_rect = play_button.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 50))
shop_button_rect = shop_button.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
exit_button_rect = exit_button.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 50))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                shoes_scene = Shoes()
                shoes_scene.update()
                running = True
                background = False
            elif shop_button_rect.collidepoint(event.pos):
                pass
            elif exit_button_rect.collidepoint(event.pos):
                pygame.quit()
                sys.exit()
    if background:
        screen.blit(background, (0, 0))
    screen.blit(play_button, play_button_rect)
    screen.blit(shop_button, shop_button_rect)
    screen.blit(exit_button, exit_button_rect)
    pygame.display.flip()