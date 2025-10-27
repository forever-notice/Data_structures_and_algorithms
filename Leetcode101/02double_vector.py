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

# class Solution(object):
#     def merge(self, nums1:list[int], m:int, nums2:list[int], n:int) -> None:
#         """
#         :type nums1: List[int]
#         :type m: int
#         :type nums2: List[int]
#         :type n: int
#         :rtype: None Do not return anything, modify nums1 in-place instead.
#         """
#         pos = n+m-1 #总长度
#         n -= 1
#         m -= 1
#         while m>=0 and n>=0:
#             if nums1[m]> nums2[n]:
#                 nums1[pos] = nums1[m]
#                 m -= 1
#             else:
#                 nums1[pos] = nums2[n]
#                 n -= 1
#             pos -= 1
#         nums1[: n + 1] = nums2[: n + 1] 
#         return nums1
# #如果 m 先等于 0，需要把第二个数组教小的数搬过来，不然会漏；
# # 但 n 先等于 0 的话第一个数组仍然在

# sol = Solution()
# result = sol.merge([2,7,11,13,0,0,0],4,[1,3,8],3)
# print("结果:", result, "预期:", [1,2,3,7,8,11,13])
# print("✅" if result == [1,2,3,7,8,11,13] else "❌")


#76. Minimum Window Substring 
# 题目描述：给定两个字符串 s 和 t，求 s 中包含 t 所有字符的最短连续子字符串
# 同时要求时间复杂度不得超过 O(n)。
# 示例：s = "ADOBECODEBANC", t = "ABC" → 输出 "BANC"

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 边界条件：如果 s 比 t 短，不可能包含
        if len(s) < len(t):
            return ""
        
        # 1. 统计 t 中每个字符需要的数量
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1
        
        # 2. 初始化滑动窗口变量
        window = {}  # 记录窗口中每个字符的数量
        left = 0     # 左指针
        right = 0    # 右指针
        valid = 0    # 窗口中满足条件的字符种类数
        
        # 记录最小覆盖子串的起始位置和长度
        start = 0
        min_len = float('inf')
        
        # 3. 移动右指针扩大窗口
        while right < len(s):
            # 即将加入窗口的字符
            c = s[right]
            right += 1  # 右指针右移
            
            # 如果这个字符是 t 中需要的字符
            if c in need:
                window[c] = window.get(c, 0) + 1
                # 如果窗口中该字符的数量达到需要的数量
                if window[c] == need[c]:
                    valid += 1  # 满足条件的字符种类数 +1
            
            # 4. 当窗口包含所有字符时，尝试收缩左边界
            while valid == len(need):
                # 更新最小覆盖子串
                if right - left < min_len:
                    start = left
                    min_len = right - left
                
                # 即将移出窗口的字符
                d = s[left]
                left += 1  # 左指针右移
                
                # 如果移出的字符是 t 中需要的字符
                if d in need:
                    # 如果窗口中该字符的数量等于需要的数量
                    if window[d] == need[d]:
                        valid -= 1  # 不再满足条件
                    window[d] -= 1
        
        # 5. 返回结果
        return "" if min_len == float('inf') else s[start:start + min_len]

# 测试用例
sol = Solution()

# 测试1：经典案例
result1 = sol.minWindow("ADOBECODEBANC", "ABC")
print(f"测试1 - 结果: '{result1}', 预期: 'BANC'")
print("✅" if result1 == "BANC" else "❌")

# 测试2：t 只有一个字符
result2 = sol.minWindow("a", "a")
print(f"测试2 - 结果: '{result2}', 预期: 'a'")
print("✅" if result2 == "a" else "❌")

# 测试3：s 不包含 t 的所有字符
result3 = sol.minWindow("a", "aa")
print(f"测试3 - 结果: '{result3}', 预期: ''")
print("✅" if result3 == "" else "❌")

# 测试4：重复字符（t 中有重复字符）
result4 = sol.minWindow("ADOBECODEBANC", "AABC")
print(f"测试4 - 结果: '{result4}', 预期: 'ADOBECODEBA'")
print("✅" if result4 == "ADOBECODEBA" else "❌")

# 测试5：更简单的重复字符测试
result5 = sol.minWindow("ABAACBAB", "ABC")
print(f"测试5 - 结果: '{result5}', 预期: 'ACB' 或 'BAC'")
print("✅" if result5 in ["ACB", "BAC"] else "❌")

# 142. Linked List Cycle II 
# 题目描述给定一个链表,如果有环路,找出环路的开始点。