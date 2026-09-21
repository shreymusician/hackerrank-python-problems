class Solution:
    def isPalindrome(self, s: str) -> bool:
        f = 0
        b = len(s)-1

        while(f <= b):
            if(s[f] != s[b]):
                return False
            
            f+=1
            b-=1
            
        return True