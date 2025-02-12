# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),

## **[0.2.1] 2025-02-12**

### **Added**
- `alien_invasion.py` - Added a Play button. Players can also press **"P"** to start the game.
- `button.py` - Added a button class to display UI buttons on the screen.
- `settings.py` - Implemented dynamic settings for game speed and difficulty.
- `scoreboard.py` - Added a scoreboard to track the player's score.
- `README.md` - Created a project README with installation instructions, usage guide, and project details.

### **Changed**
- `settings.py` - Adjusted difficulty scaling for increasing game challenge over time.

---

## **[0.2.0] - 2025-02-10**

### **Added**
- `bullet.py` - Created the bullet class with its settings and behavior.
- `alien.py` - Added alien generation logic for enemy movement and spawning.
- `game_stats.py` - Introduced a module to track game statistics.

### **Changed**
- `alien_invasion.py`
  - Refactored key event handling.
  - Added **"Q"** key to quit the game.
  - Implemented full-screen mode (disabled by default).
  - Modified `_check_keydown_events()` to allow firing bullets with the **spacebar**.
  - Created alien rows.
  - Destroyed aliens when hit by bullets.
  - Reduced ship lives when losing all three.
- `ship.py`
  - Implemented movement restrictions within screen bounds.
  - Added speed control for smoother movement.
- `settings.py`
  - Introduced speed settings for ships and bullets.
  - Set ship lives to **3**.
  - Defined alien behavior settings.

---

## **[0.1.0] - 2025-02-09**

### **Added**
- `alien_invasion.py` - Created game window, set frame rate, and drew the ship.
- `settings.py` - Added a `Settings` class to store game settings.
- `ship.py` - Implemented ship graphics and movement.
- `CHANGELOG.md` - Started the changelog for tracking changes.

---
