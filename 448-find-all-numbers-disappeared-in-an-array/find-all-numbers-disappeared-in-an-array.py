class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)

        # mark seen
        for num in nums:
            
            # get index
            index=abs(num)-1
            
            # mark negative
            nums[index] = -abs(nums[index])

        # missing numbers
        ans=[]
        for i in range(n):
            if nums[i] > 0:
                ans.append(i+1)

        return ans