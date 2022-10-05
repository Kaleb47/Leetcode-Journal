class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #first we need a hash map
        
        res = [1] * (len(nums))
        # define the prefix
        prefix = 1
        # use a for loop
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
