import curses
import time

def run_simulation(world, turns):
    curses.wrapper(_main_loop, world, turns)

def _main_loop(stdscr, world, turns):
    curses.curs_set(0)
    stdscr.nodelay(True)

    for turn in range(1, turns + 1):
        stdscr.clear()
        stdscr.addstr(0, 0, f"Turno {turn}")
        
        for y in range(world.height):
            line = ""
            for x in range(world.width):
                region = world.grid[x][y]
                line += region.civilization.symbol if region.civilization else "."
            stdscr.addstr(y + 2, 0, line)

        world.advance_turn()
        stdscr.refresh()
        time.sleep(0.5)  # velocidad de avance
