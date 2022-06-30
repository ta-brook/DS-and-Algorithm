class Solution:
    def containsDuplicate(nums: list[int]) -> bool:
        '''
        Example 1:
        Input: nums = [1,2,3,1]
        Output: true

        Input: nums = [1,2,3,4]
        Output: false

        1 <= nums.length <= 105
        -109 <= nums[i] <= 109
        '''
        # brute force
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        # mapping
        map = {}
        for idx, item in enumerate(nums):
            if item not in map:
                map[item] = 1
            else:
                return True
        return False


nums = [3, 2,]
print(Solution.containsDuplicate(nums))
