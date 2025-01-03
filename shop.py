import pygame
import sqlite3

def shop():
    pygame.init()
    clock = pygame.time.Clock()
    size = 1200, 950
    screen = pygame.display.set_mode(size)
    background = pygame.image.load("image/fon.png")
    pygame.display.set_caption("Ретро-Гонки")
    background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
    font = pygame.font.Font(None, 55)
    font_money = pygame.font.Font(None, 74)
    font_nehvat = pygame.font.Font(None, 100)
    conn = sqlite3.connect('money.db')
    cursor = conn.cursor()
    cursor.execute("SELECT chet_money FROM money")
    money = cursor.fetchone()[0]
    text_money = str(money)
    text_money_surface = font_money.render(text_money, True, (255, 255, 255))
    one_car_image = pygame.image.load('image/sprite_one.png')
    new_size = (100, 150)
    one_car_image = pygame.transform.scale(one_car_image, new_size)
    text1 = "Купить за 100"
    one_sprite = font.render(text1, True, (255, 255, 255))
    one_sprite_rect = one_sprite.get_rect(center=(150, 400))
    mouse_pos = pygame.mouse.get_pos()
    running = True
    button_clicked = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                conn.close()
                running = False
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if one_sprite_rect.collidepoint(event.pos) and money >= 100:
                    money -= 100
                    text_money = str(money)
                    cursor.execute("UPDATE money SET chet_money = ? WHERE id = 1", (text_money,))
                    conn.commit()
                    text_money_surface = font_money.render(text_money, True, (255, 255, 255))
                    button_clicked = True

        screen.blit(background, (0, 0))
        screen.blit(one_sprite, one_sprite_rect)
        screen.blit(one_car_image, (100, 200))
        screen.blit(text_money_surface, (1100, 50))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    shop()