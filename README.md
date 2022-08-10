This repositary is a solver for the online game "Wordle", which became popular in late 2021. A greedy algorithm is used to determine the best next word after each guess, by minimising the worst case remaining possibilities, that is, maximising the number of words that have already been ruled out. The word lists were taken as a snapshot during Autumn 2021 from "Wordle" website's source code, therefore are not nessesarily current.

Wordle solver run instruction:

The script outputs the first word to enter into wordle.
It then waits for the output. Please enter the output as 5 digits 
separated by commas, where 0 - gray (mistake), 1 - yellow (wrong placement),
2 - green (correct). 
For example, if the true word is 'LABEL' and you entered 'WALES', 
wordle will show:
grey, green, yellow, green, grey

and you should write in the terminal:
02120

The script will then output the next word to give to wordle and so on.

Good luck!

