class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        need = {}

        for num in range(len(nums)):

            if nums[num] in need:
                return [need[nums[num]], num]

            asw = target - nums[num]
            need[asw] = num

        return [0,0]
