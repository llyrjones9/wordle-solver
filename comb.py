# Import the guessable words list
egl = open("eligible_guesses_list.txt", "r")
esl = open("eligible_solutions_list.txt", "r")
eligible_guesses = egl.readlines()
potential_solutions = esl.readlines()

# Loop through for up to 6 guesses
for attempt in range(6):
    
    # Set initial worst case remaining words
	remaining_words_wc = len(potential_solutions)
	srmat = {}
    
    # Set a list of eligible guesses
	candidate_guesses = eligible_guesses
    
    # Choose 'snare' as first guess
	if attempt == 0:
		candidate_guesses = ["snare"]

    # Cycle through eligible guesses
	for candidate_guess in candidate_guesses:
		mat = {}
		rmat = {}
        
		for potential_solution in potential_solutions:
			tw2 = potential_solution
			match_code = [0] * 5
            
            # Check if letter is in the right place
			for c_ind in range(5):
				if candidate_guess[c_ind] == tw2[c_ind]:
					match_code[c_ind] = 2
					tw2 = tw2[:c_ind] + "*" + tw2[c_ind+1:]
                    
            # Check if letter is in the word at all
			for c_ind in range(5):
				if candidate_guess[c_ind] in tw2 and match_code[c_ind] == 0:
					match_code[c_ind] = 1
					ind_app = tw2.find(candidate_guess[c_ind])
					tw2 = tw2[:ind_app] + "*" + tw2[ind_app+1:]
                    
            # Add pattern to the matrix of possible patterns
            
            # This happens if that pattern is absent
			if tuple(match_code) not in rmat:
				rmat[tuple(match_code)] = [potential_solution]
                
            # This happens if that pattern is already present
			else:
				rmat[tuple(match_code)].append(potential_solution)
                
            # Lists every pattern between snare and each word
			mat[tuple([candidate_guess, potential_solution])] = match_code

        # Find the most popular pattern for that word
		M = max([len(val) for val in rmat.values()])
        
        # If the worst case scenario for a given word is less than the worst
        # case scenario for the current word, change the word.        
		if M < remaining_words_wc:
			remaining_words_wc = M
			chosen_word = candidate_guess
			srmat = rmat
		
	print(chosen_word)
	inp = input()
	feedback = tuple([int(el) for el in inp.split(",")])
	potential_solutions = srmat[feedback]
    
    # If only one word remains, it's the solution
	if len(potential_solutions) == 1:
		print("Done. Final word is {}".format(potential_solutions[0]))
		exit(0)

print("Failed. Did not find word after 6 attempts")

