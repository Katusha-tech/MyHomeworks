a = list(map(int, input().split()))
start = a[0]
end = a[-1]
k = start != end
a.append(k)
print(*a)
