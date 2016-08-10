#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import sys

def lcm():
    for i in xrange(2520,sys.maxint,2520):
        if all(i % j == 0 for j in xrange(11,21)):
            return i
print lcm()




#10 = > 5, 2
#9 = > 3
#8 = > 4, 2
#7 = > 7
#6 = 3, 2


#20 => 20 10,5,4,2
#19 = > 19
#18 = > 18, 9,6 ,3 2
#17 = 17
#16 = 16, 8, 4, 2
#15 = 15, 5, 3
#14 = 14, 7, 2
#13 = 13
#12 = 12, 6, 4, 3, 2
#11 = 11,





