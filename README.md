# Wordle Solver - Greedy Algorithm
This repository is a solver for the online game "Wordle", which became popular in late 2021. A greedy algorithm is used to determine the best next word after each guess, by minimizing the worst case remaining possibilities, that is, maximizing the number of words that have already been ruled out. The word lists were taken as a snapshot during Autumn 2021 from "Wordle's" website source code, therefore are not necessarily current.

## Wordle solver run instructions

1. Execute `solver.py`, the terminal will output the first word to enter into Wordle
2. Enter Wordle's response to the terminal as follows:
    - 0 - gray (mistake), 1 - yellow (wrong placement), 2 - green (correct). 
    - For example, if the true word is 'LABEL' and you entered 'WALES'
        - Wordle will show: grey, green, yellow, green, grey
        - You should write in the terminal: 02120
3. The terminal will then output the next word to guess in Wordle and so on until the solution is found or 6 guesses are used as per the game trules

Good luck!

