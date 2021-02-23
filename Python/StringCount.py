def stringCount(file, line):
    'Retorna o número de ocorrências na linha n'

    arquivo = open(file, 'r')

    line = line -1

    for i in range(line):
        arquivo.readline()

    conteudo = arquivo.read()

    print(len(conteudo))

    arquivo.close()

n_linha = stringCount('textoPy.txt', 3)