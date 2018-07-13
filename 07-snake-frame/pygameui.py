import pygame
from pygame import MOUSEBUTTONDOWN, MOUSEMOTION
from pygame import Rect

pygame.init()
"""
Button 控件
-----------
为pygame 绘制一个button
"""


class Button:
    NORMAL = 0
    CLICKED = 1
    HOVER = 2

    pos = (0, 0)
    font = pygame.font.SysFont('arial', 16)
    click = None
    surface_normal = None
    surface_hover = None
    surface_clicked = None
    status = NORMAL
    text = 'Button'

    def __init__(self, text, callable):
        self.click = callable
        self.text = text
        self._gen_surface()

    """
    绘制按钮
    """

    def on_draw(self, screen):
        if self.status == Button.HOVER:
            screen.blit(self.surface_hover, self.pos)
        elif self.status == Button.CLICKED:
            screen.blit(self.surface_clicked, self.pos)
        else:
            screen.blit(self.surface_normal, self.pos)

    """
    监控事件
    """

    def on_event(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if self._in_button_box(event.pos, self.get_box()):
                self.status = self.CLICKED
                self.click()
        elif event.type == MOUSEMOTION:
            if self._in_button_box(event.pos, self.get_box()):
                self.status = self.HOVER
            else:
                self.status = self.NORMAL
        else:
            self.status = self.NORMAL

    def _gen_surface(self):
        self.surface_normal = self.font.render(self.text, True, (0, 0, 0))
        self.surface_hover = self.font.render(self.text, True, (0, 0, 0),
                                              (0xee, 0xee, 0xee))
        self.surface_clicked = self.font.render(
            self.text, True, (0xff, 0xff, 0xff), (0x22, 0x22, 0x22))

    def get_box(self):
        return Rect(self.pos, self.surface_normal.get_size())

    def _in_button_box(self, point, box):
        p_x, p_y = point
        x, y, w, h = box
        if p_x >= x and p_x <= x + w:
            if p_y >= y and p_y <= y + h:
                return True
        return False
