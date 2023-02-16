class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left_p=0
        right_p=len(nums)-1
        while left_p <= right_p:
            mid=(left_p+right_p)//2
            if target== nums[mid]:
                return mid
            elif target < nums[mid]:
                right_p = mid-1
            else:
                left_p = mid+1
        return left_p
