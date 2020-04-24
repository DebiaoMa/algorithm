class goods:
    name = None

    def __init__(self, order, w, v):
        self.name = order
        self.w = w
        self.v = v

    def __str__(self) -> str:
        return "('%d', '%d', '%.2f')" % (self.name, self.w, self.v)

def knapsack(maxLoad, goods_set):

    goods_set.sort(key = lambda x: x.v / x.w, reverse = True)

    carry = []
    for good in goods_set:
        if maxLoad < good.w:
            continue
        else:
            carry.append(good)
            maxLoad -= good.w

    for x in carry:
        print(x.name, x.w)

if __name__ == '__main__':
    # w = np.array([-1, 1, 2, 3, 4, 5, 6])
    # v = np.array([-1, 1, 4, 1, 7, 4, 9])

    n = int(input("the number of backpack:"))

    goods_set = []
    print("please input order, weight, value of each goods:")
    while n > 0:
        order, a, b = [int(n) for n in input().split()]
        good = goods(order, a, b)
        goods_set.append(good)
        n -= 1

    knapsack(10, goods_set)