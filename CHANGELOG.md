# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.1] UNRELEASED

## [0.2.0] 2025-02-10

### Added

- `bullet.py`Generates the bullets and it settings.
- `alien.py` Generates an alien in the screen.
- `game_stats.py` Track game statistics.

### Changed

- `alien_invasion.py` Refactor key events method. Add press Q to exit game. Add full screen mode code, but not activate. Modify _check_keydown_events() to fire bullets when pressing the spacebar. Generates the alien rows. Get rid of aliens when impact bullets, also get rid of ship when loosing 3 lives.
- `ship.py` Set right and left movement of the ship, also limit to the screen are. Add speed control.
- `settings.py` Add speed setting for the ship and for the bullets. Set 3 ship lives. Create aliens settings.

## [0.1.0] 2025-02-09

### Added

- `alien_invasion.py` Creates game window, add frame rate, draw the ship.
- `settings.py` Module that contains class Settings to store all settings values.
- `ship.py` Generates the image of the ship, set right and left.
- CHANGELOG.
