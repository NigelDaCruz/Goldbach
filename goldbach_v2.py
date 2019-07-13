# Program  to implement Goldbach's conjecture and verify that a given number satisfies the condition.
# For a given number, program returns either one pair of primes that sum to the number or all pairs
# of primes that sum to that number


import math

# function checks if a number N is prime by checking if it's divisible by a number from
# 2 upto the square root of N (rounded up to nearest integer) 
def isPrime(isPrimeNum):
    if isPrimeNum == 2:
        return True
    else:
        for i in range(2, round(math.sqrt(isPrimeNum)+0.5)+1):
            if isPrimeNum % i == 0:
                prime = False
                break
            else:
                prime = True
        return prime 


print("""This program verifies Goldbach's conjecture, that is:
'Every positive even number greater than 2 is the sum of two prime numbers'.""")
print("""For a given valid number the program will return either two primes that sum to
that number or return all pairs of primes that sum to that number.""")
print()

number = input('Please enter an even number greater than 2: ')

#try block to check the input is an integer and a valid number
try:
    integer = int(number)
except ValueError:
    valid = False
else:
    if int(number) % 2 == 0 and int(number) > 2:
        valid = True
    else:
        valid = False

while valid == False:
    number = input('Invalid input, please enter an even number greater than 2: ')
    try:
        integer = int(number)
    except ValueError:
        valid = False
    else:
        if int(number) % 2 == 0 and int(number) > 2:
            valid = True
        else:
            valid = False

number = int(number)

allPairs = input('Would you like all pairs of primes? Enter y for yes and n for no: ')

if allPairs == 'y':
    returnAllPairs = True
    validLetter = True
elif allPairs == 'n':
    returnAllPairs = False
    validLetter = True
else:
    validLetter = False

while validLetter == False:
    allPairs = input('Invalid input, would you like all pairs of primes? Enter y for yes and n for no: ')
    if allPairs == 'y':
        returnAllPairs = True
        validLetter = True
    elif allPairs == 'n':
        returnAllPairs = False
        validLetter = True

primePairs = []

if returnAllPairs == True:
    if isPrime(number - 2) == True:
        pair = (2, number - 2)
        primePairs.append(pair)
    for j in range(3, number // 2+1, 2):    #iterating through odd numbers from 3 upto halfway to number
        if isPrime(j) == True:
            if isPrime(number - j) == True:
                pair = (j, number - j)
                primePairs.append(pair)
    print(primePairs)
elif returnAllPairs == False:
    if isPrime(number - 2) == True:
        pair = (2, number - 2)
        print(pair)
    for j in range(3, number // 2+1, 2):
        if isPrime(j) == True:
            if isPrime(number - j) == True:
                pair = (j, number - j)
                print(pair)
                break
