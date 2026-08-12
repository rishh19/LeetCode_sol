class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mp={0:-1}
        rsum=0

        for i in range(len(nums)):

            #running sum
            rsum+=nums[i]

            #remainder
            rem=rsum%k

            #in map
            if rem in mp:
                length = i - mp[rem] #difference between old and current position

                if length >=2:
                    return True
            if rem not in mp:
                mp[rem]= i #store
        return False


