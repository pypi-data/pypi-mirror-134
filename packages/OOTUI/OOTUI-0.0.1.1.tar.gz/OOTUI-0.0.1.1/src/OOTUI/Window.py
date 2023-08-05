import os
from .Vector2 import Vector2
from .SuperDrawable import SuperDrawable


class Window:
    """A window takes up the whole terminal and clears it before displaying its child drawables.

    You should only use a window if you want to create a complex structure with drawables, ond if you want to display nothing but drawables. \n
    A window can in some ways be seen as a drawable itself, but it has no parent drawable. \n
    In most cases you only want 1 Window object, But you might want multiple if you want multiple screens that have no relation to each other. \n
    It is recommended to update a window no more than 10 times per second. \n
    If you want to be able to resize the terminal while your program is running, use ScalableWindow instead.
    """

    _size: Vector2
    _printCache: list[str]
    _drawObjects: list[SuperDrawable] = None
    _receivedFromDrawObj: int = 0

    def __init__(self):
        self._size = Vector2(os.get_terminal_size().columns, os.get_terminal_size().lines)
        if self._drawObjects is None:
            self._drawObjects = []

    def GetSize(self) -> Vector2 | None:
        if -1 in self._size:
            return None
        else:
            return self._size

    def Display(self):
        outputStr = '\n'.join(self._printCache)
        os.system('cls')
        print(outputStr)

    def Update(self):
        self._printCache = [' '*self._size.x for _ in range(self._size.y)]
        self._receivedFromDrawObj = 0

        for draw in self._drawObjects:
            draw.DrawOn(self.GetPartialCache(draw.pos, draw.size))

    def CascadeBack(self):
        self._receivedFromDrawObj += 1
        if self._receivedFromDrawObj >= len(self._drawObjects):
            self.Display()

    def Width(self) -> int:
        return self._size.x

    def Height(self) -> int:
        return self._size.y

    def GetPrintCache(self):
        """
        Mostly for use by other OOTUI objects
        """
        return self._printCache

    def GetPartialCache(self, pos: Vector2, size: Vector2):
        """
        :param pos:
        :param size:
        :return: a smaller canvas for other objects to draw over
        Mostly for use by other OOTUI object
        """
        partialCache = []
        for y in range(pos.y, pos.y + size.y + 1):
            partialCache.append(self._printCache[y][pos.x: pos.x + size.x + 1])
        return partialCache

    def ReplacePartialCache(self, pos: Vector2, cache: list[str]):
        """
        :param pos: position of the smaller canvas in the canvas it replaces
        :param cache: smaller canvas to replace part of old cache
        :return:
        Mostly for use by other OOTUI objects
        """
        for y in range(pos.y, pos.y + len(cache)):
            self._printCache[y] = self._printCache[y][:pos.x] + cache[y - pos.y] + self._printCache[y][pos.x + len(cache[0]):]

    def AddDrawable(self, drawable: SuperDrawable):
        """
        :param drawable: a OOTUI object that inherits from SuperDrawable
        :return: None
        Mostly for use by other OOTUI objects
        """
        drawable._drawer = self
        self._drawObjects.append(drawable)
