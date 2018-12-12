from random import randint
ten=10
x=(randint(0,6))
print("Your first roll is: " + str(x))

y=(randint(0,6))
print("Your second roll is: " + str(y))

z=(randint(0,6))
print("Your third roll is: " + str(z))

print("Your total is: " + str(x+y+z))

if (int(x+y+z)) < (int(10)):
    print("Ouch, sucks to suck!")

else:
    print("Hey that's pretty good!")
