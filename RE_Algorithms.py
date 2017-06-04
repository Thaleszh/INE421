alphabet = set()
non_alphabet = set(['*', '.', '|', '?'])

def de_simone(re):
	#adding . to separate letters
	dotted = dot_placer(re)
	indexes = index_noncharacters(re)

	

# Returns the index of all the non alphabet symbols in the string, 
# ignoring the parenthesis
# The return is as the following:
# indexes = [indexes of |, indexes of ., indexes of *, indexes of ?]
def index_noncharacters(re):
	parenthesis = 0
	indexes_or = []
	indexes_and = []
	indexes_star = []
	indexes_maybe = []
	indexes = []

	for index, char in enumerate(re):
		if char == '(':
			parenthesis += 1
		elif char == ')':
			parenthesis -= 1
		elif parenthesis == 0 and char in non_alphabet:
			if char == '|':
				indexes_or.append(index)
			elif char == '.':
				indexes_and.append(index)
			elif char == '*':
				indexes_star.append(index)
			else:
				indexes_maybe.append(index)

	indexes.append(indexes_or)
	indexes.append(indexes_and)
	indexes.append(indexes_star)
	indexes.append(indexes_maybe)
	return indexes


#adds '.' to separate alphabet characters, adds characters to alphabet
def dot_placer(re):
	first = True
	new_re = ''
	alphabet.clear()

    for index, char in enumerate(re):
    	if char not in non_alphabet:
    		alphabet.add(char)
    		if first:
    			first = False
    		else:
    			# if char is ')', the dot isnt needed
    			if char != ')':
    				new_re += '.'
    				#if char is '(', there wont be a dot afterwards
	    			if char == '(':
	    				first = True
    	else:
    		first = True
    	new_re += char
    alphabet.remove('(')
    alphabet.remove(')')
    return new_re
