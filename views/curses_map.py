import curses
import time

def run_simulation(world, turns, start_turn=1):
    curses.wrapper(_main_loop, world, turns, start_turn)

def _main_loop(stdscr, world, turns, start_turn):
    curses.curs_set(0)
    stdscr.nodelay(True)
    paused = False

    for turn in range(start_turn, start_turn + turns):
        while True:
            stdscr.clear()
            stdscr.addstr(0, 0, f"Turno {turn} | Civilizaciones: {len(world.civilizations)}")
            stdscr.addstr(1, 0, f"Era actual: {world.era_manager.era}")
            if world.global_culture.dominant_ideology:
                stdscr.addstr(2, 0, f"Ideología dominante: {world.global_culture.dominant_ideology}")
            if world.religion_manager.dominant_religion:
                stdscr.addstr(3, 0, f"Religión dominante: {world.religion_manager.dominant_religion}")
            stdscr.addstr(4, 0, "(p) Pausar | (q) Salir")

            for y in range(world.height):
                line = ""
                for x in range(world.width):
                    region = world.grid[x][y]
                    line += region.civilization.symbol if region.civilization else "."
                stdscr.addstr(y + 6, 0, line)

            stdscr.refresh()

            key = stdscr.getch()
            if key == ord("q"):
                return
            if key == ord("p"):
                paused = not paused

            if not paused:
                break
            time.sleep(0.1)

        world.advance_turn()
        time.sleep(0.4)
