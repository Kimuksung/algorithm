flower_list = [0 for i in range(365)]

print(flower_list)

flowers =[[2, 5], [3, 7], [10, 11]]


for k,v in flowers:
    for t in range(k,v):
        flower_list[t] = 1

flower_list.count(1)
        