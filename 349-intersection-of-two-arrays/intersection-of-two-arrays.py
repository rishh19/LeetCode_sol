class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #seen set for nums2

        seen=set(nums2)

        ans=set()

        for num in nums1:
            if num in seen:
                ans.add(num)
            
        return list(ans)