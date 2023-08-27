from collections import defaultdict

n = int(input())
words = [input().strip() for _ in range(n)]

alpha_weight = defaultdict(int)

# 1. 각 알파벳의 가중치 계산
for word in words:
    length = len(word)
    for i in range(length):
        alpha_weight[word[i]] += 10 ** (length-i)

# 2. 가중치에 따라서 알파벳 정렬
sorted_alpha = sorted(alpha_weight.keys(), key = lambda x : alpha_weight[x], reverse=True)

alpha_to_num = {}
val = 9
# 3. 숫자로 변환 후 값 계산
for i in sorted_alpha:
    alpha_to_num[i] = str(val)
    val -= 1

ans = 0
for word in words:
    tmp = ""
    for ch in word:
        tmp += alpha_to_num[ch]
    
    ans += int(tmp)

print(ans)
    