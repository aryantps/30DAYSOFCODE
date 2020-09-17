def isPalindrome(x):
    palindrome = ""
    for i in range(len(str(x))-1,-1,-1):
        palindrome += str(x)[i]

    return (palindrome) == str(x)

x = -121
print(isPalindrome(x))