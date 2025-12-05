# Інтерполяція Лагранжа

# зчитуємо кількість точок
N = int(input("Введіть кількість точок: "))

# вводимо x
x = []
print("\nВведіть x:")
for _ in range(N):
    x.append(float(input()))

# вводимо y
y = []
print("\nВведіть y:")
for _ in range(N):
    y.append(float(input()))

# вводимо x0
x0 = float(input("\nВведіть x0: "))

# формула Лагранжа
result = 0.0

for i in range(N):
    term = y[i]
    for j in range(N):
        if i != j:
            term *= (x0 - x[j]) / (x[i] - x[j])
    result += term

print(f"\ny({x0:.3f}) = {result:.6f}")
