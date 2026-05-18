class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        distinct = set(nums)
        if(len(distinct)==len(nums)):
            return False
        return True