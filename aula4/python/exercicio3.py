A = []
B = []

for i in range(15):
    num = int(input("Digite um número: "))
    A.append(num)

for i in range(15):
    B.append(A[i] ** 2)

print("A:", A)
print("B:", B)
