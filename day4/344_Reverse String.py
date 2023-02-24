class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l_p = 0
        r_p = len(s) -1 
        while l_p <= r_p :
            s[l_p], s[r_p] = s[r_p], s[l_p]
            l_p+=1
            r_p-=1