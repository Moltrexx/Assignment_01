'''                     
                                NOTE 
                        Name : Anuraj Vishwakarma 
                        Roll no : 0176CS231036   
                        CSE  COLLEGE :  LNCTE   
                        BATCH - 6 (MTF) - 12:10 PM                                                                                                                                                                                                                                                                             '''




#Basic If–Else Problems:
#1. Write a program to check whether a number is positive, negative, or zero.
num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

#2.Write a program to check whether a number is even or odd.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#3.Write a program to check if a given year is a leap year or not.
year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not leap year")

#4.Write a program to find the greatest of two numbers.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if num2 > num2:
    print(num1, "is greater ")
elif num1>num2:
    print(num2," is greater ")
else:
    print("Both number are equal .")


#5.Write a program to check whether a person is eligible to vote (age >= 18).
age = int(input("Enter age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

#6.Write a program to check whether a given character is a vowel or consonant.
ch = input("Enter a character: ").lower()
if ch in "aeiou":
    print("Vowel")
elif ch.isalpha():
    print("Consonant")
else:
    print("Not a letter")

#7.Write a program to check if a number is divisible by 5.
num = int(input("Enter a number: "))
if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")

#8.Write a program to determine whether a given number is a single-digit, two-digit, or more than two-digit number.
num = abs(int(input("Enter a number: ")))
if num <= 9:
    print("Single-digit")
elif num <= 99:
    print("Two-digit")
else:
    print("More than two-digit")

#9.Write a program to check whether a student has passed or failed (passing marks = 40).
marks = int(input("Enter marks: "))
if marks >= 40:
    print("student is Passed")
else:
    print("student is Failed ")

#10.Write a program to find whether the entered number is a multiple of both 3 and 7.
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 7 == 0:
    print(f"{num} is Multiple of both 3 and 7")
else:
    print(f"{num} is not a multiple of both 3 and 7")




#Ladder If & Nested If:

#1. Write a program to find the greatest among three numbers.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1>num2 and num1>num3:
    print(f"{num1} is greater ")
elif num2>num1 and num2>num3:
    print(f"{num2} is greater ")
else:
    print(f"{num2} is greater ")

#2.Write a program to classify a person based on age: Child (<13), Teenager (13-19), Adult (20-59), Senior (60+).
age = int(input("Enter the person's age: "))
if age < 0:
    print("Invalid input. Age cannot be negative.")
elif age < 13:
    print("This person is a Child.")
elif age <= 19:
    print("This person is a Teenager.")
elif age <= 59:
    print("This person is an Adult.")
else:
    print("This person is a Senior.")

#3.Write a program to assign grades based on marks:90-100: A,75-89: B,50-74: C,35-49: D,<35: Fail.
marks = float(input("Enter the student's marks: "))
if marks < 0 or marks > 100:
    print("Invalid input. Marks must be between 0 and 100.")
elif marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
elif marks >= 35:
    print("Grade: D")
else:
    print("Result: Fail")

#4.Write a program to check the type of triangle (equilateral, isosceles, or scalene) based on sides.
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))
if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):

    if side1 == side2 == side3:
        print("The triangle is Equilateral.")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("The triangle is Isosceles.")
    else:
        print("The triangle is Scalene.")
else:
    print("These side lengths cannot form a valid triangle.")

#5.Write a program to check if a character is uppercase, lowercase, digit, or special symbol.
char_input = input("Enter a single character: ")
if len(char_input) == 1:
    if char_input.isupper():
        print(f"The character '{char_input}' is an Uppercase letter.")
    elif char_input.islower():
        print(f"The character '{char_input}' is a Lowercase letter.")
    elif char_input.isdigit():
        print(f"The character '{char_input}' is a Digit.")
    else:
        print(f"The character '{char_input}' is a Special Symbol.")

#6.
units = float(input("Enter the number of electricity units consumed: "))
bill = 0
if units < 0:
    print("Invalid input. Units consumed cannot be negative.")
elif units <= 100:
    bill = units * 5
    print(f"Total electricity bill: ₹{bill:.2f}")    # 2f give us the decimal value upto 2 digit 
elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)
    print(f"Total electricity bill: ₹{bill:.2f}")
else: 
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
    print(f"Total electricity bill: ₹{bill:.2f}")

#7.Write a program to determine the largest of four numbers using nested if.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
num4 = float(input("Enter the fourth number: "))

largest = 0
if num1 >= num2:

    if num1 >= num3:
        if num1 >= num4:
            largest = num1
        else:
            largest = num4
    else:
        if num3 >= num4:
                largest = num3
        else:
                largest = num4
else:
    if num2 >= num3:
        if num2 >= num4:
                largest = num2
        else:
                largest = num4
    else:
        if num3 >= num4:
                largest = num3
        else:
                largest = num4

