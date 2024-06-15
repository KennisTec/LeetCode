class Solution(object):
    def maxAera(self, height):
        # numsLength = len(height)-1
        # maxSum = 0
        # i=0
        # while i< numsLength:
        #     maxSum = max(maxSum,min(height[i],height[numsLength])* (numsLength-i))
        #     if height[i] <= height[numsLength]:
        #         i+=1
        #     else :
        #         numsLength-=1
        # return maxSum
    
        maxH, maxA, left, right = max(height), 0, 0, len(height) - 1
        while left < right:
            if height[left] < height[right]:
                if height[left] * (right - left) > maxA:
                    maxA = height[left] * (right - left)
            else:
                if height[right] * (right - left) > maxA:
                    maxA = height[right] * (right - left)
            
            if maxH * (right - left) <= maxA:
                break

            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1
        return maxA

value = Solution()
# print(value.maxAera([1,8,6,2,5,4,8,3,7]))
print(value.maxAera([1,8,6,2,5,4,8,3,7]))
# print(value.maxAera([2,3,4,5,18,17,6]))
print(value.maxAera([2,3,4,5,18,17,6]))
# print(value.maxAera([1,1]))