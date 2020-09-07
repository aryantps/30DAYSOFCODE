"""
link - https://leetcode.com/problems/plus-one/

Statement - Given a non-empty array of digits representing a non-negative integer, 
            increment one to the integer.
            The digits are stored such that the most significant digit is at the head of the list, 
            and each element in the array contains a single digit.
            You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
    Input: digits = [1,2,3]
    Output: [1,2,4]
"""

def plusOne(digits):
    if digits[0] == 0:
        return 1
    result = ''
    for i in digits:
        result += str(i)
    result = [int(d) for d in str(int(result) + 1)]

    return result



def plusOne(digits):
    result = 0
    for i in range(len(digits)):
    	result += digits[i] * pow(10, (len(digits)-1-i))
    return [int(i) for i in str(result+1)]



digits = [1,2,3]#[4,3,2,1]
print(plusOne(digits))



