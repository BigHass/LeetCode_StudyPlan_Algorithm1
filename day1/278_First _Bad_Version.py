# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left_pointer=0
        right_pointer=n
        while left_pointer<=right_pointer:
            mid=(left_pointer+right_pointer)//2
            if isBadVersion(mid):
                right_pointer=mid-1
            else:
                left_pointer=mid+1
        return left_pointer
                