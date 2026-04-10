A = []
B = []
C = []

for i in range(20):
    A.append(float(input("Digite valor de A: ")))

for i in range(20):
    B.append(float(input("Digite valor de B: ")))

for i in range(20):
    C.append(A[i] - B[i])

print("Matriz C:", C)
