class Solution:
    def twoSum(self, nums, target):
        a = {}
        for i in range(len(nums)):
            b = target - nums[i]
            if b in a:
                return [a[b], i]
            a[nums[i]] = i
        return []


c = Solution()
print(c.twoSum([2, 7, 11, 15], 9))
