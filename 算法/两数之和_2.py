class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_buff = {}
        for index, num in enumerate(nums):
            another_num = target - nums[index]
            if another_num in dict_buff:
                return [dict_buff[another_num], index]
            dict_buff[num] = index
        return None
