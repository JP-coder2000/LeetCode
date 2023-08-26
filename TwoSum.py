class Solution(object):
    def twoSum(self, nums, target):
        #we need to retren the index of the two numbers such that they add up to the target
        for i in range(len(nums)):
            for j in range(len((nums))):
                if nums[i] + nums[j] == target:
                    print([i, j])
                    return [i, j]
                else:
                    pass


solucion = Solution()
nums = [3,2,4]
target = 6

solucion.twoSum(nums, target)

#THIS SOLUTION IS PARTIALLY WRONG, IT DOESN'T WORK FOR ALL THE CASES# 