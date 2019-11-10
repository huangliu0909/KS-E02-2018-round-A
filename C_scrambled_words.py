import random
'''
L = int(20000 * random.random())
N = random.randint(2, 1000000)
print(chr(97))
print(ord('a'))
'''


def dict_equal(P, Q):
    P_keys = P.keys()
    Q_keys = Q.keys()
    if len(P_keys) != len(Q_keys):
        return False
    for a in P_keys:
        if a not in Q_keys:
            return False
        if P[a] != Q[a]:
            return False
    for b in Q_keys:
        if b not in P_keys:
            return False
        if Q[b] != P[b]:
            return False
    return True


def construct_dict(word):
    word_dict = {}
    for c in word:
        if c not in word_dict:
            word_dict[c] = 1
        else:
            word_dict[c] += 1
    return word_dict


L = 1
length = 5
# len(d) = len
DDD = ["axpaj", "apxaj", "dnrbt", "pjxdn", "abd"]
S = {}
x = {}
S[1] = 'a'
S[2] = 'a'
x[1] = ord(S[1])
x[2] = ord(S[2])
N = 50
A = 1
B = 1
C = 1
D = 30
print("L: " + str(L))
print("N: " + str(N))
for i in range(3, N + 1):
    x[i] = (A * x[i - 1] + B * x[i - 2] + C) % D
    S[i] = chr(97 + (x[i] % 26))
s = ""
for i in range(N):
    s = s + (S[i + 1])
print(s)
print(DDD)
sum = 0
for d in DDD:
    # print(d)
    dict_d = construct_dict(d)
    for i in range(N - len(d)):
        temp = ""
        for j in range(i + 1, i + len(d) + 1):
            temp = temp + S[j]
        dict_temp = construct_dict(temp)
        if dict_equal(dict_d, dict_temp):
            print(d + " in S")
            sum += 1
            break
print("sum = " + str(sum))





