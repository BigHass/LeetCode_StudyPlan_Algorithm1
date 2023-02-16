class Solution:
    def search(self, nums: List[int], target: int) -> int:
        LeftPointer=0
        RigthPointer=len(nums)-1
        while LeftPointer<=RigthPointer:
            MidIndex= ((RigthPointer-LeftPointer)//2) + LeftPointer
            if nums[MidIndex]==target:
                return MidIndex
            elif nums[MidIndex] < target:
                LeftPointer=MidIndex+1
            else:
                RigthPointer=MidIndex-1
        return -1