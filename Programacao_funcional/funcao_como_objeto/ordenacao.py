alunos = [('Flavio', 9), ('Ada', 8), ('Luciano', 4)]

alunos.sort(key=lambda aluno: aluno[1])

print(alunos)

def por_nome(aluno):
    return aluno[0]

print(sorted(alunos, key=por_nome))