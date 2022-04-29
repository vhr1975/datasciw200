'''
    File name: tip.py
    Author: Victor Ramirez
    Date created: 09/03/2021
    Date last modified: 09/05/2021
    Python Version: 3.8
'''

'''
    ### 2-1. Tip Calculator (20 points)

    Below, you can see the script we wrote to compute the tip for a meal.  
    Fix it so that it works correctly. Expect the input to be a **number.** 
    Please format the output to 2 decimal places. 

    Save your script as the file: tip.py.

    Example Grading Rubric:
    - 10 points: fixing the crash so the program works with numbers (for example: 10 or 4.99)
    - 5 points: formatting the output correctly to 2 decimal places
    - 5 points: naming the file correctly (tip.py)
'''
# save user input
user_input = input("Enter the price of a meal: ")
# enhancement TODO add user input validation

price = float(user_input)
tip = price * 0.16
total = price + tip

# format the amounts to two decinal places
format_total = "{:.2f}".format(total)
format_tip = "{:.2f}".format(tip)

print("A 16% tip would be:", format_tip)
print("The total including tip would be:", format_total)
