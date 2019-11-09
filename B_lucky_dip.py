import random
import math
'''
N = int(100 * random.random())
W = [int(100 * random.random()) for _ in range(N)]
T = int(10 * random.random())
'''
N = 5
T = 3
W = [16, 11, 7, 4, 1]
W.sort(reverse=True)
print("N: " + str(N))
print("items' weight: " + str(W))
print("redip time: " + str(T))

a = 0
for i in W:
    a += i
a = a/len(W)
num = 0
num_larger = 0
for w in W:
    if w > a:
        num += 1
        num_larger += w
    else:
        break
num_larger = num_larger / num
p = math.pow(((len(W) - num)/len(W)), T + 1)
E = {}
E[0] = a
for t in range(1, T + 1):
    num = 0
    num_larger = 0
    for w in W:
        if w > E[t - 1]:
            num += 1
            num_larger += w
        else:
            break
    num_larger = num_larger / num
    p = num/len(W)
    E[t] = num_larger * p + E[t - 1] * (1 - p)
print(E[T])




