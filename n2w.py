# The following program takes a single integer as an argument, and returns it as
# as string of grammatically correct English words.

# Dictionaries
dict_one = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
    5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
    10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
    14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
    18: "eighteen", 19: "nineteen"}
dict_two = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty",
    6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
dict_three = {1: "thousand", 2: "million", 3: "billion", 4: "trillion",
    5: "quadrillion", 6: "quintillion", 7: "sextillion", 8: "septillion",
    9: "octillion", 10: "nonillion", 11: "decillion", 12: "undecillion",
    13: "duodecillion", 14: "tredecillion", 15: "quattrodecillion",
    16: "quindecillion", 17: "sexdecillion", 18: "septendecillion",
    19: "octodecillion", 20: "novemdecillion", 21: "vigintillion"}

# Helper Functions 

# Helper function used for 0th, 3rd, 6th, etc. digits.
# Used if i % 3 == 0 in master function loop.
# Sets old_answer to answer, goes through rules to update answer (or not),
# checks to see if answer is updated, & returns updated answer or 'skip'.
def n2w_dig0(n,i,answer):
    old_answer = answer
    if answer != '':
        if int(n[-i-1]) != 0:
            if int(n[-i-2] + n[-i-1]) >= 20 or int(n[-i-2] + n[-i-1]) < 10:
                answer += dict_one[int(n[-i-1])]
    else:
        answer += dict_one[int(n[-i-1])]
    if i != 0:
        if len(n[:-i]) >= 3:
            if int(n[-i-3:-i]) != 0:
                answer += " " + dict_three[(i/3)]
                if int(n[-i:]) != 0:
                    answer += " "
        elif len(n[:-i]) == 2:
            if int(n[-i-2:-i]) != 0:
                answer += " " + dict_three[(i/3)]
                if int(n[-i:]) != 0:
                    answer += " "
        elif len(n[:-i]) == 1:
            if int(n[-i-1:-i]) != 0:
                answer += " " + dict_three[(i/3)]
                if int(n[-i:]) != 0:
                    answer += " "
    if answer != old_answer:
        return answer
    else:
        return 'skip'

# Helper function used for 1st, 4th, 7th, etc. digits.
# Used if i % 3 == 2 in master function.
# Sets old_answer to answer, goes through rules to update answer (or not),
# checks to see if answer is updated, & returns updated answer or 'skip'.
def n2w_dig1(n,i,answer):
    old_answer = answer
    if int(n[-i-1] + n[-i]) >= 20:
        answer += dict_two[int(n[-i-1])]
    if int(n[-i-1] + n[-i]) >= 20 and int(n[-i]) != 0:
        answer += "-"
    elif int(n[-i-1] + n[-i]) < 20 and int(n[-i-1] + n[-i]) >= 10:   
        answer += dict_one[int(n[-i-1] + n[-i])]
    if answer != old_answer:
        return answer
    else:
        return 'skip'

# Helper function used for 2nd, 5th, 8th, etc. digits.
# Used if i % 3 == 1 in master function.
def n2w_dig2(n,i,answer):
    old_answer = answer
    if int(n[-i-1]) != 0:
        answer += dict_one[int(n[-i-1])]
        answer += " hundred"
        if int(n[-i] + n[-i+1]) != 0:
            answer += " "
    if answer != old_answer:
        return answer
    else:
        return 'skip'

#### Master Function ####

# Master function iterates through length of argument n and uses  3 helper
# functions to initiate and build string of grammatically correct words that
# represent integer N in plain English.
def num2words(n):
	if isinstance(n, int) == True:
	    answer = ''
	    n = str(n)  
	    updated_answer = 'skip'
	    for i in reversed(range(0, len(n))):
	        if i % 3 == 0:
	            updated_answer = n2w_dig0(n,i,answer)
	            if updated_answer != 'skip':
	                answer = updated_answer
	        if i % 3 == 1:
	            updated_answer = n2w_dig1(n,i,answer)
	            if updated_answer != 'skip':
	                answer = updated_answer
	        if i % 3 == 2:
	            updated_answer = n2w_dig2(n,i,answer)
	            if updated_answer != 'skip':
	                answer = updated_answer    
	    return answer
	else:
		raise ValueError("Argument must be an integer.")