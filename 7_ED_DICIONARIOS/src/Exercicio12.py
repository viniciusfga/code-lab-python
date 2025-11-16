def calcular(notas):
    soma = 0
    for nota in notas:
        soma += nota

    media = soma / len(notas)

    if media >= 6:
        situacao = 'Aprovado'
    elif media >= 5:
        situacao = 'Recuperação'
    else:
        situacao = 'Reprovado'

    return media, situacao


alunos = ["Aluno1", "Aluno2", "Aluno3"]

notas_turma = [
    [7.5, 8.0, 6.5, 7.0],
    [4.0, 3.5, 5.0, 4.5],
    [1.0, 9.5, 1.0, 1.0]
]

for i in range(len(notas_turma)):
    media, situacao = calcular(notas_turma[i])
    print(
        alunos[i],
        "\nMédia:", f"{media:.1f}",
        "Situação:", situacao,
        "\n"
    )
