"""
link- https://leetcode.com/problems/letter-combinations-of-a-phone-number/
Statement - Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
            A mapping of digit to letters (just like on the telephone buttons) is given below. 
            Note that 1 does not map to any letters.

Example:
    Input: "23"
    Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""

def letterCombinations(digits):
    if digits == "":
        return []
    output_str = [""]
    dict =     {'2' : 'abc',
               '3' : 'def',
               '4':  'ghi',
               '5' : 'jkl',
               '6' : 'mno',
               '7' : 'pqrs',
               '8' : 'tuv',
               '9' : 'wxyz'}
    for i in digits:
        lst = dict[i]
        temp = []
        for char_ in lst:
            for string in output_str:
                temp.append(string+char_)
        output_str = temp
    return output_str


# def letterCombinations(digits):
#     if digits == "":
#         return []
#     output_str = [""]
#     dict =     {'2' : 'abc',
#                '3' : 'def',
#                '4':  'ghi',
#                '5' : 'jkl',
#                '6' : 'mno',
#                '7' : 'pqrs',
#                '8' : 'tuv',
#                '9' : 'wxyz'}
    

                    
if __name__ == "__main__":
    print(len(letterCombinations("726")))