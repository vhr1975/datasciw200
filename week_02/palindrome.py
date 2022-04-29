'''
    File name: palindrome.py
    Author: Victor Ramirez
    Date created: 09/05/2021
    Date last modified: 09/05/2021
    Python Version: 3.8
'''

'''
    ### 2-5. Palindrome (20 points)

    Write a script that prompts the user for a name (this input will be a **1 word string**). 
    Using a while loop that counts downwards, print the letters of the name reversed 
    (hint: you can use print(var, end='') in each iteration of the loop). You cannot use the 
    'reverse' function or the string slicing [::-1] method for this problem! You should 
    use s.lower() and s.upper(), as appropriate, to change the string to lowercase and print 
    it out with only the first letter of the reversed word in uppercase. If the name is the 
    same forward and backwards, print "Palindrome!" on the next line. Make sure your code prints 
    the sample examples exactly as shown below.

    Hint: You can use string concatenation in place of the reverse or string slicing [::-1] 
    methods.

    Examples:
    ```
    Enter your name: Paul
    Luap

    Enter your name: ANA
    Ana
    Palindrome!
    ```

    Save your script as: palindrome.py
'''
############################################################################################
# custom function to reverse the name var passed into the function
def reverseName(name):
    length = len(name)
    reversename = ''
    
    # while loop to display the string in reverse order    
    while(length >= 1):
        reversename += name[length - 1]
        length -= 1
           
    print(reversename.capitalize())

############################################################################################
# custom function to check if the name var passed into the function is a palindrome
def isPalindrome(name):
    bFlag = True         
    first_char = 0
    last_char = len(name) - 1
    
    # while loop to check if a palindrome
    while(first_char < last_char and bFlag == True):
        if (name[first_char] == name[last_char]):
            first_char += 1
            last_char -= 1
        else:
            bFlag = False
            break
    
    if (bFlag == True):
        print('Palindrome!')    
            
############################################################################################

# save user input
user_input = input("Enter your name: ")

reverseName(user_input.lower())
isPalindrome(user_input.lower())
