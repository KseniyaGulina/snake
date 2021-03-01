import pygame
import sys
import time
import random


class Play():
    def __init__(self):
        self.fps = pygame.time.Clock()
        self.size = self.width, self.height = 800, 600

    def end_game(self):
        font = pygame.font.Font(None, 30)
        screen.fill((0, 255, 0))
        text = font.render(f'Результат: {snake.result}', True, (255, 0, 0))
        text_x = play.width // 2 - text.get_width() // 2
        text_y = play.height // 2 - text.get_height() // 2
        screen.blit(text, (text_x, text_y))
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        sys.exit()

    def show_result(self):
        font = pygame.font.Font(None, 30)
        text = font.render(f'Результат: {snake.result}', True, (0, 0, 0))
        text_x = 10
        text_y = 10
        screen.blit(text, (text_x, text_y))

    def event(self):
        print('1')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and snake.move != 'left':
                    snake.move = 'right'
                elif event.key == pygame.K_DOWN and snake.move != 'up':
                    snake.move = 'down'
                elif event.key == pygame.K_UP and snake.move != 'down':
                    snake.move = 'up'
                elif event.key == pygame.K_LEFT and snake.move != 'right':
                    snake.move = 'left'


class Snake():
    def __init__(self):
        self.head = [400, 300]
        self.body = [[400, 300], [400, 290]]
        self.color = 'orange'
        self.move = 'up'
        self.result = 0
        self.food = 0
        self.time = 10

    def change_move(self):
        if self.move == 'right':
            self.head[0] += 10
        elif self.move == 'left':
            self.head[0] -= 10
        elif self.move == 'up':
            self.head[1] -= 10
        elif self.move == 'down':
            self.head[1] += 10

    def change_body(self):
        self.body.insert(0, list(self.head))
        if self.head == food.pos:
            food.new_pos()
            self.result += 1
            self.time += self.result // 5
        else:
            del self.body[-1]

    def draw(self):
        for x, y in self.body:
            pygame.draw.rect(screen, 'orange', pygame.Rect(x, y, 10, 10))

    def if_end(self):
        if self.head[0] > play.width - 10 or self.head[0] < 0 \
                or self.head[-1] > play.height - 10 or self.head[-1] < 0:
            play.end_game()
        for part in self.body[1:]:
            if part == self.head:
                play.end_game()

class Food():
    def __init__(self):
        self.x = random.randrange(1, play.width / 10) * 10
        self.y = random.randrange(1, play.height / 10) * 10
        self.pos = [self.x, self.y]

    def new_pos(self):
        self.x = random.randrange(1, play.width / 10) * 10
        self.y = random.randrange(1, play.height / 10) * 10
        self.pos = [self.x, self.y]

    def draw(self):
        pygame.draw.rect(screen, 'red', pygame.Rect(self.x, self.y, 10, 10))


play = Play()
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(play.size)
    pygame.display.set_caption('Змейка')
    screen.fill('green')
    font = pygame.font.Font(None, 30)
    screen.fill((0, 255, 0))
    text = font.render('Змейка', True, (255, 0, 0))
    text_x = play.width // 2 - text.get_width() // 2 - 30
    text_y = play.height // 2 - text.get_height() // 2 - 30
    screen.blit(text, (text_x, text_y))
    text = font.render('Нажмите, чтобы начать', True, (255, 0, 0))
    screen.blit(text, (text_x - 60, text_y + 40))
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                running = False
    running = True
    screen.fill('green')
    pygame.display.flip()
    snake = Snake()
    food = Food()
    while running:
        screen.fill('green')
        play.event()
        print(snake.move)
        snake.change_move()
        snake.change_body()
        food.draw()
        snake.draw()
        snake.if_end()
        play.show_result()
        pygame.display.flip()
        play.fps.tick(snake.time)
    pygame.quit()
