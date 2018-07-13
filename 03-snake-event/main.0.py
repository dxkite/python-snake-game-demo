import pygame 
# 1. 先初始化游戏框架
pygame.init()
# 2. 创建一个窗口
screen = pygame.display.set_mode((200,150),0,32)
# 加载字体 (使用系统字体)
font = pygame.font.SysFont('arial', 16)
# 运行标志
running = True
# 1. 游戏死循环
while running:
    # 2. 获取事件流
    for event in pygame.event.get():
        # 3. 处理事件流
        if event.type == pygame.QUIT:
            print('quit game')
            # 结束运行
            running = False
    # 2.1 屏幕填充白色
    screen.fill((0xff,0xff,0xff))
    # 2.3 渲染文字
    text = font.render("Hello World" ,True,(0xff,0,0))
    # 2.4 贴图文字
    screen.blit(text,(0,0))
    # 3. 刷新显示窗口
    pygame.display.flip()  

# 4. 退出框架
pygame.quit()
