class Solution:
    def eraseOverlapIntervals(self, iv: List[List[int]]) -> int:
        iv.sort()

        count=0

        #initial
        start1 = iv[0][0]
        end1 = iv[0][1]

        for i in range(1,len(iv)):

            #nxt intervals
            start2=iv[i][0]
            end2=iv[i][1]

            #if overlapping then increase count
            if end1> start2:
                count+=1

                #assume that overlap is deleted by taking min end
                end1=min(end1,end2)

            else:
                start1=start2
                end1=end2

        return count

