class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l_p = 0 
        for r_p in range(len(nums)):
            if nums[r_p] != 0:
                nums[l_p], nums[r_p] = nums[r_p], nums[l_p]
                l_p += 1
            else: 
                pass

            