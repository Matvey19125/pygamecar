import pygame
from osnovscene import Shoes


def razvil():
    pygame.init()
    size = 800, 950
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Ретро-Гонки")
    background = pygame.image.load("image/fon.png")
    font_text = pygame.font.Font(None, 85)
    font_big = pygame.font.Font(None, 80)
    text_prom = "Выберите режим"
    button_prom = font_text.render(text_prom, True, (255, 255, 255))
    font = pygame.font.Font(None, 75)
    exit_text = "Выход"
    exit_button = font.render(exit_text, True, (255, 255, 255))
    exit_button_rect = exit_button.get_rect(center=(100, 50))
    text_shash = "Шашки"
    button_shash = font.render(text_shash, True, (255, 255, 255))
    button_shash_rect = button_shash.get_rect(center=(400, 300))
    text_revers = "Реверс"
    button_revers = font.render(text_revers, True, (255, 255, 255))
    button_revers_rect = button_revers.get_rect(center=(400, 400))
    pygame.display.set_caption("Ретро-Гонки")
    background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
    text_parcing = "Парковка"
    button_parcing = font.render(text_parcing, True, (255, 255, 255))
    button_parcing_rect = button_parcing.get_rect(center=(400, 500))
    running = True
    mouse_pos = pygame.mouse.get_pos()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_shash_rect.collidepoint(event.pos):
                    shoes_scene = Shoes()
                    shoes_scene.update()
                if button_revers_rect.collidepoint(event.pos):
                    from revers import Rervers
                    scene = Rervers()
                    scene.update()
                if button_parcing_rect.collidepoint(event.pos):
                    from levelparking import level_menu
                    scene = level_menu()
                    scene.level_menu()
                if exit_button_rect.collidepoint(event.pos):
                    from Menu import menu
                    scene = menu()
                    scene.menu()
        if button_shash_rect.collidepoint(mouse_pos):
            button_shash = font_big.render(text_shash, True, (255, 0, 0))
            button_shash_rect = button_shash.get_rect(center=button_shash_rect.center)
        else:
            button_shash = font.render(text_shash, True, (255, 255, 255))
            button_shash_rect = button_shash.get_rect(center=button_shash_rect.center)
        if exit_button_rect.collidepoint(mouse_pos):
            font_exit = pygame.font.Font(None, 85)
            exit_button = font_exit.render(exit_text, True, (255, 0, 0))
        else:
            exit_button = font_big.render(exit_text, True, (255, 255, 255))
        if button_revers_rect.collidepoint(mouse_pos):
            button_revers = font_big.render(text_revers, True, (255, 0, 0))
        else:
            button_revers = font.render(text_revers, True, (255, 255, 255))
        if button_parcing_rect.collidepoint(mouse_pos):
            button_parcing = font_big.render(text_parcing, True, (255, 0, 0))
        else:
            button_parcing = font.render(text_parcing, True, (255, 255, 255))
        screen.blit(background, (0, 0))
        screen.blit(button_prom, (175, 150))
        screen.blit(button_revers, button_revers_rect)
        screen.blit(button_parcing, button_parcing_rect)
        screen.blit(exit_button, exit_button_rect)
        screen.blit(button_shash, button_shash_rect)
        pygame.display.flip()


if __name__ == "__main__":
    razvil()