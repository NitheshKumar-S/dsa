# Given array nums, return array answer where
# answer[i] = product of all elements except nums[i]

# Must solve in O(n) time. Cannot use division.

# Example:
# Input:  [1, 2, 3, 4]
# Output: [24, 12, 8, 6]

# Because:
# answer[0] = 2*3*4 = 24
# answer[1] = 1*3*4 = 12
# answer[2] = 1*2*4 = 8
# answer[3] = 1*2*3 = 6


# For index i:
# answer[i] = (product of everything LEFT of i)
#           × (product of everything RIGHT of i)

# Array:    [1,  2,  3,  4]

# Prefix:   [1,  1,  2,  6]
#           (nothing left of 0 = 1)
#           (1 left of index 1 = 1)
#           (1×2 left of index 2 = 2)
#           (1×2×3 left of index 3 = 6)

# Suffix:   [24, 12, 4,  1]
#           (2×3×4 right of index 0 = 24)
#           (3×4 right of index 1 = 12)
#           (4 right of index 2 = 4)
#           (nothing right of 3 = 1)

# Answer:   prefix × suffix
#           [1×24, 1×12, 2×4, 6×1]
#         = [24,   12,   8,   6]  ✅

def productExceptSelf(nums):
    n = len(nums)
    result = [1] * n
    
    # Build prefix products into result
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]
    
    # Multiply suffix products into result
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    
    return result

# Time: O(n) | Space: O(1) extra (result array doesn't count)

# Test
print(productExceptSelf([1, 2, 3, 4]))   # [24, 12, 8, 6]
print(productExceptSelf([-1, 1, 0, -3])) # [0, 0, 9, 0]

# I make two passes. First pass left to right — 
# each position stores the product of everything 
# to its left. Second pass right to left — multiply 
# each position by the product of everything to 
# its right. Result is product of all elements 
# except itself.