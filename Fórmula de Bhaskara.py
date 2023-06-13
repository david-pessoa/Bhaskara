import math
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
delta = b**2 - 4*a*c
x = (-b) / (2*a)
if (delta < 0):
  print("Não há raízes reais para esta equação.")
elif(delta == 0):
    print("A equação apresenta duas raízes, que são coincidentes no ponto ", x)
else:
     x1 = (-b + math.sqrt(delta)) / (2*a)
     x2 = (-b - math.sqrt(delta)) / (2*a)
     print("A equação apresenta os pontos ", x1, "e", x2, "como raízes.")

yv = -(delta) / (4*a)

print(f"x do vértice: {x}")
print(f"y do vértice: {yv}")

