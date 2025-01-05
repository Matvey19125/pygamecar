import pygame
import sys
from osnovscene import Shoes
from shop import shop


def menu():
    pygame.init()
    size = 800, 950
    screen = pygame.display.set_mode(size)
    background = pygame.image.load("image/fon.png")
    pygame.display.set_caption("Ретро-Гонки")
    background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
    WHITE = (255, 255, 255)
    RED = (255, 50, 0)
    font = pygame.font.Font(None, 74)
    play_text = 'Играть'
    shop_text = 'Магазин'
    exit_text = 'Выход'
    play_button_normal = font.render(play_text, True, WHITE)
    shop_button_normal = font.render(shop_text, True, WHITE)
    exit_button_normal = font.render(exit_text, True, WHITE)
    font_large = pygame.font.Font(None, 80)
    play_button_hover = font_large.render(play_text, True, RED)
    shop_button_hover = font_large.render(shop_text, True, RED)
    exit_button_hover = font_large.render(exit_text, True, RED)
    play_button_rect = play_button_normal.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 100))
    shop_button_rect = shop_button_normal.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    exit_button_rect = exit_button_normal.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 100))
    play_button_hover_rect = play_button_hover.get_rect(center=play_button_rect.center)
    shop_button_hover_rect = shop_button_hover.get_rect(center=shop_button_rect.center)
    exit_button_hover_rect = exit_button_hover.get_rect(center=exit_button_rect.center)
    mouse_pos = pygame.mouse.get_pos()
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(event.pos):
                    shoes_scene = Shoes()
                    shoes_scene.update()
                    running = False
                elif shop_button_rect.collidepoint(event.pos):
                    scene = shop()
                    scene.shop()
                    running = True
                elif exit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        if play_button_rect.collidepoint(mouse_pos):
            play_button_to_draw = play_button_hover
            play_button_rect_to_use = play_button_hover_rect
        else:
            play_button_to_draw = play_button_normal
            play_button_rect_to_use = play_button_rect

        if shop_button_rect.collidepoint(mouse_pos):
            shop_button_to_draw = shop_button_hover
            shop_button_rect_to_use = shop_button_hover_rect
        else:
            shop_button_to_draw = shop_button_normal
            shop_button_rect_to_use = shop_button_rect

        if exit_button_rect.collidepoint(mouse_pos):
            exit_button_to_draw = exit_button_hover
            exit_button_rect_to_use = exit_button_hover_rect
        else:
            exit_button_to_draw = exit_button_normal
            exit_button_rect_to_use = exit_button_rect

        screen.blit(background, (0, 0))
        screen.blit(play_button_to_draw, play_button_rect_to_use)
        screen.blit(shop_button_to_draw, shop_button_rect_to_use)
        screen.blit(exit_button_to_draw, exit_button_rect_to_use)
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    menu()