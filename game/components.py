"""Common component classes."""

from __future__ import annotations

from typing import Self

import attrs


@attrs.define(frozen=True)
class Position:
    """Entity position."""

    x: int
    y: int

    @property
    def ij(self) -> tuple[int, int]:
        """Return the matrix index of this position, a (y, x) tuple."""
        return self.y, self.x

    def __add__(self, other: Position | tuple[int, int]) -> Self:
        """Add a vector to this position."""
        if isinstance(other, Position):
            return self.__class__(self.x + other.x, self.y + other.y)
        x, y = other
        return self.__class__(self.x + x, self.y + y)


@attrs.define(frozen=True)
class Graphic:
    """Visible glyph info of an entity."""

    ch: int
    fg: tuple[int, int, int] = (255, 255, 255)
