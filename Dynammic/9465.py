for i in range(int(input())):
    n = int(input())
    a1 = list(map(int, input().split()))
    a2 = list(map(int, input().split()))

    for i in range(1, n):
        if i == 1:
            a1[1] += a2[0]
            a2[1] += a1[0]

        else:
            a1[i] = max(a2[i-1], a2[i-2]) + a1[i]
            a2[i] = max(a1[i-1], a1[i-2]) + a2[i]

    print(max(a1[n-1], a2[n-1]))


