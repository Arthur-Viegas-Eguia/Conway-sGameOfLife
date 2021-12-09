# Conway's Game of Life
The program Emulates the ALife classic program Conway's Game of Life. The game has a rectangular board, each of the positions in it represent a cell which can be either populated or unpopulated. The goal of the game is to see the behaviour of the cells across generations. The rules of the game are the following:
- If a populated cell has two or three living neighbours it survives for the next generation
- If a poplated cell has less than two neighbours it dies, as if by underpopulation
- If a populated cell has more than three neighbours it dies, as if by overpopulation
- If an unpopulated cell has exactly three populated neighbours it becomes populated, as if by reproduction

## Features

- Decide the number of lines and columns of the board, via command line input
- Determine which cells are populated on generation 0
- Determine when you want to see the next generation of cells ingame
- Have the board printed to you at every generation

## Usage
To run the code after downloading symply type the following
    python ConwayGameOfLife.py numRows numCols file.txt
Where numRows and numCols are respectively the number of rows and columns on the board, and file is the link to an external file containing the populated cells of the game.
The file must have two integers separated by space 
