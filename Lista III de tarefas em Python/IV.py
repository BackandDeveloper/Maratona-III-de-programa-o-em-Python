# Questão IV:
ratos = int(input("Digite a quantidade de ratos: "))
sapos = int(input("Digite a quantidade de sapos: "))
coelhos = int(input("Digite a quantidade de coelhos: "))

# Cálculo do total de cobaias
total_cobaias = ratos + sapos + coelhos

# Cálculo dos percentuais
percentual_ratos = (ratos / total_cobaias) * 100
percentual_sapos = (sapos / total_cobaias) * 100
percentual_coelhos = (coelhos / total_cobaias) * 100

# Saída dos resultados
print(f"Total: {total_cobaias} cobaias")
print(f"Percentual de coelhos: {percentual_coelhos:.2f}%")
print(f"Percentual de ratos: {percentual_ratos:.2f}%")
print(f"Percentual de sapos: {percentual_sapos:.2f}%")
