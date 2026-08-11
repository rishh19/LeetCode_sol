class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count=0
        n=len(nums)
        p_sum = 0
        mp={0:1}

        for i in range(n):
            p_sum+=nums[i]

            rem=p_sum%k

            if rem<0:
                rem+=k

            if rem in mp:
                count+=mp[rem]
            
            mp[rem] = mp.get(rem,0)+1

        return count
            
