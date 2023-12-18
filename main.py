import json
UserAuth: [int, str];
done: int = 0;
option: int;
print("Welcome, type Login or Signup")
while(1):
    userInput = input().lower()
    if(userInput == "exit"):
        print("Exiting...")
        exit()
    if(userInput == "login"):
        UserID = input("User ID: ")
        password = input("Password: ")
        with open("acc.txt", "r") as file:
            array = json.load(file)
        for item in array:
            if(item[0] == UserID and item[1] == password):
                UserAuth = item;
                done = 1;
                break;
            
        if(done == 1):
            break;
        else:
            print("Invalid Creditentials, try again!")
            
    elif(userInput == "signup"): 
        UserID = input("User ID: ")
        password = input("Password: ")
        email = input("Email: ")
        name = input("Name: ")
        with open("acc.txt", "r") as file:
            array = json.load(file)
        with open('acc.txt', 'w') as file:
            json.dump([[UserID, password, email, name, 0]] + array, file)
        print("Signed up! you may now login")
    else:
        print("Invalid Input, try again")
        
if(UserAuth[-1] == 1):
    print("Welcome back Dr." + item[-2] + "\n\nOptions:\n\nGrade Quizzes --> 1\nList Students --> 2\nManage Quizzes --> 3")
    while(1):
     userInput = input()
     if(userInput == "exit"):
        exit()
     if(userInput == "1"):
        print("Grade")
        option = 1
     elif(userInput == "2"):
        print("list")
        option = 2
     elif(userInput == "3"):
        print("manage")
        option = 3
        break;
     else:
        print("Input the order of your choice")
else:
    print("Welcome back " + item[-2] + "\n\nOptions:\n\nShow Quizzes --> 1\nQuiz Results--> 2")
    while(1):
     userInput = input()
     if(userInput == "exit"):
        exit()
     if(userInput == "1"):
        print("Show Quizzes")
        option = 1
     elif(userInput == "2"):
        print("Results")
        option = 2
     else:
        print("Input the order of your choice")
if(option == 3 and UserAuth[-1] == 1):
    print("Create a quiz (1) or delete (2)")
    while(1):
        userInput = input()
        if(userInput == "exit"):
            exit()
            
        if(userInput == "1"):
            QuestionsData = []
            QuizTitle = input("Quiz Title: ")
            QuizID = input("Enter Quiz ID: ")
# remmeber to add the random function for the ID
            quesNumbers = int(input("Enter Question Numbers: "))
            for i in range(quesNumbers):
              questionid = input("Enter your QuestionID: ")
              question = input("Enter your question: ")
              answers: [str] = []
              for y in range(4):
                  answer = input("Enter answer no." + str(y+1) + ": ")
                  answers.append(answer)
              QuestionsData.append([questionid, question, answers])
                  
            arr = ([QuizID, QuizTitle] + QuestionsData)
            with open("questions.txt", "r") as file:
               array: [str] = json.load(file)
            with open("questions.txt", "w") as file:
                json.dump([arr] + array, file)
        elif(userInput == "2"):
         quizID = input("Enter the quiz ID")
         with open("questions.txt", "r") as file:
             array = json.load(file)
         for x in array:
            if(x[0] == quizID):
              array.remove(x)
              with open("questions.txt", "w") as file:
                  json.dump(array, file)
              break
            else:
                print("Invalid ID")
        else:
            print("Enter a valid option")
                
                
             
