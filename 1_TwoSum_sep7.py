"""
Link - https://leetcode.com/problems/two-sum/

Statement - Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
            You may assume that each input would have exactly one solution, and you may not use the same element twice.
            You can return the answer in any order.

Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Output: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

def twoSum(nums,target):
    n = len(nums)
    lst = sorted(nums)
    left = 0
    right = n-1
    while left < right:
        print(f"left pointer is {left} and right pointer is {right}")
        if lst[left] + lst[right] == target:
            return ([nums.index(lst[left]), nums.index(lst[right])])
        elif lst[left] + lst[right] < target:
            left += 1
        else:
            right -=1

nums = [3,2,4] #[2,7,11,15]          # 
target = 6
print(twoSum(nums,target))

