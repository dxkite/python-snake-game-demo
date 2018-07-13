import pygame
from pygame import KEYDOWN, K_UP, K_DOWN, K_LEFT, K_RIGHT
import copy


class Snake:
    # 方向说明
    HEAD_UP = 0
    HEAD_DOWN = 1
    HEAD_LEFT = 2
    HEAD_RIGHT = 3
    # 移动方向
    direction = HEAD_LEFT
    # 身体数据
    body = []
    # 默认15帧移动一格
    speed = 15
    # 显示图片
    img_head = None
    img_body = None

    # 帧数计算
    frame_count = 0
    # 初始化

    def __init__(self, x, y):
        self.body = [[x, y], [x - 1, y], [x-2, y]]
        self.direction = self.HEAD_RIGHT
        self.img_head = [pygame.image.load(
            'img/head_' + str(i+1) + '.png') for i in range(4)]
        self.img_body = pygame.image.load('img/body.png')
    # 监听按键

    def on_event(self, event):
        if event.key == K_UP and self.direction != self.HEAD_DOWN:
            self.direction = self.HEAD_UP
        elif event.key == K_DOWN and self.direction != self.HEAD_UP:
            self.direction = self.HEAD_DOWN
        elif event.key == K_LEFT and self.direction != self.HEAD_RIGHT:
            self.direction = self.HEAD_LEFT
        elif event.key == K_RIGHT and self.direction != self.HEAD_LEFT:
            self.direction = self.HEAD_RIGHT

    # 绘制贪吃蛇
    def on_draw(self, view):
        # 绘制已有的身体
        for i in range(len(self.body)):
            if i == 0:
                view.draw_surface(self.body[i], self.img_head[self.direction])
            else:
                view.draw_surface(self.body[i], self.img_body)
        # 计算移动
        if self.frame_count < self.speed:
            self.frame_count = self.frame_count + 1
        else:
            self.frame_count = 0
            # 调整头部方向
            move = copy.deepcopy(self.body[0])
            # 计算移动
            if self.direction == self.HEAD_UP:
                move[1] = move[1] - 1
                if move[1] < 0:
                    move[1] = view.h - 1
                self.body.insert(0, move)
            elif self.direction == self.HEAD_DOWN:
                move[1] = move[1] + 1
                if move[1] >= view.h:
                    move[1] = 0
                self.body.insert(0, move)
            elif self.direction == self.HEAD_LEFT:
                move[0] = move[0] - 1
                if move[0] < 0:
                    move[0] = view.w - 1
                self.body.insert(0, move)
            else:
                move[0] = move[0] + 1
                if move[0] >= view.w:
                    move[0] = 0
                self.body.insert(0, move)
            # 剔除最末尾
            self.body.pop(len(self.body) - 1)

    # 判断是否吃到食物
    def has_eat(self, food):
        pass

    # 判断是否撞到物品
    def has_hit(self, blocks):
        pass
