#this is my first major project
#kbcp game
print("=======================================*kaun bnega crore pati*============================================\n\n")

question = ["1.what is capital of india",
            "2.who is prime minister of india",
            "3.who is best coder",
            "4.what is my favorite dish",
            "5.who is best teacher for coding"]

option = [["1.delhi","2.maharashtra","3.hydrabad","4.haryana"],
          ["1.amit-shah","2.narendra-modi","3.yogi-aditynath","4.vladimir-putin"],
          ["1.ali-hasan","2.code_with_harry","3.aditya","4.rakshit"],
          ["1.nihari","2.haleem","3.biryani","4.chole-bhature"],
          ["1.NYC","2.code_with_harry","4.gate-wallah","5.microsoft_wali_didi"]]

answer = [0,1,0,2,1] 
prizes = [1000000,3000000,6000000,30000000,30000000]

money = 0
for i in range(len(question)):
    print(question[i],sep ="\n")
    for options in option[i]:
        print(options)
        print()
    user_answer = int(input("enter your answer: "))
    user_answer-=1
    if user_answer == answer[i]:
        money+=prizes[i]
        print("correct answer:",answer[i]+1)
        print("you won:",prizes[i])
        print("total amount:",money)
        print("\n")
    else:
        print("correct answer",answer[i]+1)
        print("you loose")
        print(money)
        break        