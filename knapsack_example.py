a = [2, 5, 9, 21, 45, 103, 215, 450, 946]
perm = [2, 5, 1, 9, 3, 6, 4, 8, 7]
M = 2003
W = 1289

b = [(W * a[perm[i]-1]) % M for i in range(len(a))]

plaintext = "001110111"
y = sum([b[i] for i in range(len(plaintext)) if plaintext[i] == "1"])
s = pow(W, -1, M) * y % M
s_temp = s

r = []
for i in range(len(a)-1, -1, -1):
    if a[i] <= s_temp:
        s_temp -= a[i]
        r.append(1)
    else:
        r.append(0)

r = r[::-1]

plaintext = [r[perm[i]-1] for i in range(len(r))]

print(f'b: {b}')
print(f'y: {y}')
print(f's: {s}')
print(f'r: {r}')
print(f'plaintext: {plaintext}')
