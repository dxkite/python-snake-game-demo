import pygame 
from pygame import K_UP,K_DOWN,K_LEFT,K_RIGHT,QUIT,KEYDOWN

# 1. 先初始化游戏框架
pygame.init()
# 2. 创建一个窗口
screen = pygame.display.set_mode((200,150),0,32)
# 加载字体 (使用系统字体)
font = pygame.font.SysFont('arial', 16)
# 运行标志
running = True
# 案件方向
text  = 'No Key Event'
# 1. 游戏死循环
while running:
    # 2. 获取事件流
    for event in pygame.event.get():
        text = 'No Key Event'
        # 3. 处理事件流
        if event.type == QUIT:
            # 结束运行
            running = False
        elif event.type == KEYDOWN:
            # 键盘按下事件
            if event.key == K_UP:
                text = 'K_UP'
            elif event.key == K_DOWN:
                text = 'K_DOWN'
            elif event.key == K_LEFT:
                text = 'K_LEFT'
            elif event.key == K_RIGHT:
                text = 'K_RIGHT'
    # 2.1 屏幕填充白色
    screen.fill((0xff,0xff,0xff))
    # 2.3 渲染文字
    text_surface = font.render(text,True,(0xff,0,0))
    # 2.4 贴图文字
    screen.blit(text_surface,(0,0))
    # 3. 刷新显示窗口
    pygame.display.flip()  

# 4. 退出框架
pygame.quit()