print(f"The largest number is: {largest}")

#8.Write a program to check if a given year is a century year and also a leap year.
year = int(input("Enter a year to check: "))
if year % 100 == 0:
    if year % 400 == 0:
        print(f"The year {year} is a century year and a leap year.")
    else:
        print(f"The year {year} is a century year, but it is not a leap year.")
else:
    print(f"The year {year} is not a century year.")

#9.Write a program to classify BMI value: Underweight (<18.5), Normal (18.5-24.9), Overweight (25-29.9),Obese (30+).
bmi = float(input("Enter your BMI value: "))
print("Invalid input. BMI cannot be a negative number.")
if bmi < 0:
        print("Invalid input. BMI cannot be a negative number.")
elif bmi < 18.5:
    print("Your BMI category is: Underweight")
elif bmi < 25:  
    print("Your BMI category is: Normal weight")
elif bmi < 30: 
    print("Your BMI category is: Overweight")
else:  
    print("Your BMI category is: Obese")

#10.Write a program to display the smallest number among three using nested if.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
smallest = 0
if num1 <= num2:
    if num1 <= num3:
        smallest = num1
    else:
        smallest = num3
else:
    if num2 <= num3:
        smallest = num2
    else:
        smallest = num3

print(f"The smallest number is: {smallest}")


#For Loop Problem

#1.Write a program using a for loop to print all Armstrong numbers between 100 and 999. (Armstrong number: sum of cubes of digits equals the number itself. Example: 153 => 13+53+33 = 153).
print("Armstrong numbers between 100 and 999 are:")

for num in range(100, 1000):
    sum_of_cubes = 0
    temp_num = num
    while temp_num > 0:
        digit = temp_num % 10
        sum_of_cubes += digit ** 3

        temp_num //= 10

    if num == sum_of_cubes:
        print(num)
    
#2.Write a program to generate and display the first n prime numbers using a for loop.
n = int(input("Enter the number of prime numbers you want to generate: "))

if n <= 0:
    print("Please enter a positive number.")
else:
    print(f"The first {n} prime numbers are:")
        
    count = 0 
    num = 2    
        
    while count < n:
        is_prime_flag = True 
        if num <= 1:
            is_prime_flag = False
        else:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime_flag = False
                    break 

        if is_prime_flag:
            print(num, end=" ")
            count += 1
            
        num += 1 
        
    print() 

#3.Write a program to display all numbers from 1 to 500 that are divisible by 3, but the sum of their digits should not exceed 10.
print("Numbers from 1 to 500 that are divisible by 3 and have a digit sum of 10 or less:")
for num in range(1, 501):
    

    if num % 3 == 0:
        
        sum_of_digits = 0
        temp_num = num
        
        while temp_num > 0:
            digit = temp_num % 10
            sum_of_digits += digit
            temp_num //= 10
        if sum_of_digits <= 10:
            print(num, end=" ")

#4.Write a program using a for loop to print a pyramid of stars (*) of height n. Example for n=4:

#*
#***
#*****
#*******

n = int(input("Enter the height of the pyramid (n): "))

if n <= 0:
        print("Please enter a positive integer for the height.")
else:
    for i in range(1, n + 1):
        spaces = n - i
        stars = 2 * i - 1
        print(" " * spaces + "*" * stars)

#5.Write a program to accept a string and check whether it is a pangram (contains all 26 alphabets at least once) using a for loop.
input_string = input("Enter a string to check if it's a pangram: ")
alphabet = "abcdefghijklmnopqrstuvwxyz"


is_pangram = True

for char in alphabet:
    if char not in input_string.lower():
            is_pangram = False
    break 

if is_pangram:
        print("The entered string is a pangram.")
else:
        print("The entered string is not a pangram.")

#6.Write a program using a for loop to print all twin primes between 1 and 100. (Twin primes: pairs of prime numbers with a difference of 2, e.g., (3,5), (11,13)).
print("Twin prime numbers between 1 and 100 are:")
for num in range(1, 99):
    is_num_prime = True
    if num <= 1:
        is_num_prime = False
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_num_prime = False
                break
    if is_num_prime:
  
        is_num_plus_2_prime = True
        num2 = num + 2
        for i in range(2, int(num2**0.5) + 1):
            if num2 % i == 0:
                is_num_plus_2_prime = False
                break

        if is_num_plus_2_prime:
            print(f"({num}, {num2})", end=" ")

#7.Write a program that accepts a number from the user and prints whether it is a Harshad number (number divisible by the sum of its digits) using a for loop.
num_str = input("Enter a number: ")
number = int(num_str)
if number <= 0:
    print("Please enter a positive integer.")
else:
    sum_of_digits = 0
    for digit_char in num_str:
            sum_of_digits += int(digit_char)
    if sum_of_digits != 0 and number % sum_of_digits == 0:
        print(f"{number} is a Harshad number.")
    else:
        print(f"{number} is not a Harshad number.")
        
