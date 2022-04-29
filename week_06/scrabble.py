'''
    File name: scrabble.py
    Author: Victor Ramirez
    Date created: 09/29/2021
    Date last modified: 09/30/2021
    Python Version: 3.8
'''

import sys
import wordscore
import re

def check_for_numbers(input):
    ''' takes a string and returns true if string contains a digit '''

    for character in input:

        if character.isdigit():

            return True

    return False

print('Number of arguments:', len(sys.argv), 'arguments.')
# print('Argument List:', str(sys.argv))
# print('Argument[0]', sys.argv[0])
# print('Argument[1]', sys.argv[1])

# open file in a dict 
with open("sowpods.txt","r") as dict_file:

    # raw_input = infile.readlines()
    data = {datum.strip('\n') for datum in dict_file}

# test cases: ZAEFIEE
# word = 'ZAEFIEE'
# word = 'ZAEFI?E'        
# word = '?F'
# word = '*F'
# word = '*?F'
word = sys.argv[1]

# check all the possible errors with the user input
# - Allow anywhere from 2-7 character tiles (letters A-Z) to be inputted. 
# - Do not restrict the number of same tiles (e.g., a user is allowed to input ZZZZZQQ).
# - You need to handle input errors from the user and suggest what that error might be 
#   caused by and how to fix it (i.e., a helpful error message)
# - There can be a total of **only** two wild cards in any user input (that is, one of 
#   each character: one `*` and one `?`). 

rack_lenght = len(word)
wildcard_a_count = word.count('*') 
wildcard_q_count = word.count('?') 

# input error checking
if rack_lenght < 2:

    print('please enter a word more then 2 characters')

elif rack_lenght > 7:

    print('please enter a word less then 7 characters')

elif check_for_numbers(word):

    print('please do not enter any numbers')

elif wildcard_a_count >= 2:

    print('please only enter one wildcard (*) sterisk')

elif wildcard_q_count >= 2:

    print('please only enter one wildcard (?) question mark')

# check to see if input contins a wildcard
elif re.match(r'^[\?\*A-Z]*$', word):

    if re.match('[A-Z]*[\?\*]+[A-Z]*',word):

        wildcard_list = wordscore.wildcards(word)
        wordscore.wildcard_print_utilty(wildcard_list)

    # else no wildcards
    else:

        wordscore.score_word(word, data)
