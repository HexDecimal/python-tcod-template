"""Global variables."""

from __future__ import annotations

import tcod.context
import tcod.ecs

import game.state

context: tcod.context.Context
"""Active tcod context."""

states: list[game.state.State] = []
"""Stack of states, the last state is the active state."""

world: tcod.ecs.World
"""Active ECS registry."""
