# Alien Invasion Game

## Overview
Alien Invasion is a classic retro 🕹️ game that we all have played as children, and some might still be enjoying it. Players control a spaceship that must defend the Earth by shooting down waves of alien invaders.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting Started With Game](#getting-started-with-game)
    * [Prerequisites](#prerequisites)
    * [Installation](#installation)
    * [Virtual Environment Setup](#virtual-environment-setup)
    * [Running the Game](#running-the-game)
- [Button Mapping](#button-mapping)
- [Code Structure](#code-structure)
- [Development Journey](#development-journey)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Player Control**: Move the spaceship left, right, and shoot bullets.
- **Increasing Difficulty**: Game speeds ups to increase the difficulty.
- **Scoring System**: Points awarded for shooting down aliens.
- **Game Over**: The game ends if an alien reaches the bottom of the screen or collides with the spaceship.

## Getting Started With Game

1. ### Prerequisites
- Python 3.12.2
- Pygame library

2. ### Installation
    1. Clone the repository:
       ```bash
       git clone https://github.com/Sarthak-G0yal/Alien-Invasion-Game.git
       ```
    2. Navigate to the project directory:
       ```bash
       cd alien-invasion
       ```

3. ### Running the Game
    Run the following command to start the game:
    ```bash
    start alien_invasion.exe
    ```

## Button Mapping
|Function|Button|
|----|----|
|Move Left|Left Arrow|
|Move Right|Right Arrow|
|Shoot|SpaceBar|
|Exit|Q|

## Code Structure
- `alien_invasion.py`: The main game file that initializes the game and contains the game loop.
- `settings.py`: Configuration file for game settings such as screen dimensions and colors.
- `ship.py`: Class for managing the player's spaceship.
- `bullet.py`: Class for managing bullets fired by the spaceship.
- `alien.py`: Class for managing the alien invaders.
- `game_stats.py`: Class for tracking game statistics.
- `scoreboard.py`: Class for displaying the score.

## Development Journey
This is a Classic Retro🕹️ game that we all have played as a child or some might even be enjoying it right now. I built this game as my first big project using **Python** and its **Pygame** Module. 

It was a fun project which helped me learn a lot about the flow of development, code management, refactoring, the importance of descriptive names, and many other things. 

I have used [**Python Crash Course By Eric Matthes 2<sup>nd</sup> Edition**](https://ehmatthes.github.io/pcc/) as my guide. It is a very good book to learn Python from, as it focuses more on implementation rather than just the theory. It has many interesting project-based chapters that are fun to do and teach us many concepts.

## Contributing
Contributions are welcome! If you have suggestions or improvements, please open an issue or submit a pull request.

## License
This project is licensed under the GPL-V3 License - see the [LICENSE](#license) file for details.
