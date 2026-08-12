class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # Sort intervals by starting value
        for i in range(len(intervals)):
            for j in range(0, len(intervals) - i - 1):
                if intervals[j][0] > intervals[j + 1][0]:
                    intervals[j], intervals[j + 1] = intervals[j + 1], intervals[j]

        result = []

        # Take the first interval
        start1 = intervals[0][0]
        end1 = intervals[0][1]

        for i in range(1, len(intervals)):

            # Take the next interval
            start2 = intervals[i][0]
            end2 = intervals[i][1]

            # If intervals overlap, combine them
            if end1 >= start2:
                end1 = max(end1, end2)

            # If they do not overlap, save the current interval
            else:
                result.append([start1, end1])

                # Move to the next interval
                start1 = start2
                end1 = end2

        # Save the final interval
        result.append([start1, end1])

        return result