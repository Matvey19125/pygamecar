import pygame
import sqlite3


def level_menu():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Ретро-Гонки")
    size = 800, 950
    screen = pygame.display.set_mode(size)
    background = pygame.image.load("image/fon.png")
    conn_money = sqlite3.connect('level.db')
    cursor_money = conn_money.cursor()
    cursor_money.execute("""CREATE TABLE IF NOT EXISTS leveltable ( id INTEGER PRIMARY KEY, two INTEGER, three INTEGER, four INTEGER, five INTEGER)""")
    cursor_money.execute("SELECT * FROM leveltable WHERE id = 1")
    row = cursor_money.fetchone()

    if row is None:
        count_two_level = 0
        count_three_level = 0
        count_four_level = 0
        count_five_level = 0
        cursor_money.execute(
            """INSERT INTO leveltable (id, two, three, four, five) VALUES (?, ?, ?, ?, ?)""",
            (1, count_two_level, count_three_level, count_four_level, count_five_level))
        conn_money.commit()
    else:
        count_two_level = row[1]
        count_three_level = row[2]
        count_four_level = row[3]
        count_five_level = row[4]
    pygame.display.set_caption("Ретро-Гонки")
    background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
    font = pygame.font.Font(None, 55)
    font_big = pygame.font.Font(None, 65)
    font_menu = pygame.font.Font(None, 75)
    font_menu_plus = pygame.font.Font(None, 80)
    text_menu = "Выберите уровень"
    text_menu_render = font_menu.render(text_menu, True, (255, 255, 255))
    text_menu_render_rect = text_menu_render.get_rect(center=(400, 75))
    text1 = "Уровень 1"
    one_level = font.render(text1, True, (255, 255, 255))
    one_level_rect = one_level.get_rect(center=(400, 200))
    text2 = "Уровень 2"
    two_level = font.render(text2, True, (255, 255, 255))
    two_level_rect = two_level.get_rect(center=(400, 300))
    text3 = "Уровень 3"
    three_level = font.render(text3, True, (255, 255, 255))
    three_level_rect = three_level.get_rect(center=(400, 400))
    text4 = "Уровень 4"
    four_level = font.render(text4, True, (255, 255, 255))
    four_level_rect = four_level.get_rect(center=(400, 500))
    text5 = "Уровень 5"
    five_level = font.render(text5, True, (255, 255, 255))
    five_level_rect = five_level.get_rect(center=(400, 600))
    text_exit = "Выход"
    exit_level = font_menu.render(text_exit, True, (255, 255, 255))
    exit_level_rect = exit_level.get_rect(center=(400, 800))
    mouse_pos = pygame.mouse.get_pos()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if one_level_rect.collidepoint(event.pos):
                    from levelone import park
                    scene = park()
                    scene.park()
                if two_level_rect.collidepoint(event.pos):
                    from leveltwo import park2
                    scene = park2()
                    scene.park2()
                if three_level_rect.collidepoint(event.pos):
                    from levelthree import park3
                    scene = park3()
                    scene.park3()
                if four_level_rect.collidepoint(event.pos):
                    from levelfour import park4
                    scene = park4()
                    scene.park4()
                if five_level_rect.collidepoint(event.pos):
                    from levelfive import park5
                    scene = park5()
                    scene.park5()
                if exit_level_rect.collidepoint(event.pos):
                    from razvil import razvil
                    scene = razvil()
                    scene.razvil()
            if one_level_rect.collidepoint(mouse_pos):
                one_level = font_big.render(text1, True, (255, 0, 0))
                one_level_rect = one_level.get_rect(center=one_level_rect.center)
            else:
                one_level = font.render(text1, True, (255, 255, 255))
                one_level_rect = one_level.get_rect(center=one_level_rect.center)
            if two_level_rect.collidepoint(mouse_pos):
                two_level = font_big.render(text2, True, (255, 0, 0))
                two_level_rect = two_level.get_rect(center=two_level_rect.center)
            else:
                two_level = font.render(text2, True, (255, 255, 255))
                two_level_rect = two_level.get_rect(center=two_level_rect.center)
            if three_level_rect.collidepoint(mouse_pos):
                three_level = font_big.render(text3, True, (255, 0, 0))
                three_level_rect = three_level.get_rect(center=three_level_rect.center)
            else:
                three_level = font.render(text3, True, (255, 255, 255))
                three_level_rect = three_level.get_rect(center=three_level_rect.center)
            if four_level_rect.collidepoint(mouse_pos):
                four_level = font_big.render(text4, True, (255, 0, 0))
                four_level_rect = four_level.get_rect(center=four_level_rect.center)
            else:
                four_level = font.render(text4, True, (255, 255, 255))
                four_level_rect = four_level.get_rect(center=four_level_rect.center)
            if five_level_rect.collidepoint(mouse_pos):
                five_level = font_big.render(text5, True, (255, 0, 0))
                five_level_rect = five_level.get_rect(center=five_level_rect.center)
            else:
                five_level = font.render(text5, True, (255, 255, 255))
                five_level_rect = five_level.get_rect(center=five_level_rect.center)
            if exit_level_rect.collidepoint(mouse_pos):
                exit_level = font_menu_plus.render(text_exit, True, (255, 0, 0))
                exit_level_rect = exit_level.get_rect(center=exit_level_rect.center)
            else:
                exit_level = font_menu.render(text_exit, True, (255, 255, 255))
                exit_level_rect = exit_level.get_rect(center=exit_level_rect.center)
        screen.blit(background, (0, 0))
        screen.blit(one_level, one_level_rect)
        screen.blit(text_menu_render, text_menu_render_rect)
        if count_two_level == 1:
            screen.blit(two_level, two_level_rect)
        else:
            pass
        if count_three_level == 1:
            screen.blit(three_level, three_level_rect)
        else:
            pass
        if count_four_level == 1:
            screen.blit(four_level, four_level_rect)
        else:
            pass
        if count_five_level == 1:
            screen.blit(five_level, five_level_rect)
        else:
            pass
        screen.blit(exit_level, exit_level_rect)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
    level_menu()