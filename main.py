# I can edit files right here inside the terminal right away :D
import json
from tabulate import tabulate
import os

# for visual purposes (cleans the console)
def clear():
    os.system("cls" if os.name == "nt" else "clear")


# Reads the file content
def fetchFile(filePath):
    Data = open(filePath, "r")
    return json.load(Data)

# Edits the file content
def modifyFile(filePath, newData):
    Data = open(filePath, "w")
    json.dump(newData, Data)


# Output data in table format
def tableOutput(Data, Headers):
    print(tabulate(Data, headers=Headers, tablefmt="grid"))


# These are essential vars, UserAuth holds the logged in info
UserAuth = []

clear()
print("------------------------------")
print(
    "         Howdy! Good day, isn't it? :D  "
    + "\nYou can exit the program anytime with ctrl + c or ctrl + z\n"
    + "Commands List: \n\nLogin: login / 1 / li\nSign Up: signup / 2 / su"
)

#################### Login Section
while 1:
    userInput = input().lower()

    if userInput == "login" or userInput == "1" or userInput == "li":

        clear()
        print("---------Enter your account info to proceed--------")
        UserID = input("User ID: ")
        password = input("Password: ")
        clear()
        data = fetchFile("res/accounts.txt")
        for item in data:
            if item[0] == UserID and item[1] == password:
                UserAuth = item
                break
        else:
            print(
                '❌ Invalid Creditentials\nType "login" to try again! or "signup" to create an account'
            )
            continue
        break
    elif userInput == "signup" or userInput == "su" or userInput == "2":
        clear()
        print("---------Enter your account info to proceed--------")
        UserID = input("User ID: ")
        password = input("Password: ")
        email = input("Email: ")
        name = input("Name: ")
        year = input("Academic Year: ")
        age = input("Age: ")

        data = fetchFile("res/accounts.txt")
        for item in data:
            if item[0] == UserID:
                print("Sorry, ID already exits")
                break
        else:
            modifyFile(
                "res/accounts.txt",
                [[UserID, password, email, age, year, [], name, 0]] + data,
            )
            clear()
            print('✅ You may now login with your info.\nType "login"')
    else:
        print(
            "❌ Invalid Input, avalaible commands are:\n\nLogin: login / 1 / li\nSign Up: signup / 2 / su"
        )


######################### Professors Commands section

