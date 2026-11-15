# 1. Two Sum

# ============================ Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# ============================ Explanation:
# The sum of nums[0] and nums[1] is 2 + 7 = 9, which equals the target. Therefore, the indices [0, 1] are returned.
# ============================= Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# ============================= Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]
# ============================= Constraints:
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

nums=[2,7,11,15]
target=9
# ===================================== Approch ONE 
''' BRUTE FORCE METHOD '''
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if(nums[i]+nums[j]==target):
#             print( [i,j] )       

# ===================================== Approch TWO
'''reduced the time complexity'''
# def TwoSum(nums,target):
#     for i in range(len(nums)):
#         prod = target - nums[i]
#         if prod in nums and nums.index(prod)!=i:
#             return [i,nums.index(prod)]
# print( TwoSum([2,7,11,15],9))

# ==================================== Approch Three
'''Optimal Approach'''
seen={}
complementry=0
def TwoSum(nums,target):
    for i in range(len(nums)):
        complementry=target-nums[i]
        if complementry not in seen:
            seen[nums[i]]=i
        


print( TwoSum([2,7,11,15],9))
 
