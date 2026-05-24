"""
Problem: Longest Substring Without Repeating Characters
LeetCode #3 | Difficulty: Medium
Topic: Sliding Window, HashSet/HashMap

Pattern: Sliding Window
- Two pointers: left and right
- Expand right each iteration
- Shrink left when duplicate found
- Track maximum window size

Approach 1: HashSet + while loop
Time: O(n) | Space: O(n)

Approach 2: HashMap (jump left directly)
Time: O(n) | Space: O(n)
More efficient — no inner loop
"""

def lengthOfLongestSubstring(s):
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length

def lengthOfLongestSubstring_optimized(s):
    char_index = {}
    left = 0
    max_length = 0
    
    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        char_index[char] = right
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Tests
tests = ["abcabcbb", "bbbbb", "pwwkew", "", "a", "dvdf"]
for t in tests:
    print(f'"{t}" → {lengthOfLongestSubstring_optimized(t)}')
# "abcabcbb" → 3
# "bbbbb"    → 1
# "pwwkew"   → 3
# ""         → 0
# "a"        → 1
# "dvdf"     → 3

# My initial implementation
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = []
        maxi = 0
        for i in s:
            if i in substring:
                substring = substring[substring.index(i)+1:]
            substring.append(i)
            maxi = max(maxi,len(substring))
        return maxi