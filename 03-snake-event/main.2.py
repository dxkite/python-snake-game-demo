import pygame 
from pygame import K_UP,K_DOWN,K_LEFT,K_RIGHT,QUIT,MOUSEMOTION,MOUSEBUTTONUP,MOUSEBUTTONDOWN

# 1. 先初始化游戏框架
pygame.init()
# 2. 创建一个窗口
screen = pygame.display.set_mode((300,150),0,32)
# 加载字体 (使用系统字体)
font = pygame.font.SysFont('arial', 16)
# 运行标志
running = True
# 案件方向
mouse  = (0,0)
mouse_move = (0,0)
mouse_key = None
text = 'No Event'

# 1. 游戏死循环
while running:
    # 2. 获取事件流
    for event in pygame.event.get():
        # 3. 处理事件流
        if event.type == QUIT:
            # 结束运行
            running = False
        elif event.type == MOUSEMOTION:
            mouse = event.pos
            mouse_move = event.rel
            text = 'mouse pos %s rel %s ' % (str(mouse),str(mouse_move))
        elif event.type == MOUSEBUTTONUP:
            mouse = event.pos
            mouse_key = event.button 
            text = 'mouse pos %s button %s' % (str(mouse),str(mouse_key))
        elif event.type == MOUSEBUTTONDOWN:
            mouse = event.pos
            mouse_key = event.button 
            text = 'mouse pos %s button %s' % (str(mouse),str(mouse_key))

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
