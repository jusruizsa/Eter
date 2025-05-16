def show_civilizations(civilizations):
    for civ in civilizations:
        print(f"\nCivilización: {civ.name}")
        print(f"  ID: {civ.id}")
        print(f"  Ideología: {civ.ideology}")
        print(f"  Regiones ocupadas: {len(civ.regions)}")
        print("  Historia reciente:")
        for event in civ.history[-3:]:
            print(f"    - {event}")
