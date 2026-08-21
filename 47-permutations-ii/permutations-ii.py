class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans=[]

        def bt(path,remain):
            if len(remain)==0:
                ans.append(path.copy())
                return

            used=set()

            for i in range(len(remain)):
                num=remain[i]

                if num in used:
                    continue

                used.add(num)

                bt(path+[num],remain[:i]+remain[i+1:])

        bt([],nums)

        return ans