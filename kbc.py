from questions import QUESTIONS


def isAnswerCorrect(question, answer):

    '''
    :param question: question (Type JSON)
    :param answer:   user's choice for the answer (Type INT)
    :return:
        True if the answer is correct
        False if the answer is incorrect
    '''
    
    return True if question["answer"] == answer  else  False      #remove this


def lifeLine(ques):

    '''
    :param ques: The question for which the lifeline is asked for. (Type JSON)
    :return: delete the key for two incorrect options and return the new ques value. (Type JSON)
    '''
    
    if(ques["answer"]==1):
        del ques["option2"]
        del ques["option3"]
        print( "option 1 : " + ques["option1"])
        print("option 4 : " + ques["option4"])
    elif(ques["answer"]==4):
        del ques["option2"]
        del ques["option3"]
        print( "option 1 : " + ques["option1"])
        print("option 4 : " + ques["option4"])
    elif(ques["answer"]==2):
        del ques["option1"]
        del ques["option3"]
        print( "option 2 : " + ques["option2"])
        print("option 4 : " + ques["option4"])
    elif(ques["answer"]==3):
        del ques["option2"]
        del ques["option4"]
        print( "option 3 : " + ques["option3"])
        print("option 4 : " + ques["option4"])        
    
def kbc():
    '''
        Rules to play KBC:
        * The user will have 15 rounds
        * In each round, user will get a question
        * For each question, there are 4 choices out of which ONLY one is correct.
        * Prompt the user for input of Correct Option number and give feedback about right or wrong.
        * Each correct answer get the user money corresponding to the question and displays the next question.
        * If the user is:
            1. below questions number 5, then the minimum amount rewarded is Rs. 0 (zero)
            2. As he correctly answers question number 5, the minimum reward becomes Rs. 10,000 (First level)
            3. As he correctly answers question number 11, the minimum reward becomes Rs. 3,20,000 (Second Level)
        * If the answer is wrong, then the user will return with the minimum reward.
        * If the user inputs "lifeline" (case insensitive) as input, then hide two incorrect options and
            prompt again for the input of answer.
        * NOTE:
            50-50 lifeline can be used ONLY ONCE.
            There is no option of lifeline for the last question( ques no. 15 ), even if the user has not used it before.
        * If the user inputs "quit" (case insensitive) as input, then user returns with the amount he has won until now,2
            instead of the minimum amount.
    '''
    flag=0
    #  Display a welcome message only once to the user at the start of the game.
    #  For each question, display the prize won until now and available life line.
    # For now, the below code works for only one question without LIFE-LINE and QUIT checks
    for x in range(15):
        print(f'\tQuestion %d : {QUESTIONS[x]["name"]}' % (x+1) )
        print(f'\t\tOptions:')
        print(f'\t\t\tOption 1: {QUESTIONS[x]["option1"]}')
        print(f'\t\t\tOption 2: {QUESTIONS[x]["option2"]}')
        print(f'\t\t\tOption 3: {QUESTIONS[x]["option3"]}')
        print(f'\t\t\tOption 4: {QUESTIONS[x]["option4"]}')
        if (x!=0):
            stop =input("Do you want to quit : ")
            if(stop == "quit"):
                print(f'your reward money {QUESTIONS[x-1]["money"]}')
                break

        if flag ==0 and x!=14:
            choice = input("Do you want to use lifeline : ")
            if (choice == "yes"):
                flag=flag+1
                lifeLine(QUESTIONS[x])
        # check for the input validations2
        
        ans = input('Your choice ( 1-4 ) : ')
        if isAnswerCorrect(QUESTIONS[x], int(ans) ):
            # print the total money won.
            # See if the user has crossed a level, print that if yes
            print('\nCorrect !')
            if ((x+1)<=4):
                print(f'your reward is {QUESTIONS[x]["money"]}')
            elif ((x+1)==5)
                print("Amount Rewarded is 10,000")
                print("you completed first level")
            elif((x+1)<=9):
                print(f'your reward is {QUESTIONS[x]["money"]}')
            elif((x+1)==10):
                print("Amount Rewarded is 3,20,000")
                print("you completed second level")
            else:
                print(f'your reward is {QUESTIONS[x]["money"]}')

        else:
        # end the game now.
        # also print the correct answer
            print('\nIncorrect !')
            print(f'correct answer is option {QUESTIONS[x]["answer"]}' )
            if(x<5):
                print("your reward is zero")
            elif(x<9):
                print("your reward is 10,000")
            else:
                print(f'your reward is {QUESTIONS[x]["money"]}')

            break
        # print the total money won in the end.


kbc()
