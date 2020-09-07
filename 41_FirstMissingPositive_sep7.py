"""
link - https://leetcode.com/problems/first-missing-positive/
"""


def firstMissingPositive(nums):
    if len(nums)!=0:
        maxi = max(nums)
        if maxi < 0:
            return 1
        else:
            return 1
    index = 1
    result = None
    while index <= maxi:
        #print(f'index : {index} and result : {result}')
        if index not in nums:
            result = index
            break
        else:
            index += 1
    if index > maxi:
        result = maxi + 1
    return result
nums = [-5]#[1,2,0]#[7,8,9,11,12]
print(firstMissingPositive(nums))

