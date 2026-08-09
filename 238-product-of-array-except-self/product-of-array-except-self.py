class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)

        answer=[0]*n

        #left product
        left=1

        for i in range(n):
            answer[i]=left
            left*=nums[i]

        #right product

        right=1

        for i in range(n-1,-1,-1):
            answer[i]=answer[i]*right
            right=right*nums[i]

        return answer