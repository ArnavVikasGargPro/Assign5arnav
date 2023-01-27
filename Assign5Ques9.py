#Write a program to count the number of occurences of each word in the list (List entered by the user)
#22105015 ECE 
x=str(input("Please enter the list of words you want to check with space between them :----"))
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count(x))
#22105015 
