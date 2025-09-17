# challenge 5

earth_weight = float(input("What is your weight on Earth? "))

nr = int(input("What number is your planet? "))

if nr == 1:
    dweight = earth_weight * 0.38
elif nr == 2:
    dweight = earth_weight * 0.91
elif nr == 3:
    dweight = earth_weight * 0.38
elif nr == 4:
    dweight = earth_weight * 2.53
elif nr == 5:
    dweight = earth_weight * 1.07
elif nr == 6:
    dweight = earth_weight * 0.89
elif nr == 7:
    dweight = earth_weight * 1.14
else:
    print("Invalid planet number")

print(dweight)
