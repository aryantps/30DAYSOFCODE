def check_pal(string):
    #print(string[::-1])
    return string[::-1] == string

def longestPalindrome(s):
    dict = {}
    for i in range(len(s)):
        print(f'i = {i} and string is {s[i:]} and {s[:i]}')
        string1 = s[i:]
        string2 = s[:i]
        if check_pal(string1)==True:
            dict[len(string1)] = string1
        if check_pal(string2)==True:
            dict[len(string2)] = string2
    #print(dict)
    print(dict[max(dict.keys())])
        
        
        
(longestPalindrome("babad"))
#print(check_pal('bab'))