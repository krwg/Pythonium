import pygame
import random

BLACK = (0, 0, 0)  #цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

WIDTH = 800  #настройки окна
HEIGHT = 600
SIZE = 20

FPS = 15
SPEED = 1

class Snake:    #класс змеи
    def __init__(self):
        self.body = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = "RIGHT"
        self.change_direction = self.direction
        self.score = 0
        self.alive = True

    def move(self):
        if self.alive:
            if self.change_direction == "RIGHT":
                self.body.insert(0, (self.body[0][0] + SIZE, self.body[0][1]))
            elif self.change_direction == "LEFT":
                self.body.insert(0, (self.body[0][0] - SIZE, self.body[0][1]))
            elif self.change_direction == "UP":
                self.body.insert(0, (self.body[0][0], self.body[0][1] - SIZE))
            elif self.change_direction == "DOWN":
                self.body.insert(0, (self.body[0][0], self.body[0][1] + SIZE))
            self.body.pop()

    def draw(self, screen):
        for x, y in self.body:
            pygame.draw.rect(screen, GREEN, (x, y, SIZE, SIZE))

    def check_collision(self):
        
        if self.body[0][0] < 0 or self.body[0][0] >= WIDTH or self.body[0][1] < 0 or self.body[0][1] >= HEIGHT:  #проверка на столкновение с границей
            self.alive = False
            return True

        
        for i in range(1, len(self.body)): #проверка на столкновение с самой собой
            if self.body[0] == self.body[i]:
                self.alive = False
                return True

        return False

    def eat(self, food):
        if self.body[0] == food.pos:
            self.score += 1
            food.new_pos()
            self.body.append(self.body[-1])
            return True
        return False

    def reset(self):
        self.body = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = "RIGHT"
        self.change_direction = self.direction
        self.score = 0
        self.alive = True

#класс кубиков (еды для змеи)
class Food:
    def __init__(self):
        self.new_pos()

    def new_pos(self):
        self.pos = (random.randrange(0, WIDTH, SIZE), random.randrange(0, HEIGHT, SIZE))

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.pos[0], self.pos[1], SIZE, SIZE))

#инициализация pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")
clock = pygame.time.Clock()

#создание объектов
snake = Snake()
food = Food()

#основной цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake.change_direction != "RIGHT":
                snake.change_direction = "LEFT"
            elif event.key == pygame.K_RIGHT and snake.change_direction != "LEFT":
                snake.change_direction = "RIGHT"
            elif event.key == pygame.K_UP and snake.change_direction != "DOWN":
                snake.change_direction = "UP"
            elif event.key == pygame.K_DOWN and snake.change_direction != "UP":
                snake.change_direction = "DOWN"
            # Начать игру заново по нажатию на любую клавишу после смерти
            elif event.key in (pygame.K_SPACE, pygame.K_RETURN): 
                snake.reset()  # Сбрасываем змею
            # Выход из игры по нажатию на ESC
            elif event.key == pygame.K_ESCAPE:
                running = False

    #обновление змейки
    if snake.alive:
        snake.move()

    #проверка на столкновение
    if snake.check_collision():
        #отановить змею
        #running = False 
        #следственно, вывод сообщения о проигрыше
        font = pygame.font.Font(None, 72)
        text = font.render("Игра окончена!", True, WHITE)
        screen.blit(text, (WIDTH // 2 - 200, HEIGHT // 2 - 50))
        text = font.render("Нажмите пробел или Enter, чтобы начать заново", True, WHITE)
        screen.blit(text, (WIDTH // 2 - 300, HEIGHT // 2 + 50))
        pygame.display.flip()
        #ожидаем нажатия клавиши (space or escape)
        while not snake.alive: 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_SPACE, pygame.K_RETURN):
                        snake.reset()
                    elif event.key == pygame.K_ESCAPE:
                        running = False
                        break

    if snake.eat(food):    #проверка на съедение еды
        SPEED += 0.1
        FPS += 1

    screen.fill(BLACK)  #отрисовка
    snake.draw(screen)
    food.draw(screen)

    font = pygame.font.Font(None, 36)      #счет
    text = font.render("Счёт: {}".format(snake.score), True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.flip()

    clock.tick(FPS)

#конец
pygame.quit()