class Solution:
    def twoSum(nums, target):
        '''
        https://leetcode.com/problems/two-sum/
        
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        You can return the answer in any order.

        Constraints:
        2 <= nums.length <= 10^4
        -10^9 <= nums[i] <= 10^9
        -10^9 <= target <= 10^9
        Only one valid answer exists.

        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

        Input: nums = [3,2,4], target = 6
        Output: [1,2]

        Input: nums = [3,3], target = 6
        Output: [0,1]
        '''

        # TODO let's brute force first!
        for i in range(len(nums)): # O(n^2)
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i, j]

        # TODO from hint2 if we fix one variable
        # by doing this I got 5 times faster from function above
        for i in range(len(nums)): # O(n)
            value = target - nums[i]
            if value in nums and nums.index(value) != i:
                return [i, nums.index(value)]
        
        # TODO can we try hash table
        # this is the fastest here come with O(n)
        map = {}
        for idx, num in enumerate(nums):
            value = target - num
            if value in map.keys():
                return [idx, map[value]]
            map[num] = idx



print(Solution.twoSum(nums=[2, 7, 11, 15], target=9))
