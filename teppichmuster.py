
base = '.' * 20
for i in range(20):
    if i % 4 == 0:
        s = '+' * 20
    else:
        s = base
    s = s[:i] + '#' + s[i+1:]
    s = s[:20-i-1] + '*' + s[20-i:]
    s = s[:i % 5] + '%' + s[i % 5 + 1:]
    print(s)


zeichen = "*#+-%"
start = 1
end = 19
for i in range(20):
    s = base
    z = zeichen[i % 5]
    s = s[:start] + z * (end-start) + s[end:]
    if i < 9:
        start += 1
        end -= 1
    else:
        start -= 1
        end += 1
    print(s)
