import json

from civilization import Civilization
from world import World

def export_world_state(world, turn, filename="world_export.json"):
    data = {
        "turn": turn,
        "width": world.width,
        "height": world.height,
        "dominant_ideology": world.global_culture.dominant_ideology,
        "dominant_religion": world.religion_manager.dominant_religion,
        "era": world.era_manager.era,
        "civilizations": [],
        "regions": []
    }

    for civ in world.civilizations:
        data["civilizations"].append({
            "id": civ.id,
            "name": civ.name,
            "ideology": civ.ideology,
            "religion": civ.religion,
            "symbol": civ.symbol,
            "personality": civ.personality,
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


    def load_world_state(filename="world_export.json"):
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)

        width = data["width"]
        height = data["height"]
        world = World(width, height, civilization_count=0)

        civ_map = {}
        for civ_data in data["civilizations"]:
            civ = Civilization(region=None)
            civ.id = civ_data["id"]
            civ.name = civ_data["name"]
            civ.ideology = civ_data["ideology"]
            civ.religion = civ_data["religion"]
            civ.symbol = civ_data["symbol"]
            civ.personality = civ_data["personality"]
            civ.history = civ_data["history"]
            civ.allies = set(civ_data["allies"])
            civ.regions = []
            civ_map[civ.id] = civ
            world.civilizations.append(civ)

        for rdata in data["regions"]:
            region = world.grid[rdata["x"]][rdata["y"]]
            civ_id = rdata["civilization"]
            if civ_id:
                civ = civ_map[civ_id]
                region.civilization = civ
                civ.regions.append(region)

        world.global_culture.dominant_ideology = data.get("dominant_ideology")
        world.religion_manager.dominant_religion = data.get("dominant_religion")
        world.era_manager.era = data.get("era", "Edad Antigua")

        return world, data.get("turn", 0)

