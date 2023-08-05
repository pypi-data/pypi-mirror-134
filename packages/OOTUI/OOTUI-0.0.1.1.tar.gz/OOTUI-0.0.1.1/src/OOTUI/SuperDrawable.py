from .Vector2 import Vector2


class SuperDrawable:
    """
    Used to draw on a canvas. \n
    A Drawable is a child of a window or other drawable. \n
    When a window or drawable updates, all of its children will update as well. \n
    A window or draw object cascades its canvas to all its children and their children, all these children draw over (their part of) the canvas. \n
    When the final child has drawn over (their part of) the canvas, it will send the canvas to its parent, who will assemble a canvas of all its children, and send it to its parent. This continues until the canvas arrives at the Window object (or an orphan drawable) and gets printed out to the terminal
    """
    pos: Vector2
    size: Vector2
    _drawer: 'SuperDrawable' = None
    _children: list['SuperDrawable'] = None
    _printCache: list[str] = None
    _receivedFromChildren: int = 0

    def __init__(self, pos: Vector2 = Vector2(), size: Vector2 = Vector2(1, 1)):
        self.pos = pos
        self.size = size
        if self._children is None:
            self._children = []
        if self._printCache is None:
            self._printCache = []

    def Update(self, canvas: list[str] = None):
        ...

    def DrawOn(self, canvas: list[str]):
        """
        :param: canvas the canvas to draw over, anything already in place can be replaced
        :return: The input canvas with the new drawable over it
        """
        self._receivedFromChildren = 0
        self._printCache = self._GetEmptyCanvas()
        self.Update(canvas)
        if self._children:
            [child.DrawOn(self.GetPartialCache(child.pos, child.size)) for child in self._children]
        else:
            self.CascadeBack()

    def CascadeBack(self):
        self._receivedFromChildren += 1
        if self._receivedFromChildren >= len(self._children):
            if self._drawer:
                self._drawer.ReplacePartialCache(self.pos, self._printCache)
                self._drawer.CascadeBack()

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

    def AddDrawable(self, drawable: 'SuperDrawable'):
        """
        :param drawable: a OOTUI object that inherits from SuperDrawable
        :return: None
        Mostly for use by other OOTUI objects
        """

        drawable._drawer = self
        self._children.append(drawable)

    def _GetEmptyCanvas(self):
        return [' '*self.size.x for _ in range(self.size.y)]
