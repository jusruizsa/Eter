import json

def export_world_state(world, turn, filename="world_export.json"):
    data = {
        "turn": turn,
        "width": world.width,
        "height": world.height,
        "dominant_ideology": world.global_culture.dominant_ideology,
        "civilizations": [],
        "regions": []
    }

    civ_index = {civ.id: idx for idx, civ in enumerate(world.civilizations)}

    for civ in world.civilizations:
        data["civilizations"].append({
            "id": civ.id,
            "name": civ.name,
            "ideology": civ.ideology,
            "symbol": civ.symbol,
            "history": civ.history,
            "region_coords": [(r.x, r.y) for r in civ.regions],
            "allies": list(civ.allies)
        })

    for x in range(world.width):
        for y in range(world.height):
            region = world.grid[x][y]
            data["regions"].append({
                "x": x,
                "y": y,
                "civilization": region.civilization.id if region.civilization else None
            })

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
