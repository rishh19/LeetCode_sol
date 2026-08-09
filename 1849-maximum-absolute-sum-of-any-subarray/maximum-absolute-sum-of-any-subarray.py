class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0

        max_sum=nums[0]
        min_sum=nums[0]
        res=abs(nums[0])

        for i in range(1,n):
            best_sum_max = max_sum
            best_sum_min = min_sum

            max_sum = max(best_sum_max+nums[i],nums[i])
            min_sum = min(best_sum_min+nums[i],nums[i])

            res=max(res,max_sum,abs(min_sum))
        
        return res