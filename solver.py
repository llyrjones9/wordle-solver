# Standard library imports
from importlib import import_module

# Toggle between Welsh and English Version
selected_version = 'cymraeg'
if selected_version == 'cymraeg':
	initial_guess = 'buwch'
elif selected_version == 'english':
	initial_guess = 'cough'

# Import the modules containing guessable words and eligible solutions lists
eligible_guesses_list = import_module(f'{selected_version}.eligible_guesses_list')
eligible_solutions_list = import_module(f'{selected_version}.eligible_solutions_list')

# Extract lists from relevant modules
eligible_guesses = eligible_guesses_list.eligible_guesses
potential_solutions = eligible_solutions_list.potential_solutions

# Loop through for up to 6 guesses
for attempt in range(6):
    
    # Set initial worst case remaining words
	remaining_words_wc = len(potential_solutions)
    
    # Set a list of eligible guesses
	candidate_guesses = eligible_guesses
    
    # Choose first guess
	if attempt == 0:
		candidate_guesses = [initial_guess]

    # Cycle through eligible guesses
	for candidate_guess in candidate_guesses:
        # List of patterns and solutions that would yield
        # that pattern for a candidate guess
		pattern_dict = {}
        
		# Cycle through potential solutions
		for potential_solution in potential_solutions:

			# Copy potential solution to temporary variable
			temp_ps = potential_solution
			# Initiate match code to all zeros
			match_code = [0] * 5
            
			# Check if each letter is in the right place
			for char_idx in range(5):
				if candidate_guess[char_idx] == temp_ps[char_idx]:
					# Change '0' to '2'
					match_code[char_idx] = 2
					# Add a '*' to the string
					temp_ps = temp_ps[:char_idx] + '*' + temp_ps[char_idx+1:]
                    
			# Check if unmatched letters are in the solution at all
			for char_idx in range(5):
            	# Check if letter is in the word at all
				if candidate_guess[char_idx] in temp_ps and match_code[char_idx] == 0:
					# Change '0' to '1'
					match_code[char_idx] = 1
                    
            # Add pattern to the matrix of possible patterns
            # This happens if that pattern is absent
			if tuple(match_code) not in pattern_dict:
				pattern_dict[tuple(match_code)] = [potential_solution]
                
            # This happens if that pattern is already present
			else:
				pattern_dict[tuple(match_code)].append(potential_solution)

        # Find the most popular pattern for that word
		N = max([len(val) for val in pattern_dict.values()])
        
        # If the worst case scenario for a given word is less than the worst
        # case scenario for the current word, change the word.        
		if N < remaining_words_wc:            
            # Update the proposed guess
			chosen_word = candidate_guess  
            # Save the pattern dictonary for the proposed guess
			chosen_pattern_dict = pattern_dict
                      
            # Update the worst case scenario we are trying to beat
			remaining_words_wc = N        
            
    # Propose the next guess to the user
	print(f'\n\nThe next guess is {chosen_word.upper()}\n')
    
    # Ask for the result of that guess
	inp = input('Please enter the Wordle response.\n')
	feedback = tuple(map(int, inp))

	# Trivial response for first user feedback of '22222'
	if feedback == tuple([2]*5):
		print(f'Hole in one! The solution was {initial_guess}.')
		break
    
    # Trim the list of potential solutions by selecting the appropriate
    # list from the pattern dictionary
	potential_solutions = chosen_pattern_dict[feedback]
    
    # If only one word remains, it's the solution
	if len(potential_solutions) == 1:
		print(f'\n\nFinished.\nThe solution is {potential_solutions[0].upper()}')
		break