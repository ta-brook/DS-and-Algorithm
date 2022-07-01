class Solution:
    def twoSum(nums: list[int], target: int) -> list[int]:
        '''
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        You can return the answer in any order.

        Example 1:
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

        Example 2:
        Input: nums = [3,2,4], target = 6
        Output: [1,2]

        Constraints:

        2 <= nums.length <= 104
        -109 <= nums[i] <= 109
        -109 <= target <= 109
        Only one valid answer exists.
        '''

        # brute force
        # for idx, num1 in enumerate(nums):
        #     for jdx in range(idx+1, len(nums)):
        #         print(idx, jdx)
        #         if num1 + nums[jdx] == target:
        #             return [idx, jdx]
        # return False

        # hash table
        map = {}
        for idx, num in enumerate(nums):
            value = target - num
            if value in map.keys():
                return [map[value], idx]
            map[num] = idx

nums = [3, 2, 4]
target = 6
print(Solution.twoSum(nums, target))
