alunos = [('Flavio', 9), ('Ada', 8), ('Luciano', 4)]

# Listcomprehension
print([(nome, nota) for nome, nota in alunos if nota > 5])


def nota_maior_5(aluno):
    _, nota = aluno
    return nota > 5

print(list(filter(nota_maior_5, alunos)))