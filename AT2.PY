def calcular_media(notas):
    soma = 0
    for nota in notas:
        soma = soma + nota
    media = soma / len(notas)
    return media

notas = []
quantidade = int(input("Quantas notas você quer digitar? "))

for i in range(quantidade):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas.append(nota)

print("Média:", calcular_media(notas))