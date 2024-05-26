class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numsLength = len(nums)
        for i in range(numsLength):
            for j in range(i+1, numsLength):
                if nums[j] == target -nums[i]:
                    return [i,j]

value = Solution()
print(value.twoSum([2,5,9,27], 9))
print(value.twoSum([2,9,27,7,5], 9))
print(value.twoSum([3,3], 6))