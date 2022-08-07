#https://lonely-journalclub.com/algorithm/leetcode/post-319/

#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#from typing import List

#nums is the list given and target is the target int

class Solution:
    # frm python 3.9, we have list support
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Dictionary can be used as hashmap or hash table in python
        hashmap = {}
        # for loop in
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i


res = Solution()

nums = [2, 7, 11, 15]
target = 9
out = res.twoSum(nums, target)
print(f'nums: {nums} target: {target} The output array: {out}')