import json

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang=\"es\">
<head>
    <meta charset=\"UTF-8\">
    <title>Historia del Mundo Simulado</title>
    <style>
        body {{ font-family: sans-serif; padding: 2em; background: #f4f4f4; }}
        .map {{ font-family: monospace; background: #fff; padding: 1em; border: 1px solid #ccc; white-space: pre; }}
        .civ {{ margin-bottom: 2em; background: #fff; padding: 1em; border: 1px solid #ccc; }}
        h2 {{ margin-top: 0; }}
    </style>
</head>
<body>
    <h1>Historia del Mundo Simulado</h1>
    <p><strong>Turno:</strong> {turn}</p>
    <p><strong>Era:</strong> {era}</p>
    <p><strong>Ideología Dominante:</strong> {dominant_ideology}</p>
    <p><strong>Religión Dominante:</strong> {dominant_religion}</p>
    <h2>Mapa</h2>
    <div class=\"map\">{map_text}</div>
    <h2>Civilizaciones</h2>
    {civilization_blocks}
</body>
</html>
"""

CIV_BLOCK = """
<div class=\"civ\">
  <h3>{name} ({symbol})</h3>
  <p><strong>ID:</strong> {id}</p>
  <p><strong>Ideología:</strong> {ideology}</p>
  <p><strong>Religión:</strong> {religion}</p>
  <p><strong>Personalidad:</strong> {personality}</p>
  <p><strong>Regiones:</strong> {region_count}</p>
  <p><strong>Eventos:</strong></p>
  <ul>
    {event_list}
  </ul>
</div>
"""

def export_to_html(world, turn, filename="world_report.html"):
    map_lines = []
    for y in range(world.height):
        line = ""
        for x in range(world.width):
            region = world.grid[x][y]
            line += region.civilization.symbol if region.civilization else "."
        map_lines.append(line)
    map_text = "\n".join(map_lines)

    civ_blocks = []
    for civ in world.civilizations:
        events = "\n    ".join([f"<li>{e}</li>" for e in civ.history[-5:]])
        civ_blocks.append(CIV_BLOCK.format(
            name=civ.name,
            symbol=civ.symbol,
            id=civ.id,
            ideology=civ.ideology,
            religion=civ.religion or "ninguna",
            personality=civ.personality,
            region_count=len(civ.regions),
            event_list=events
        ))

    html = HTML_TEMPLATE.format(
        turn=turn,
        era=world.era_manager.era,
        dominant_ideology=world.global_culture.dominant_ideology or "ninguna",
        dominant_religion=world.religion_manager.dominant_religion or "ninguna",
        map_text=map_text,
        civilization_blocks="\n".join(civ_blocks)
    )

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
