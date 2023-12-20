import json
from tabulate import tabulate
import os

# for the visual purposes (cleans the console)
def clear():
    os.system("cls" if os.name == "nt" else "clear")


UserAuth: [int, str] = []
done: int = 0
clear()
print("------------------------------")
print(
    "         Howdy! Good day, isn't it? :D  "
    + "Commands List: \n\nLogin: login / 1 / li\nSign Up: signup / 2 / su"
)
while 1:
    userInput = input().lower()
    if userInput == "exit":
        print("✅ Exiting...")
        clear()
        exit()
    if userInput == "login" or userInput == "1" or userInput == "li":
        print("Enter your info to proceed!")
        UserID = input("User ID: ")
        password = input("Password: ")
        clear()
        with open("res/accounts.txt", "r") as file:
            array = json.load(file)
        for item in array:
            if item[0] == UserID and item[1] == password:
                UserAuth = item
                done = 1
                break
        if done == 1:
            break
        else:
            print(
                '❌ Invalid Creditentials\nType "login" to try again! or "signup" to create an account'
            )
    elif userInput == "signup" or userInput == "su" or userInput == "2":
        print("Enter your info to proceed!")
        UserID = input("User ID: ")
        password = input("Password: ")
        email = input("Email: ")
        name = input("Name: ")
        with open("res/accounts.txt", "r") as file:
            array = json.load(file)
        with open("res/accounts.txt", "w") as file:
            json.dump([[UserID, password, email, name, 0]] + array, file)
        clear()
        print('✅ You may now login with your info.\nType "login"')
    else:
        print(
            "❌ Invalid Input, avalaible commands are:\n\nLogin: login / 1 / li\nSign Up: signup / 2 / su"
        )
########################################################
if UserAuth[-1] == 1:
    print(
        "Welcome back, Dr."
        + item[-2]
        + "\n\navalaible commands are:\n\nGrade Quizzes: NOT DONE YET\nList Students: list / 2\nManage Quizzes: quizzes / 3 / manage"
    )
    while 1:
        userInput = input().lower()
        if userInput == "exit":
            exit()
        if userInput == "1":
            print("Beta?")
        ### CREATE THE QUIZ ANSWERED OR NOT FOR EACH STUDENT IN THE MENU OR PROVIDE A CUSTOM MENU
        elif userInput == "2" or userInput == "list":
            with open("res/accounts.txt", "r") as file:
                array = json.load(file)
            for x in array:
                if x[-1] == 1:
                    array.remove(x)
                else:
                    x.pop(1)
                    x.pop(1)
                    x.pop(-1)
            print(tabulate(array, headers=["Student ID", "Name"]))
        elif userInput == "3" or userInput == "manage" or userInput == "quizzes":
            clear()
            print(
                "Avalaible commands are:\n\nCreate a Quiz: 1 / create\nDelete a Quiz: 2 / delete"
            )
            userInput = input()
            if userInput == "exit":
                exit()
            if userInput == "1" or userInput == "create":
                QuestionsData = []
                QuizTitle = input("Quiz Title: ")
                QuizID = input("Enter Quiz ID: ")
                # remmeber to add the random function for the ID
                quesNumbers = int(input("Enter Question Numbers: "))
                for i in range(quesNumbers):
                    questionid = i + 1
                    question = input("Enter Your Question: ")
                    answers: [str] = []
                    for y in range(4):
                        answer = input("Enter Answer No." + str(y + 1) + ": ")
                        answers.append(answer)
                    QuestionsData.append([questionid, question, answers])
                    print("----------------")

                arr = [QuizID, QuizTitle, quesNumbers] + QuestionsData
                with open("res/questions.txt", "r") as file:
                    array: [str] = json.load(file)
                with open("res/questions.txt", "w") as file:
                    json.dump([arr] + array, file)
                clear()
                print("✅ Successfully created your quiz with the ID of " + str(QuizID))
            elif userInput == "2" or userInput == "delete":
                quizID = input("Enter the quiz ID: ")
                with open("res/questions.txt", "r") as file:
                    array = json.load(file)
                for x in array:
                    if x[0] == quizID:
                        array.remove(x)
                        with open("res/questions.txt", "w") as file:
                            json.dump(array, file)
                        print('Deleted "' + str(QuizTitle) + '"')
                        break
                    else:
                        print("❌ Invalid ID, try double checking")
                else:
                    print(
                        "❌ Enter a valid option\n\nAvalaible commands are:\n\nCreate a Quiz: 1 / create\nDelete a Quiz: 2 / delete"
                    )

        else:
            print(
                "❌ Invalid Command\n\navalaible commands are:\n\nGrade Quizzes: NOT DONE YET\nList Students: list / 2\nManage Quizzes: quizzes / 3 / manage"
            )
