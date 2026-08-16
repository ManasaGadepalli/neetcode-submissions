class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for index, value in enumerate(nums):
            complement = target - value
            if complement in dict:
                return [dict[complement], index]
            else:
                dict[value] = index
            
        