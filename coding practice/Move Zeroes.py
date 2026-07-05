# Q. Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        new_nums = []

        for num in nums:
            if num != 0:
                new_nums.append(num)

        for num in nums:
            if num == 0:
                new_nums.append(0)

        nums[:] = new_nums


# Driver Code
nums = [0, 1, 0, 3, 12]

obj = Solution()
obj.moveZeroes(nums)

print(nums)