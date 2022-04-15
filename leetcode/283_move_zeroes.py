class Solution:
    def moveZeroes(nums):
        """
        Do not return anything, modify nums in-place instead.

        Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

        Note that you must do this in-place without making a copy of the array.

        Example 1:
        Input: nums = [0,1,0,3,12]
        Output: [1,3,12,0,0]

        Example 2:
        Input: nums = [0]
        Output: [0]

        Constraints:
        1 <= nums.length <= 104
        -231 <= nums[i] <= 231 - 1

        Follow up: Could you minimize the total number of operations done?
        """

        # TODO my own trial
        '''
        this code have:
        O(n) time complexity
        O(n) space complexity
        It's fast but used a lot of space? I guess. let's try to reduce that space
        '''
        count_zeroes = 0
        get_index = []
        for idx, num in enumerate(nums):
            if num == 0:
                get_index.append(idx)
                count_zeroes += 1

        for zero in reversed(get_index):
            nums.pop(zero)

        nums.extend([0 for zero in range(count_zeroes)])
        # return nums

        # TODO improved version
        '''
        this code have:
        O(n) time complexity
        O(1) space complexity
        '''
        for idx in reversed(range(len(nums))):
            if nums[idx] == 0:
                nums.pop(idx)
                nums.append(0)
        # return nums

        # TODO hint version from leetcode with `two-pointer` <- will check this one
        '''
        this is so cool. but used more memory than the 2nd one
        this code have:
        O(n) time complexity
        O(1) space complexity
        '''
        current_index = 0
        for idx, num in enumerate(nums):
            if num != 0:
                nums[current_index], nums[idx] = nums[idx], nums[current_index]
                current_index += 1


nums = [0, 1, 0, 3, 12, 8, 9, 0, 0, 9, 0, 0, 0]
# nums = [0]
print(Solution.moveZeroes(nums))
