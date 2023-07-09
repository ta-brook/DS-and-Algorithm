class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        '''
        Example 1:
        Input: nums = [1,2,3,1]
        Output: true

        Input: nums = [1,2,3,4]
        Output: false

        1 <= nums.length <= 105
        -109 <= nums[i] <= 109
        '''

        # # TODO brute force -> well it's should work smh
        # for idx, num1 in enumerate(nums):
        #     for jdx, num2 in enumerate(nums[idx+1:]):
        #         if num1 == num2:
        #             return True
        # return False

        # # TODO Reduce loop by using 
        # lst = []
        # for num in nums:
        #     if num in lst:
        #         return True
        #     lst.append(num)
        # return False

        # # TODO Using hashMap (dict)
        # map = {}
        # for idx, num in enumerate(nums):
        #     print(map, num)
        #     if num not in map:
        #         map[num] = 1
        #     else:
        #         return True
        # return False

        # TODO Using Set() to find distinct
        st = set()
        for num in nums:
            if num in st:
                return True
            st.add(num)
        return False



nums = [2,14,18,22,22]
if __name__ == '__main__':
    ans = Solution()
    print(ans.containsDuplicate(nums))

    
