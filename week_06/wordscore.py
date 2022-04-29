'''
    File name: wordscore.py
    Author: Victor Ramirez
    Date created: 09/29/2021
    Date last modified: 10/02/2021
    Python Version: 3.8
'''

import itertools
import string

word_list = []
scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
          "x": 8, "z": 10}

def score_word(word, data):
    ''' function takes a word and data dict argument and returns a word score '''

    # loop by the length of the possible valid word lengths ie (2, 8-1):
    for word_length in range(2, 8):

        # find all the possible_words
        word_list = find_words(word, data, word_length)

    # score the valid words
    tuple_score = score_utility(word_list)       

    return tuple_score

def find_words(word_string, data, length):
    ''' takes a word string and data dict of words and finds all the permutations of valid words'''

    global word_list

    # use the Python lib to permutate all the words based on the string length entered
    for perm in itertools.permutations(word_string, length):

        # join chars to form words
        word = ''.join(perm)

        # check if the perm word is in the dict
        if word in data:  
            word_list.append(word)            
    
    # remove any duplicates
    word_list = list(set(word_list))

    return word_list

def score_utility(word_list):
    ''' takes a word list and returns a tuple of word , score '''
    
    total = 0
    points = []

    # loop the list of words
    for w in word_list:

        # set the word to the current word in the list
        word = w   
               
        # loop the score sheet to total the score
        for letter in word.lower():
            
            total += scores[letter]

        points.append(total)
        # reset total
        total = 0
    
    list_score_tuple = [(word_list[i], points[i]) for i in range(0, len(word_list))]

    # sort word alphabetically
    list_score_tuple = sorted(list_score_tuple, key = lambda x : x[0])

    # sort by score
    list_score_tuple = sorted(list_score_tuple, key = lambda x : x[1], reverse=True)

    print_tuples(list_score_tuple)

    return list_score_tuple

def print_tuples(tuple_list):
    ''' takes a list of tuples and prints the tuple list contents '''

    for x in tuple_list:

        print ( '(', x[1], ',', x[0], ')')

    print('Total number of words: ', len(tuple_list))

###############################################################################################

def wildcard_valid_word(user_input_word):
    ''' takes in user input and returns list of valid words from data '''

    with open("sowpods.txt","r") as infile:

        raw_input = infile.readlines()
        data = [datum.strip('\n') for datum in raw_input]

    words=[]

    # loop all the words in data
    for word in data:

        user_input_word_list = list(user_input_word)
        # When you use enumerate(), the function gives you back two loop variables:
        # The index of the current iteration
        # The lettere of the item at the current iteration
        for index, letter in enumerate(word):
            
            # check if the user input matches the letter in the current word
            if letter in user_input_word_list:

                # pop or remove letter
                user_input_word_list.remove(letter)

            else:

                # no match break out of inner loop move on to the next word
                break
            
            # check if a valid word length            
            if index == len(word) - 1:
                
                # valid word found append to list
                words.append(word)

    return words

def wildcard_score_utility(word):
    ''' takes a word argument and returns the score '''

    word_score = 0

    # loop each letter in word
    for letter in word:
        
        # score letter and keep running total of word score
        word_score += scores[letter.lower()]

    return word_score

def wildcard_print_utilty(score_list):
    ''' takes a list of tuples and prints the tuple list contents '''

    tuple_list = score_list
    
    # sort word alphabetically
    tuple_list = sorted(tuple_list, key = lambda x : x[1]) 

    # sort by score
    tuple_list = sorted(tuple_list, key = lambda x : x[0], reverse=True)
    
    # loop the tuples
    for word in tuple_list:

        print(word)
    
    # print the grand total
    print("Total number of words:",len(tuple_list))


def wildcards(input_word):
    '''To handle inputs with wildcard characters'''
    
    # list of valid word
    words = wildcard_valid_word(input_word.replace('?','').replace('*',''))
    
    # list of valid word scores
    words_scores = [(wildcard_score_utility(word),word.lower()) for word in words]

    # if a ? wildcard found    
    if '?' in input_word:

        # loop A-Z and replace the wildcard
        for letter in list(string.ascii_uppercase):

            # score the letters
            score_letter = wildcard_score_utility(letter)
            
            # generate a new word
            new_word = input_word.replace('?',letter)

            # if a * wildcard found            
            if '*' in input_word:
                
                # loop A-Z and replace the wildcard
                for next_letter in list(string.ascii_uppercase):
                    
                    # generate a new word
                    new_word = input_word.replace('?',letter).replace('*',next_letter)

                    # score the new word letters
                    score_next_letter = score_letter + wildcard_score_utility(next_letter)

                    # adjust word score based on wildcards used
                    word_set_list = [
                                        (wildcard_score_utility(word) - score_next_letter, word.lower())
                                        for word in wildcard_valid_word(new_word) 
                                        if word not in words
                                    ]

                    # append the new word
                    words.extend(wildcard_valid_word(new_word))
                    
                    # save set of words
                    words=list(set(words))

                    # append the the score 
                    words_scores.extend(word_set_list)

                    # print('new_word = ', new_word)
            else:
                # only one wildcard used
                # adjust word score based on wildcards used
                words_scores.extend([
                    (wildcard_score_utility(word) - score_letter,word.lower()) 
                    for word in wildcard_valid_word(new_word) 
                    if word not in words])

                # print('new_word = ', new_word)
                
                # append new word
                words.append(new_word)
        
        return words_scores
    
    # if a * wildcard found
    elif '*' in input_word:

        # loop A-Z and replace the wildcard
        for letter in list(string.ascii_uppercase):

            # score the letters
            score_letter = wildcard_score_utility(letter)
            
            # generate a new word
            new_word = input_word.replace('*',letter)
            
            # adjust word score based on wildcards used
            words_scores.extend
            ([
                (wildcard_score_utility(word)-score_letter,word.lower()) 
                for word in wildcard_valid_word(new_word) 
                if word not in words
            ])
        
        return words_scores
            