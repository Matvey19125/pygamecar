import pygame
import random
import sqlite3
import pygame_gui
import time
pygame.init()
clock = pygame.time.Clock()
TIMEREVENT = pygame.USEREVENT + 1
timerpot = pygame.USEREVENT + 2
SPEEDUP_TIMEREVENT = pygame.USEREVENT + 3
pygame.time.set_timer(timerpot, 1250)
pygame.time.set_timer(SPEEDUP_TIMEREVENT, 500)
pygame.time.set_timer(TIMEREVENT, 15000)
pygame.display.set_caption("Ретро-Гонки")
count_stolk = 0


class Shoes:
    def __init__(self):
        global count_stolk
        count_stolk = 0
        self.size = self.width, self.height = 800, 950
        self.screen = pygame.display.set_mode(self.size)
        self.colors = [(0, 0, 0), (255, 255, 255), (255, 0, 0)]
        self.car_x = 350
        self.car_y = 800
        self.car_width = 120
        self.car_height = 150
        self.conn = sqlite3.connect('vibr.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT count_vibr FROM vibr")
        result = self.cursor.fetchone()
        self.count_vibr = result[0]
        self.scrin_car = [('image/one_car_image.png'), ('image/sprite_one.png'), ('image/two_car.png'), ('image/three_car.png'), ('image/four_car.png')]
        self.sprite_image = pygame.image.load(self.scrin_car[self.count_vibr])
        self.money_sprite = pygame.image.load('image/money_image.png')
        self.scaled_sprite = pygame.transform.scale(self.sprite_image, (self.car_width, self.car_height))
        self.money_sprite = pygame.transform.scale(self.money_sprite, (70, 70))
        self.count = 0
        self.money_y = 50
        self.money_x = random.choice([100, 350, 600])
        self.car_collider = self.scaled_sprite.get_rect(topleft=(self.car_x, self.car_y))
        self.money_collider = self.money_sprite.get_rect(topleft=(self.money_x, self.money_y))
        self.chet_money = 0
        self.conn = sqlite3.connect('money.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS money (id INTEGER PRIMARY KEY, chet_money INTEGER)''')
        self.conn.commit()
        self.cursor.execute("SELECT chet_money FROM money WHERE id = 1")
        result = self.cursor.fetchone()
        if result:
            self.chet_money = result[0]
        else:
            self.chet_money = 0
            self.cursor.execute("INSERT INTO money (id, chet_money) VALUES (1, 0)")
            self.conn.commit()
        self.active_streams = []
        self.speed = 10

    def collider_money(self):
        self.money_y += self.speed
        self.car_collider.topleft = (self.car_x, self.car_y)
        self.money_collider.topleft = (self.money_x, self.money_y)
        if self.car_collider.colliderect(self.money_collider):
            self.money_x = -100
            self.chet_money = int(self.chet_money)
            self.chet_money += 1
            self.money_chet()

    def collider_potok(self):
        global count_stolk
        self.car_collider.topleft = (self.car_x, self.car_y)
        self.count_stolk = 0
        for stream in self.active_streams:
            stream['collider'].topleft = (stream['x'], stream['y'])
            if self.car_collider.colliderect(stream['collider']):
                count_stolk += 1
            if count_stolk >= 1:
                self.screen.fill((0, 0, 0))
                self.lose_scene()

    def potok(self):
        self.x_potok = random.choice([100, 350, 600])
        self.y_potok = 0
        sprite_potol1 = pygame.image.load("image/potok_car1.png")
        sprite_potol2 = pygame.image.load("image/potok_car2.png")
        sprite_potol3 = pygame.image.load("image/potok_car3.png")
        sprite_potol4 = pygame.image.load("image/potok_car4.png")
        sprite_potol5 = pygame.image.load("image/potok_car5.png")
        sprite_potol6 = pygame.image.load("image/potok_car6.png")
        sprite_potok = [sprite_potol1, sprite_potol2, sprite_potol3, sprite_potol4, sprite_potol5, sprite_potol6]
        scaled_potok = pygame.transform.scale(random.choice(sprite_potok), (120, 150))
        scaled_potok = pygame.transform.rotate(scaled_potok, 180)
        potok_collider = scaled_potok.get_rect(topleft=(self.x_potok, self.y_potok))
        stream = {'x': self.x_potok, 'y': self.y_potok, 'scaled_potok': scaled_potok, 'collider': potok_collider}
        self.active_streams.append(stream)

    def pot_dvish(self):
        for stream in self.active_streams:
            stream['y'] += self.speed
            if stream['y'] > 950:
                self.active_streams.remove(stream)
            else:
                stream['collider'].topleft = (stream['x'], stream['y'])
                self.screen.blit(stream['scaled_potok'], (stream['x'], stream['y']))

    def save_money(self):
        self.cursor.execute("UPDATE money SET chet_money = ? WHERE id = 1", (self.chet_money,))
        self.conn.commit()

    def update(self):
        cycle()

    def money_chet(self):
        global count_stolk
        self.chet_money = str(self.chet_money)
        pygame.font.init()
        font = pygame.font.SysFont(None, 80)
        text = font.render(self.chet_money, True, (255, 255, 255))
        text_rect = text.get_rect(topleft=(60, 40))
        self.screen.blit(text, text_rect)
        pygame.display.flip()

    def draw(self):
        self.screen.fill((128, 128, 128))
        rect_x = 55
        rect_y = 0
        rect_width = 700
        rect_height = 950
        pygame.draw.rect(self.screen, self.colors[0], pygame.Rect(rect_x, rect_y, rect_width, rect_height))
        og = 1
        count = 0
        for i in range(0, 75):
            rect_x = 250
            rect_x2 = 515
            rect_width = 35
            rect_height = 95 - count
            pygame.draw.rect(self.screen, self.colors[1], pygame.Rect(rect_x, rect_y, rect_width, rect_height))
            pygame.draw.rect(self.screen, self.colors[1], pygame.Rect(rect_x2, rect_y, rect_width, rect_height))
            count -= 55
        self.screen.blit(self.scaled_sprite, (self.car_x, self.car_y))
        self.screen.blit(self.money_sprite, (self.money_x, self.money_y))

    def car_right(self):
        if self.count == 0:
            self.car_x = 600
            self.count += 1
        else:
            self.car_x = 350
            self.count = 0

    def car_left(self):
        if self.count == 0:
            self.car_x = 100
            self.count += 1
        else:
            self.car_x = 350
            self.count = 0

    def spawn_money(self):
        self.money_y = 50
        self.money_x = random.choice([115, 375, 615])

    def lose_scene(self):
        running = True
        clock = pygame.time.Clock()
        manager = pygame_gui.UIManager((800, 600))
        restart_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 450), (200, 150)),
                                                      text='Заново',
                                                      manager=manager)
        menu_exit = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((450, 450), (200, 150)),
                                                 text='Выход',
                                                 manager=manager)
        while running:
            time_delta = clock.tick(60) / 1
            self.screen.fill((0, 0, 0))
            font = pygame.font.Font(None, 35)
            text = font.render("Вы врезались! Нажмите кнопку 'Заново' для перезагрузки", True, (255, 255, 255))
            text_rect = text.get_rect(center=(400, 250))
            self.screen.blit(text, text_rect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == restart_button:
                        self.__init__()
                        return
                    if event.ui_element == menu_exit:
                        from Menu import menu
                        scene = menu()
                        scene.menu()
                manager.process_events(event)
            manager.update(time_delta)
            manager.draw_ui(self.screen)
            pygame.display.update()


def cycle():
    conn_awards = sqlite3.connect("awards.db")
    cursor_awards = conn_awards.cursor()
    cursor_awards.execute(
        """ CREATE TABLE IF NOT EXISTS awards_table ( id INTEGER PRIMARY KEY, count_parking INTEGER, count_revers INTEGER, count_shashki INTEGER ) """)
    cursor_awards.execute("SELECT * FROM awards_table WHERE id = 1")
    i = cursor_awards.fetchone()
    if i is None:
        count_shashki = 0
        cursor_awards.execute(
            """ INSERT INTO awards_table (id, count_parking, count_revers, count_shashki) VALUES (1, ?, ?, ?) """,
            (count_shashki,))
    else:
        count_shashki1 = i[3]
    shoes = Shoes()
    running = True
    w_held_down = False
    s_held_down = False
    awards = False
    start_timer_awards = time.time()
    while running:
        current_time_awards = time.time()
        if (current_time_awards - start_timer_awards) >= 250  and awards == False:
            count_shashki = 1
            cursor_awards.execute(""" UPDATE awards_table SET count_shashki = ? WHERE id = 1 """, (count_shashki,))
            conn_awards.commit()
            print(1)
            awards = True
        clock.tick(140)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    shoes.car_right()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                elif event.key == pygame.K_a:
                    shoes.car_left()
            elif event.type == TIMEREVENT:
                shoes.spawn_money()
            elif event.type == SPEEDUP_TIMEREVENT:
                if w_held_down:
                    shoes.potok()
            elif event.type == timerpot:
                if not w_held_down:
                    shoes.potok()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            w_held_down = True
            if shoes.speed < 40:
                shoes.speed += 1
        else:
            w_held_down = False

        if keys[pygame.K_s]:
            s_held_down = True
            if shoes.speed > 5:
                shoes.speed -= 1
        else:
            s_held_down = False
        if not w_held_down and not s_held_down:
            shoes.speed = 10
        shoes.pot_dvish()
        shoes.save_money()
        shoes.collider_potok()
        shoes.money_chet()
        shoes.collider_money()
        shoes.draw()
    pygame.quit()


if __name__ == "__main__":
    cycle()