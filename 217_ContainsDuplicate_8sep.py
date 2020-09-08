"""
Link - https://leetcode.com/problems/contains-duplicate/
Statement - Given an array of integers, find if the array contains any duplicates.
            Your function should return true if any value appears at least twice in the array, 
            and it should return false if every element is distinct.

Example 1:
    Input: [1,2,3,1]
    Output: true
"""

def containsDuplicate(nums):
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
    return False

def containsDuplicate(nums):
    return len(set(nums))!= len(nums)

def containsDuplicate(nums):
    dic = {}
    return len(dic.fromkeys(nums))!= len(nums)


nums = [3,3,5,6]
print(containsDuplicate(nums))