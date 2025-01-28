import pygame

def manual_parking():
    pygame.init()
    clock = pygame.time.Clock()
    size = 800, 950
    screen = pygame.display.set_mode(size)
    background = pygame.image.load("image/fon.png")
    pygame.display.set_caption("Ретро-Гонки")
    background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
    font_text = pygame.font.Font(None, 50)
    font_button = pygame.font.Font(None, 70)
    font_button_big = pygame.font.Font(None, 80)
    text_manual = "Чтобы заработать награду в режиме 'Парковка' нужно пройти 5 уровней"
    text_exit = 'Понятно'
    exit_button = font_button.render(text_exit, True, (255, 255, 255))
    exit_button_rect = exit_button.get_rect(center=(410, 750))
    lines = text_manual.split(' ')
    wrapped_lines = []
    mouse_pos = pygame.mouse.get_pos()
    current_line = ""
    max_width = 600
    for word in lines:
        test_line = current_line + word + " "
        if font_text.size(test_line)[0] < max_width:
            current_line += word + " "
        else:
            wrapped_lines.append(current_line[:-1])
            current_line = word + " "
    if current_line != "":
        wrapped_lines.append(current_line[:-1])
    y_offset = 400
    line_spacing = 30
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button_rect.collidepoint(event.pos):
                    from razvil_manual import manual
                    scene = manual()
                    scene.manual()
        if exit_button_rect.collidepoint(mouse_pos):
            exit_button = font_button_big.render(text_exit, True, (255, 0, 0))
            exit_button_rect = exit_button.get_rect(center=exit_button_rect.center)
        else:
            exit_button = font_button.render(text_exit, True, (255, 255, 255))
            exit_button_rect = exit_button.get_rect(center=exit_button_rect.center)
        screen.blit(background, (0, 0))
        screen.blit(exit_button, exit_button_rect)
        for i, line in enumerate(wrapped_lines):
            text_surface = font_text.render(line, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(screen.get_width() // 2, y_offset + i * line_spacing))
            screen.blit(text_surface, text_rect.topleft)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    manual_parking()