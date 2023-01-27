'''Ques8-Input 10 integer values from the user. Write a python program to find and print the following:
a. positive numbers
b. negative numbers
c. odd numbers
d. even numbers
e. Number of times each number occurs in the List'''
list_nums = []
for i in range(10):
    num = int(input('Enter a number: '))#22105015
    list_nums.append(num)
# Positive numbers
print('Positive numbers: ', end='')
for i in list_nums:
    if i >= 0:
        print(i, end=' ')
print()

# Negative numbers
print('Negative numbers: ', end='')
for i in list_nums:
    if i < 0:#22105015
        print(i, end=' ')
print()#22105015

# Odd numbers
print('Odd numbers: ', end='')#22105015
for i in list_nums:
    if i % 2 != 0:
        print(i, end=' ')
print()
#22105015
# Even numbers
print('Even numbers: ', end='')#22105015
for i in list_nums:
    if i % 2 == 0:
        print(i, end=' ')
print()#22105015

# Number of times each number occurs in the List
for i in list_nums:#22105015
    print(f'{i} occurs {list_nums.count(i)} times in the list')
