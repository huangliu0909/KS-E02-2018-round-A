import random
x = int(10000000000000000 * random.random())
print(x)
ds = [int(w) for w in str(x)]
print(ds)
first_o = -1
first_o_num = -1
for i in range(len(ds)):
    if ds[i] % 2 != 0:
        first_o = i
        first_o_num = ds[i]
        break
if first_o == -1:
    print("press num is 0")
else:
    if first_o_num == 9:
        # 29678 -> 28888, 92 -> 88, 229 -> 228, 9->8
        r = ""
        for i in range(first_o):
            r += str(ds[i])
        # print("copy: " + r)
        for i in range(first_o - 1, len(ds) - 1):
            r += str(8)
        print(r)
        print("press num is %d" % (x - int(r)))
    else:
        if first_o == len(ds) - 1:
            # 247 -> 246 or 248
            print(str(x - 1) + " or " + str(x + 1))
            print("press num is 1")
        else:
            # 2856 -> 2860, 2852 ->2848
            second = first_o + 1
            if ds[second] > 4:
                r = ""
                for i in range(first_o):
                    r += str(ds[i])
                # print("copy: " + r)
                r += str(first_o_num + 1)
                for i in range(first_o, len(ds) - 1):
                    r += str(0)
                print(r)
                print("press num is %d" % (int(r) - x))
            elif ds[second] < 4:
                r = ""
                for i in range(first_o):
                    r += str(ds[i])
                # print("copy: " + r)
                r += str(first_o_num - 1)
                for i in range(first_o, len(ds) - 1):
                    r += str(8)
                print(r)
                print("press num is %d" % (x - int(r)))
            else:
                r0 = ""
                for i in range(first_o):
                    r0 += str(ds[i])
                # print("copy: " + r)
                r0 += str(first_o_num + 1)
                for i in range(first_o, len(ds) - 1):
                    r0 += str(0)

                r = ""
                for i in range(first_o):
                    r += str(ds[i])
                # print("copy: " + r)
                r += str(first_o_num - 1)
                for i in range(first_o, len(ds) - 1):
                    r += str(8)

                if int(r0) - x > x - int(r):
                    print(r)
                    print("press num is %d" % (x - int(r)))
                elif int(r0) - x < x - int(r):
                    print(r0)
                    print("press num is %d" % (x - int(r)))
                else:
                    print(r)
                    print(r0)
                    print("press num is %d" % (x - int(r)))









