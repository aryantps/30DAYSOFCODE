"""
link - https://leetcode.com/problems/first-missing-positive/

Statement - Given an unsorted integer array, find the smallest missing positive integer.

Example 1:
    Input: [1,2,0]
    Output: 3
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
            return index
        else:
            index += 1
    if index > maxi:
        return maxi + 1
nums = [-5]#[1,2,0]#[7,8,9,11,12]
print(firstMissingPositive(nums))

