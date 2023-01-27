'''Ques7-Write a python program to find the numbers which are multiple of 7 and divisible by 11 in the range
1-500'''
# enter the starting range number
start_num = int(1)
  
# enter the ending range number
end_num = int(500)
  
# initialise counter with starting number
cnt = start_num
  
# check until end of the range is achieved
while cnt <= end_num:
    
    # if number divisible by 7 and 5
    if cnt % 7 == 0 and cnt % 11 == 0:
        print(cnt, " is multiple of 7and divisible by 11.")          
        # increment counter
    cnt += 1
#22105015
