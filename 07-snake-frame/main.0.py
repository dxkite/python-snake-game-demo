import pygame
from pygame import QUIT
from pygameui import Button
from views import MainView


class Game:
    # 运行状态
    running = True
    GAME_START = 0
    GAME_OVER = 1
    # 屏幕状态
    screen = None
    # 显示界面
    view = None
    # 运行时钟
    clock = None

    def __init__(self):
        pygame.init()
        # 初始化基础界面
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((300, 150), 0, 32)
        self.view = MainView(self)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                # 分发界面事件
                self.view.on_event(event)
                if event.type == QUIT:
                    self.running = False
            self.screen.fill((0xff, 0xff, 0xff))
            # 调用界面显示
            self.view.on_draw()
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    Game().run()
