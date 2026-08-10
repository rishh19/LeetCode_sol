class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # valid subarrays
        count = 0
        # current sum
        Sum = 0
        # old sums and frequency
        mp = {0: 1}

        for num in nums:

            # add current number
            Sum += num

            # old sum needed
            needed = Sum - k

            # check needed sum
            if needed in mp:

                # add frequency
                count += mp[needed]

            # store current sum
            mp[Sum] = mp.get(Sum, 0) + 1

        # return answer
        return count