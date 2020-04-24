import numpy as np


def dpKnap(w, v):
    maxLoad = 10
    graph = np.full((len(w), maxLoad + 1), 0, dtype=int)

    for i in range(1, len(w)):
        for j in range(1, maxLoad+1):
            if j >= w[i]:
                graph[i][j] = max(graph[i-1][j-w[i]] + v[i], graph[i-1][j])  #能放下当前物品的时候比较
                                                                             #当前子问题下背包容量
                                                                             #可承载的
            else:
                graph[i][j] = graph[i-1][j]    #放不下当前物品

    print(graph)



if __name__ == '__main__':
    w = np.array([-1, 1, 2, 3, 4, 5, 6])
    v = np.array([-1, 1, 4, 1, 7, 4, 9])

    dpKnap(w, v)