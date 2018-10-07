###########HACKERRANK CODE###############
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
#---->MY CODE<----
def timeInWords(h, m):
    time_in_words = ""
    
    in_words = {1 : "one", 2 : "two", 3 : "three", 4 : "four", 5 : "five", 6 : "six", 7 : "seven"
               , 8: "eight", 9 : "nine", 10 : "ten", 11 : "eleven", 12 : "twelve",
                13 : "thirteen", 14 : "fourteen", 15 : "quarter", 16 : "sixteen", 
                17 : "seventeen", 18 : "eighteen", 19 : "nineteen", 20 : "twenty", 30 : "half"}
    if m == 0:
        time_in_words = in_words[h] + " o' clock"
        print(time_in_words)
    elif m == 1:
        time_in_words = in_words[m] + " minute past " + in_words[h] 
        print(time_in_words)
    elif m == 15 or m == 30:
        time_in_words = in_words[m] + " past " + in_words[h]
        print(time_in_words)
    elif m == 45:
        time_in_words = in_words[15] + " to " + in_words[h+1]
        print(time_in_words)
    else:
        if m <= 20:
            time_in_words = in_words[m] + " minutes past " + in_words[h]
            print(time_in_words)
        else:
            if m < 30:
                time_in_words = in_words[(m - (m%10))] + " " + in_words[m%10] 
                time_in_words += " minutes past " + in_words[h] 
                #broken into two lines for better readability
                print(time_in_words)
            else:
                m = 60 - m  
                if m <= 20:
                    time_in_words = in_words[m] + " minutes to " + in_words[h+1]
                    print(time_in_words)
                else:
                    time_in_words = in_words[(m - (m%10))] + " " + in_words[m%10] 
                    time_in_words += " minutes to " + in_words[h + 1] 
                    #broken into two lines for better readability
                    print(time_in_words)
    return time_in_words
    
###########HACKERRANK CODE###############
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
