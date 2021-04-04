def stringCount(file, line):
    'Retorna o número de ocorrências na linha n'

    arquivo = open(file, 'r')
    pontuacao = [',','!','?',';',':']

    line = line -1

    for i in range(line):
        arquivo.readline()

    conteudo = arquivo.read()
    lista_palavras = conteudo.split()
    count_lista_palavras = len(lista_palavras)
    
    print(lista_palavras)
    print(count_lista_palavras)

    arquivo.close()

n_linha = stringCount('textoPy.txt', 2)