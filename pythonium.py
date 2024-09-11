import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

WIDTH = 1000
HEIGHT = 600
SIZE = 20

FPS_BASE = 15 
SPEED_BASE = 1

HIGH_SCORE = 0

class Snake:
    def __init__(self, speed, fps):
        self.body = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = "RIGHT"
        self.change_direction = self.direction
        self.score = 0
        self.alive = True
        self.speed = speed
        self.fps = fps

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
        if self.body[0][0] < 0 or self.body[0][0] >= WIDTH or self.body[0][1] < 0 or self.body[0][1] >= HEIGHT: #проверка на столкновение с границей
            self.alive = False
            return True

        if self.check_self_collision(): #проверка на столкновение с самим собой
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

    #функция для проверки столкновения с самой собой
    def check_self_collision(self):
        head = self.body[0]
        for i in range(1, len(self.body)):
            if head == self.body[i]:
                return True
        return False

class Food:
    def __init__(self):
        self.new_pos()

    def new_pos(self):
        self.pos = (random.randrange(0, WIDTH, SIZE), random.randrange(0, HEIGHT, SIZE))

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.pos[0], self.pos[1], SIZE, SIZE))

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pythonium")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)  # Шрифт для текста в меню

def show_menu():
    screen.fill(BLACK)  #заполняем экран черным цветом
    #заголовок меню
    text = font.render("Pythonium", True, WHITE)
    screen.blit(text, (WIDTH // 2 - 50, HEIGHT // 2 - 100))
    #варианты сложности
    text = font.render("Легкий [1]", True, WHITE)
    screen.blit(text, (WIDTH // 2 - 50, HEIGHT // 2 - 50))
    text = font.render("Средний [2]", True, WHITE)
    screen.blit(text, (WIDTH // 2 - 50, HEIGHT // 2))
    text = font.render("Сложный [3]", True, WHITE)
    screen.blit(text, (WIDTH // 2 - 50, HEIGHT // 2 + 50))
    pygame.display.flip()  

running = True
while running:
    show_menu()  #отображение меню
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:  #легкий уровень
                SPEED_BASE = 1
                FPS_BASE = 15
            elif event.key == pygame.K_2:  #средний уровень
                SPEED_BASE = 1.5
                FPS_BASE = 20
            elif event.key == pygame.K_3:  #сложный
                SPEED_BASE = 2
                FPS_BASE = 25
            elif event.key == pygame.K_ESCAPE:
                running = False
            
            #запуск игры, если выбрана какая-то из сложностей
            if event.key in (pygame.K_1, pygame.K_2, pygame.K_3):
                snake = Snake(SPEED_BASE, FPS_BASE)
                food = Food() 
                game_running = True
                while game_running:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                            game_running = False
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_LEFT and snake.change_direction != "RIGHT":
                                snake.change_direction = "LEFT"
                            elif event.key == pygame.K_RIGHT and snake.change_direction != "LEFT":
                                snake.change_direction = "RIGHT"
                            elif event.key == pygame.K_UP and snake.change_direction != "DOWN":
                                snake.change_direction = "UP"
                            elif event.key == pygame.K_DOWN and snake.change_direction != "UP":
                                snake.change_direction = "DOWN"
                            #начало игры заново по нажатию на любую клавишу после смерти
                            elif event.key in (pygame.K_SPACE, pygame.K_RETURN): 
                                snake.reset()
                            #выход из игры по нажатию на ESC
                            elif event.key == pygame.K_ESCAPE:
                                running = False
                                game_running = False

                    if snake.alive: #обновление змейки
                        snake.move()

                    #проверка на столкновение
                    if snake.check_collision():
                        font = pygame.font.Font(None, 72)
                        text = font.render("Игра окончена!", True, WHITE)
                        screen.blit(text, (WIDTH // 2 - 200, HEIGHT // 2 - 50))
                        text = font.render("Нажмите пробел или Enter, чтобы начать заново", True, WHITE)
                        screen.blit(text, (WIDTH // 2 - 300, HEIGHT // 2 + 50))
                        pygame.display.flip()
                        #ожидание нажатия клавиши
                        while not snake.alive: 
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if event.key in (pygame.K_SPACE, pygame.K_RETURN):
                                        snake.reset()
                                    elif event.key == pygame.K_ESCAPE:
                                        running = False
                                        game_running = False
                                        break

                    #проверка на съедение еды
                    if snake.eat(food):
                        snake.speed += 0.1
                        snake.fps += 1

                    #обновление рекорда
                    if snake.score > HIGH_SCORE:
                        HIGH_SCORE = snake.score

                    #отрисовка
                    screen.fill(BLACK)
                    snake.draw(screen)
                    food.draw(screen)

                    #вывод счета
                    font = pygame.font.Font(None, 36)
                    text = font.render("Счёт: {}".format(snake.score), True, WHITE)
                    screen.blit(text, (10, 10))
                    text = font.render("Рекорд: {}".format(HIGH_SCORE), True, WHITE)
                    screen.blit(text, (10, 50))

                    #обновление экрана
                    pygame.display.flip()

                    #регулирование скорости
                    clock.tick(snake.fps)

# конец (the end)
pygame.quit()