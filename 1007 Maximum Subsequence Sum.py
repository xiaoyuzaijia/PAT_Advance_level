K = int(input())
l = list(map(int, input().split()))
l.insert(0, 0)
s = [0 for _ in range(K+1)]

all_maxsum = -1
all_i = current_i = 1
all_j = current_j = K
for i in range(1, K+1):
    if s[i-1] + l[i] >= l[i]:
        s[i] = s[i-1] + l[i]
        current_j = i
    else:
        s[i] = l[i]
        current_i = i
        current_j = i
    
    if s[i] > all_maxsum:
        all_maxsum = s[i]
        all_i = current_i
        all_j = current_j

if all_maxsum == -1:
    all_maxsum = 0
print(all_maxsum, l[all_i], l[all_j])