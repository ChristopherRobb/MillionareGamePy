answer = ""
userName = ""
pointA = 10
pointB = 20
pointC = 30
pointD = 40
pointE = 100
totalPoint = 0



print("~" * 50)
print("~~~         Who Wants to Be a Millionaire     ~~~")
print("~" * 50)


print("Feeling Lucky?? \n")
userName = input("Please enter your first name: ").strip().title()
print("\nI will ask you 5 questions, if you get more than 200 points you win $1,000,000,000\n")
print("Lets Go", userName, "!!!")


file = open("Millionare.txt", "r")

try:

    print("\nA)",file.readline())

    print("1) 200 Feet\n2) 75 Feet\n3) 300 Feet")
    print("4)",file.readline())
    print("This question is worth", pointA, "points\n")
    answer = int(input("Select 1 2  3 or 4: "))
    if answer == 4 :
        totalPoint += pointA
        print("Correct")
    else:
        print("Wrong")

    print("~" * 50)
    print("                    score: ", totalPoint,)
    print("~" * 50)



    print("\nB)",file.readline())
    print("1) Bird\n2) Fish\n3) Volcano")
    print("4)",file.readline())
    print("This question is worth", pointB, "points\n")
    answer= int(input("Select 1 2  3 or 4: "))
    if answer == 4 :
        totalPoint += pointB
        print("Correct")
    else:
        print("Wrong")

    print("~" * 50)
    print("                    score: ", totalPoint)
    print("~" * 50)


    

    print("\nC)",file.readline())
    print("1) Deep Waters Feet\n2) Sparta\n3) Harry Potter")
    print("4)",file.readline())
    print("This question is worth", pointC, "points\n")
    answer= int(input("Select 1 2  3 or 4: "))
    if answer == 4 :
        totalPoint += pointC
        print("Correct")
    else:
        print("Wrong")

    print("~" * 50)
    print("                     score: ", totalPoint)
    print("~" * 50)



    print("\nD)",file.readline())
    print("1) Jamie Foxx\n2) Adam Sandler\n3) Denzel Washington")
    print("4)",file.readline())
    print("This question is worth", pointD, "points\n")
    answer= int(input("Select 1 2  3 or 4: "))
    if answer == 4 :
        totalPoint += pointD
        print("Correct")
        
    else:
        print("Wrong")

    print("~" * 50)
    print("                      score: ", totalPoint)
    print("~" * 50)




    print("\nE)",file.readline())
    print("1) Alabama\n2) Texas\n3) Boston")
    print("4)",file.readline())
    print("This question is worth", pointE, "points\n")
    answer= int(input("Select 1 2  3 or 4: "))
    
    if answer == 4 :
        totalPoint += pointE
        print("Correct\n")
    else:
        print("Wrong\n")


    


except ValueError:
    print("You must enter 1-4")




file.close()

print("Total Points: ", totalPoint)

#Highscore file

f1 = open("highscore.txt","r")
f1_line = int(f1.read())






if totalPoint == 200:
    print("~" * 50)
    print("Congrats!!! You won $1,000,000,000!!!\n")
    print("Go see Professor Cox to claim your prize!!")
    print("~" * 50)




elif totalPoint > f1_line or totalPoint < 200:
    print("~" * 50)
    print("\nOld High Score: ", f1_line)
    print("\nNot Millionare status, but you now own the new High Score!! ", totalPoint ,"points")
    print("~" * 50)


else:
    print("~" * 50)
    print("Goodbye", userName)
    print("~" * 50)




print("Goodbye", userName)
print("~" * 50)



f1.close

#Write highscore

file = open("highscore.txt", "w")
if totalPoint >= int(f1_line):
    file.write(str(totalPoint))

else:
    file.write("150")
    

file.close()



