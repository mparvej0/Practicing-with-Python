# Questions quiz project
questions = [
 [

    "Which language was used to create fb?", "Python", "French", "JavaScript", "Php", "None", 4
    ],
[
    "Which language was used to create fb?", "Python", "French", "JavaScript", "Php", "None", 4
    ],
[
    "Which language was used to create fb?", "Python", "French", "JavaScript", "Php", "None", 4
    ],
 ]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]

for i in range(0, len(questions)):
    question = questions[i]
    print(f"\n\nQuestion for RS. {levels[i]}")
    print(f"a. {questions[i][1]} b. {questions[i][2]}")
    print(f"c. {questions[i][3]} d. {questions[i][4]}")
    reply = int(input("Enter your answer (1-4) or 0 to quite"))
    if (reply == 0):
       money = levels[i]
       break
    if(reply == questions[-1]):
        print(f"Correct answer, you have won RS. {levels[i]}")
        if(i == 3):
            money = 10000
        elif (i == 1):
          money = 32000
        elif (i == 4):
          money = 10000000
    else:
        print("Correct answer!")
        break
    print(f"Your take home money is {money}")