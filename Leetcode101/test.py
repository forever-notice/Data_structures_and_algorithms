def find_target():
    for i in range(3):
        print(f"\n外循环：i = {i}")
        for j in range(5):
            print(f"  内循环：j = {j}")
            if i == 1 and j == 2:
                print("  找到目标，return！")
                return (i, j)  # 直接退出整个函数
    return None

result = find_target()
print(f"结果：{result}")

# 输出：
# 外循环：i = 0
#   内循环：j = 0
#   内循环：j = 1
#   内循环：j = 2
#   内循环：j = 3
#   内循环：j = 4
# 
# 外循环：i = 1
#   内循环：j = 0
#   内循环：j = 1
#   内循环：j = 2
#   找到目标，return！
# 结果：(1, 2)