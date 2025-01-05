import pygame
import sqlite3


def shop():
    pygame.init()
    count_vibr = 0
    clock = pygame.time.Clock()
    size = 1200, 950
    screen = pygame.display.set_mode(size)
    background = pygame.image.load("image/fon.png")
    pygame.display.set_caption("Ретро-Гонки")
    background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
    font = pygame.font.Font(None, 55)
    font_money = pygame.font.Font(None, 74)
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
    conn_sprites = sqlite3.connect('sprites.db')
    cursor_sprites = conn_sprites.cursor()
    cursor_sprites.execute("CREATE TABLE IF NOT EXISTS sprites (id INTEGER PRIMARY KEY, count_one_sprite INTEGER, count_two_sprite INTEGER, count_three_sprite INTEGER, count_four_sprite)")
    cursor_sprites.execute("SELECT * FROM sprites WHERE id = 1")
    row = cursor_sprites.fetchone()
    if row is None:
        count_one_sprite = 0
        count_two_sprite = 0
        count_three_sprite = 0
        count_four_sprite = 0
        cursor_sprites.execute("INSERT INTO sprites (id, count_one_sprite, count_two_sprite, count_three_sprite) VALUES (1, ?, ?, ?)",
                               (count_one_sprite, count_two_sprite, count_three_sprite))
        conn_sprites.commit()
    else:
        count_one_sprite = row[1]
        count_two_sprite = row[2]
        count_three_sprite = row[3]
        count_four_sprite = row[4]
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
    text_money = str(money)
    text_money_surface = font_money.render(text_money, True, (255, 255, 255))
    one_car_image = pygame.image.load('image/sprite_one.png')
    text_exit_button = "Выход"
    exit_button = font_money.render(text_exit_button, True, (255, 255, 255))
    exit_button_rect = exit_button.get_rect(center=(100, 90))
    new_size = (100, 150)
    one_car_image = pygame.transform.scale(one_car_image, new_size)
    text1 = "Купить за 100"
    one_sprite = font.render(text1, True, (255, 255, 255))
    one_sprite_rect = one_sprite.get_rect(center=(150, 400))
    running = True
    baza_car_image = pygame.image.load("image/one_car_image.png")
    baza_car_image = pygame.transform.scale(baza_car_image, new_size)
    text2 = "Выбрано"
    baza_sprite = font.render(text2, True, (255, 255, 255))
    baza_sprite_rect = one_sprite.get_rect(center=(600, 400))
    text3 = "Купить за 50"
    two_sprite_car = font.render(text3, True, (255, 255, 255))
    two_sprite_car_rect = two_sprite_car.get_rect(center=(925, 400))
    two_car_image = pygame.image.load("image/two_car.png")
    two_car_image = pygame.transform.scale(two_car_image, new_size)
    text4 = "Купить за 150"
    three_sprite_car = font.render(text4, True, (255, 255, 255))
    three_sprite_car_rect = three_sprite_car.get_rect(center=(200, 800))
    three_car_image = pygame.image.load("image/three_car.png")
    three_car_image = pygame.transform.scale(three_car_image, new_size)
    text5 = "Купить за 75"
    four_sprite_car = font.render(text5, True, (255, 255, 255))
    four_sprite_car_rect = four_sprite_car.get_rect(center=(835, 800))
    four_car_image = pygame.image.load("image/four_car.png")
    four_car_image = pygame.transform.scale(four_car_image, new_size)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                conn_money.close()
                conn_sprites.close()
                conn_vibr.close()
                running = False
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if one_sprite_rect.collidepoint(event.pos) and money >= 100 and count_one_sprite == 0:
                    count_one_sprite = 1
                    text1 = "Выбрать"
                    one_sprite = font.render(text1, True, (255, 255, 255))
                    money -= 100
                    text_money = str(money)
                    cursor_money.execute("UPDATE money SET chet_money = ? WHERE id = 1", (text_money,))
                    conn_money.commit()
                    cursor_sprites.execute("UPDATE sprites SET count_one_sprite = ? WHERE id = 1", (count_one_sprite,))
                    conn_sprites.commit()
                    text_money_surface = font_money.render(text_money, True, (255, 255, 255))
                elif two_sprite_car_rect.collidepoint(event.pos) and money >= 50 and count_two_sprite == 0:
                    count_two_sprite = 1
                    text3 = "Выбрать"
                    two_sprite_car = font.render(text3, True, (255, 255, 255))
                    money -= 100
                    text_money = str(money)
                    cursor_money.execute("UPDATE money SET chet_money = ? WHERE id = 1", (text_money,))
                    conn_money.commit()
                    cursor_sprites.execute("UPDATE sprites SET count_two_sprite = ? WHERE id = 1", (count_two_sprite,))
                    conn_sprites.commit()
                    text_money_surface = font_money.render(text_money, True, (255, 255, 255))
                elif count_four_sprite == 0 and four_sprite_car_rect.collidepoint(event.pos) and money >= 75:
                    count_four_sprite = 1
                    text5 = "Выбрать"
                    four_sprite_car = font.render(text5, True, (255, 255, 255))
                    money -= 100
                    text_money = str(money)
                    cursor_money.execute("UPDATE money SET chet_money = ? WHERE id = 1", (text_money,))
                    conn_money.commit()
                    cursor_sprites.execute("UPDATE sprites SET count_four_sprite = ? WHERE id = 1", (count_four_sprite,))
                    conn_sprites.commit()
                    text_money_surface = font_money.render(text_money, True, (255, 255, 255))
                elif three_sprite_car_rect.collidepoint(event.pos) and money >= 150 and count_three_sprite == 0:
                    count_three_sprite = 1
                    text4 = "Выбрать"
                    three_sprite_car = font.render(text4, True, (255, 255, 255))
                    money -= 100
                    text_money = str(money)
                    cursor_money.execute("UPDATE money SET chet_money = ? WHERE id = 1", (text_money,))
                    conn_money.commit()
                    cursor_sprites.execute("UPDATE sprites SET count_three_sprite = ? WHERE id = 1", (count_three_sprite,))
                    conn_sprites.commit()
                    text_money_surface = font_money.render(text_money, True, (255, 255, 255))
                elif one_sprite_rect.collidepoint(event.pos) and count_one_sprite == 1:
                    text1 = "Выбрано"
                    one_sprite = font.render(text1, True, (255, 255, 255))
                    count_vibr = 1
                    cursor_vibr.execute("UPDATE vibr SET count_vibr = ? WHERE id = 1", (count_vibr,))
                    conn_vibr.commit()
                elif four_sprite_car_rect.collidepoint(event.pos) and count_four_sprite == 1:
                    text5 = "Выбрано"
                    four_sprite_car = font.render(text5, True, (255, 255, 255))
                    count_vibr = 4
                    cursor_vibr.execute("UPDATE vibr SET count_vibr = ? WHERE id = 1", (count_vibr,))
                    conn_vibr.commit()
                elif three_sprite_car_rect.collidepoint(event.pos) and count_three_sprite == 1:
                    text4 = "Выбрано"
                    three_sprite_car = font.render(text4, True, (255, 255, 255))
                    count_vibr = 3
                    cursor_vibr.execute("UPDATE vibr SET count_vibr = ? WHERE id = 1", (count_vibr,))
                    conn_vibr.commit()
                elif two_sprite_car_rect.collidepoint(event.pos) and count_two_sprite == 1:
                    text3 = "Выбрано"
                    two_sprite_car = font.render(text3, True, (255, 255, 255))
                    count_vibr = 2
                    cursor_vibr.execute("UPDATE vibr SET count_vibr = ? WHERE id = 1", (count_vibr,))
                    conn_vibr.commit()
                elif baza_sprite_rect.collidepoint(event.pos) and count_vibr != 0:
                    count_vibr = 0
                    cursor_vibr.execute("UPDATE vibr SET count_vibr = ? WHERE id = 1", (count_vibr,))
                    conn_vibr.commit()
                    text2 = "Выбрано"
                    baza_sprite = font.render(text2, True, (255, 255, 255))
                    baza_sprite_rect = one_sprite.get_rect(center=(565, 400))
                if exit_button_rect.collidepoint(event.pos):
                    from Menu import menu
                    scene = menu()
                    scene.menu()
            if count_one_sprite == 1:
                text1 = "Выбрать"
                one_sprite = font.render(text1, True, (255, 255, 255))
                one_sprite_rect = one_sprite.get_rect(center=(150, 400))
            if count_two_sprite == 1:
                text3 = "Выбрать"
                two_sprite_car = font.render(text3, True, (255, 255, 255))
                two_sprite_car_rect = two_sprite_car.get_rect(center=(925, 400))
            if count_four_sprite == 1:
                text5 = "Выбрать"
                four_sprite_car = font.render(text5, True, (255, 255, 255))
                four_sprite_car_rect = four_sprite_car.get_rect(center=(845, 800))
            if count_vibr != 0:
                text2 = "Выбрать"
                baza_sprite = font.render(text2, True, (255, 255, 255))
                baza_sprite_rect = one_sprite.get_rect(center=(565, 400))
            if count_vibr == 1:
                text1 = "Выбрано"
                one_sprite = font.render(text1, True, (255, 255, 255))
            if count_vibr == 3:
                text4 = "Выбрано"
                three_sprite_car = font.render(text4, True, (255, 255, 255))
            if count_vibr == 4:
                text5 = "Выбрано"
                four_sprite_car = font.render(text5, True, (255, 255, 255))
            if count_vibr == 2:
                text3 = "Выбрано"
                two_sprite_car = font.render(text3, True, (255, 255, 255))
            if count_vibr != 1 and count_one_sprite == 1:
                text1 = "Выбрать"
                one_sprite = font.render(text1, True, (255, 255, 255))
            if count_vibr != 2 and count_two_sprite == 1:
                text3 = "Выбрать"
                two_sprite_car = font.render(text3, True, (255, 255, 255))
            if count_vibr != 3 and count_three_sprite == 1:
                text4 = "Выбрать"
                three_sprite_car = font.render(text4, True, (255, 255, 255))
                three_sprite_car_rect = three_sprite_car.get_rect(center=(200, 800))
            if count_vibr != 4 and count_four_sprite == 1:
                text5 = "Выбрать"
                four_sprite_car = font.render(text5, True, (255, 255, 255))
        screen.blit(background, (0, 0))
        screen.blit(one_sprite, one_sprite_rect)
        screen.blit(one_car_image, (100, 200))
        screen.blit(baza_sprite, baza_sprite_rect)
        screen.blit(exit_button, exit_button_rect)
        screen.blit(two_sprite_car, two_sprite_car_rect)
        screen.blit(three_sprite_car, three_sprite_car_rect)
        screen.blit(four_sprite_car, four_sprite_car_rect)
        screen.blit(four_car_image, (800, 600))
        screen.blit(three_car_image, (150, 600))
        screen.blit(two_car_image, (885, 200))
        screen.blit(baza_car_image, (515, 200))
        screen.blit(text_money_surface, (1050, 50))
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
    shop()