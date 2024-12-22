import pygame
import random

pygame.init()
clock = pygame.time.Clock()
TIMEREVENT = pygame.USEREVENT + 1

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
        self.scaled_sprite = pygame.transform.scale(self.sprite_image, (self.car_width, self.car_height))
        self.count = 0

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

    def money(self):
        self.sprite_money = pygame.image.load('image/money_image.png')
        self.prof = random.randint(1, 3)
        self.money_width = 60
        self.money_height = 60
        self.money_y = 60
        if self.prof == 1:
            self.money_x = 100
        elif self.prof == 2:
            self.money_x = 350
        elif self.prof == 3:
            self.money_x = 600
        self.money_sprite = pygame.transform.scale(self.sprite_image, (self.money_width, self.money_height))
        while self.money_y != 900:
            self.money_y += 10
            self.screen.blit(self.scaled_sprite, (self.money_x, self.money_y))

shoes = Shoes()
running = True
while running:
    clock.tick(60)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if TIMEREVENT % 2 == 0:
            shoes.money()
        elif keys[pygame.K_d]:
            shoes.car_right()
            shoes.money()
        elif keys[pygame.K_a]:
            shoes.car_left()
    shoes.draw()
pygame.quit()
print('Негры')