<div align="center">

# Pythonium

**Classic Snake — pygame edition.**

[![Python](https://img.shields.io/badge/python-3.12+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/pygame-2.6-5c4e9e?style=flat-square)](requirements.txt)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-4a5568?style=flat-square)](#quick-start)
[![License](https://img.shields.io/badge/license-MIT-af52de?style=flat-square)](#license)

</div>

---

A small **Snake** clone built with **Python** and **Pygame** — menu, three difficulty presets, score, session high score, and speed that ramps as you eat.

UI strings are in **Russian** (difficulty labels, game over). Game logic is a single file, easy to read and tweak.

---

## Quick start

```bash
git clone https://github.com/krwg/pythonium.git
cd pythonium
python -m pip install --upgrade pip
pip install -r requirements.txt
python pythonium.py
```

**Requirements:** Python **3.12+** recommended · Windows, macOS, or Linux with a display.

---

## Controls

| Key | Action |
|-----|--------|
| **1 / 2 / 3** | Easy / Medium / Hard (starts game) |
| **Arrow keys** | Move |
| **Space / Enter** | Restart after game over |
| **Esc** | Quit |

| Difficulty | Base FPS |
|------------|----------|
| Easy | 15 |
| Medium | 20 |
| Hard | 25 |

Speed and FPS increase slightly each time the snake eats.

---

## Project layout

```
pythonium/
├── pythonium.py      # entire game
├── requirements.txt  # pygame==2.6.0
└── README.md
```

---

## Releases

Prebuilt downloads (if published): [GitHub Releases](https://github.com/krwg/pythonium/releases) — tag **0.5** and earlier builds.

---

## License

MIT — see repository license. Built as a learning / portfolio pygame project.

---

<div align="center">

By [krwg](https://github.com/krwg) · eat the apple, don't eat yourself

</div>
