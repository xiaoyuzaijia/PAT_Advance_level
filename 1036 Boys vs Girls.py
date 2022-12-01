N = int(input())

m_info = []
f_info = []
for _ in range(N):
    n, ge, id_, gr = input().split()
    if ge == 'M':
        m_info.append((n, ge, id_, int(gr)))
    else:
        f_info.append((n, ge, id_, int(gr)))

if not f_info:
    print("Absent")
else:
    f_max = max(f_info, key=lambda x: x[3])
    print(f_max[0], f_max[2])

if not m_info:
    print("Absent")
else:
    m_min = min(m_info, key=lambda x: x[3])
    print(m_min[0], m_min[2])

if not m_info or not f_info:
    print("NA")
else:
    print(f_max[3] - m_min[3])