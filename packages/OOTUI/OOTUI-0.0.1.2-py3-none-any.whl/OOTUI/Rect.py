from .SuperDrawable import SuperDrawable
from .Vector2 import Vector2


class Rect(SuperDrawable):
    """ A rectangle drawable

    solid rectangle
    """
    char: str

    def __init__(self, pos: Vector2 = Vector2(), size: Vector2 = Vector2(1, 1), char: str = '█'):
        super().__init__(pos, size)
        if len(char) == 1:
            self.char = char
        else:
            raise Exception("param 'char' must be of length 1")

    def Update(self, canvas: list[str] = None):
        self._printCache = [self.char*self.size.x for _ in range(self.size.y)]
