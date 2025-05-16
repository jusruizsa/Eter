from world import World
from views.civilization_view import show_civilizations
from views.history_logger import log_history
from views.curses_map import run_simulation
from export.json_exporter import export_world_state


if __name__ == "__main__":
    WIDTH = 20
    HEIGHT = 10
    CIV_COUNT = 6
    TURNS = 50

    world = World(WIDTH, HEIGHT, CIV_COUNT)

    run_simulation(world, TURNS)

    # Registro final
    show_civilizations(world.civilizations)
    for turn in range(1, TURNS + 1):
        log_history(turn, world.civilizations)

    # Exportar estado completo del mundo
    export_world_state(world, TURNS)
