"""Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

eg: 
Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

# Naive solution
def romanToInt(str):

    count = 0
    prev = None
    for num in str:
        if num == 'I':
            count +=1
            prev = num
        elif prev == 'I' and num == 'V':
            count += 3
            prev = num
        elif num== 'V' and prev!='I':
            count += 5
            prev = num
        elif prev == 'I' and num == 'X':
            count +=8
            prev = num
        elif num== 'X' and prev!='I':
            count += 10
            prev = num
        elif prev == 'X' and num == 'L':
            count += 30
            prev = num
        elif num== 'L' and prev!='X':
            count += 50
            prev = num
        elif prev == 'X' and num == 'C':
            count += 80
            prev = num
        elif num== 'C' and prev!='X':
            count += 100
            prev = num
        elif prev == 'C' and num == 'D':
            count +=300
            prev = num
        elif num== 'D' and prev!='C':
            count += 500
            prev = num
        elif prev == 'C' and num == 'M':
            count += 800
            prev = num
        elif num== 'M' and prev!='C':
            count += 1000
            prev = num
    return count


print(romanToInt('MMMXLV'))

#Optimized Solution
def romanToInt_optimized(s):
    dic = {"M": 1000,  "D": 500, "C": 100,
        "L": 50, "X": 10, "V": 5,  "I": 1}
    arr = list(map(lambda x: dic[x], [char for char in s]))
    n = len(arr)
    integer = 0
    for i in range(n-1):
        if arr[i] < arr[i+1]:
            integer -= arr[i]
        else:
            integer += arr[i]
    integer += arr[n-1]
    return integer

print(romanToInt_optimized('MMMXLV'))