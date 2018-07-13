import pygame

# 1. 先初始化游戏框架
pygame.init()
# 2. 创建一个窗口
screen = pygame.display.set_mode((100 , 100 ),0,32)
# 2.1 屏幕填充白色
screen.fill((0xff,0xff,0xff))
# 2.2 加载图片
image = pygame.image.load('0.png')
# 2.3 贴图图片
screen.blit(image,(10,10),(0,0,10,10))
# 3. 刷新显示窗口
pygame.display.flip()  
# 假装进行了什么操作 （延时2秒）
pygame.time.wait(2000)
# 4. 退出框架
pygame.quit()
