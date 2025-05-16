from world import World
from views.civilization_view import show_civilizations
from views.history_logger import log_history
from views.curses_map import run_simulation

if __name__ == "__main__":
    WIDTH = 20
    HEIGHT = 10
    CIV_COUNT = 6
    TURNS = 50

    world = World(WIDTH, HEIGHT, CIV_COUNT)

    run_simulation(world, TURNS)

    # Al final mostramos resumen
    show_civilizations(world.civilizations)
    for turn in range(1, TURNS + 1):
        log_history(turn, world.civilizations)
