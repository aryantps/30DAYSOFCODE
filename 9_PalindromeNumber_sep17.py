"""

link - https://leetcode.com/problems/palindrome-number/
Statement - Determine whether an integer is a palindrome. 
            An integer is a palindrome when it reads the same backward as forward.
Example:
    Input: 121
    Output: true

"""

# def isPalindrome(x):
#     palindrome = ""
#     for i in range(len(str(x))-1,-1,-1):
#         palindrome += str(x)[i]

#     return (palindrome) == str(x)


#2nd approch
# def isPalindrome(x):
#     if x < 0 or (x % 10 ==0 and x != 0):
#         return False
        
# # reverse of the last half of the palindrome should be the same as the first half of the number, 
# # if the number is a palindrome.
# # example,input - 1221, if we can revert the last part of the number "1221" from "21" to "12", and compare it with the first half of the number "12"


#     revert = 0
#     while(x>revert):
#         revert = revert * 10 + x % 10
#         x = x // 10
        
#     return x == revert or x == revert // 10

#pythonic solution
def isPalindrome(x):
    if x < 0 or (x % 10 ==0 and x != 0):
        return False

    return (str(x)[::-1]) == str(x)


x = -121
print(isPalindrome(x))