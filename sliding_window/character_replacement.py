# Given string s and integer k, you can replace 
# at most k characters in the string.
# Find length of longest substring containing 
# the same letter after replacements.

# Example:
# Input:  s = "AABABBA", k = 1
# Output: 4

# Explanation: Replace one 'B' with 'A'
# "AABABBA" → "AAABBA" or consider "AABA" = 4

# Key insight:
# Window is valid when:
# (window_size - count_of_most_frequent_char) <= k

# Why? 
# The characters we need to REPLACE = 
# window_size - most_frequent_count

# If replacements needed <= k → window is valid

def characterReplacement(s, k):
    count = {}      # frequency of each char in window
    left = 0
    max_freq = 0    # highest frequency char in window
    max_length = 0
    
    for right in range(len(s)):
        # Add right character to window
        char = s[right]
        count[char] = count.get(char, 0) + 1
        
        # Update max frequency
        max_freq = max(max_freq, count[char])
        
        # Check if window is valid
        window_size = right - left + 1
        replacements_needed = window_size - max_freq
        
        if replacements_needed > k:
            # Window invalid — shrink from left
            count[s[left]] -= 1
            left += 1
        
        # Update answer (window size is always valid or just shrunk by 1)
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Time: O(n) | Space: O(26) = O(1)

print(characterReplacement("ABAB", 2))    # 4
print(characterReplacement("AABABBA", 1)) # 4

"""
i didn't try to solve this problem on my own, i did it for streak i will learn it later
"""     
