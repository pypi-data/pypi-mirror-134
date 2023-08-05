from .SuperDrawable import SuperDrawable
from .Vector2 import Vector2


class BorderRect(SuperDrawable):
    """ A rectangle drawable with no fill

    Can be used for encasing other objects (make other objects children of this one for easy modifiability). \n
    Inner space does **NOT** overwrite any other drawables, so it can be used to partially overlay other drawables
    """
    char: str

    def __init__(self, pos: Vector2 = Vector2(), size: Vector2 = Vector2(3, 3), char: str = '█'):
        if len(char) == 1:
            super().__init__(pos, size)
            self.char = char
        else:
            raise Exception('param: "char" must be of length 1')

    def Update(self, canvas: list[str] = None):
        if canvas is None:
            canvas = self._GetEmptyCanvas()

        self._printCache[0] = self.char * self.size.x
        for y in range(1, self.size.y - 1):
            self._printCache[y] = self.char + canvas[y][1:-2] + self.char
        self._printCache[-1] = self.char * self.size.x
