n  = int(input())

for _ in range(n):
    p = int(input())
    dic = {}
    for _ in range(p):
        price, name = input().split()
        dic[name] = int(price)
    li = sorted(dic.items(), key = lambda x:-x[1])
    print(li[0][0])