import random

def random_list():
    list = []
    for i in range(10):
        list.append(random.randint(0,100))
    return list

def max_num():
    list_ = random_list()
    el = list_[0]
    for i in range(len(list_)):
        if el < i:
            el = i
    return el

def min_num():
    list_ = random_list()
    el = list_[0]
    for i in range(len(list_)):
        if el > i:
            el = i
    return el

print(f" Випадковий список: {random_list()}")
print(f"Максимальне число: {max_num()}")
print(f"Мінімальне число:{min_num()}")