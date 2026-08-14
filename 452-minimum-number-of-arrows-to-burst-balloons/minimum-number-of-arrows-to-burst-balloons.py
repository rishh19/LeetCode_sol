class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        #sort accoridng to end

        points.sort(key=lambda x : x[1])

        #initial one arrow needed
        count=1

        #arrow points at the end of balloon
        arrow=points[0][1]

        for i in range(len(points)):
            start=points[i][0]
            end=points[i][1]

            #will arrow can burst the balloon??
            if start>arrow:
                count+=1

                arrow=end

        return count


