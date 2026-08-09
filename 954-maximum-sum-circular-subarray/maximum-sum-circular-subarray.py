class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = nums[0]
        min_sum = nums[0]

        max_best = nums[0]
        min_best = nums[0]

        total = nums[0]

        for i in range(1, len(nums)):
            best_max_sum = max_sum
            best_min_sum = min_sum

            max_sum = max(best_max_sum + nums[i], nums[i])
            min_sum = min(best_min_sum + nums[i], nums[i])

            max_best = max(max_best, max_sum)
            min_best = min(min_best, min_sum)

            total += nums[i]

        if max_best < 0:
            return max_best

        circular_max = total - min_best

        return max(max_best, circular_max)