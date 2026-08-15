class Solution:

  def removeCoveredIntervals(self, iv: List[List[int]]) -> int:
    # Sort by start ascending, then by end descending
    iv.sort(key=lambda x: (x[0], -x[1]))
    count = 0
    max_end = 0  # Farthest end reached by any interval

    for start, end in iv:
      # If the current interval's end is beyond the max_end, it is not covered
      if end > max_end:
        count += 1
        max_end = end

    return count
