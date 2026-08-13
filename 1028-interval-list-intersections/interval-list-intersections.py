class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        result = []

        i = 0
        j = 0

        while i < len(firstList) and j < len(secondList):

            start1 = firstList[i][0]
            end1 = firstList[i][1]

            start2 = secondList[j][0]
            end2 = secondList[j][1]

            # Find overlap
            start = max(start1, start2)
            end = min(end1, end2)

            # If they overlap
            if start <= end:
                result.append([start, end])

            # Move the interval that ends first
            if end1 < end2:
                i += 1
            else:
                j += 1

        return result