"""
Link - https://leetcode.com/problems/friends-of-appropriate-ages/
Statement - Some people will make friend requests. 
            The list of their ages is given and ages[i] is the age of the ith person. 
            Person A will NOT friend request person B (B != A) 
            if any of the following conditions are true:
                age[B] <= 0.5 * age[A] + 7
                age[B] > age[A]
                age[B] > 100 && age[A] < 100
            Otherwise, A will friend request B.
            Note that if A requests B, B does not necessarily request A.  
            Also, people will not friend request themselves.
            How many total friend requests are made?
Example 1:
    Input: [16,16]
    Output: 2
"""

# def numFriendRequests(ages):
#     total_req = 0
#     for i in range(len(ages)):
#         for j in range(len(ages)):
#             if i != j:
#                 if (ages[j] > 0.5 * ages[i] + 7) and (ages[j] <= ages[i]):
#                     total_req += 1
               

               
#     return total_req


def numFriendRequests(ages):
    if not ages:
        return 0
    count = [0] * 121
    for age in ages:
        count[age]+=1
    total_req = 0

    for i in range(120,-1,-1):
        for j in range(i,-1,-1):
            if j <= i*0.5 + 7:
                break 
            total_req += count[i] * count[j]
            
            # We might have counted some cases twice. For people with same age,
            if i == j:
                total_req -= count[i]
    return total_req


ages = [20,30,100,110,120]
print(numFriendRequests(ages))
