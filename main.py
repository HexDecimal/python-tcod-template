#!/usr/bin/env python3
"""Main script."""

from __future__ import annotations

import tcod.console
import tcod.context
import tcod.ecs
import tcod.event
import tcod.tileset

import g
import game.state
import game.states
from game.components import Graphic, Position


def main() -> None:
    """Main entry point."""
    tileset = tcod.tileset.load_bdf("assets/cozette.bdf")
    console = tcod.console.Console(80, 50)
    g.states = [game.states.ExampleState()]
    g.world = tcod.ecs.World()
    g.world["player"].components.update(
        {
            Position: Position(20, 20),
            Graphic: Graphic(ord("@")),
        }
    )

    with tcod.context.new(console=console, tileset=tileset) as g.context:
        while g.states:
            console.clear()
            g.states[-1].on_draw(console)
            g.context.present(console)
            for event in tcod.event.wait():
                match event:
                    case tcod.event.Quit():
                        raise SystemExit()
                match g.states[-1].on_event(event):
                    case game.state.Push(new_state):
                        g.states.append(new_state)
                    case game.state.Pop():
                        g.states.pop()
                    case game.state.Rebase(new_state):
                        g.states = [new_state]


if __name__ == "__main__":
    main()
