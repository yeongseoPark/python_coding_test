t = int(input())

a = 300
b = 60
c = 10

alphas = [a,b,c]
ans = [0,0,0]
for i in range(len(alphas)):
    if (t // alphas[i]) > 0:
        ans[i] += t // alphas[i]
        t -= alphas[i] * (t // alphas[i])

if t != 0:
    print(-1)
else:
    for i in ans:
        print(i, end =" ")