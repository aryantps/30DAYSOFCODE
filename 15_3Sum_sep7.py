"""
Link - https://leetcode.com/problems/3sum/

Statement - Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
            Find all unique triplets in the array which gives the sum of zero.
            Notice that the solution set must not contain duplicate triplets.


Example 1:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
"""
# #Approch1
# def threeSum(nums):
#     n = len(nums)
#     for i in range(0,n-2):
#         for j in range(1,n-1):
#             for k in range(2,n):
#                 if nums[i] + nums[j] + nums[k] == 0:
#                     print(nums[i],nums[j],nums[k])
# nums = [-1,0,1,2,-1,-4]
# threeSum(nums)


# [[1, 1], [0, 1]]


# #Approch2 - Two pointers algo
# def threeSum(nums):
#     Sum3 = list()
#     n = len(nums)
#     nums.sort()

#     for i in range(n):
        
#         if i > 0 and nums[i] == nums[i-1]: continue
        
#         leftPointer = i+1
#         rightPointer = n-1

#         while leftPointer < rightPointer:
#             if (nums[leftPointer] + nums[rightPointer] == - nums[i]):
#                 Sum3.append([nums[i],nums[leftPointer],nums[rightPointer]])
#                 print(nums[i],nums[leftPointer],nums[rightPointer])
#                 print('left index : ',leftPointer)
#                 print('right index : ',rightPointer)

#                 leftPointer+= 1
#                 rightPointer-=1        
#             elif (nums[leftPointer] + nums[rightPointer] < - nums[i]):
#                 leftPointer += 1
#             else:
#                 rightPointer -= 1
#     print('three sum : ',(Sum3))
#     print(removeDuplicates(Sum3))

# nums = [-2,0,0,2,2]#[-1,0,1,2,-1,-4]
# threeSum(nums)


# def removeDuplicates(lst):
#     '''
#     Remove Duplicates From a Python List of Lists
#     '''

#     #lst = [[1, 1], [0, 1], [0, 1], [1, 1]]

#     dup_free = []
#     dup_free_set = set()
#     for x in lst:
#         if tuple(x) not in dup_free_set:
#             dup_free.append(x)
#             dup_free_set.add(tuple(x))

#     return(dup_free)



def threeSum(nums):
    Sum3 = list()
    unique = set()
    n = len(nums)
    nums.sort()

    for i in range(n):
        
        unique.clear()

        if i > 0 and nums[i] == nums[i-1]: continue
        
        leftPointer = i+1
        rightPointer = n-1

        while leftPointer < rightPointer:
            if (nums[leftPointer] + nums[rightPointer] == - nums[i]):

                if nums[leftPointer] not in unique: 
                    Sum3.append([nums[i],nums[leftPointer],nums[rightPointer]])
                    print(nums[i],nums[leftPointer],nums[rightPointer])
                    print('left index : ',leftPointer)
                    print('right index : ',rightPointer)
                    unique.add(nums[leftPointer])

                leftPointer+= 1
                rightPointer-=1        
            elif (nums[leftPointer] + nums[rightPointer] < - nums[i]):
                leftPointer += 1
            else:
                rightPointer -= 1
    print('three sum : ',(Sum3))

nums = [-2,0,0,2,2]#[-1,0,1,2,-1,-4]
threeSum(nums)