import pygame
# 1. 先初始化游戏框架
pygame.init()
# 2. 创建一个窗口
screen = pygame.display.set_mode((100 , 100 ),0,32)
# 3. 刷新显示窗口
pygame.display.flip()  
# 假装进行了什么操作 （延时2秒）
pygame.time.wait(2000)
# 4. 退出框架
pygame.quit()
