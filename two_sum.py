#https://lonely-journalclub.com/algorithm/leetcode/post-319/


#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#nums is the list given and target is the target int

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary can be used as hashmap or hash table in python
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i