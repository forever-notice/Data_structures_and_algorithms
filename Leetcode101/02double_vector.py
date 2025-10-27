# 167 Two sum
# 在一个增序的整数数组里找到两个数，使它们的和为给定值。已知有且只有一对解

# class Solution:
#     def twoSum(self,numbers:list[int],target:int):
#         l,r = 0,len(numbers)-1
#         while l < r:
#             two_sum = numbers[l]+ numbers[r]
#             if two_sum == target:
#                 break
#             if two_sum < target:
#                 l += 1
#             else:
#                 r -= 1
#         return [l+1,r+1]

# sol = Solution()
# result = sol.twoSum([2,7,11,13],18)
# print("结果:", result, "预期:", [2,3])
# print("✅" if result == [2,3] else "❌")

# 88. Merge Sorted Array 
# 题目描述给定两个有序数组,把两个数组合并为一个

class Solution(object):
    def merge(self, nums1:list[int], m:int, nums2:list[int], n:int) -> None:
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        pos = n+m-1 #总长度
        n -= 1
        m -= 1
        while m>=0 and n>=0:
            if nums1[m]> nums2[n]:
                nums1[pos] = nums1[m]
                m -= 1
            else:
                nums1[pos] = nums2[n]
                n -= 1
            pos -= 1
        nums1[: n + 1] = nums2[: n + 1] 
        return nums1
#如果 m 先等于 0，需要把第二个数组教小的数搬过来，不然会漏；
# 但 n 先等于 0 的话第一个数组仍然在

sol = Solution()
result = sol.merge([2,7,11,13,0,0,0],4,[1,3,8],3)
print("结果:", result, "预期:", [1,2,3,7,8,11,13])
print("✅" if result == [1,2,3,7,8,11,13] else "❌")