else:
    print(
        "Welcome back, "
        + item[-2]
        + "\n\navalaible commands are:\n\nAnswer Quizzes: answer [QUIZ_ID]\nList Quizzes: list / 1"
    )
    while 1:
        userInput = input()
        if userInput == "exit":
            exit()
        if "answer" in userInput:
            clear()
            if len(userInput.split()) < 2:
                quizID = input("Enter your quiz ID: ")
            else:
                quizID = userInput.split()[1]
            with open("res/questions.txt", "r") as file:
                data = json.load(file)
            for item in data:
                if item[0] == quizID:
                    data.clear()
                    data.extend(item)
                    break
            if not (data[0] == quizID):
                print("❌ Quiz not found, Double check the ID!")
                continue
            with open("res/answers.txt", "r") as fileRead:
                IndexedData = json.load(fileRead)
            solved: int = 0
            for answer in IndexedData:
                if answer[0] == quizID and answer[-2][0] == UserAuth[0]:
                    solved = 1
                    break
            if solved == 1:
                print("⚠️ You've already answered this quiz")
                continue
            finalData = [data[0], data[1], data[2]]
            print(
                "-------------------------⚠️ Solving Quiz ⚠️---------------"
                + "\n"
                + "Quiz Title: "
                + data[1]
                + "\n"
                + "Quiz ID: "
                + str(data[0])
                + "\n"
                + "Total Questions: "
                + str(data[2])
            )
            print(
                "-------------------------------------------------------------------------"
            )
            for x in range(3):
                data.pop(0)
            for item in data:
                print(
                    str(item[0])
                    + ") "
                    + item[1]
                    + "\n1- "
                    + item[2][0]
                    + "    2- "
                    + item[2][1]
                    + "\n3- "
                    + item[2][2]
                    + "    4- "
                    + item[2][3]
                    + "\n--------\n"
                )
                answer = input("Your answer (1/2/3/4): ")
                clear()
                finalData.append([item[0], item[1], item[2][int(answer) - 1]])
            with open("res/answers.txt", "r") as file:
                oldArray = json.load(file)
            finalData.append(UserAuth)
            finalData.append(-1)
            with open("res/answers.txt", "w") as file:
                json.dump([finalData] + oldArray, file)
            print("✅ Answers sent to your professor, please wait for the grades!")
        elif userInput == "1" or userInput == "list":
            clear()
            print("-----------------------------------------------")
            with open("res/questions.txt", "r") as file:
                array: [str] = json.load(file)
            with open("res/answers.txt", "r") as file:
                IndexedAnswers = json.load(file)
            for x in array:
                for y in range(len(x) - 2):
                    x.pop()
                for answer in IndexedAnswers:
                    if answer[0] == x[0] and answer[-2][0] == UserAuth[0]:
                        x.append("✅")
                        if answer[-1] == -1:
                            x.append("Grading...")
                        else:
                            x.append(answer[-1])

            print(
                tabulate(array, headers=["Quiz ID", "Quiz Title", "Answered", "Grade"])
            )
            print("-----------------------------------------------")
            print('HINT: To answer a quiz, type "answer [QUIZ_ID]"')
        else:
            print(
                "❌ Invalid Command\n\navalaible commands are:\n\nAnswer Quizzes: answer [QUIZ_ID]\nList Quizzes: list / 1"
            )
