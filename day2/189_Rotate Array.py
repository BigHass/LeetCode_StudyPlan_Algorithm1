class Solution:
    def reverse(self,nums: list[int], l_p: int, r_p: int) -> None:
        while l_p < r_p:
            nums[l_p], nums[r_p] = nums[r_p], nums[l_p]
            l_p += 1
            r_p -= 1
    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums)-1)
