k, n = map(int, input().split(" "))
block = [0 for i in range(k+1)]
order = [0 for i in range(k+1)]

for i in range(n):
    a, b = map(int, input().split(" "))
    order[a-1] += 1
    order[b] -= 1

block[0] = order[0]

for i in range(1, k+1):
    block[i] = block[i-1] + order[i]

block.sort()

print(block[len(block)//2])