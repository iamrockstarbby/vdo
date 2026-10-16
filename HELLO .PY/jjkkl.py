
def print_order(i, j):
    if i == j:
        print(f"A{i}", end="")
        return

    print("(", end="")
    print_order(i, s[i][j])
    print_order(s[i][j] + 1, j)
    print(")", end="")


n = int(input())
d = list(map(int, input().split()))

m = [[0] * (n + 1) for _ in range(n + 1)]
s = [[0] * (n + 1) for _ in range(n + 1)]

for L in range(2, n + 1):
    for i in range(1, n - L + 2):
        j = i + L - 1
        m[i][j] = float("inf")

        for k in range(i, j):
            cost = m[i][k] + m[k + 1][j] + d[i - 1] * d[k] * d[j]

            if cost < m[i][j]:
                m[i][j] = cost
                s[i][j] = k

print(m[1][n])
print_order(1, n)
print()
