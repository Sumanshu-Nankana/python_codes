class Solution(object):
    def prisonAfterNDays(self, cells, N):
        output = []
        output.append(0)
        j = 0
        while j < N:
            for i in range(1, len(cells)-1):
                if cells[i-1]==0 and cells[i+1]==0:
                    output.append(1)
                elif cells[i-1]==1 and cells[i+1]==1:
                    output.append(1)
                else:
                    output.append(0)
            
            output.append(0)
            cells = output
            temp = output
            output = []
            output.append(0)
            j+=1
        return temp
            

obj = Solution()
cells = [1,0,0,1,0,0,1,0]
N = 1000000000
print(obj.prisonAfterNDays(cells, N))