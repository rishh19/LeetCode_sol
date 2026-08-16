class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #start

        slow=nums[0]
        fast=nums[0]

        #loop one for meeting point

        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]

            if slow==fast:
                break

        #loop two to detect cycle entrance

        slow=nums[0]  #reset the slow to starting point
        #fast remain same as previous loop
        while slow!=fast:
            slow=nums[slow]
            fast=nums[fast]

        return slow