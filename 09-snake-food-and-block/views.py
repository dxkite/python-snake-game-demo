import random

import pygame
from pygame import KEYDOWN

from pygameui import Button
from snake import Snake


class View:
    screen = None

    """
    界面初始化
    """

    def __init__(self, screen):
        self.screen = screen

    """
    界面绘制处理
    """

    def on_draw(self):
        pass

    """
    界面事件分发
    """

    def on_event(self, event):
        pass


class GameView(View):
    block = None
    food = None
    snake = None
    _block = []

    def __init__(self, context):
        View.__init__(self, context.screen)
        # 加载基础资源
        self.block = pygame.image.load('img/block.jpg')
        self.food = pygame.image.load('img/food.png')
        self.w = 12
        self.h = 12
        self.BLOCK_SIZE = self.block.get_size()
        context.screen = pygame.display.set_mode(
            (self.w*self.BLOCK_SIZE[0], self.h * self.BLOCK_SIZE[1]), 0, 32)
        # 初始化蛇
        self.snake = Snake(0, 0)
        self._food = self._random()
        self._block = [self._get_random_block()
                       for i in range(random.randrange(3, 6))]

    """""""""""""""""""""
    在某个位置绘制一个块
    """""""""""""""""""""

    def draw_surface(self, pos, surface):
        self.screen.blit(
            surface, (pos[0]*self.BLOCK_SIZE[0], pos[1]*self.BLOCK_SIZE[1]))

    def on_draw(self):
        self.snake.on_draw(self)
        self.draw_surface(self._food, self.food)
        for block in self._block:
            self.draw_surface(block, self.block)

    def on_event(self, event):
        if event.type == KEYDOWN:
            self.snake.on_event(event)

    # 随机生成地图坐标
    def _random(self):
        return (random.randrange(0, self.w), random.randrange(0, self.h))

    # 随机生成无冲突坐标
    def _get_random_block(self):
        block = self._random()
        for pos in self.snake.body:
            if pos[0] == block[0] and pos[1] == block[1]:
                return self._get_random_block()
        for pos in self._block:
            if pos[0] == block[0] and pos[1] == block[1]:
                return self._get_random_block()
        if block[0] == self._food[0] and block[1] == self._food[1]:
            return self._get_random_block()
        return block


class GameOverView(View):
    pass


class MainView(View):

    logo = None
    btn_start = None
    btn_exit = None
    context = None

    def __init__(self, context):
        self.btn_start = Button('Start Game', self._on_start)
        self.btn_exit = Button('Exit Game', self._on_exit)
        self.context = context
        self.logo = pygame.image.load('img/logo.png')
        w, h = self.logo.get_size()
        # 调整界面适应 Logo 大小以及显示按钮
        self.context.screen = pygame.display.set_mode(
            (int(w * 1.5), int(h * 2)), 0, 32)
        # 设置界面标题
        pygame.display.set_caption('Python Snake Game v1.0')
        View.__init__(self, context.screen)

    def on_draw(self):
        # 绘制界面
        self._on_draw()
        # 绘制按钮
        self.btn_start.on_draw(self.context.screen)
        self.btn_exit.on_draw(self.context.screen)

    def on_event(self, event):
        # 监控各种事件
        self.btn_start.on_event(event)
        self.btn_exit.on_event(event)

    def _on_exit(self):
        # 控制退出状态
        print('exit game')
        self.context.running = False

    def _on_start(self):
        # 切换界面到游戏界面
        print('start game')
        self.context.view = GameView(self.context)

    def _on_draw(self):
        '''
        计算各个按钮的位置以及Logo的位置
        '''
        s_w, s_h = self.context.screen.get_size()
        l_w, l_h = self.logo.get_size()
        x, y, bs_w, bs_h = self.btn_start.get_box()
        x, y, be_w, be_h = self.btn_exit.get_box()
        y_start = l_h + 50
        '''
        界面元素排版
        '''
        self.btn_start.pos = (s_w/2 - bs_w / 2, y_start)
        self.btn_exit.pos = (s_w/2 - be_w / 2, y_start + bs_h + 4)
        self.context.screen.blit(self.logo, (s_w/2-l_w/2, s_h/2-l_h/2))
