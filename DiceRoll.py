from random import randrange
#Roll the die three times
for i in range(0, 3):
#Generate random number in the range 1...6
val = randrange(1, 6)
#Show the die
print("+-------+")
if val == 1:
print("| |")
print("| * |")
print("| |")
elif val == 2:
print("| * |")
print("| |")
print("| * |")
elif val == 3:
print("| * |")
print("| * |")
print("| * |")
elif val == 4:
print("| * * |")
print("| |")
print("| * * |")
elif val == 5:
print("| * * |")
print("| * |")
print("| * * |")
elif val == 6:
print("| * * * |")
print("| |")
print("| * * * |")
else:
print(" *** Error: illegal die value ***")
print("+-------+")
