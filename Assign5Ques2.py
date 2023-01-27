'''ques2--Python Program to Print all Numbers in a Range Divisible by a Given Number. (user inputs the range
and the number)
'''
#22105015
lowernum = int(input("Enter lower range limit..."))
uppernum = int(input("Enter upper range limit..."))
divnum = int(input("Enter the number that should be divided by..."))
for i in range(lowernum,uppernum+1):
   if(i%divnum==0):
      print(i)
'''ece22105015arnavvikasgarg'''
