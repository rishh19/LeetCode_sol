class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        # longest length found
        max_len = 0

        # running sum
        Sum = 0

        # first position of each Sum
        mp = {0: -1}

        # go through array using index
        for i in range(len(nums)):

            # 0 becomes -1, 1 becomes +1
            if nums[i] == 0:
                Sum += -1
            else:
                Sum += 1

            # check if Sum was seen before
            if Sum in mp:

                # calculate current possible length
                length = i - mp[Sum]

                # keep maximum length
                max_len = max(max_len, length)

            else:

                # store ONLY first position
                mp[Sum] = i

        # return longest length
        return max_len


