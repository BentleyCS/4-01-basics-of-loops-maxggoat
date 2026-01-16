#All questions must use a loop for full points.

def oddNumbers(n:int) ->str:
    """
    Print out all odd numbers from 1 to n(inclusive) in a single string separated by spaces.
    example oddNumbers(5) -> "1 3 5"
    example oddNumbers(8) -> "1 3 5 7"
    example oddNumbers(-8) -> ""
    """

    str0 = ""
    i=0
    x=n
    while i<=x:
        if i%2==1:
            if i==1:
                str0 = str0  + str(i)
            else:
                str0 = str0 + " " + str(i)
        i=i+1
    print(str0)

oddNumbers(5)
oddNumbers(8)
oddNumbers(-8)
oddNumbers(80)

def backwards(n)-> int:
    """
    modify the below function such that it prints out all the numbers from n to 1
    inclusive starting at n and counting down to 1
    example backwards(5) -> "5 4 3 2 1"
    example backwards(8) -> "8 7 6 5 4 3 2 1"
    example backwards(-2) -> ""
    """
    x=n
    i=x
    str0=""
    while i>0:
       if i==x:
           str0=str0 +str(i)
       else:
           str0 = str0 + " " + str(i)
       i=i-1
    print(str0)

backwards(5)

def randomRepeating():
    """
    Print out a random number from 1-10 until you get a 10. Then print out how many
    times it took to roll a 10
    NOTE: Given randomness no test for this question
    :return:
    """
    import random

    tries = 0
    roll = 0
    while roll != 10:
        roll = random.randint(1, 10)
        tries = tries + 1
    print(f"it took {tries} tries to get a 10")

def randomRange(n):
    """
    Generate a random number from 1 to 100 n number of times. Then after that is
    done print out what the highest number and the lowers number was from the rolled numbers.
    NOTE: Given randomness no test for this question
    :param n:
    :return:
    """
    import random

    x = []
    for i in range(n):
        roll = random.randint(1, 100)
        x.append(roll)
    x.sort()
    print(x[0])

randomRange(10)

def reverse(word:str)->str:
    """
    Takes in a string as an argument and return the given string in reverse.
    example reverse("cat") -> "tac"
    example reverse("Hello") -> "olleH"
    """
    str0 = word
    str1=""
    x=len(str0)
    i=x
    while i>0:
        str1=str1+str0[i-1]
        i=i-1
    print(str1)

SS=reverse("Hello")
reverse("Hello World")

def fizzBuzzContinuous(n):
    """
    Modify the function such that it does the fizzbuzz operation on all numbers
    from 1 to n(inclusive).
    Fizz buzz is defined as
    if the number is divisible by 3 print fizz
    if the number is divisible by 5 print buzz
    if the number is divisible by both 3 and 5 print fizzbuzz
    if none of the above apply print the number.

    As with above questions add each answer to a string and return the final string.
    :param n:
    :return:
    """
    str0=""
    for i in range(n):
        i1=i+1
        if i1==1:
            str0=str0+str(i1)
        else:
            if i1 % 3 == 0 and i1 % 5 == 0:
                str0=str0+ " " + "FizzBuzz"
            if i1 % 3 == 0 and i1 % 5 != 0:
                str0=str0+ " " + "Fizz"
            if i1 % 5 == 0 and i1 % 3 != 0:
                str0=str0+ " " + "Buzz"
            if i1 % 5 != 0 and i1 % 3 != 0:
                str0 = str0 + " " + str(i1)

    print(str0)

fizzBuzzContinuous(15)

def collatz(n):
    """
    Modify this function such that it mimics the collatz conjecture starting at n
    and prints out each number.
    The collatz conjecture is that if n is an even number divide it by 2. if n is
    an odd number multiply it by 3 and add 1.
    Repeat this process until n == 1.
    :param n:
    :return:
    """
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            print(n)
        else:
            n = 3*n + 1
        print(n)

collatz(5)


def fibonacci(n):
    """
    for the given argument n print out the first n numbers of the fibonacci
    sequence in a single string separated by spaces.
    The fibonacci sequence is defined as a sequence that starts with 0 then 1 as
    the first two numbers. Every subsequent number is the prior two numbers added together.
    Example fibonacci(6) -> "0 1 1 2 3 5"
    Example fibonacci(10) -> "0 1 1 2 3 5 8 13 21 34"
    Example fibonacci(1) -> "0"
    :param n:
    :return:
    """
    if n == 1:
        print("fibonacci(0) -> 0")
    if n == 2:
        print("fibonacci(1) -> 0 1")
    if n >= 3:
        x=[0,1]
        str0="fibonacci(1) -> 0 1"
        i=3

        while i <= n:
            str0=str0+" "+str(x[i-3] + x[i-2])
            x.append(x[i - 3] + x[i - 2])
            i=i+1

    print(str0)

fibonacci(300)
