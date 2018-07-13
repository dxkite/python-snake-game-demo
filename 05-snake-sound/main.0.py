import pygame
from pygame import QUIT, KEYDOWN
from pygame.mixer import Sound
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
# 加载音效
sound = Sound('eat.wav')

# 1. 游戏死循环
while running:
    # 2. 获取事件流
    for event in pygame.event.get():
        # 3. 处理事件流
        if event.type == QUIT:
            # 结束运行
            running = False
        elif event.type == KEYDOWN:
            # 播放音频
            sound.play()

    # 2.1 屏幕填充白色 (Red,Green,Blue) 颜色取值范围：0~0xff
    screen.fill((0xff, 0xff, 0xff))
    # 2.3 渲染文字
    text_surface = font.render(text, True, (0xff, 0, 0))
    # 2.4 贴图文字
    screen.blit(text_surface, (0, 0))
    # 3. 刷新显示窗口
    pygame.display.flip()
    clock.tick(60)

# 4. 退出框架
pygame.quit()
