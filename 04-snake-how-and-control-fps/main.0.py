import pygame 
from pygame import QUIT

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
text = 'fps: %s'
fps = 0
FPS_MAX = 60

clock = pygame.time.Clock()

# 1. 游戏死循环
while running:
    # 2. 获取事件流
    for event in pygame.event.get():
        # 3. 处理事件流
        if event.type == QUIT:
            # 结束运行
            running = False

    # 2.1 屏幕填充白色
    screen.fill((0xff,0xff,0xff))
    # 2.3 渲染文字
    text_surface = font.render(text % fps ,True,(0xff,0,0))
    # 2.4 贴图文字
    screen.blit(text_surface,(0,0))
    # 3. 刷新显示窗口
    pygame.display.flip() 
    passed_time = clock.tick() 
    print(passed_time)
    if passed_time <=0 :
        passed_time = 1
    fps =  int(1/passed_time*1000)

# 4. 退出框架
pygame.quit()
