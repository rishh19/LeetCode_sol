class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        total=sum(nums)

        left=0

        #finding pivot index
        for i in range(len(nums)):
            right=total-nums[i]-left

            if left==right:
                return i
            #update left by moving ahead  
            left+=nums[i]
        return -1
        

