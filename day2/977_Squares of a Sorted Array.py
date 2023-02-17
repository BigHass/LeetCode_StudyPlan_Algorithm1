class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l_p=0
        r_p=len(nums) - 1
        result=list()
        while l_p<=r_p:
            l_val_sqr=nums[l_p]**2
            r_val_sqr=nums[r_p]**2

            if l_val_sqr < r_val_sqr:
                result.append(r_val_sqr)
                r_p-=1
            else:
                result.append(l_val_sqr)
                l_p+=1
        return result[::-1]