entrada = input("Digite os números: ")

numeros = entrada.split(',')
soma = 0

for n in numeros:
    soma += int(n)

print(f"Soma = {soma}")