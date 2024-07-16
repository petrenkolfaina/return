# task1
def square(a,b):
    c= a*b
    return c

print(f"Площа прямокутники: {square(2,5)}")

# task2

def even(a):
    if a % 2 == 0:
        return a
    else:
        print("The number isn`t even")

print(f"{even(10)} is even")

# task3
def fuctorial(a):
    if a < 0:
        print("A negative number can`t be a factorial")
    elif a == 0:
        return 1
    else:
        return a * fuctorial(a-1)

print(fuctorial(6))
# task4

def palindrom(string):
    if string == string[::-1]:
        return True
    else:
        return False

print(palindrom("око"))

# task5
def vowels(word):
    volwes = 'аеоіиєюяї'
    k = 0
    for i in word:
        if i in volwes:
            k += 1
    return k
print(vowels("океан"))

# task6
def sorting(a):
    a.sort()
    return a

print(sorting([5,9,45,8,6]))


# task7
def nsd(a, b):
    while a*b != 0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    return a + b

print (nsd(7, 14))

# task8
def prime(a):
    if a <= 1:
        return False
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True

print(prime(98))

# task9
numbers = [2,8,6,24,128,7]
def average(numbers):
    return sum(numbers)/len(numbers)

print(average(numbers))

"""
# task10
def least(string, n):
    text = string.split()
    word = text()
    for word in text:
        
"""
