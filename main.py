from world import World
from views.civilization_view import show_civilizations
from views.history_logger import log_history

if __name__ == "__main__":
    WIDTH = 10
    HEIGHT = 10
    CIV_COUNT = 5
    TURNS = 10

    world = World(WIDTH, HEIGHT, CIV_COUNT)

    for turn in range(1, TURNS + 1):
        print(f"\n--- Turno {turn} ---")
        world.advance_turn()
        world.display_state()
        show_civilizations(world.civilizations)
        log_history(turn, world.civilizations)
