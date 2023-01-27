'''Ques3. Program to calculate the area of a triangle using heron’s formula. (check condition if the combination of
sides is possible).
'''
# Condition to check if the combination of sides is possible
def isValidTriangle(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        return True
    else:
        return False
#arnavvikasgarg
# Function to calculate area using Heron's Formula
def calculateArea(a, b, c):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area
#22105015
# Main program
a = float(input("Enter side 1 of the triangle: "))
b = float(input("Enter side 2 of the triangle: "))
c = float(input("Enter side 3 of the triangle: "))

if isValidTriangle(a, b, c):
    area = calculateArea(a, b, c)
    print("The area of the triangle is", area)
else:
    print("The combination of sides is not possible!")
