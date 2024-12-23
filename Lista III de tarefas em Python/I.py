# Questão I:
X = int(input("Digite a distância total percorrida (em Km): "))
Y = float(input("Digite o total de combustível gasto (em litros): "))

# Cálculo do consumo médio
if Y != 0:
    consumo_medio = X / Y
else:
    consumo_medio = 0

# Saída do resultado
print(f"{consumo_medio:.3f} km/l")
