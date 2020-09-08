"""
link - https://leetcode.com/problems/merge-sorted-array/
Statement - Given two sorted integer arrays nums1 and nums2, 
            merge nums2 into nums1 as one sorted array.

Example:
    Input:
        nums1 = [1,2,3,0,0,0], m = 3
        nums2 = [2,5,6],       n = 3
    Output: [1,2,2,3,5,6]
"""
def merge(nums1, m, nums2, n):
   
    i = m - 1
    j = n - 1
    k = m + n - 1
    while i >= 0 and  j >= 0:
        if nums1[i] < nums2[j]:
            nums1[k] = nums2[j]
            nums2.remove(nums2[j])
            j = j -1
        else:
            nums1[k] = nums1[i]
            i = i - 1
        k = k - 1
    if j>=0:
        nums1[:k+1] = nums2[:j+1]
    #return nums1


def merge(nums1, m, nums2, n):
    k = m+n-1
    while m > 0 and n > 0:
        if nums1[m-1] < nums2[n-1]:
            nums1[k] = nums2[n-1]
            n = n -1
        else:
            nums1[k] = nums1[m-1]
            m = m - 1
        k = k - 1
    if n > 0:
        nums1[:n] = nums2[:n]
    #return nums1



nums1 = [1,2,3,0,0,0]
m =3
nums2 = [2,5,6]#[1,2,3]
n = 3

print(merge(nums1, m, nums2, n))
