from __future__ import annotations

# 笔记：
# 1. pop() 的返回值是被删除的元素
# 2. -> 箭头表示函数返回值的类型

def plusOne(digits: list[int]) -> list[int]:
    """给数组表示的数字加一
    例如: [1,2,3] 表示 123，加一后变成 124，返回 [1,2,4]
    """
    digits = [0] + digits  # 在前面加个0，防止最高位进位（如 [9,9,9] -> [1,0,0,0]）
    digits[len(digits) - 1] += 1  # 最后一位加1
    
    # 从后往前处理进位
    for i in range(len(digits)-1, 0, -1):
        if digits[i] != 10:
            break  # 没有进位，结束
        else:
            digits[i] = 0      # 当前位变0
            digits[i - 1] += 1  # 前一位加1（进位）
        
    # 如果第一位是0，说明没有进位到最高位，去掉这个0
    if digits[0] == 0:
        return digits[1:] 
    else:
        return digits  # 否则保留所有位（说明有进位，如 999 -> 1000）

# 测试示例
print("=" * 60)
print("plusOne 函数测试")
print("=" * 60)

test_cases = [
    [1, 2, 3],      # 123 + 1 = 124
    [9, 9, 9],      # 999 + 1 = 1000
    [1, 9, 9],      # 199 + 1 = 200
    [0],            # 0 + 1 = 1
    [9],            # 9 + 1 = 10
]

for digits in test_cases:
    original = digits.copy()  # 保存原始值用于显示
    result = plusOne(digits)
    print(f"{original} + 1 = {result}")

print("\n" + "=" * 60)
print("类型注解说明：")
print("def plusOne(digits: list[int]) -> list[int]:")
print("                   ↑                ↑")
print("              参数类型         返回值类型")
print("表示：接收一个整数列表，返回一个整数列表")
print("=" * 60)