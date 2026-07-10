class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, value in enumerate(nums):
            complement = target - nums[i]
            if complement in dict:
                return [dict[complement], i]
            else:
                dict[value] = i