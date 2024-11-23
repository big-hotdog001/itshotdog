from math import inf

def minWaste(box_sizes, package):
    min_waste = inf  # 初始化最小浪費為無窮大
    fitProvider = False  # 初始化是否有合適供應商為 False
    for s in range(len(box_sizes)):  # 遍歷每個箱子尺寸組合
        cur_waste = 0  # 初始化當前浪費為 0
        p = 0  # 包裹索引
        b = 0  # 箱子索引
        while b < len(box_sizes[s]):  # 當還有箱子可用時
            while p < len(package) and package[p] <= box_sizes[s][b]:  # 當包裹可以放入當前箱子時
                cur_waste += box_sizes[s][b] - package[p]  # 計算浪費
                p += 1  # 移動到下一個包裹
                if p >= len(package):  # 如果所有包裹都已經放入
                    min_waste = min(cur_waste, min_waste)  # 更新最小浪費
                    fitProvider = True  # 設置有合適供應商為 True
                    break  # 跳出內層循環
            b += 1  # 移動到下一個箱子
            if p >= len(package):  # 如果所有包裹都已經放入
                break  # 跳出外層循環
    
    if fitProvider:  # 如果找到合適供應商
        return min_waste  # 返回最小浪費
    return -1  # 如果沒有合適供應商，返回 -1

# 接收輸入的包裹尺寸，並轉換為整數列表
packages = list(map(int, input().split()))
packages.sort()  # 將包裹尺寸從小到大排序

providers = int(input())  # 輸入供應商數量
box_sizes = [[] for _ in range(providers)]  # 初始化每個供應商的箱子尺寸列表
for s in range(providers):
    box_sizes[s] = list(map(int, input().split()))  # 接收每個供應商的箱子尺寸，並轉換為整數列表
    box_sizes[s].sort()  # 將箱子尺寸從小到大排序

# 計算並輸出最小浪費
print(minWaste(box_sizes, packages))