"""Abstract state classes."""
from __future__ import annotations

from typing import Protocol

import attrs
import tcod.console
import tcod.event


@attrs.define()
class Push:
    """Push a state onto the top of the stack."""

    state: State


@attrs.define()
class Pop:
    """Pop the current state."""


@attrs.define()
class Rebase:
    """Replace all states with a new state."""

    state: State


StateResult = Push | Pop | Rebase | None
"""State change instructions."""


class State(Protocol):
    """Common state protocol."""

    __slots__ = ()

    def on_event(self, event: tcod.event.Event) -> StateResult:
        """Handle tcod events and return state changes."""
        return None

    def on_draw(self, console: tcod.console.Console) -> None:
        """Render the current state."""
