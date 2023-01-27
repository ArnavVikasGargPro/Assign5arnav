#Ques6-Write a python program to print the prime numbers for a user input range.
min = int(input("Enter the number to start  : "))
max = int(input("Enter the number till where you want the prime no to come : "))
if max>min and max>=0 and min>=0:
 for n in range(min,max + 1):
   if n > 1:
       for i in range(2,n):
           if (n % i) == 0:
               break
       else:
           print(n)
else:
    print("pls put right range ")
#madeby22105015Arnav
