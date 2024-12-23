# Questão VI:
T1 = int(input("Digite o número de tomadas da régua 1: "))
T2 = int(input("Digite o número de tomadas da régua 2: "))
T3 = int(input("Digite o número de tomadas da régua 3: "))
T4 = int(input("Digite o número de tomadas da régua 4: "))

# Cálculo do número máximo de aparelhos que podem ser conectados
max_aparelhos = (T1 - 1) + (T2 - 1) + (T3 - 1) + T4

# Saída do resultado
print(f"O número máximo de aparelhos que podem ser conectados é: {max_aparelhos}")
