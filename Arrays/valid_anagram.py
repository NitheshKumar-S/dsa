"""
Problem: Valid Anagram (LeetCode #242)
Difficulty: Easy
Topic: Arrays, Hashing, Strings
Link: https://leetcode.com/problems/valid-anagram/

Approach 1: Sorting
Time: O(n log n) | Space: O(n)
Sort both strings — anagrams are identical when sorted

Approach 2: HashMap (Optimal)
Time: O(n) | Space: O(n)
Count character frequency in s, subtract for t

Approach 3: Counter (Cleanest)
Time: O(n) | Space: O(n)
Python Counter does frequency map automatically

Key insight:
Anagrams have identical character frequency maps.
Counter(s) == Counter(t) checks this directly.
"""

from collections import Counter

# Approach 1: Sorting
def isAnagram_sort(s, t):
    return sorted(s) == sorted(t)

# Approach 2: HashMap
def isAnagram_hashmap(s, t):
    if len(s) != len(t):
        return False
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for char in t:
        count[char] = count.get(char, 0) - 1
        if count[char] < 0:
            return False
    return True

# Approach 3: Counter
def isAnagram_counter(s, t):
    return Counter(s) == Counter(t)

# My intial implementation
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res = t

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in res:
                res = res.replace(s[i], "", 1)
            else:
                return False

        return len(res) == 0

# Tests
print(isAnagram_counter("anagram", "nagaram"))  # True
print(isAnagram_counter("rat", "car"))           # False
print(isAnagram_counter("listen", "silent"))     # True
print(isAnagram_counter("hello", "world"))       # False