if UserAuth[-1] == 1:
    clear()
    print(
        "Welcome back, Dr. "
        + item[-2]
        + "\n\navalaible commands are:\n\nGrade Quizzes: grade / 1\nList Students: list / 2\nManage Quizzes: quizzes / 3 / manage"
    )
    while 1:
        userInput = input().lower()

        ############### Grade Command
        if userInput == "grade" or userInput == "1":

            clear()
            Questions = fetchFile("res/questions.txt")
            for item in Questions:
                for i in range(item[2]):
                    item.pop(-1)
            tableOutput(Questions, ["ID", "Title", "No. of Questions"])
            quizid = input("Enter the ID of the quiz you wanna grade: ")
            Questions = fetchFile("res/questions.txt")
            quizData = []
            validQuizID = 0
            validAnswerID = 0
            while validQuizID == 0:
                for item in Questions:
                    if item[0] == quizid:
                        quizData = item
                        validQuizID = 1
                        break
                else:
                    print("❌ Invalid ID, double check it\n")
                    quizid = input("Enter your quiz ID again: ")

            clear()
            print("All students that have answered this quiz: ")
            Answers = fetchFile("res/answers.txt")
            studentsAnswers = []
            for item in Answers:
                if item[0] != quizid:
                    continue
                student = item[item[2] + 3]
                for i in range(5):
                    student.pop(1)
                student.pop(-1)
                studentsAnswers.append(student)
            tableOutput(studentsAnswers, ["ID", "Name"])
            answerID = input("Enter ID of the student you wanna grade: ")
            index = -1
            while validAnswerID == 0:
                for item in Answers:
                    ++index
                    if item[0] == quizid:
                        if item[-2][0] == answerID:
                            Quiz = item
                            QuestionsData = item
                            validAnswerID = 1
                            break
                else:
                    print("Invalid ID, try again\n")
                    answerID = input("Enter the student ID again: ")
            clear()
            print("------------------⚠️ Grading Quiz ⚠️------------------")
            print(
                "Title: "
                + Quiz[1]
                + "\nNo. Of Questions: "
                + str(Quiz[2])
                + "\nID: "
                + Quiz[0]
                + "\nStudent Name: "
                + Quiz[-2][-2]
                + "\nGrade: "
                + str(Quiz[-1])
            )
            for i in range(3):
                QuestionsData.pop(0)
            QuestionsData.pop(-1)
            QuestionsData.pop(-1)
            tableOutput(QuestionsData, ["Order", "Question", "Student Answer"])
            newGrade = input("Enter the grade to modify it (ex. +A): ").upper()
            Answers = fetchFile("res/answers.txt")
            for item in Answers:
                if item[0] == quizid and item[-2][0] == answerID:
                    item[-1] = newGrade
                    break
            modifyFile("res/answers.txt", Answers)
            clear()
            print("✅ Modified the grade!")

        ##################### List students command

        elif userInput == "2" or userInput == "list":
            Questions = fetchFile("res/questions.txt")
            for item in Questions:
                for i in range(item[2]):
                    item.pop(-1)
            tableOutput(Questions, ["ID", "Title", "No. of Questions"])
            quizid = input("Enter the ID of the quiz you wanna check: ")
            Questions = fetchFile("res/questions.txt")
            quizData = []
            validQuizID = 0
            validAnswerID = 0
            while validQuizID == 0:
                for item in Questions:
                    if item[0] == quizid:
                        quizData = item
                        validQuizID = 1
                        break
                else:
                    print("❌ Invalid ID, double check it\n")
                    quizid = input("Enter your quiz ID again: ")

            answers = fetchFile("res/answers.txt")
            accounts = fetchFile("res/accounts.txt")
            clear()
            finalData = []
            for user in accounts:
                if (user[-1] == 1):
                    accounts.remove(user)
                    continue
                else:
                   if(quizid in user[-3]):
                     solved = "✅"
                   else:
                     solved = "❌"
                for answer in answers:
                    if(answer[0] == quizid and answer[-2][0] == user[0]):
                        grade = answer[-1]
                        break
                    else:
                        grade = " "
                finalData.append([user[0], user[-2], solved, grade])
            tableOutput(finalData, ["Student ID", "Name", "Solved", "Grade"])
            print("HINT: type 2 to continue checking!")
                    

        #################### Manage Quizzes command

        elif userInput == "3" or userInput == "manage" or userInput == "quizzes":
            clear()
            print(
                "Avalaible commands are:\n\nCreate a Quiz: 1 / create\nDelete a Quiz: 2 / delete"
            )
            userInput = input().lower()

            ################ Create Quiz

            while int(userInput) > 2 or int(userInput) < 1:
              
                print("❌ Invalid Option, try again")
                userInput = input("Enter your option: ")

            if userInput == "1" or userInput == "create":
                QuestionsData = []
                QuizTitle = input("Quiz Title: ")
                QuizID = input("Enter Quiz ID: ")
                quesNumbers = int(input("Enter Question Numbers: "))
                for i in range(quesNumbers):
                    questionid = i + 1
                    question = input("Enter Your Question: ")
                    answers = []
                    for y in range(4):
                        answer = input("Enter Answer No." + str(y + 1) + ": ")
                        answers.append(answer)
                    validInt = 0
                    while validInt == 0:
                        
                     ValidAnswer = input("Enter the valid answer (1/2/3/4): ")
                     if(int(ValidAnswer) > 0 and int(ValidAnswer) < 5):
                         validInt = 1
                     else:
                         print("❌ Invalid Input")
                    answers.append(answers[int(ValidAnswer) - 1])
                    QuestionsData.append([questionid, question, answers])
                    print("----------------")

                newData = [QuizID, QuizTitle, quesNumbers] + QuestionsData
                oldData = fetchFile("res/questions.txt")
                modifyFile("res/questions.txt", [newData] + oldData)
                clear()
                print("✅ Successfully created your quiz with the ID of " + str(QuizID))

            ############## Delete Quiz
            elif userInput == "2" or userInput == "delete":
                quizID = input("Enter the quiz ID: ")
                questions = fetchFile("res/questions.txt")
                for question in questions:
                    if question[0] == quizID:
                        questions.remove(question)
                        modifyFile("res/questions.txt", questions)
                        print('✅ Deleted "' + str(question[1]) + '"')
                        break
                else:
                    print("❌ Invalid ID, try double checking")

        else:
            print(
                "❌ Invalid Command\n\navalaible commands are:\n\nGrade Quizzes: Grade / 1\nList Students: list / 2\nManage Quizzes: quizzes / 3 / manage"
            )


