'''
- import random from the python library
- create an empty dictionary where users and ...
...their corresponding scores will be added at the end of the quiz
- create an empty list where all users scores only gets
added to allow calculation of the average score of all users at the end of the quiz
- define a function that will hold the dictionary with the questions, it's options and the right answers
'''
import random
user_score = {}
score_list = []


def question_dictionary():
    my_question_dictionary = {
        'Q. How many teeth does an adult individual have?\na. 40 \nb. 30 \nc. 32': 'c',
        'Q. How many teeth do children have? \na. 20 \nb. 30 \nc. 15': 'a',
        "Q. Children’s teeth are called milk teeth?\na. False \nb. True": 'b',
        'Q. The teeth doctor is called a Dentist;\na. True \nb. False': 'a',
        'Q. The dentist recommends that we brush twice daily.\na. True \nb. False': 'a',
        'Q. What is 16 + 32?\na. 52 \nb. 42 \nc. 48': 'c',
        'Q. How old is the Queen of England?\na.101 \nb. 95 \nc. 97': 'b',
        'Q. Which country in Africa was never colonised?\na. Kenya \nb. Ethiopia \nc. Ghana': 'b',
        'Q. What is a female cow called?\na. Heifer \nb. Doe \nc. Kid': 'a',
        'Q. Which is the largest city in the United kingdom? \na. London \nb. Manchester \nc. Birmingham': 'a',
    }
    shuffled_questions = list(my_question_dictionary.items())
    random.shuffle(shuffled_questions)
    return shuffled_questions


'''
- to use random function with a dictionary, you have to first convert the dictionary to a tuple 
and then the tuple to a list to randomly select questions 
- from the dictionary, call the random function of the converted dictionary
'''


'''
- def the function that plays the quiz and keeps a running score
- ask user for their name and convert their input into a string
- use a while loop to make sure user inputs rather than leave blank
- get questions from the dictionary function
- running the quiz questions using a for loop
- set user score to zero and increment in the for loop
- if the answer is correct, display correct
- increment score by 1 if correct
- if incorrect or wrong input, display incorrect
- display the right answer
- get final score out of total number of questions
- use the final score variable to calculate the percentage
- print the users name and score in a friendly message along the percentage
- add score of individual user to the empty list created
- add each users name and score to the empty dictionary created
'''


def play_my_quiz(n):
    name = str(input('What is your name? '))
    while name == "" or name == " ":
        name = str(input('What is your name? '))
    questions = question_dictionary()
    score = 0
    for question in questions[0:n]:
        print(question[0])
        answer = input('\n> ').lower()
        if answer == question[1]:
            print('Correct')
            score += 1
        else:
            print('Incorrect')
            print(f'The correct answer is {question[1]}')
    final_score = score / len(questions)
    percentage_score = format(final_score, '.1%')
    print(f'{name}, you scored {score} out of {len(questions)}: {percentage_score}')
    score_list.append(score)
    user_score[name] = score


'''
# define a function to display the welcome notes, the instructions,
# gives the user the option to choose number of questions, allows a repaet of the quiz for multiple user
# and calls the play quiz function
# call the play quiz function with the variable choice of questions as parameter
# ask user for the number of question user will like to answer
# handle user input error to ensure a digit is entered
# convert the dictionary with all user nd their score to a tuple and then a list to allow for sorting
'''


def main_menu():
    print('Hello, welcome to my quiz 😁\n')
    print('-----------------------------------------------')
    print('Please read the instructions carefully!!!')
    print(
        """1. This is a multiple choice where only one answer is correct\n
        2. Type the corresponding alphabets as your answer\n
        3. Not answering according to the instructions will make you lose marks\n

        Now that we are clear,\n
        Let's being!\n
        ---------------------------------------------"""
    )
    choice_questions = input(
        'How many questions will you like to answer out of 10? ')
    if (choice_questions.isdigit()) and (choice_questions != " " or ""):
        choice_questions = int(choice_questions)
        play_my_quiz(choice_questions)
    else:
        print('Invalid entry, Please try again and enter a number between 1 & 10')
        main_menu()
    repeat_quiz = input('Would anyone else like to take this quiz? yes/no\n>')
    if repeat_quiz.lower() == 'yes':
        main_menu()
    else:
        print('PLEASE VIEW ALL SCORES BELOW;')
        quit


main_menu()

sorted_user_score = list(user_score.items())


'''
# define another function to sort dictionary with user name and
# score such that the user with the highest score is displayed first
# followed by the other users in descending order of their scores
# returns sorted list based on the highest score
# to get the average score of all users, set total user score to zero
# use a for loop to iterate over the list of scores created earlier
# increment total user score by adding all the individual scores
# print out average
'''


def sorted_list_of_user_score(item):
    return item[1]


sorted_user_score.sort(key=sorted_list_of_user_score, reverse=True)
print(sorted_user_score)
total_user_score = 0
for score in score_list:
    total_user_score += score
average = total_user_score / len(score_list)
print(f'The average score for all players is {average}')
print('Thank you for taking my quiz today.\nGoodbye!')
