import pygame
import sqlite3

def awards():
    pygame.init()
    size = 800, 950
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(size)
    background = pygame.image.load("image/fon.png")
    pygame.display.set_caption("Ретро-Гонки")
    conn_awards = sqlite3.connect("awards.db")
    cursor_awards = conn_awards.cursor()
    cursor_awards.execute(
        """ CREATE TABLE IF NOT EXISTS awards_table ( id INTEGER PRIMARY KEY, count_parking INTEGER, count_revers INTEGER, count_shashki INTEGER ) """)
    cursor_awards.execute("SELECT * FROM awards_table WHERE id = 1")
    i = cursor_awards.fetchone()
    if i is None:
        count_parking = 0
        count_shashki = 0
        count_revers = 0
        cursor_awards.execute(
            """ INSERT INTO awards_table (id, count_parking, count_revers, count_shashki) VALUES (1, ?, ?, ?) """,
            (count_parking,))
    else:
        count_revers = i[2]
        count_parking = i[1]
        count_shashki = i[3]
    font_big = pygame.font.Font(None, 75)
    text_awards = "Ваши награды"
    text_awards_rect = font_big.render(text_awards, True, (255, 255, 255))
    exit_text = "Выход"
    exit_button = font_big.render(exit_text, True, (255, 255, 255))
    exit_button_rect = exit_button.get_rect(center=(110, 50))
    text_rules = "Как получить?"
    rules_button = font_big.render(text_rules, True, (255, 255, 255))
    rules_button_rect = rules_button.get_rect(center=(575, 50))
    background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
    parking_image = pygame.image.load("image/pot_parking_awards.png")
    parking_image_rect = pygame.transform.scale(parking_image, (90, 90))
    revers_image = pygame.image.load("image/pot_revers_awards.png")
    revers_image_rect = pygame.transform.scale(revers_image, (90, 90))
    shashki_image = pygame.image.load("image/pot_shashki_awards.png")
    parking_awards = pygame.image.load("image/parcing awards.png")
    parking_awards_rect = pygame.transform.scale(parking_awards, (90, 90))
    shashki_awards = pygame.image.load("image/shahki awards.png")
    revers_awards = pygame.image.load("image/revers awards.png")
    font_exit_big = pygame.font.Font(None, 85)
    mouse_pos = pygame.mouse.get_pos()
    sound = pygame.mixer.Sound("audio/awards.mp3")
    sound.play(loops=-1)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.stop()
                pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button_rect.collidepoint(event.pos):
                    pygame.mixer.stop()
                    from Menu import menu
                    scene = menu()
                    scene.menu()
                if rules_button_rect.collidepoint(event.pos):
                    pygame.mixer.stop()
                    from razvil_manual import manual
                    scene = manual()
                    scene.menu()
        screen.blit(background, (0, 0))
        if exit_button_rect.collidepoint(mouse_pos):
            exit_button = font_exit_big.render(exit_text, True, (255, 0, 0))
            exit_button_rect = exit_button.get_rect(center=exit_button_rect.center)
        else:
            exit_button = font_big.render(exit_text, True, (255, 255, 255))
            exit_button_rect = exit_button.get_rect(center=exit_button_rect.center)
        if rules_button_rect.collidepoint(mouse_pos):
            rules_button = font_exit_big.render(text_rules, True, (255, 0, 0))
            rules_button_rect = rules_button.get_rect(center=rules_button_rect.center)
        else:
            rules_button = font_big.render(text_rules, True, (255, 255, 255))
            rules_button_rect = rules_button.get_rect(center=rules_button_rect.center)
        if count_parking == 0:
            screen.blit(parking_image, (100, 600))
        else:
            screen.blit(parking_awards, (100, 600))
        if count_revers == 0:
            screen.blit(revers_image, (500, 600))
        else:
            screen.blit(revers_awards, (500, 600))
        if count_shashki == 0:
            screen.blit(shashki_image, (285, 300))
        else:
            screen.blit(shashki_awards, (285, 300))
        screen.blit(text_awards_rect, (225, 150))
        screen.blit(exit_button, exit_button_rect)
        screen.blit(rules_button, rules_button_rect)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    awards()