#8.Write a program to generate Pascal’s Triangle up to n rows using a for loop.

n = int(input("Enter the number of rows for Pascal's Triangle: "))
if n <= 0:
    print("Please enter a positive integer for the number of rows.")
else:
 
    triangle = [[1]]
    print("Pascal's Triangle:")


    for i in range(1, n):

        prev_row = triangle[-1]

        new_row = [1]

        for j in range(len(prev_row) - 1):
            new_row.append(prev_row[j] + prev_row[j+1])
            

        new_row.append(1)

        triangle.append(new_row)

    max_width = len(" ".join(map(str, triangle[-1])))

    for row in triangle:
        row_str = " ".join(map(str, row))
        print(row_str.center(max_width))

#9.Write a program using a for loop to display the sum of the series: 12 + 22 + 32 + ... + n2
n = int(input("Enter the value of n: "))

if n <= 0:
    print("Please enter a positive integer.")
else:

    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i * i  
    print(f"The sum of the series 1^2 + 2^2 + ... + {n}^2 is: {total_sum}")

#10.Write a program that accepts a number from the user and prints whether it is a Strong number (sum of factorials of digits = number itself) using a for loop. Example: 145 => 1! + 4! + 5! = 145.
num_str = input("Enter a number: ")
number = int(num_str)
if number < 0:
    print("Please enter a non-negative integer.")
else:
    sum_of_factorials = 0
    for digit_char in num_str:
        digit = int(digit_char)
        factorial = 1
        if digit == 0:
            factorial = 1 
        else:
            for i in range(1, digit + 1):
                factorial *= i
            
        sum_of_factorials += factorial

    if sum_of_factorials == number:
            print(f"{number} is a Strong number.")
    else:
            print(f"{number} is not a Strong number.")



#While Loop Problem :


#1. Write a program using a while loop to find the reverse of a number and check if the reversed number is prime. Example: Input = 73 → Reverse = 37 → Prime.
original_number = int(input("Enter a number: "))
if original_number < 0:
    print("Please enter a non-negative integer.")
else:
    number = original_number
    reversed_number = 0
    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10
        
    print(f"The reverse of {original_number} is {reversed_number}.")
    is_prime = True
    if reversed_number <= 1:
            is_prime = False
    else:
        for i in range(2, int(reversed_number**0.5) + 1):
            if reversed_number % i == 0:
                is_prime = False
                break 
    if is_prime:
        print(f"{reversed_number} is a prime number.")
    else:
        print(f"{reversed_number} is not a prime number.")

#2.Write a program that continues to accept numbers from the user until the sum of digits of all numbers entered becomes greater than 100.
total_digit_sum = 0
print("Enter numbers. The program will stop when the sum of the digits of all entered numbers exceeds 100.")
print("-" * 80)
while total_digit_sum <= 100:
    num_str = input(f"Current total digit sum is {total_digit_sum}. Enter a number: ")
    number = int(num_str)
    current_digit_sum = 0
    for digit_char in str(abs(number)):
        current_digit_sum += int(digit_char)
    total_digit_sum += current_digit_sum
        
    print(f"-> Sum of digits for {number} is {current_digit_sum}. Running total is now {total_digit_sum}.")
    print("-" * 80)

print("\nThe total sum of digits has exceeded 100. Program terminated.")
print(f"Final total sum of digits: {total_digit_sum}")

#3.Write a program using a while loop to check whether a number is a Duck number (a number containing zero but not starting with zero, e.g., 202, 1203).
num_str = input("Enter a number: ")
number = int(num_str)
temp_number = number
    
found_zero = False
if number <= 0:
        print(f"{number} is not a Duck number (it must be a positive number).")
else:
    while temp_number > 0:
        digit = temp_number % 10        
        if digit == 0:
                found_zero = True
        break       
        temp_number //= 10
    if found_zero:
            print(f"{number} is a Duck number.")
    else:
            print(f"{number} is not a Duck number.")

#4.Write a program using a while loop to accept a number and check if it is a Happy number. (A number is happy if repeatedly replacing it with the sum of squares of its digits eventually reaches 1). Example: 19 is a happy number.
num_str = input("Enter a number: ")
number = int(num_str)
temp_number = number
found_zero = False
if number <= 0:
    print(f"{number} is not a Duck number (it must be a positive number).")
else:
    while temp_number > 0:
        digit = temp_number % 10
            
        if digit == 0:
            found_zero = True
            break
        temp_number //= 10
            
    if found_zero:
        print(f"{number} is a Duck number.")
    else:
        print(f"{number} is not a Duck number.")

#5.Write a program using a while loop to find the largest prime factor of a given number.
original_number = int(input("Enter a number to find its largest prime factor: "))
number = original_number

