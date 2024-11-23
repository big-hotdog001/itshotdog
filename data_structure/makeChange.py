def makeChange(m):
    Changes = [50, 10, 5, 1]
    count = 0
    for item in Changes:
        count += m//item
        m %= item

    return count

m = int(input())
print(makeChange(m))