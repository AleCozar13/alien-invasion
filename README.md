# Alien Invasion

## General Description
Alien Invasion is a simple space shooter game where the player controls a rocket ship positioned at the bottom center of the screen. The player can move the ship left and right using the arrow keys and shoot bullets using the spacebar. The objective is to destroy a fleet of aliens before they reach the bottom of the screen or collide with the player's ship.

### Game Mechanics
- A fleet of aliens moves across and down the screen.
- The player must shoot and destroy all aliens to progress.
- Each new fleet moves faster than the previous one.
- The player has three ships; losing all ships ends the game.

This project is a personal adaptation of the game from the *Python Crash Course* book.

---

## Installation Instructions

### Requirements
This project runs with **Python** and **Poetry**.

- **Python**: `>=3.13`
- **Dependencies**:
  - `pygame (>=2.6.1,<3.0.0)`

### Setup Steps
1. Install Poetry (if not already installed):
   ```sh
   pip install poetry
   ```
2. Clone the repository:
   ```sh
   git clone https://github.com/your-username/alien-invasion.git
   cd alien-invasion
   ```
3. Install dependencies:
   ```sh
   poetry install
   ```
4. Run the game:
   ```sh
   poetry run python alien_invasion/src/alien_invasion.py
   ```

---

## Usage Instructions
To play the game, simply run:
```sh
poetry run python alien_invasion/src/alien_invasion.py
```
Use **arrow keys** to move and **spacebar** to shoot.

---

## Configuration & Environment Variables
No additional configuration or `.env` files are required.

---

## Technologies Used
- Python
- Pygame

---

## Project Structure
```
/alien-invasion/
├── alien_invasion/
│   ├── src/
│   │   ├── images/
│   │   ├── alien_invasion.py
│   │   ├── alien.py
│   │   ├── bullet.py
│   │   ├── button.py
│   │   ├── game_stats.py
│   │   ├── scoreboard.py
│   │   ├── settings.py
│   │   ├── ship.py
├── .gitignore
├── CHANGELOG.md
├── poetry.lock
├── pyproject.toml
├── README.md
```

---

## Contributing
This project is not open for contributions at this time.

---

## License
No specific license has been assigned to this project.

