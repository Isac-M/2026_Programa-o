expressao = input("Digite a expressão: ")

if '+' in expressao:
    valores = expressao.split('+')
    resultado = int(valores[0]) + int(valores[1])
elif '-' in expressao:
    valores = expressao.split('-')
    resultado = int(valores[0]) - int(valores[1])
elif '*' in expressao:
    valores = expressao.split('*')
    resultado = int(valores[0]) * int(valores[1])
elif '/' in expressao:
    valores = expressao.split('/')
    resultado = int(valores[0]) / int(valores[1])

print(f"O resultado é {resultado}")