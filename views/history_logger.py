def log_history(turn, civilizations, filename="history_log.txt"):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"\n=== TURNO {turn} ===\n")
        for civ in civilizations:
            f.write(f"Nombre: {civ.name}\n")
            f.write(f"  ID: {civ.id}\n")
            f.write(f"  Ideología: {civ.ideology}\n")
            f.write(f"  Regiones ocupadas: {len(civ.regions)}\n")
            f.write("  Últimos eventos:\n")
            for event in civ.history[-3:]:
                f.write(f"    - {event}\n")
        f.write("\n")
