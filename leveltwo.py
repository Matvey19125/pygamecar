import pygame
import random
import sqlite3
from levelthree import park3

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Ретро-Гонки")


def park2():
    size = width, height = 800, 960
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Ретро-Гонки")
    fence_color = (150, 75, 0)
    car_x = 50
    car_y = 50
    car_width = 100
    car_height = 130
    font = pygame.font.Font(None, 55)
    conn_money = sqlite3.connect('money.db')
    cursor_money = conn_money.cursor()
    cursor_money.execute("CREATE TABLE IF NOT EXISTS money (id INTEGER PRIMARY KEY, chet_money INTEGER)")
    cursor_money.execute("SELECT * FROM money WHERE id = 1")
    row = cursor_money.fetchone()
    if row is None:
        money = 0
        cursor_money.execute("INSERT INTO money (id, chet_money) VALUES (1, ?)", (money,))
        conn_money.commit()
    else:
        money = row[1]
    text = str(money)
    conn_car = sqlite3.connect('level.db')
    cursor_car = conn_car.cursor()
    cursor_car.execute(
        """ CREATE TABLE IF NOT EXISTS leveltable ( id INTEGER PRIMARY KEY, two INTEGER, three INTEGER, four INTEGER, five INTEGER ) """)
    cursor_car.execute("SELECT * FROM leveltable WHERE id = ?", (1,))
    row = cursor_car.fetchone()
    if row is None:
        count_two_level = 0
        count_three_level = 0
        count_four_level = 0
        count_five_level = 0

        cursor_car.execute(""" INSERT INTO leveltable (id, two, three, four, five) VALUES (?, ?, ?, ?, ?) """,
                           (1, count_two_level, count_three_level, count_four_level, count_five_level))
    else:
        count_three_level = row[1]
    text_money_surface = font.render(text, True, (255, 255, 255))
    conn = sqlite3.connect('vibr.db')
    cursor = conn.cursor()
    cursor.execute("SELECT count_vibr FROM vibr")
    result = cursor.fetchone()
    count_vibr = result[0]
    scrin_car = [
        'image/one_car_image.png',
        'image/sprite_one.png',
        'image/two_car.png',
        'image/three_car.png',
        'image/four_car.png'
    ]
    sprite_image = pygame.image.load(scrin_car[count_vibr]).convert_alpha()
    scaled_sprite = pygame.transform.scale(sprite_image, (car_width, car_height))
    car_collider = scaled_sprite.get_rect(topleft=(car_x, car_y))
    car_angle = 0
    money_image = pygame.image.load('image/money_image.png')
    money_scaled = pygame.transform.scale(money_image, (80, 80))
    money_collider = pygame.Rect((635, 100, 60, 60))
    tochka_win = pygame.image.load("image/win.png")
    tochka_win_scaled = pygame.transform.scale(tochka_win, (20, 20))
    tochka_win_collider = pygame.Rect((50, 665, 20, 20))
    parcing_image = pygame.image.load('image/parcing.png')
    parcing_scaled = pygame.transform.scale(parcing_image, (60, 90))
    parcing_collider = pygame.Rect((50, 680, 80, 80))
    nps_car = ['image/potok_car1.png', 'image/potok_car2.png', 'image/potok_car3.png', 'image/potok_car4.png',
               'image/potok_car5.png', 'image/potok_car6.png']
    nps_one_sprite = pygame.image.load(nps_car[random.randrange(0, 6)])
    nps_one_scaled = pygame.transform.scale(nps_one_sprite, (car_width, car_height))
    nps_one_collider = nps_one_scaled.get_rect(topleft=(200, 400))
    nps_two_sprite = pygame.image.load(nps_car[random.randrange(0, 6)])
    nps_two_scaled = pygame.transform.scale(nps_two_sprite, (car_width, car_height))
    nps_two_collider = nps_two_scaled.get_rect(topleft=(200, 535))
    nps_three_sprite = pygame.image.load(nps_car[random.randrange(0, 6)])
    nps_three_scaled = pygame.transform.scale(nps_three_sprite, (car_width, car_height))
    nps_three_collider = nps_three_scaled.get_rect(topleft=(550, 400))
    nps_four_sprite = pygame.image.load(nps_car[random.randrange(0, 6)])
    nps_four_scaled = pygame.transform.scale(nps_four_sprite, (car_width, car_height))
    nps_four_collider = nps_four_scaled.get_rect(topleft=(305, 670))
    nps_five_sprite = pygame.image.load(nps_car[random.randrange(0, 6)])
    nps_five_scaled = pygame.transform.scale(nps_five_sprite, (car_width, car_height))
    nps_five_collider = nps_five_scaled.get_rect(topleft=(305, 400))
    nps_six_sprite = pygame.image.load(nps_car[random.randrange(0, 6)])
    nps_six_scaled = pygame.transform.scale(nps_six_sprite, (car_width, car_height))
    nps_six_collider = nps_six_scaled.get_rect(topleft=(60, 490))
    nps_seven_sprite = pygame.image.load(nps_car[random.randrange(0, 6)])
    nps_seven_sprite = pygame.transform.rotate(nps_seven_sprite, 90)
    nps_seven_scaled = pygame.transform.scale(nps_seven_sprite, (car_height, car_width))
    nps_seven_collider = nps_seven_scaled.get_rect(topleft=(150, 700))
    nps_eith_sprite = pygame.image.load(nps_car[random.randrange(0, 6)])
    nps_eith_scaled = pygame.transform.scale(nps_eith_sprite, (car_width, car_height))
    nps_eith_collider = nps_eith_scaled.get_rect(topleft=(500, 50))
    nps_nine_sprite = pygame.image.load(nps_car[random.randrange(0, 6)])
    nps_nine_scaled = pygame.transform.scale(nps_nine_sprite, (car_width, car_height))
    nps_nine_collider = nps_nine_scaled.get_rect(topleft=(650, 350))
    sound = pygame.mixer.Sound("audio/level2.mp3")
    sound.play(loops=-1)
    running = True

    def lose():
        pygame.mixer.stop()
        pygame.mixer.init()
        crash_sound = pygame.mixer.Sound("audio/crash.mp3")
        channel = crash_sound.play()
        running1 = True
        font_button = pygame.font.Font(None, 60)
        text_restart = "Заново"
        text_menu = "В меню"
        button_restart = font_button.render(text_restart, True, (255, 255, 255))
        button_menu = font_button.render(text_menu, True, (255, 255, 255))
        button_restart_rect = button_restart.get_rect(center=(200, 700))
        button_menu_rect = button_menu.get_rect(center=(600, 700))
        clock = pygame.time.Clock()
        sound_playing = True
        show_button = False
        mouse_pos = pygame.mouse.get_pos()
        while running1:
            time_delta = clock.tick(60) / 1000.0
            screen.fill((0, 0, 0))
            font = pygame.font.Font(None, 35)
            text = font.render("Вы врезались! Нажмите кнопку 'Заново' для перезагрузки", True, (255, 255, 255))
            text_rect = text.get_rect(center=(400, 250))
            if not channel.get_busy():
                sound_playing = False
                if not show_button:
                    show_button = True
            if show_button:
                screen.blit(text, text_rect)
                screen.blit(button_restart, button_restart_rect)
                screen.blit(button_menu, button_menu_rect)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
                    if event.type == pygame.MOUSEMOTION:
                        mouse_pos = pygame.mouse.get_pos()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if button_restart_rect.collidepoint(event.pos):
                            park2()
                            return
                        if button_menu_rect.collidepoint(event.pos):
                            from Menu import menu
                            scene = menu()
                            scene.menu()
                            return
                if button_restart_rect.collidepoint(mouse_pos):
                    font_button_big = pygame.font.Font(None, 75)
                    button_restart = font_button_big.render(text_restart, True, (255, 0, 0))
                    button_restart_rect = button_restart.get_rect(center=button_restart_rect.center)
                else:
                    button_restart = font_button.render(text_restart, True, (255, 255, 255))
                    button_restart_rect = button_restart.get_rect(center=button_restart_rect.center)

                if button_menu_rect.collidepoint(mouse_pos):
                    font_button_big = pygame.font.Font(None, 75)
                    button_menu = font_button_big.render(text_menu, True, (255, 0, 0))
                    button_menu_rect = button_menu.get_rect(center=button_menu_rect.center)
                else:
                    button_menu = font_button.render(text_menu, True, (255, 255, 255))
                    button_menu_rect = button_menu.get_rect(center=button_menu_rect.center)
            pygame.display.update()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.mixer.stop()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d and car_x + car_width < width - 20:
                    car_angle = 270
                    car_x += 30
                    car_collider.x = car_x
                if event.key == pygame.K_a and car_x > 20:
                    car_angle = 90
                    car_x -= 30
                    car_collider.x = car_x
                if event.key == pygame.K_w and car_y > 20:
                    car_angle = 0
                    car_y -= 30
                    car_collider.y = car_y
                if event.key == pygame.K_s and car_y + car_height < height - 50:
                    car_angle = 180
                    car_y += 30
                    car_collider.y = car_y
        rotated_sprite = pygame.transform.rotate(scaled_sprite, car_angle)
        car_collider = rotated_sprite.get_rect(topleft=(car_x, car_y))
        if car_collider.colliderect(nps_one_collider) or car_collider.colliderect(
                nps_two_collider) or car_collider.colliderect(nps_three_collider) or car_collider.colliderect(
                nps_four_collider):
            lose()
        if car_collider.colliderect(nps_five_collider) or car_collider.colliderect(
                nps_six_collider) or car_collider.colliderect(nps_seven_collider) or car_collider.colliderect(
                nps_eith_collider) or car_collider.colliderect(nps_nine_collider):
            lose()
        if money_collider.x >= 0 and money_collider.y >= 0:
            if car_collider.colliderect(money_collider):
                money += 10
                cursor_money.execute("UPDATE money SET chet_money = ? WHERE id = 1", (money,))
                conn_money.commit()
                money_collider.x = -100
                money_collider.y = -100
        if car_collider.colliderect(parcing_collider):
            parcing_collider.x = -100
            parcing_collider.y = -100
        if car_collider.colliderect(tochka_win_collider):
            pygame.mixer.stop()
            money += 15
            cursor_money.execute("UPDATE money SET chet_money = ? WHERE id = 1", (money,))
            conn_money.commit()
            running1 = True
            clock = pygame.time.Clock()

            # Создаем кнопки для меню победы
            font_button = pygame.font.Font(None, 60)
            text_restart = "Далее"
            text_menu = "В меню"
            button_restart = font_button.render(text_restart, True, (255, 255, 255))
            button_menu = font_button.render(text_menu, True, (255, 255, 255))
            button_restart_rect = button_restart.get_rect(center=(200, 700))
            button_menu_rect = button_menu.get_rect(center=(600, 700))

            while running1:
                mouse_pos = pygame.mouse.get_pos()
                time_delta = clock.tick(60) / 1000.0
                screen.fill((0, 0, 0))
                font = pygame.font.Font(None, 35)
                text = font.render("Поздравляем! Вы прошли уровень!", True, (255, 255, 255))
                text_rect = text.get_rect(center=(400, 250))
                screen.blit(text, text_rect)

                # Рисуем кнопки
                screen.blit(button_restart, button_restart_rect)
                screen.blit(button_menu, button_menu_rect)

                # Обработка событий
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if button_restart_rect.collidepoint(event.pos):
                            count_three_level = 1
                            cursor_car.execute(""" UPDATE leveltable SET three = ? WHERE id = 1 """,
                                               (count_three_level,))
                            conn_car.commit()
                            scene = park3()
                            scene.park3()
                            return
                        if button_menu_rect.collidepoint(event.pos):
                            from Menu import menu
                            scene = menu()
                            scene.menu()
                            return

                # Подсветка кнопок при наведении
                if button_restart_rect.collidepoint(mouse_pos):
                    font_button_big = pygame.font.Font(None, 75)
                    button_restart = font_button_big.render(text_restart, True, (255, 0, 0))
                    button_restart_rect = button_restart.get_rect(center=button_restart_rect.center)
                else:
                    button_restart = font_button.render(text_restart, True, (255, 255, 255))
                    button_restart_rect = button_restart.get_rect(center=button_restart_rect.center)

                if button_menu_rect.collidepoint(mouse_pos):
                    font_button_big = pygame.font.Font(None, 75)
                    button_menu = font_button_big.render(text_menu, True, (255, 0, 0))
                    button_menu_rect = button_menu.get_rect(center=button_menu_rect.center)
                else:
                    button_menu = font_button.render(text_menu, True, (255, 255, 255))
                    button_menu_rect = button_menu.get_rect(center=button_menu_rect.center)

                pygame.display.update()

        text = str(money)
        text_money_surface = font.render(text, True, (255, 255, 255))
        screen.blit(text_money_surface, (20, 20))
        pygame.display.flip()
        text = str(money)
        text_money_surface = font.render(text, True, (255, 255, 255))
        screen.blit(text_money_surface, (20, 20))
        pygame.display.flip()
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, fence_color, (0, 0, width, 10))
        pygame.draw.rect(screen, fence_color, (0, height - 10, width, 10))
        pygame.draw.rect(screen, fence_color, (0, 0, 10, height))
        pygame.draw.rect(screen, fence_color, (width - 10, 0, 10, height))
        screen.blit(rotated_sprite, car_collider)
        screen.blit(nps_two_scaled, nps_two_collider)
        screen.blit(nps_one_scaled, nps_one_collider)
        screen.blit(nps_three_scaled, nps_three_collider)
        screen.blit(nps_four_scaled, nps_four_collider)
        screen.blit(nps_five_scaled, nps_five_collider)
        screen.blit(nps_six_scaled, nps_six_collider)
        screen.blit(nps_seven_scaled, nps_seven_collider)
        screen.blit(nps_eith_scaled, nps_eith_collider)
        screen.blit(nps_nine_scaled, nps_nine_collider)
        screen.blit(money_scaled, money_collider)
        screen.blit(tochka_win_scaled, tochka_win_collider)
        screen.blit(parcing_scaled, parcing_collider)
        screen.blit(text_money_surface, (20, 20))
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    park2()