######### Student Commands
else:
    print(
        "Welcome back, "
        + item[-2]
        + "\n\navalaible commands are:\n\nAnswer Quizzes: answer [QUIZ_ID]\nList Quizzes: list / 1"
    )
    while 1:
        userInput = input().lower()
        ############ Answer Command
        if "answer" in userInput:
            clear()
            if len(userInput.split()) < 2:
                quizID = input("Enter your quiz ID: ")
            else:
                quizID = userInput.split()[1]
            questionsData = fetchFile("res/questions.txt")
            for item in questionsData:
                if item[0] == quizID:
                    questionsData.clear()
                    questionsData.extend(item)
                    break
            if not (questionsData[0] == quizID):
                print("❌ Quiz not found, Double check the ID!")
                continue
            IndexedData = fetchFile("res/answers.txt")
            solved = 0
            for answer in IndexedData:
                if answer[0] == quizID and answer[-2][0] == UserAuth[0]:
                    solved = 1
                    break
            if solved == 1:
                print("⚠️ You've already answered this quiz")
                continue
            Score = 0
            finalData = [questionsData[0], questionsData[1], questionsData[2]]
            print(
                "-------------------------⚠️ Solving Quiz ⚠️---------------"
                + "\n"
                + "Quiz Title: "
                + questionsData[1]
                + "\n"
                + "Quiz ID: "
                + str(questionsData[0])
                + "\n"
                + "Total Questions: "
                + str(questionsData[2])
            )
            print(
                "-------------------------------------------------------------------------"
            )
            for x in range(3):
                questionsData.pop(0)
            for item in questionsData:
                print(
                    str(item[0])
                    + ") "
                    + item[1]
                    + "\n1) "
                    + item[2][0]
                    + "    2) "
                    + item[2][1]
                    + "\n3) "
                    + item[2][2]
                    + "    4) "
                    + item[2][3]
                    + "\n--------\n"
                )
                validChoice = 0
                while validChoice == 0:
                    answer = input("Your answer (1/2/3/4): ")
                    if int(answer) < 5 and int(answer) > 0:
                        validChoice = 1
                    else:
                        print("Invalid option, only enter the order of your answer")
                clear()
                if item[2][int(answer) - 1] == item[2][-1]:
                    Score = Score + 1
                finalData.append([item[0], item[1], item[2][int(answer) - 1]])
            oldData = fetchFile("res/answers.txt")
            finalData.append(UserAuth)
            per = (Score / finalData[2]) * 100
            if per == 100:
                grade = "+A"
            elif per < 100 and per > 89:
                grade = "A"
            elif per < 90 and per > 79:
                grade = "B"
            elif per < 80 and per > 59:
                grade = "C"
            elif per < 60 and per > 49:
                grade = "D"
            else:
                grade = "F"
            finalData.append(grade)
            accounts = fetchFile("res/accounts.txt")
            UserAuth[-3].append(finalData[0])
            for item in accounts:
                if item[0] == UserAuth[0]:
                    item.clear()
                    item.extend(UserAuth)
            modifyFile("res/accounts.txt", accounts)
            modifyFile("res/answers.txt", [finalData] + oldData)
            print("✅ Answers sent to your professor, your grade is " + grade)
        ######## List quizzes for the student
        elif userInput == "1" or userInput == "list":
            clear()

            Questions = fetchFile("res/questions.txt")
            IndexedAnswers = fetchFile("res/answers.txt")
            for question in Questions:
                for i in range(len(question) - 2):
                    question.pop()
                for answer in IndexedAnswers:
                    if answer[-2][0] != UserAuth[0]:
                        continue
                    if answer[0] == question[0]:
                        question.append("✅")
                        question.append(answer[-1])

            tableOutput(Questions, ["Quiz ID", "Quiz Title", "Answered", "Grade"])
            print('HINT: To answer a quiz, type "answer [QUIZ_ID]"')
        else:
            print(
                "❌ Invalid Command\n\navalaible commands are:\n\nAnswer Quizzes: answer [QUIZ_ID]\nList Quizzes: list / 1"
            )
