"""Game states."""

from __future__ import annotations

import attrs
import tcod.console
import tcod.event
from tcod.event import KeySym

import g
from game.components import Graphic, Position
from game.state import State, StateResult

MOVE_KEYS = {
    KeySym.UP: (0, -1),
    KeySym.DOWN: (0, 1),
    KeySym.LEFT: (-1, 0),
    KeySym.RIGHT: (1, 0),
}


@attrs.define()
class ExampleState(State):
    """Example state class."""

    def on_event(self, event: tcod.event.Event) -> StateResult:
        """Handle player movement."""
        match event:
            case tcod.event.KeyDown(sym=sym) if sym in MOVE_KEYS:
                g.world["player"].components[Position] += MOVE_KEYS[sym]
        return None

    def on_draw(self, console: tcod.console.Console) -> None:
        """Example drawing."""
        console.rgb["bg"][::2, ::2] = console.rgb["bg"][1::2, 1::2] = 0x10
        console.print(0, 0, "Hello World")
        for pos, graphic in g.world.Q[Position, Graphic]:
            if 0 <= pos.x < console.width and 0 <= pos.y < console.height:
                console.rgb[["ch", "fg"]][pos.y, pos.x] = graphic.ch, graphic.fg
