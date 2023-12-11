def busca(nome, lista):
    
    for i, jogador in enumerate(lista):
        if nome == jogador[0]:
            return i
        
    return None
def cadastra_historico(nome, moeda, level):
    global arql
    print('cadastrei')
    
    i = busca(nome, arql)
    if i != None:
        arql[i][1] += 1
        arql[i].append([moeda, level])
    else:
        arql.append([nome, 1,[moeda, level]])
    
def escrve():
    global arql
    print('escrevi')
    arqS = open('ranking.txt', 'w')

    for jogador in arql:
        nome = jogador[0]
        tentativas = jogador[1]
        arqS.write('%s, %d\n' % (nome, tentativas))
        for tentativa in range(tentativas):
            moedas = jogador[2][0]
            level = jogador[2][1]
            arqS.write(f'{moedas},{level}\n' )
    arqS.close()

arqE = open('ranking.txt', 'r')
arql = []
for i, linha in enumerate(arqE):
    linha = linha.strip().split(',')
    nome = linha[0]
    tentativas = int(linha[1])
    arql.append([nome, tentativas])

    for tentativa in range(tentativas):
        linha = arqE.readline().strip().split(',')
        moedas = linha[0]
        fase = linha[1]
        arql[i].append([moedas, fase])

arqE.close()








            
