# ejem: derivada = [(5, 2), (3, 1)]
# derivada[0]: Selecciona el primer término en la lista derivada. Usando el ejemplo anterior, derivada[0] sería (5, 2).
# derivada[0][0]: Selecciona el primer elemento de la primera tupla en derivada, que es el coeficiente. En el ejemplo, derivada[0][0] sería 5.
# derivada[1]: Selecciona el segundo término en la lista derivada. En el ejemplo, derivada[1] sería (3, 1).
# derivada[1][0]: Selecciona el primer elemento de la segunda tupla en derivada, que es el coeficiente del segundo término. En el ejemplo, derivada[1][0] sería 3.


















































































n1 = 0
n2 = 1
print(f"{n1}, {n2}")

s = n1 + n2

# while s < 50:
#     print(f"{s}")
#     n1 = n2
#     n2 = s
#     s = n1 + n2

for i in range(50):
    print(f"{s}, ")
    n1 = n2
    n2 = s
    s = n1 + n2