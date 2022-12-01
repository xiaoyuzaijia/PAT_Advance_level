n1 = input()
n2 = str(int(n1) * 2)
if sorted(n1) == sorted(n2):
    print("Yes")
else:
    print("No")
print(n2)