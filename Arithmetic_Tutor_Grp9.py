'''
arithmetic_tutor.py
-------------------
    python script that displays a menu and prompts user to select an arithmetic task (addition, subtraction, multiplication, division).
    Generates 2 random single digit numbers then prompts user for answer to arithmetic question.
    Provides feedback to user as to correctness
    provides count of tries and number of correct answers
    - another design option would be to have single function that accepts the operator as a parameter
-------------------------------------------------------------------------------------------------------------------------------------------
'''
import random

def ourmenu ():
#Display menu.  Validate choice
    Valid = ["1", "2", "3", "4", "5"]
    print (f"\tMain Menu\n1: Addition\n"
           "2: Subtraction\n"
           "3: Multiplication\n"
           "4: Division\n5: Exit\n")
    uchoice = input("Enter a choice (1-5): ") 
    if uchoice not in Valid:
        print (f"{uchoice} is not a valid selection!")
    return uchoice

def addition (num1, num2):
#    user chose addition 
    print (f"what is {num1} + {num2}? ", end='')
    answer = input ()
    if answer.isnumeric():
        if int(answer) == num1 + num2:
            print (f"*** Great Job *** {answer} is correct") 
            return 1
        else:
            print (f"You answered {answer}!\nSorry, {num1} + {num2} is {num1 + num2}\n ")
            return 0
    else: 
        print (f"{answer} isn't a number!")
        return 0
    
def division (num1, num2):
#   user chose division 
#   Use try / except to handle potential of string not being convertible to floating point 
    print (f"what is {num1} / {num2}? ", end='')
    answer = input ()
    try:
        answer = float(answer)
        if round(answer, 2)  == round((num1 / num2), 2):
            print (f"\tGreat Job!\t\t{num1} / {num2} is {answer}") 
            return 1
        else:
            print (f"You answered {answer}!\nOops, {num1} / {num2} is {num1 / num2}\n ")
            return 0
    except: 
        print (f"{answer} isn't a number!")
        return 0

def multiplication (num1, num2):
#    user chose multiplication
    print (f"what is {num1} * {num2}? ", end='')
    answer = input ()
    if answer.isnumeric():
        if int(answer) == num1 * num2:
            print (f"\tGreat Job! {answer} is correct\n") 
            return 1
        else:
            print (f"You answered {answer}!\tSorry, {num1} * {num2} is {num1 * num2}\n ")
            return 0
    else: 
        print (f"{answer} isn't a number!")
        return 0

def subtraction (num1, num2):
    ''' 
        User chose subtraction
        subtract num2 from num1
        can assume num1 is larger than num2
    '''
    print (f"what is {num1} - {num2}? ", end='')
    answer = input ()
    if answer.isnumeric():
        if int(answer) == num1 - num2:
            print (f"\tGreat Job! {num1} - {num2} is {answer} \n") 
            return 1
        else:
            print (f"You answered {answer}!\tSorry, {num1} - {num2} is {num1 - num2}\n ")
            return 0
    else: 
        print (f"{answer} isn't a number!")
        return 0

def get_nums ():
    ''' get 2 random single digit numbers and return the pair as a tuple'''
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    return (num1, num2)    


# Initialize variables 
uchoice = "0"
right_cnt = 0
tries = 0

#   Loop until user chooses to exit
while uchoice != "5":
    uchoice = ourmenu()
    tries += 1

#   get 2 random single digit integers    
    numbers = get_nums()

    if uchoice == "1":
        right_cnt += addition (numbers[0], numbers[1])
    elif uchoice == "2":
        while (numbers[1] > numbers[0]):
            numbers = get_nums()
        right_cnt += subtraction (numbers[0], numbers[1])
    elif uchoice == "3":
        right_cnt += multiplication (numbers[0], numbers[1])
    elif uchoice == "4":
        while (numbers[1] == 0):
            numbers = get_nums()
        right_cnt += division (numbers[0], numbers[1])

#   All done
#    Provide summary for user
#---------------------------------------
pct_correct = round((right_cnt / (tries-1)) * 100, 2)
print (f"You got {right_cnt} correct out of {tries-1} questions - {pct_correct}%")
       

