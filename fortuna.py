import pygame
import math
import random
import sqlite3
import time


# Функция для отрисовки текста по кругу
def draw_text_in_circle(surface, text, center, radius, color, font_size=30):
    font = pygame.font.SysFont('Arial', font_size)
    text_surface = font.render(text, True, color)
    rect = text_surface.get_rect()
    num_angles = len(text)
    angle_step = 360 / num_angles
    for i, char in enumerate(text):
        angle = math.radians(-90 + i * angle_step)
        pos_x = int(center[0] + radius * math.cos(angle)) - rect.width // 2
        pos_y = int(center[1] + radius * math.sin(angle)) - rect.height // 2
        surface.blit(text_surface, (pos_x, pos_y))


# Основная функция игры
def fortuna():
    pygame.init()
    size = 1200, 950
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Ретро-Гонки")

    # Загрузка фона
    background = pygame.image.load("image/fon.png").convert()
    background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))

    # Шрифты
    font = pygame.font.Font(None, 45)
    font_money = pygame.font.Font(None, 50)
    font_exit = pygame.font.Font(None, 65)

    # Подключение к базе данных
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

    # Отображение денег
    text_money = str(money)
    text_money_sprite = font_money.render(text_money, True, (255, 255, 255))
    text_money_sprite_rect = text_money_sprite.get_rect(center=(85, 60))

    # Текст кнопки
    text_button = "Крутить барабан за 10"
    button_sprite = font.render(text_button, True, (255, 255, 255))
    button_sprite_rect = button_sprite.get_rect(center=(600, 850))

    # Курсор
    cursor_image = pygame.image.load("image/cursor.png")
    cursor_image = pygame.transform.scale(cursor_image, (70, 70))

    # Кнопка выхода
    exit_text = "Выход"
    exit_button = font_exit.render(exit_text, True, (255, 255, 255))
    exit_button_rect = exit_button.get_rect(center=(1080, 50))
    count = 0
    # Текст победы
    win_text = "Вы выиграли!"
    win_text_sprite = font.render(win_text, True, (255, 255, 255))
    win_text_sprite_rect = win_text_sprite.get_rect(center=(600, 475))
    lose_text = "Вы проиграли"
    lose_text_sprite = font.render(lose_text, True, (255, 255, 255))
    lose_text_sprite_rect = lose_text_sprite.get_rect(center=(600, 475))
    # Параметры барабана
    wheel_center = (600, 450)
    wheel_radius = 300
    sectors = ["1", "2", "3", "4", "5", "6"]  # Теперь у нас шесть секторов
    sector_colors = [(255, 0, 0), (0, 255, 0), (255, 0, 0), (0, 255, 0), (255, 0, 0), (0, 255, 0)]  # Три красных и три зеленых сектора

    current_angle = 0
    rotating = False
    speed = 0
    result_shown = False
    running = True
    start_time = None
    clock = pygame.time.Clock()
    first_spin_completed = False
    mouse_pos = pygame.mouse.get_pos()
    click_time = 0
    passed_time = 0
    show_win_timer = 0  # Переменная для отслеживания времени показа сообщения о победе
    show_lose_timer = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEBUTTONDOWN and not rotating:
                if exit_button_rect.collidepoint(event.pos):
                    from Menu import menu
                    scene = menu()
                    scene.menu()
                if button_sprite_rect.collidepoint(event.pos):
                    if money >= 10:
                        money -= 10
                        text_money = str(money)
                        cursor_money.execute("UPDATE money SET chet_money = ? WHERE id = 1", (text_money,))
                        conn_money.commit()
                        text_money_sprite = font_money.render(text_money, True, (255, 255, 255))
                        rotating = True
                        speed = random.randint(5, 15)
                        result_shown = False
                        first_spin_completed = False

        if exit_button_rect.collidepoint(mouse_pos):
            font_exit_big = pygame.font.Font(None, 73)
            exit_button = font_exit_big.render(exit_text, True, (255, 0, 0))
        else:
            exit_button = font_exit.render(exit_text, True, (255, 255, 255))

        if button_sprite_rect.collidepoint(mouse_pos):
            font_button_big = pygame.font.Font(None, 55)
            button_sprite = font_button_big.render(text_button, True, (255, 0, 0))
            button_sprite_rect = button_sprite.get_rect(center=button_sprite_rect.center)
        else:
            button_sprite = font.render(text_button, True, (255, 255, 255))
            button_sprite_rect = button_sprite.get_rect(center=button_sprite_rect.center)

        screen.blit(background, (0, 0))
        screen.blit(button_sprite, button_sprite_rect)

        # Рисуем секторы барабана
        for i in range(len(sectors)):
            start_angle = math.radians(i * 60)  # Каждый сектор занимает 60 градусов
            end_angle = math.radians((i + 1) * 60)
            pygame.draw.arc(screen, sector_colors[i],
                            [wheel_center[0] - wheel_radius, wheel_center[1] - wheel_radius, 2 * wheel_radius,
                             2 * wheel_radius],
                            start_angle, end_angle, 20)
            text_pos = (
                int(wheel_center[0] + (wheel_radius - 100) * math.cos(start_angle + (end_angle - start_angle) / 2)),
                int(wheel_center[1] + (wheel_radius - 100) * math.sin(start_angle + (end_angle - start_angle) / 2))
            )
            draw_text_in_circle(screen, sectors[i], text_pos, 50, (0, 0, 0))

        # Обновляем угол поворота барабана
        if rotating:
            current_angle += speed
            speed *= 0.98
            if speed < 0.05:
                rotating = False
                current_angle %= 360
                first_spin_completed = True

        # Поворачиваем курсор
        cursor_rotation_angle = current_angle + 270
        rotated_cursor = pygame.transform.rotate(cursor_image, -cursor_rotation_angle)
        cursor_rect = rotated_cursor.get_rect(
            center=(int(wheel_center[0] + wheel_radius * math.cos(math.radians(current_angle))),
                    int(wheel_center[1] + wheel_radius * math.sin(math.radians(current_angle))))
        )

        # Отображаем кнопку выхода
        screen.blit(exit_button, exit_button_rect)

        # Отображаем курсор
        screen.blit(rotated_cursor, cursor_rect)

        # Отображаем деньги
        screen.blit(text_money_sprite, text_money_sprite_rect)

        # Проверяем результат вращения
        if not rotating and not result_shown and first_spin_completed:
            final_sector_index = int((current_angle % 360) // 60)
            final_color = sector_colors[final_sector_index]
            if final_color == (255, 0, 0):  # Красный сектор
                money += 20
                text_money = str(money)
                cursor_money.execute("UPDATE money SET chet_money = ? WHERE id = 1", (text_money,))
                conn_money.commit()
                text_money_sprite = font_money.render(text_money, True, (255, 255, 255))
                show_win_timer = pygame.time.get_ticks()  # Запускаем таймер
                print("Победа")
            elif final_color == (0, 255, 0):
                print("Поражение")
                show_lose_timer = pygame.time.get_ticks()
            result_shown = True
        if show_win_timer > 0 and pygame.time.get_ticks() - show_win_timer <= 3000:  # Показывать 2 секунды
            screen.blit(win_text_sprite, win_text_sprite_rect)
        if show_lose_timer > 0 and pygame.time.get_ticks() - show_lose_timer <= 3000:
            screen.blit(lose_text_sprite, lose_text_sprite_rect)

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

if __name__=="__main__":
    fortuna()