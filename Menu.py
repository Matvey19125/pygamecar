import pygame
import sys
import sqlite3
from razvil import razvil
from shop import shop
from awards import awards
from fortuna import fortuna


def menu():
    pygame.init()
    size = 800, 950
    screen = pygame.display.set_mode(size)
    background = pygame.image.load("image/fon.png")
    pygame.display.set_caption("Ретро-Гонки")
    background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
    WHITE = (255, 255, 255)
    RED = (255, 50, 0)
    count_vibr = 0
    count_parking = 0
    count_revers = 0
    count_shashki = 0
    conn_vibr = sqlite3.connect('vibr.db')
    cursor_vibr = conn_vibr.cursor()
    cursor_vibr.execute("CREATE TABLE IF NOT EXISTS vibr (id INTEGER PRIMARY KEY, count_vibr INTEGER)")
    cursor_vibr.execute("SELECT * FROM vibr WHERE id = 1")
    row = cursor_vibr.fetchone()
    if row is None:
        cursor_vibr.execute("INSERT INTO vibr (id, count_vibr) VALUES (1, ?)", (count_vibr,))
        conn_vibr.commit()
    else:
        count_vibr = row[1]
    conn_awards = sqlite3.connect("awards.db")
    cursor_awards = conn_awards.cursor()
    cursor_awards.execute(
        """ CREATE TABLE IF NOT EXISTS awards_table ( id INTEGER PRIMARY KEY, count_parking INTEGER, count_revers INTEGER, count_shashki INTEGER ) """)
    cursor_awards.execute("SELECT * FROM awards_table WHERE id = 1")
    i = cursor_awards.fetchone()
    if i is None:
        cursor_awards.execute(
            """ INSERT INTO awards_table (id, count_parking, count_revers, count_shashki) VALUES (1, ?, ?, ?) """,
            (count_parking, count_revers, count_shashki))
    conn_awards.commit()
    font = pygame.font.Font(None, 74)
    play_text = 'Играть'
    shop_text = 'Магазин'
    fortune_wheel_text = 'Колесо Фортуны'
    exit_text = 'Выход'
    awards_text = "Награды"
    button_awards = font.render(awards_text, True, WHITE)
    play_button_normal = font.render(play_text, True, WHITE)
    shop_button_normal = font.render(shop_text, True, WHITE)
    fortune_wheel_button_normal = font.render(fortune_wheel_text, True, WHITE)
    exit_button_normal = font.render(exit_text, True, WHITE)
    font_large = pygame.font.Font(None, 80)
    play_button_hover = font_large.render(play_text, True, RED)
    shop_button_hover = font_large.render(shop_text, True, RED)
    fortune_wheel_button_hover = font_large.render(fortune_wheel_text, True, RED)
    exit_button_hover = font_large.render(exit_text, True, RED)
    awards_button_hover = font_large.render(awards_text, True, RED)
    play_button_rect = play_button_normal.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 200))
    shop_button_rect = shop_button_normal.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 125))
    fortune_wheel_button_rect = fortune_wheel_button_normal.get_rect(
        center=(screen.get_width() // 2, screen.get_height() // 2 + 25))
    awards_button_rect = button_awards.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 50))
    exit_button_rect = exit_button_normal.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 100))
    play_button_hover_rect = play_button_hover.get_rect(center=play_button_rect.center)
    shop_button_hover_rect = shop_button_hover.get_rect(center=shop_button_rect.center)
    fortune_wheel_button_hover_rect = fortune_wheel_button_hover.get_rect(center=fortune_wheel_button_rect.center)
    awards_button_hover_rect = awards_button_hover.get_rect(center=awards_button_rect.center)
    exit_button_hover_rect = exit_button_hover.get_rect(center=exit_button_rect.center)
    moving_image = pygame.image.load("image/one_car_image.png")
    moving_image_rect = moving_image.get_rect(center=screen.get_rect().midbottom)
    animation_speed = 5
    animation_speed2 = 3
    moving_image2 = pygame.image.load("image/two_car.png")
    moving_image2 = pygame.transform.rotate(moving_image2, 180)
    moving_image2_rect = moving_image2.get_rect(center=(screen.get_rect().midtop[0] - 100, screen.get_rect().midtop[1]))
    moving_image3 = pygame.image.load("image/three_car.png")
    moving_image3_rect = moving_image3.get_rect(center=(screen.get_rect().midbottom[0] - 200, screen.get_rect().midbottom[1]))
    moving_image4 = pygame.image.load("image/four_car.png")
    moving_image4 = pygame.transform.rotate(moving_image4, 180)
    moving_image4_rect = moving_image4.get_rect(center=(screen.get_rect().midtop[0] + 100, screen.get_rect().midtop[1]))
    moving_image5 = pygame.image.load("image/sprite_one.png")
    moving_image5_rect = moving_image5.get_rect(center=(screen.get_rect().midbottom[0] + 200, screen.get_rect().midbottom[1]))
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
                    shoes_scene = razvil()
                    shoes_scene.razvil()
                    running = False
                elif shop_button_rect.collidepoint(event.pos):
                    scene = shop()
                    scene.shop()
                    running = True
                elif fortune_wheel_button_rect.collidepoint(event.pos):
                    scene = fortuna()
                    scene.fortuna()
                elif awards_button_rect.collidepoint(event.pos):
                    scene = awards()
                    scene.awards()
                elif exit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
        moving_image_rect.y -= animation_speed
        moving_image2_rect.y += animation_speed2
        moving_image3_rect.y -= 7
        moving_image4_rect.y += 4
        moving_image5_rect.y -= 9
        if moving_image_rect.bottom < 0:
            moving_image_rect.midbottom = screen.get_rect().midbottom
        moving_image2_rect.y += animation_speed2
        if moving_image2_rect.top > screen.get_rect().height:
            moving_image2_rect.topleft = (screen.get_rect().midtop[0] - 100, 0)
        if moving_image3_rect.bottom < 0:
            moving_image3_rect.midbottom = (screen.get_rect().midbottom[0] - 200, screen.get_rect().midbottom[1])
        if moving_image4_rect.top > screen.get_rect().height:
            moving_image4_rect.topleft = (screen.get_rect().midtop[0] + 100, 0)
        if moving_image5_rect.bottom < 0:
            moving_image5_rect.midbottom = (screen.get_rect().midbottom[0] + 200, screen.get_rect().midbottom[1])
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
        if fortune_wheel_button_rect.collidepoint(mouse_pos):
            fortune_wheel_button_to_draw = fortune_wheel_button_hover
            fortune_wheel_button_rect_to_use = fortune_wheel_button_hover_rect
        else:
            fortune_wheel_button_to_draw = fortune_wheel_button_normal
            fortune_wheel_button_rect_to_use = fortune_wheel_button_rect

        if awards_button_rect.collidepoint(mouse_pos):
            awards_button_to_draw = awards_button_hover
            awards_button_rect_to_use = awards_button_hover_rect
        else:
            awards_button_to_draw = button_awards
            awards_button_rect_to_use = awards_button_rect
        if exit_button_rect.collidepoint(mouse_pos):
            exit_button_to_draw = exit_button_hover
            exit_button_rect_to_use = exit_button_hover_rect
        else:
            exit_button_to_draw = exit_button_normal
            exit_button_rect_to_use = exit_button_rect

        screen.blit(background, (0, 0))
        screen.blit(moving_image2, moving_image2_rect)
        screen.blit(moving_image, moving_image_rect)
        screen.blit(moving_image3, moving_image3_rect)
        screen.blit(moving_image4, moving_image4_rect)
        screen.blit(moving_image5, moving_image5_rect)
        screen.blit(play_button_to_draw, play_button_rect_to_use)
        screen.blit(shop_button_to_draw, shop_button_rect_to_use)
        screen.blit(fortune_wheel_button_to_draw, fortune_wheel_button_rect_to_use)
        screen.blit(awards_button_to_draw, awards_button_rect_to_use)
        screen.blit(exit_button_to_draw, exit_button_rect_to_use)
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    menu()