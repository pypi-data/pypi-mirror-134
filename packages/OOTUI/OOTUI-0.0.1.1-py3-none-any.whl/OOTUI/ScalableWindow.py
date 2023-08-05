from .Window import Window
from .Vector2 import Vector2
import os


class ScalableWindow(Window):
    """A window that re sets its size everytime its updates

    Should only be used if the Update function is called often, and if terminal resizing is expected. Other wise: use Window instead
    """
    def Update(self):
        self._size = Vector2(os.get_terminal_size().columns, os.get_terminal_size().lines)
        super().Update()
