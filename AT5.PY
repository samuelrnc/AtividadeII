def filtrar_aprovados(notas):
    aprovados = []
    for nota in notas:
        if nota >= 7:
            aprovados.append(nota)
    return aprovados

notas = []
quantidade = int(input("Quantas notas você quer digitar? "))

for i in range(quantidade):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas.append(nota)

aprovados = filtrar_aprovados(notas)
print("Notas aprovadas:", aprovados)