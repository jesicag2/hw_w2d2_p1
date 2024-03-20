# HW1_P2: The Greatest Showdown

# Task 1: Identify the Greatest
'''
Write a Python program that prompts the user to enter three numbers. 
The program should then identify and print out the largest number among the three.
'''

numa = input("Please enter first number: ")
numb = input("Please enter second number: ")
numc = input("Please enter third number: ")

if numa > numb and numa > numc:
    print("The largest number is the first number:", numa)
elif numb > numa and numb > numc:
    print("The largest number is the second number:", numb)
elif numc > numa and numc > numb:
    print("The largest number is the third number:", numc)


# Task 2: Identify the Smallest
'''
Extend your program from Task 1 to also determine the smallest number among the three and print it out.
'''

numa = input("Please enter first number: ")
numb = input("Please enter second number: ")
numc = input("Please enter third number: ")

if numa > numb and numa > numc:
    print("The largest number is the first number:", numa)
elif numb > numa and numb > numc:
    print("The largest number is the second number:", numb)
elif numc > numa and numc > numb:
    print("The largest number is the third number:", numc)

if numa < numb and numa < numc:
    print("The smallest number is the first number:", numa)
elif numb < numa and numb < numc:
    print("The smallest number is the second number:", numb)
elif numc < numa and numc < numb:
    print("The smallest number is the third number:", numc)


# Task 3: Equality Check
'''
Enhance your program to handle cases where two or all of the numbers are equal. 
The program should display appropriate messages like "Two numbers are equal and the largest" 
or "All numbers are equal".

Expected Outcome: If we provide the numbers 3, 3, and 4, it should print out that 
"The smallest number is 3. The largest number is 4. There are two numbers equal to 
each other." Printing out which numbers are equal would be a great added bonus.
'''

numa = input("Please enter first number: ")
numb = input("Please enter second number: ")
numc = input("Please enter third number: ")

if numa >= numb and numa >= numc:
    print("The largest number is:", numa)
elif numb >= numa and numb >= numc:
    print("The largest number is:", numb)
elif numc >= numa and numc >= numb:
    print("The largest number is:", numc)

if numa <= numb and numa <= numc:
    print("The smallest number is:", numa)
elif numb <= numa and numb <= numc:
    print("The smallest number is:", numb)
elif numc <= numa and numc <= numb:
    print("The smallest number is:", numc)

if numa == numb == numc:
    print("All numbers are equal")
elif numa == numb or numa == numc or numb == numc:
    print("There are two numbers equal to eachother:")
    if numa == numb:
        print(numa, "and", numb)
    elif numa == numc:
        print(numa, "and", numc)
    elif numb == numc:
        print(numb, "and", numc)
