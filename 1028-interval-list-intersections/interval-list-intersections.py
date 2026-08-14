class Solution:
    def intervalIntersection(self, flist: List[List[int]], slist: List[List[int]]) -> List[List[int]]:

        result = []

        i = 0 # points to current interval of flist
        j = 0 # points to current interval of slist
        

        while i < len(flist) and j < len(slist):

            start1 = flist[i][0]
            end1 = flist[i][1]

            start2 = slist[j][0]
            end2 = slist[j][1]

            # Find overlap
            start = max(start1, start2)
            end = min(end1, end2)

            #they overlap, append them
            if start <= end:
                result.append([start, end])

            # Move the interval that ends first
            if end1 < end2:
                i += 1
            else:
                j += 1

        return result