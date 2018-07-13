import pygame
from pygame import QUIT

from pygameui import Button

# 1. 先初始化游戏框架
pygame.init()
# 2. 创建一个窗口
screen = pygame.display.set_mode((300, 150), 0, 32)
# 加载字体 (使用系统字体)
font = pygame.font.SysFont('arial', 16)
# 运行标志
running = True

text = 'Play music with any keydown'

clock = pygame.time.Clock()
'''
初始化音频播放器
'''
# 初始化
pygame.mixer.init()


def click_test():
    print('button clicked')


button = Button(text='Start Game', callable=click_test)

# 1. 游戏死循环
while running:
    # 2. 获取事件流
    for event in pygame.event.get():
        button.on_event(event)
        # 3. 处理事件流
        if event.type == QUIT:
            # 结束运行
            running = False
    screen.fill((0xff, 0xff, 0xff))
    button.on_draw(screen)
    # 3. 刷新显示窗口
    pygame.display.flip()
    clock.tick(60)

# 4. 退出框架
pygame.quit()
