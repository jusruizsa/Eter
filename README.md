# Simulador de Civilizaciones Emergentes

Este proyecto es un simulador narrativo en el que civilizaciones aparecen, evolucionan, compiten y colapsan en un mundo dividido por regiones.

Incluye cultura, religión, diplomacia, historia y visualización en tiempo real.

---

## 🧠 Características

* Generación automática de civilizaciones con personalidad e ideología
* Expansión, conquista, escisión y colapso
* Diplomacia con alianzas y traiciones
* Cultura dominante global que puede ser adoptada
* Religiones emergentes con propagación y dominio
* Eras históricas que alteran el comportamiento del mundo
* Eventos aleatorios que afectan civilizaciones
* Interfaz visual en tiempo real en terminal (`curses`)
* Exportación a HTML y JSON
* Capacidad de guardar y cargar mundos

---

## 🔄 Reglas de la simulación

### Creación inicial

* El mundo es una cuadrícula de dimensiones definidas.
* Se colocan civilizaciones aleatoriamente.
* Cada civilización tiene nombre, ideología, personalidad, símbolo y una región inicial.

### Turnos

En cada turno:

1. **Expansión:** intentan ocupar regiones vecinas o conquistar.
2. **Diplomacia:** pueden formar alianzas o traicionar.
3. **Escisión:** si son grandes, puede haber divisiones.
4. **Colapso:** si están débiles, pueden desaparecer.
5. **Eventos:** efectos como desastres, milagros o rebeliones.

### Cultura global

* Se calcula la ideología más común.
* Las demás civilizaciones pueden adoptarla (según la era).

### Religión

* Se pueden fundar religiones (10% chance).
* Estas se propagan entre civilizaciones.
* Se mantiene un registro de la religión dominante.

### Eras históricas (cambian cada 10 turnos)

| Era          | Expansión | Escisiones | Cultura  | Colapsos |
| ------------ | --------- | ---------- | -------- | -------- |
| Edad Antigua | Alta      | Media      | Baja     | Baja     |
| Edad Media   | Baja      | Alta       | Baja     | Media    |
| Edad Moderna | Media     | Baja       | Alta     | Baja     |
| Edad Dorada  | Muy alta  | Nula       | Muy alta | Mínima   |
| Edad Oscura  | Muy baja  | Muy alta   | Mínima   | Alta     |

---

## 💻 Visualización

* Terminal interactiva con `curses`.
* Se muestra:

  * Turno actual
  * Era histórica
  * Ideología y religión dominante
  * Mapa del mundo con símbolos
* Se puede pausar (`p`) o salir (`q`).

---

## 📦 Exportar y cargar

* `world_export.json`: exporta todo el estado del mundo.
* `world_report.html`: informe visual en navegador.
* Puedes cargar desde JSON y continuar desde cualquier turno.

---

## 📂 Estructura sugerida del proyecto

```
project/
├── main.py
├── world.py
├── region.py
├── civilization.py
├── utils/
│   ├── name_generator.py
│   └── ideology_pool.py
├── events/
│   ├── event_manager.py
│   ├── base_event.py
│   └── event_types.py
├── culture/
│   └── global_culture.py
├── religion/
│   └── religion_manager.py
├── eras/
│   └── era_manager.py
├── diplomacy/
│   └── alliances.py
├── export/
│   ├── json_exporter.py
│   ├── json_loader.py
│   └── html_exporter.py
├── views/
│   ├── civilization_view.py
│   ├── history_logger.py
│   └── curses_map.py
└── world_export.json
```

---

## ✅ Requisitos

* Python 3.10+
* En Windows: `pip install windows-curses`

---

## 🧪 Ejecutar

```bash
python main.py
```

## 🔁 Continuar una simulación

```python
from export.json_loader import load_world_state
from views.curses_map import run_simulation

world, turn = load_world_state()
run_simulation(world, turns=50, start_turn=turn + 1)
```

---

## ✨ Créditos

Construido con una simulación modular y narrativa guiada por decisiones emergentes.

Puedes expandir este mundo con comercio, razas, tecnología, arte o historia profunda.
