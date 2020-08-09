"""
Description: The sequence of triangle numbers
is generated by adding the natural numbers. 
The 7th triangle number would be:
1+2+3+4+5+6+7 = 28. We can see that 
28 is the first triangle number to have over 
five divisors 

**Note this experiences a time out for tests 5-8 
import math
def highlyDivisibleTriangularNumber(divisors):
    sumOfNaturalNumbers = 1 
    naturalNumber = 2a
    while(True):
        divisorCount = 0 
        divisorList = [] 
        for i in range(1, int(math.ceil(math.sqrt(sumOfNaturalNumbers)))):
            if(sumOfNaturalNumbers % i  == 0):
                divisorCount += 1 
                divisorList.append(i) 
            if (divisorCount * 2 > divisors):
                print(sumOfNaturalNumbers)
                return sumOfNaturalNumbers
        sumOfNaturalNumbers += naturalNumber
        naturalNumber += 1

t = int(input())
for a0 in range(t):
    n = int(input())
    highlyDivisibleTriangularNumber(n)

"""