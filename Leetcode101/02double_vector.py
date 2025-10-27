# 167 Two sum
# 在一个增序的整数数组里找到两个数，使它们的和为给定值。已知有且只有一对解

class Solution:
    def twoSum(self,numbers:list[int],target:int):
        l,r = 0,len(numbers)-1
        while l < r:
            two_sum = numbers[l]+ numbers[r]
            if two_sum == target:
                break
            if two_sum < target:
                l += 1
            else:
                r -= 1
        return [l+1,r+1]

sol = Solution()
result = sol.twoSum([2,7,11,13],18)
print("结果:", result, "预期:", [2,3])
print("✅" if result == [2,3] else "❌")