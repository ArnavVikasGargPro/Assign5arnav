'''Ques5-Write a python program to print a triangular pattern of the alphabet (user input the number of rows).
Example: Input the number of rows = 5, then the pattern should come out as given below.
If the count of the alphabet gets exhausted, repeat the alphabet from A.

A
BC
DEF
GHIJ
KLMNO'''
num_rows = int(input("Input the number of rows:"))
#22105015
alphabets = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
alphabet_index = 0
for row in range(1, num_rows + 1):
    for column in range(1, row + 1):
        print(alphabets[alphabet_index], end="")
        alphabet_index += 1
        if alphabet_index == len(alphabets):
            alphabet_index = 0
    print()
