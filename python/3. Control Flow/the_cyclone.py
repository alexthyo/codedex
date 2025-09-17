# 15

height = int(input("Enter your height here: "))
credits = int(input("Enter your credits here: "))

# tall enough and enough credits:
if height > 136 and credits > 9:
    print("Enjoy the ride!")
# enough credits, not tall enough:
elif credits > 9 and height < 137:
    print("You are not tall enough to ride.")
# tall enough, but not enough credits:
elif height > 136 and credits < 10:
    print("You don't have enough credits.")
# "You don't meet either requirement."
else:
    print("You don't meet either requirement.")
