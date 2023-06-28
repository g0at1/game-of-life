# Conway's Game of Life 

## Description
Conway's Game of Life is a cellular automaton devised by mathematician John Horton Conway in 1970. This project provides a Python implementation of Conway's Game of Life using the Pygame library. The Pygame version allows you to interactively observe the evolution of cells on a two-dimensional grid and enjoy a visual representation of the simulation.

## Features
- Simulate the evolution of cells in Conway's Game of Life.
- Observe the dynamic patterns and interactions between cells.
- Interactive visualization using Pygame.

## Installation
1. Ensure that you have Python 3 installed on your system.
2. Clone this repository or download the source code as a ZIP file.
3. Extract the contents of the ZIP file (if applicable) to a directory of your choice.
4. Install the required dependencies using the following command:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Open a terminal or command prompt and navigate to the directory where the source code is located.
2. Run the program using the following command:
   ```bash
   python main.py
   ```
3. The Pygame window will open, displaying the grid and the evolution of cells.
4. Press the "Space" key to pause or resume the simulation.
5. Press the "Esc" key or close the window to exit the program.

## Rules
Conway's Game of Life follows these simple rules:
1. Any live cell with two or three live neighbors survives.
2. Any dead cell with three live neighbors becomes a live cell.
3. All other live cells die in the next generation, and all other dead cells remain dead.

## Contributing
Contributions to this project are welcome! If you have any ideas, suggestions, or bug reports, please submit an issue or a pull request on the GitHub repository.
