# Task 1: while loop
number = 0
while number <= 20:
    if number % 2 ==0:
        if number == 16:
            break
        print (number)
    number +=1

# Task 2: for loop with continue
for num in range(1, 16):
    if num % 3 == 0:
        continue
    print (num)

# Task 3: if-else statement
number = int(input("Enter a number: "))
if number > 0:
    print ("positive")
elif number == 0:
    print("zero")
else:
    print("negative")

# Task 4: Nested loops
for i in range(1, 6):
    for j in range(1, 6):
        print (i, "x", j, "=", i*j)