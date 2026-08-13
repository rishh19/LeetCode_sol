class Solution:
    def insert(self, iv: List[List[int]], niv: List[int]) -> List[List[int]]:
        #insert 
        result=[]
        insert = False
        for i in range(len(iv)):
            if not insert and niv[0] < iv[i][0]:
                result.append(niv)
                insert = True
            result.append(iv[i])
        
        #no merge i.e. put new interval at last
        if not insert:
            result.append(niv)

        #final merge
        final=[]

        start1=result[0][0]
        end1=result[0][1]

        for i in range(1,len(result)):

            #assign upcoming intervals
            start2 = result[i][0]
            end2 = result[i][1]

            if end1>=start2:
                end1=max(end1,end2)
                start1=start1

            else:
                final.append([start1,end1])
                start1=start2
                end1=end2

        #left over put in the final
        final.append([start1,end1])
        return final



