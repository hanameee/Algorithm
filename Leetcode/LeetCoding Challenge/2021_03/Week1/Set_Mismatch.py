class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        S = sum(list(range(1, len(nums)+1)))
        s = sum(nums)
        duplicated_num = None
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                duplicated_num = nums[i]
        return [duplicated_num, S-s+duplicated_num]
