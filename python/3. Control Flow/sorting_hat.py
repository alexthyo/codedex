# 16

hufflepuff = 0
slytherin = 0
ravenclaw = 0
gryffindor = 0

print("(Q1) Do you like Dawn or Dusk?\n"
      "1) Dawn\n"
      "2) Dusk)")
answer = int(input("Enter your answer (1-4): "))
if answer == 1:
    gryffindor += 1
    slytherin += 1
elif answer == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print("Wrong input.")

print("Q2) When I’m dead, I want people to remember me as:\n"
      "1) The Good\n"
      "2) The Great\n"
      "3) The Wise\n"
      "4) The Bold")
answer = int(input("Enter your answer (1-4): "))
if answer == 1:
    hufflepuff += 2
elif answer == 2:
    slytherin += 2
elif answer == 3:
    ravenclaw += 2
elif answer == 4:
    gryffindor += 2
else:
    print("Wrong input.")

print("Q3) Which kind of instrument most pleases your ear?\n"
      "1) The violin\n"
      "2) The trumpet\n"
      "3) The piano\n"
      "4) The drum")
answer = int(input("Enter your answer (1-4): "))
if answer == 1:
    slytherin += 4
elif answer == 2:
    hufflepuff += 4
elif answer == 3:
    ravenclaw += 4
elif answer == 4:
    gryffindor += 4
else:
    print("Wrong input.")

print("The score for Syltherin is: ", slytherin)
print("The score for Hufflepuff is: ", hufflepuff)
print("The score for Ravenclaw is: ", ravenclaw)
print("The score for Gryffindor is: ", gryffindor)
