def isPalindrome(s):
    # Clean string: keep only alphanumeric, lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    # Check if equals its reverse
    return cleaned == cleaned[::-1]
# Time: O(n) | Space: O(n)

# Two pointer approach (optimal space)
def isPalindrome_twopointer(s):
    left, right = 0, len(s) - 1
    while left < right:
        # Skip non-alphanumeric from left
        while left < right and not s[left].isalnum():
            left += 1
        # Skip non-alphanumeric from right
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
# Time: O(n) | Space: O(1)

# My initial implementation
class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = s.lower()
        word = re.sub(r'[^a-z0-9]',"",word)
        return word==word[::-1]