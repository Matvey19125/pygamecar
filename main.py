import pygame
import random
import sqlite3

pygame.init()
clock = pygame.time.Clock()
TIMEREVENT = pygame.USEREVENT + 1
timerpot = pygame.USEREVENT + 2
pygame.time.set_timer(timerpot, 2000)
pygame.time.set_timer(TIMEREVENT, 15000)
pygame.display.set_caption("Ретро-Гонки")


class Shoes:
    def __init__(self):
        self.size = self.width, self.height = 800, 950
        self.screen = pygame.display.set_mode(self.size)
        self.colors = [(0, 0, 0), (255, 255, 255), (255, 0, 0)]
        self.car_x = 350
        self.car_y = 800
        self.car_width = 120
        self.car_height = 150
        self.sprite_image = pygame.image.load('image/one_car_image.png')
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

    def collider(self):
        self.car_collider.topleft = (self.car_x, self.car_y)
        self.money_collider.topleft = (self.money_x, self.money_y)
        if self.car_collider.colliderect(self.money_collider):
            self.money_x = -100
            self.chet_money = int(self.chet_money)
            self.chet_money += 1
            shoes.money_chet()

    def potok(self):
        x_potok = random.choice([100, 350, 600])
        y_potok = 0
        sprite_potol1 = pygame.image.load("image/potok_car1.png")
        sprite_potol2 = pygame.image.load("image/potok_car2.png")
        sprite_potol3 = pygame.image.load("image/potok_car3.png")
        sprite_potok = [sprite_potol1, sprite_potol2, sprite_potol3]
        scaled_potok = pygame.transform.scale(random.choice(sprite_potok), (120, 150))
        scaled_potok = pygame.transform.rotate(scaled_potok, 180)
        stream = {'x': x_potok, 'y': y_potok, 'scaled_potok': scaled_potok}
        self.active_streams.append(stream)

    def pot_dvish(self):
        for stream in self.active_streams:
            stream['y'] += 60
            if stream['y'] > 950:
                self.active_streams.remove(stream)
            else:
                self.screen.blit(stream['scaled_potok'], (stream['x'], stream['y']))

    def save_money(self):
        self.cursor.execute("UPDATE money SET chet_money = ? WHERE id = 1", (self.chet_money,))
        self.conn.commit()

    def money_chet(self):
        self.chet_money = str(self.chet_money)
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
        og = self.height // 2
        count = 0
        for i in range(0, og):
            rect_x = 250
            rect_x2 = 515
            rect_width = 35
            rect_height = 95 - count
            pygame.draw.rect(self.screen, self.colors[1], pygame.Rect(rect_x, rect_y, rect_width, rect_height))
            pygame.draw.rect(self.screen, self.colors[1], pygame.Rect(rect_x2, rect_y, rect_width, rect_height))
            count -= 55
        self.screen.blit(self.scaled_sprite, (self.car_x, self.car_y))
        self.screen.blit(self.money_sprite, (self.money_x, self.money_y))
        pygame.display.flip()

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


shoes = Shoes()
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == TIMEREVENT:
            shoes.spawn_money()
        elif event.type == timerpot:
            shoes.potok()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                shoes.car_right()
            elif event.key == pygame.K_a:
                shoes.car_left()

    shoes.pot_dvish()
    shoes.money_y += 50
    shoes.save_money()
    shoes.money_chet()
    shoes.collider()
    shoes.draw()
pygame.quit()