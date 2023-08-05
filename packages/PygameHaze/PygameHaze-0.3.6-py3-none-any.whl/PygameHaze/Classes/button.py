# MIT License
#
# Copyright (c) 2021 Emc2356
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


"""
a button class with a lot of abilities
"""


from typing import Tuple, List, Union

import pygame

from PygameHaze.utils import *
from PygameHaze.constants import *
from PygameHaze.exceptions import *


class Button:
    """
    Creates a button on the screen

    Parameters:
    -----------
    WIN: pygame.surface.Surface
        the screen that the button is going to be drawn in
    x: int
        the x position of the button
    y: int
        the y position of the button
    w: int
        the width of the button
    h: int
        the height of the button
    inactive_color: Tuple[int, int, int]
        the color of the button when it is inactive
    hover_inactive_color: Tuple[int, int, int]
        the color of the button when it is inactive and the mouse is over it
    active_color: Tuple[int, int, int]
        the color of the button when it is active
    hover_active_color: Tuple[int, int, int]
        the color of the button when it is active and the mouse is over it
    **kwargs: optional parameters
        optional parameters

    Methods:
    -----------
    update():
        it updates the text and the button rect
    draw():
        it draws the button on the screen
    event_handler(pygame.event.Event):
        it handles the events
    """
    def __init__(self,
                 WIN: pygame.surface.Surface,
                 x: int,
                 y: int,
                 w: int,
                 h: int,
                 inactive_color: Tuple[int, int, int]=WHITE,
                 hover_inactive_color: Tuple[int, int, int]=WHITESMOKE,
                 active_color: Tuple[int, int, int]=WHITE,
                 hover_active_color: Tuple[int, int, int]=WHITESMOKE,
                 **kwargs):

        # get the screen to draw the button
        self.WIN: pygame.surface.Surface = WIN

        # get the positions/dimensions of the button
        self._x: int = int(x)
        self._y: int = int(y)
        self._w: int = int(w)
        self._h: int = int(h)
        self.pressed: bool = False
        self.border_radius: int = kwargs.get("border_radius", 0)
        self.anchor: str = kwargs.get("anchor", TOPLEFT).lower()
        self.button_rect: pygame.Rect = pygame.Rect(1, 1, 1, 1)

        # get the colors
        self.inactive_color: Tuple[int, int, int] = inactive_color
        self.hover_inactive_color: Tuple[int, int, int] = hover_inactive_color
        self.active_color: Tuple[int, int, int] = active_color
        self.hover_active_color: Tuple[int, int, int] = hover_active_color
        self.color: Tuple[int, int, int] = self.active_color if self.pressed else self.inactive_color

        # get the images if there is any
        transform_scale_image = kwargs.get("transform_scale_image", True)

        inactive_sprite = kwargs.get("inactive_sprite", None)  # the sprite that is used when the button is deactivated
        if isinstance(inactive_sprite, pygame.surface.Surface):
            inactive_sprite = inactive_sprite.convert_alpha()
        elif isinstance(inactive_sprite, str):
            inactive_sprite = load_alpha_image(inactive_sprite)
        if transform_scale_image and inactive_sprite is not None:
            inactive_sprite = resize_smooth_image(inactive_sprite, (self._w, self._h))
        self.inactive_sprite = inactive_sprite

        inactive_hover_sprite = kwargs.get("inactive_hover_sprite", None)  # the sprite that is used when the button is deactivated and the mouse is over it
        if isinstance(inactive_hover_sprite, pygame.surface.Surface):
            inactive_hover_sprite = inactive_hover_sprite.convert_alpha()
        elif isinstance(inactive_hover_sprite, str):
            inactive_hover_sprite = load_alpha_image(inactive_hover_sprite)
        if transform_scale_image and inactive_hover_sprite is not None:
            inactive_hover_sprite = resize_smooth_image(inactive_hover_sprite, (self._w, self._h))
        self.inactive_hover_sprite = inactive_hover_sprite

        active_sprite = kwargs.get("active_sprite", None)  # the sprite that is used when the button is activated
        if isinstance(active_sprite, pygame.surface.Surface):
            active_sprite = active_sprite.convert_alpha()
        elif isinstance(active_sprite, str):
            active_sprite = load_alpha_image(active_sprite)
        if transform_scale_image and active_sprite is not None:
            active_sprite = resize_smooth_image(active_sprite, (self._w, self._h))
        self.active_sprite = active_sprite

        active_hover_sprite = kwargs.get("active_hover_sprite", None)  # the sprite that is used when the button is activated and the mouse is over it
        if isinstance(active_hover_sprite, pygame.surface.Surface):
            active_hover_sprite = active_hover_sprite.convert_alpha()
        elif isinstance(active_hover_sprite, str):
            active_hover_sprite = load_alpha_image(active_hover_sprite)
        if transform_scale_image and active_hover_sprite is not None:
            active_hover_sprite = resize_smooth_image(active_hover_sprite, (self._w, self._h))
        self.active_hover_sprite = active_hover_sprite

        self.current_sprite: pygame.surface.Surface = self.inactive_sprite if not self.pressed else self.active_sprite

        # get the functions if the user has set any
        self.on_click = kwargs.get("on_click", None)  # the function that is called when the button is activated
        self.on_click_args = kwargs.get("on_click_args", None)  # the positional arguments of the function that is called when the button is activated
        self.on_click_kwargs = kwargs.get("on_click_kwargs", None)  # the key-word arguments of the function that is called when the button is activated
        self.on_release = kwargs.get("on_release", None)  # the function that is called when the button is deactivated
        self.on_release_args = kwargs.get("on_release_args", None)  # the positional arguments of the function that is called when the button is deactivated
        self.on_release_kwargs = kwargs.get("on_release_kwargs", None)  # the key-word arguments of the function that is called when the button is deactivated

        # get the text info
        self._text = kwargs.get("text", "")  # for multiple lines use "\n"
        self.antialias = kwargs.get("antialias", True)
        self.text_color = kwargs.get("text_color", (0, 0, 0))
        self.font_type = kwargs.get("font_type", "camicsans")
        self.font_size = kwargs.get("font_size", 60)
        self.font = get_font(self.font_size, self.font_type)
        self.rendered_text_surfaces: List[Union[pygame.surface.Surface, List[int, int]]] = []

        self.kwargs = kwargs

        self.__internal_mouse_motion_event: pygame.event.Event = pygame.event.Event(pygame.USEREVENT+4000, {"pos": pygame.mouse.get_pos()})
        pygame.event.post(self.__internal_mouse_motion_event)

        self.update()

    def update(self) -> None:
        """
        it updates the button's rect and surfaces (automatically getting called when you set the x, y, w, h, text)
        :return: None
        """
        try:
            self.button_rect = pygame.Rect(self._x, self._y, self._w, self._h)
            self.button_rect.__setattr__(self.anchor, (self._x, self._y))
        except AttributeError:
            raise InvalidAnchor(f"""The anchor '{self.anchor}' is not a valid anchor.""")

        self.rendered_text_surfaces = []
        font_h = self.font.get_height()
        y = self.button_rect.centery - ((len(self._text.split("\n"))*font_h)/2)

        for i, text in enumerate(self._text.split("\n")):
            surf = self.font.render(text, self.antialias, self.text_color)
            pos = [self.button_rect.centerx - surf.get_width()/2, y + (i * font_h)]
            self.rendered_text_surfaces.append([surf, pos])

            width = surf.get_width()
            if width > self._w:
                raise TextOfOutBounds(f"the given string: '{text}' is {width - self._w}pxls out of bounds in the x-axis")

        if self._text != "":
            h = len(self._text.split("\n"))*font_h
            if h > self._h:
                raise TextOfOutBounds(f"the text: [{self._text}] is {h - self._h}pxls out of bounds in the y-axis")

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, val: int) -> None:
        self._x = val
        self.update()

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, val: int) -> None:
        self._y = val
        self.update()

    @property
    def w(self) -> int:
        return self._w

    @w.setter
    def w(self, val: int) -> None:
        self._w = val
        self.update()

    @property
    def h(self) -> int:
        return self._h

    @h.setter
    def h(self, val: int) -> None:
        self._h = val
        self.update()

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, text: str) -> None:
        self._text = text
        self.update()

    def draw(self) -> None:
        """
        it draws the button on the screen
        :return: None
        """
        pygame.draw.rect(self.WIN, self.color, self.button_rect, border_radius=self.border_radius)
        if self.current_sprite is not None:
            self.WIN.blit(self.current_sprite, self.button_rect)

        if self.rendered_text_surfaces:
            for surf, pos in self.rendered_text_surfaces:
                self.WIN.blit(surf, pos)

    def event_handler(self, event: pygame.event.Event) -> None:
        """
        it handles the events that the class can check
        :param event: pygame.event.Event
        :return: None
        """
        if event.type == self.__internal_mouse_motion_event.type or event.type == pygame.MOUSEMOTION:
            if self.pressed:
                if self.button_rect.collidepoint(event.pos):
                    self.color = self.hover_active_color
                    self.current_sprite = self.active_hover_sprite
                else:
                    self.color = self.active_color
                    self.current_sprite = self.active_sprite
            else:
                if self.button_rect.collidepoint(event.pos):
                    self.color = self.hover_inactive_color
                    self.current_sprite = self.inactive_hover_sprite
                else:
                    self.color = self.inactive_color
                    self.current_sprite = self.inactive_sprite
        elif left_click(event):
            if self.button_rect.collidepoint(event.pos):
                if self.pressed:
                    if self.on_release:
                        if self.on_release_kwargs and self.on_release_args: self.on_release(*self.on_release_args, **self.on_release_kwargs)
                        elif self.on_release_args: self.on_release(*self.on_release_args)
                        elif self.on_release_kwargs: self.on_release(**self.on_release_kwargs)
                        else: self.on_release()

                elif not self.pressed:
                    if self.on_click:
                        if self.on_click_kwargs and self.on_click_args: self.on_click(*self.on_click_args, **self.on_click_kwargs)
                        elif self.on_click_args: self.on_click(*self.on_click_args)
                        elif self.on_click_kwargs: self.on_click(**self.on_click_kwargs)
                        else: self.on_click()

                pygame.event.post(self.__internal_mouse_motion_event)
                self.pressed = not self.pressed

    def __repr__(self):
        return f"""Button at: {self._x, self._y} | with dimensions: {self._w, self._h}{f" | with text: {self._text}" if self._text != '' else ''}"""
