# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: [1, 2, 3, 1]
# Output: true

# Explanation: The element 1 occurs at the indices 0 and 3.

# Example 2:
# Input: [1, 2, 3, 4]
# Output: false

# Explanation: All elements are distinct.

# Example 3:
# Input: [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

# Output: true

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

lis=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
seen = set()
def containsDuplicate(nums):
    # for num in nums:
    #     if nums.count(num)>1:
    #         return True
    #     return False
    
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
print(containsDuplicate(lis))



