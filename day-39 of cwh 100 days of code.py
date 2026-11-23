#***done by myself***
questions = ["what is capital of india.",
            "who i am.",
            "how much days i have covered till now."]
options = [["1.mumbai","2.delhi","3.hydrabad","4.haryana"],
           ["1.ali","2.harry","3.tanuj","4.krish"],
           ["1.39","2.40","3.45","4.31"]]
answers = [2,1,1]
for i in range(len(questions)):
    print(questions[i])
    
    for option in options[i]:
        print(option)

    answer = int(input("select option: "))

    if answer == answers[i]:
        print("correct answer\n")
    else:
        print("incorrect answer\n")



#***done afte learning from cwh lecture***



