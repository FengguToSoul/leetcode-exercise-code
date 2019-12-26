class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            res = target - nums[i]
            if res in nums:
                if nums.index(res) == i and nums.count(res) > 1:
                    nums[nums.index(res)] = target + 1
                if nums.index(res) == i and nums.count(res) == 1:
                    continue
                return [i, nums.index(res)]
