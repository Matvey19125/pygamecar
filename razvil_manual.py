import pygame
Igor_down = True


def manual():
    pygame.init()
    clock = pygame.time.Clock()
    size = 800, 950
    screen = pygame.display.set_mode(size)
    background = pygame.image.load("image/fon.png")
    pygame.display.set_caption("Ретро-Гонки")
    background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
    mouse_pos = pygame.mouse.get_pos()
    font_def = pygame.font.Font(None, 65)
    font_zagl = pygame.font.Font(None, 52)
    font_button = pygame.font.Font(None, 70)
    font_button_big = pygame.font.Font(None, 80)
    exit_text = "Выход"
    exit_button = font_def.render(exit_text, True, (255, 255, 255))
    exit_button_rect = exit_button.get_rect(center=(100, 50))
    text_razvil = "Выберите режим о котором хотите узнать"
    text_razvil_surface = font_zagl.render(text_razvil, True, (255, 255, 255))
    text_shash = "Шашки"
    button_shash = font_button.render(text_shash, True, (255, 255, 255))
    button_shash_rect = button_shash.get_rect(center=(400, 300))
    text_revers = "Реверс"
    button_revers = font_button.render(text_revers, True, (255, 255, 255))
    button_revers_rect = button_revers.get_rect(center=(400, 410))
    text_parcing = "Парковка"
    button_parcing = font_button.render(text_parcing, True, (255, 255, 255))
    button_parcing_rect = button_parcing.get_rect(center=(405, 510))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button_rect.collidepoint(event.pos):
                    from Menu import menu
                    scene = menu()
                    scene.menu()
                if button_shash_rect.collidepoint(event.pos):
                    from manual_shashki import manual_shashki
                    scene = manual_shashki()
                    scene.manual_shashki()
                if button_revers_rect.collidepoint(event.pos):
                    from manual_revers import manual_revers
                    scene = manual_revers()
                    scene.manual_revers()
                if button_parcing_rect.collidepoint(event.pos):
                    from manual_parking import manual_parking
                    scene = manual_parking()
                    scene.manual_parking()
        if exit_button_rect.collidepoint(mouse_pos):
            fonexit = pygame.font.Font(None, 75)
            exit_button = fonexit.render(exit_text, True, (255, 0, 0))
            exit_button_rect = exit_button.get_rect(center=exit_button_rect.center)
        else:
            exit_button = font_def.render(exit_text, True, (255, 255, 255))
            exit_button_rect = exit_button.get_rect(center=exit_button_rect.center)
        if button_shash_rect.collidepoint(mouse_pos):
            button_shash = font_button_big.render(text_shash, True, (255, 0, 0))
            button_shash_rect = button_shash.get_rect(center=button_shash_rect.center)
        else:
            button_shash = font_button.render(text_shash, True, (255, 255, 255))
            button_shash_rect = button_shash.get_rect(center=button_shash_rect.center)
        if button_revers_rect.collidepoint(mouse_pos):
            button_revers = font_button_big.render(text_revers, True, (255, 0, 0))
            button_revers_rect = button_revers.get_rect(center=button_revers_rect.center)
        else:
            button_revers = font_button.render(text_revers, True, (255, 255, 255))
            button_revers_rect = button_revers.get_rect(center=button_revers_rect.center)
        if button_parcing_rect.collidepoint(mouse_pos):
            button_parcing = font_button_big.render(text_parcing, True, (255, 0, 0))
            button_parcing_rect = button_parcing.get_rect(center=button_parcing_rect.center)
        else:
            button_parcing = font_button.render(text_parcing, True, (255, 255, 255))
            button_parcing_rect = button_parcing.get_rect(center=button_parcing_rect.center)
        screen.blit(background, (0, 0))
        screen.blit(exit_button, exit_button_rect)
        screen.blit(text_razvil_surface, (45, 150))
        screen.blit(button_shash, button_shash_rect)
        screen.blit(button_revers, button_revers_rect)
        screen.blit(button_parcing, button_parcing_rect)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


if Igor_down:
    manual()
