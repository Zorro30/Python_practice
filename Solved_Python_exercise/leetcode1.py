class Solution:
    def twoSum(self, nums, target):
        num_dict = {}
        for ind, val in enumerate(nums):
            if target - val in num_dict:
                return [num_dict[target-val], ind]
            num_dict[val] = ind
            print(num_dict)
        return []

ven = Solution()
print(ven.twoSum([2,7,3,2,15],4))