import pygame

# 1. 先初始化游戏框架
pygame.init()
# 2. 创建一个窗口
screen = pygame.display.set_mode((100 , 100 ),0,32)
# 2.1 屏幕填充白色
screen.fill((0xff,0xff,0xff))
# 2.2 加载字体 (使用系统字体)
font = pygame.font.SysFont('arial', 16)
# 2.3 渲染文字
text = font.render("Hello World",True,(0,0,0))
# 2.4 贴图文字
screen.blit(text,(0,0))
# 3. 刷新显示窗口
pygame.display.flip()  
# 假装进行了什么操作 （延时2秒）
pygame.time.wait(2000)
# 4. 退出框架
pygame.quit()