largest_prime_factor = -1

while number % 2 == 0:
    largest_prime_factor = 2
    number //= 2
i = 3
while i * i <= number:
    while number % i == 0:
        largest_prime_factor = i
        number //= i
    i += 2
if number > 2:
    largest_prime_factor = number

if original_number < 2:
    print("Prime factors are not defined for numbers less than 2.")
else:
    print(f"The largest prime factor of {original_number} is {largest_prime_factor}.")

#6.Write a program to repeatedly accept a string from the user until the string entered is a palindrome.
while True:
        input_string = input("Enter a string (the program will stop when you enter a palindrome): ")
        formatted_string = ""
        for char in input_string:
            if char.isalnum():
                formatted_string += char.lower()

        if formatted_string == formatted_string[::-1]:
            print(f"\nSuccess! '{input_string}' is a palindrome.")
            print("Exiting the program.")
            break
        else:
            print(f"'{input_string}' is not a palindrome. Please try again.")
            print("-" * 20)

#7.Write a program using a while loop to compute the sum of digits of a number until the result becomes a single-digit number (Digital root). Example: 9875 => 9+8+7+5=29 => 2+9=11 => 1+1=2.
original_number_str = input("Enter a number: ")
number = int(original_number_str)
original_number = number
while number > 9:
    sum_of_digits = 0
    temp_number = number
    while temp_number > 0:
        digit = temp_number % 10
        sum_of_digits += digit
        temp_number //= 10
    print(f"The sum of the digits of {number} is {sum_of_digits}.")
    number = sum_of_digits

print(f"\nThe digital root of {original_number} is {number}.")

#8.Write a program using a while loop to generate the Collatz sequence for a given number. (Rule: If n is even => n/2, if odd => 3n+1. Continue until n=1).
number = int(input("Enter a positive integer: "))
if number <= 0:
        print("Please enter a positive integer greater than 0.")
else:
    original_number = number
    sequence = [original_number]


    while number != 1:
        if number % 2 == 0:
            number = number // 2 

        else:
            number = 3 * number + 1
            
    sequence.append(number)

    print(f"\nThe Collatz sequence for {original_number} has been generated.")

#9.Write a program using a while loop to accept a number and check whether it is a Kaprekar number. (Kaprekar number: if square of the number can be split into two parts whose sum equals the number. Example: 452=2025 => 20+25=45).

num = int(input("Enter a number to check if it's a Kaprekar number: "))
if num < 0:
    print("Please enter a non-negative number.")
else:

    square = num ** 2

    square_str = str(square)
    n_digits = len(square_str)
        
    is_kaprekar = False
        
    i = 1
    while i < n_digits:
        part1_str = square_str[:i]
        part2_str = square_str[i:]
        if part2_str:
            part1 = int(part1_str)
            part2 = int(part2_str)
            if part2 != 0 and (part1 + part2 == num):
                is_kaprekar = True
                break 
            
        i += 1
    if num == 1:
        is_kaprekar = True
    if is_kaprekar:
        print(f"{num} is a Kaprekar number.")
    else:
        print(f"{num} is not a Kaprekar number.")

#10.Write a program to simulate an ATM machine using a while loop where a user can:• Check balance• Deposit mone• Withdraw money (only if balance is sufficient)• ExitContinue until the user chooses to exit.

balance = 1000.00
print("Welcome to the ATM Machine!")
run_atm = True
while run_atm:
    print("\n" + "="*30)
    print("      ATM MENU")
    print("="*30)
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    print("="*30)
    user_option = input("Please choose an option (1-4): ")

    if user_option == '1':
        print(f"\nYour current balance is: ₹{balance:.2f}")


    elif user_option == '2':
        deposit_amount = float(input("Enter amount to deposit: ₹"))
        if deposit_amount > 0:
            balance += deposit_amount
            print(f"Successfully deposited ₹{deposit_amount:.2f}")
            print(f"Your new balance is: ₹{balance:.2f}")
        else:
            print("Invalid amount. Please enter a positive number.")


    elif user_option == '3':
        withdraw_amount = float(input("Enter amount to withdraw: ₹"))
        if withdraw_amount <= 0:
            print("Invalid amount. Please enter a positive number.")
        elif withdraw_amount > balance:
            print("Insufficient balance. Cannot withdraw.")
            print(f"Your current balance is: ₹{balance:.2f}")
        else:
            balance -= withdraw_amount
            print(f"Successfully withdrew ₹{withdraw_amount:.2f}")
            print(f"Your remaining balance is: ₹{balance:.2f}")
    
    elif user_option == '4':
        print("\nThank you for using the ATM. Goodbye!")
        run_atm = False 
    else:
        print("Invalid choice. Please select a number from 1 to 4.")