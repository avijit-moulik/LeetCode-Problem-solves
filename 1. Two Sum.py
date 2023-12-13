class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_len = len(nums)
        
        for i in range(num_len):
            for j in range(num_len):
                if i == j:
                    continue
                ans = nums[i] + nums[j]
                if ans == target:
                    return [i, j]
