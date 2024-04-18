import random

address = "Hello Everyone, Welcome to the annual national quiz competition. in this years event, there are twenty questions in total to win a prize."
print(address.upper())

print()#this empty print is to create a space in the output

address2 = "Each question has a score of one and the sum of all questions would be percentiled. So good luck!"

print(address2.upper())

print()

print("OPTIONS: You can choose any number of questions to answer.")

print("HINT: Use numbers for questions that have the option")

print()#this empty print is to create a space in the output

questions = {"What is the capital of England? ": "london",
        "Water is drinkable, true or false?: ": "true",
        "What is the biggest mammal: ": "whale",
        "The earth is spherical, yes or no: ": "yes",
        "Where can the Sphinx be found?: ": "egypt",
        "Which month of the year has the lowest day?: ": "february",
        "Which city has the tallest building?: ": "dubai",
        "What sweet substance comes from bees?: ": "honey",
        "Where was the 2022 World Cup played?: ": "qatar",
        "Romeo and Juliet was written by Shakespeare, true or false ": "true",
        "Which organ in the human body pumps blood, lungs or heart?: ": "heart",
        "Which animal is considered as mans best friend?: ": "dog",
        "Water is made up of Hydrogen and Oxygen, true of false?: ": "true",
        "What language does Computer understand, binary or english?: ": "binary",
        "All birds fly; true or false?: ": "false",
        "Do Electric vehicles emit zero carbon; yes or no?: ": "yes",
        "Which language was spoken by ancient Romans, Latin, Greek or Italian?: ": "latin",
        "How many days make a week, 7 or 8?: ": "7",
        "How many legs does an elephant have, 4 or 6?: ": "4",
        "How many continents do we have, 6 or 7?: ": "7"
        }

quiz = list(questions.items())#converting the dictionary to list for randomization and flexibility of the quiz questions

user_data = {} #this empty dictionary collects and stores user data i.e name and score


def number_question(): #additional feature

    question_list = []#this empty list holds the randomized number of questions to ask the user
    number_of_questions = int(input("How many questions do you want to answer(Choose between 2 and 20): "))#this collects the number of questions each user wishes to answer
    if number_of_questions < 2 or number_of_questions <= 0 or number_of_questions > 20:
        print("Please choose a number between 2 and 20")
        number_of_questions = int(input("How many questions do you want to answer(Choose between 2 and 20): "))
    else:
        pass
        
    for i in range(0, number_of_questions):#the for loop selects only the selected number of questions to ask the user
        questions = random.randint(0,len(quiz)-1)#this functionality randomizes the questions and the minus 1 eliminates repetition of a  question
        while questions in question_list:
            questions = random.randint(0,len(quiz)-1)
        question_list.append(questions)#this appends the randomized questions to the empty list created as question_list

    return question_list

def quiz_statements():
    
    score = 0
    user_name = input("Type in your name: ")

    while True:
        if user_name == "":
            print("Wrong input")
            user_name = input("Please type in your name: ")
        else:
            break
    
    question_list = number_question()
    print(question_list)
    for i in question_list: #this for loop runs through the number of questions selected ramdomly, gives a score of 1 if the response is the same a the question value
        print(quiz[i][0])
        response = input("Type in your answer: ")
        if (response.lower()).strip() == quiz[i][1].lower(): #the lower() method converts the users cases to lower case letters and strip() removes white space errors
            score += 1
            print("Correct")
        else:
            print("Sorry, that was wrong. The correct answer is ",quiz[i][1])

    print()

    def new_user():
        print("Does anyone want to take the quiz?")
        try_again = input("Type in yes or no: ").lower()
        print()
        while True: #this while loop runs through the program again for a new user if the "ans" is "yes"
            ans = "yes"
            if (try_again.lower()).strip() == ans: 
                quiz_statements()
                try_again += (f"ans - ans")
            else:
               break

    new_user()

    user_data[user_name] = score # stores each username and score 

    print()
    
    def grade():
        percentage = int((score/len(question_list)) * 100)
        print("Hi",user_name, "thanks, your final score is", score)
        print(f"You scored {percentage}% of 100%")

    grade()
    
    print()
     

quiz_statements()


average_score = float(sum(user_data.values()) / len(user_data)) # the float ensures a pinpoint accuracy

highest_score = max(user_data.values())
#print(highest_score)this option was commented out to avoid excessive code printing

#the code below will give out all names and score of the highest scorers in the quiz 
highest_scorer_name = [key for key, value in user_data.items() if value == max(user_data.values())] # this code allocates the highest score to the highest scorer or scorers in the quiz
#print(highest_scorer_name) this option was commented out to avoid excessive code printing

print(highest_scorer_name, "scored", highest_score, "which is the highest score")

print()

print("Overall, the average score in the quiz is", average_score)

print()
    
print(user_data)

print()

print("Thats all, Thank you.")






