class Solution:
    def armstrongNumber(self, n: int) -> bool:
        l = 0
        nc = n
        while(nc > 0):
            nc = nc // 10
            l += 1
        
        ncc = n
        res = 0
        while(ncc > 0):
            dig = ncc % 10
            ncc = ncc // 10
            res += dig ** l
        
        if res == n:
            return True
        
        else:
            return False