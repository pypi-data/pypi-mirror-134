class Vector2:
    """Represents a point in a 2d space \n

    Allows for math between 2 Vector2's \n
    Allows for unpacking: ```v = Vector2(3, 5)\nx, y = v```
    """
    x: int
    y: int
    _iter: int = 0

    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)

        raise NotImplementedError(f"{other} must be of type: Vector2")

    def __sub__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x - other.x, self.y - other.y)

        raise NotImplementedError

    def __mul__(self, other):
        if isinstance(other, int):
            return Vector2(self.x * other, self.y * other)
        elif isinstance(other, Vector2):
            return Vector2(self.x * other.x, self.y * other.y)

        raise NotImplementedError(f"{other} must be of type: Vector2 | int")

    def __copy__(self):
        return Vector2(self.x, self.y)

    def __hash__(self):
        return hash(self.x, self.y)

    def __eq__(self, other):
        if isinstance(other, Vector2):
            return self.x == other.x and self.y == other.y

        raise NotImplementedError

    def __iter__(self):
        return self

    def __next__(self):
        if self._iter < 2:
            val = (self.x, self.y)[self._iter]
            self._iter += 1
            return val
        else:
            raise StopIteration

    def __int__(self):
        return self.x + self.y

    def __repr__(self):
        return f"Vector2({self.x}, {self.y})"
