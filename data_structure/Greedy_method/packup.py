def packup(objects, argW):
    i = total_p = 0  # 初始化索引 i 與總價值 total_p
    left_capacity = argW  # 剩餘容量初始化為最大容量 argW
    while (i < len(objects) & left_capacity > 0) :  # 當還有物品且剩餘容量大於 0 時
        if objects[i][2] <= 0:  # 如果物品的重量小於等於 0
            total_p += objects[i][3]  # 將該物品的價值加到總價值
            left_capacity -= objects[i][2]  # 扣除該物品的重量
        else:  # 否則，當物品不能完整放入背包
            total_p += (objects[i][0] * left_capacity)  # 按比例計算剩餘容量的價值
            left_capacity = 0  # 背包已經放滿
        i += 1  # 進行下一個物品
    return total_p  # 返回總價值

W_limit = int(input())  # 輸入最大容量 W_limit
n = int(input())  # 輸入物品數量 n
name = input().split()  # 輸入物品名稱，並以空格分割成串列
Weight = list(map(int, input().split()))  # 輸入物品重量，並轉換為整數串列
Value = list(map(int, input().split()))  # 輸入物品價值，並轉換為整數串列
items = [ [ ] for _ in range(n)]  # 初始化物品清單
for i in range(n):
    items[i] = [Value[i]/Weight[i], name[i], Weight[i], Value[i]]  # 計算物品性價比，並存入物品清單

items.sort(reverse = True)  # 根據性價比排序，從大到小排序
print(packup(items, W_limit))  # 計算背包所能得到的最大價值並輸出