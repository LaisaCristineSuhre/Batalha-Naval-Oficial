jogo=True

cont_b=0
cont_c=0

li=[]
co=[]

barcos_colocados = []
barcos_colocados2 = []

barcos = ["◘◘", "◘◘◘", "◘◘◘", "◘◘◘◘", "◘◘◘◘◘"]
global blocos1
global blocos2
blocos1 = ["◘", "◘", "◘", "◘", "◘", "◘", "◘", "◘", "◘", "◘", "◘", "◘", "◘", "◘", "◘"] 
blocos2 = ["◘", "◘", "◘", "◘", "◘", "◘", "◘", "◘", "◘", "◘", "◘", "◘", "◘", "◘", "◘"]  #Quando o jogador acertar um navio, será retirado um desses bloquinhos,
#e quando não houver mais, o jogador venceu.

#Porta avião: ◘◘◘◘◘; encouraçado: ◘◘◘◘; submarino e destroyer: ◘◘◘; barco de patrulha: ◘◘. 

def gera_tab(n):  #Esta é a função do tabuleiro.
    tab = []
    for _ in range(n):
        line = []
        for __ in range(n):
            line.append('██')
        tab.append(line)

    return tab

def print_tab(tab, vez):  #Tabuleiro do jogador 1.
    print("Tabuleiro do Jogador 1:")
    for line in tab:
        print(''.join(line))

def print_tab2(tab2, vez):  #Tabuleiro do jogador 2.
    print("Tabuleiro do Jogador 2:")
    for line in tab2:
        print(''.join(line))

def posiciona_barco(pos, d, t, tab): #Serve para colocar a embarcação na direção escolhida pelo usuário.
    n = int(t)
    if d=='N' or d=='n':
        for i in range(pos[0], pos[0] - n, -1):
            tab[i][pos[1]] = "░░"
    elif d=='S' or d=='s':
        for i in range(pos[0], pos[0] + n, +1):
            tab[i][pos[1]] = "░░"
    elif d=='O' or d=='o':
        for i in range(pos[1], pos[1] - n, -1):
            tab[pos[0]][i] = "░░"
    elif d=='L' or d=='l':
        for i in range(pos[1], pos[1] + n, +1):
            tab[pos[0]][i] = "░░"

    barcos_colocados.append(t)

def posiciona_barco2(pos, d, t, tab): #Serve para colocar a embarcação na direção escolhida pelo usuário.
    n = int(t)
    if d=='N' or d=='n':
        for i in range(pos[0], pos[0] - n, -1):
            tab[i][pos[1]] = "░░"
    elif d=='S' or d=='s':
        for i in range(pos[0], pos[0] + n, +1):
            tab[i][pos[1]] = "░░"
    elif d=='L' or d=='l':
        for i in range(pos[1], pos[0] - n, -1):
            tab[i][pos[1]] = "░░"
    elif d=='O' or d=='o':
        for i in range(pos[1], pos[0] + n, +1):
            tab[i][pos[1]] = "░░"

    barcos_colocados2.append(t)    
                
def validar(coords, d, t, tab):  #Para validar as jogadas.
    eh_valido = True 
    if coords[0] > 19 or coords[1] > 19:
        eh_valido = False
        print("Essa posição não existe no tabuleiro. Tente outra vez.")
    if tab[coords[0]][coords[1]]=='░░':
        eh_valido = False
        print("Posição ocupada! Tente outra vez.")
    if int(t)>5:
        print("O barco é muito grande.")
        eh_valido = False
    if t in barcos_colocados:
        print("Você já posicionou esse barco!")
        eh_valido = False
    return eh_valido

def validar2(coords, d, t, tab2):  #Para validar as jogadas do jogador 2.
    eh_valido = True
    if coords[0] > 19 or coords[1] > 19:
        eh_valido = False
        print("Essa posição não existe no tabuleiro. Tente outra vez.")
    if tab2[coords[0]][coords[1]]=='░░':
        eh_valido = False
        print("Posição ocupada! Tente outra vez.")
    if int(t)>5:
        print("O barco é muito grande.")
        eh_valido = False
    if t in barcos_colocados2:
        print("Você já posicionou esse barco!")
        eh_valido = False
    return eh_valido
        

print("")
print("=============BATALHA NAVAL==============")  
print("")
print("Essas são suas embarcações, nºs 1-5:", barcos)

tab1 = gera_tab(20)  #Os tabuleiros dos jogadores 1 e 2, com os barcos posicionados.
tab2 = gera_tab(20)
print_tab(tab1, True)
print_tab2(tab2, True)

tab_at1 = gera_tab(20)  #Os tabuleiros dos jogares 1 e dois, que mostra as posições em que eles atiraram.
tab_at2 = gera_tab(20)

while cont_b<5: #Aqui começa o jogo, pedindo para os usuários a posição em que eles querem colocar as embarcações.
    pos, d, t = tuple(input("Jogador 1, onde você quer colocar o barco? (posição(ex: 4(y),5(x))-direção(N, S, L, O)-embarcação): ").split('-'))
    linha, coluna = tuple(pos.split(','))
    coords = (int(linha), int(coluna))

    while not validar(coords, d, t, tab1):  #Aqui é para qu enquanto o que o usuário digitar não condizer com o que precisa ser digitado, o programa repita até que o que o usuário digitar ficar de acordo.
        pos, d, t = tuple(input("Onde você quer colocar o barco? (posição(ex: 4,5)-direção(N, S, L, O)-embarcação): ").split('-'))
        linha, coluna = tuple(pos.split(','))
        coords = (int(linha), int(coluna))

    posiciona_barco(coords, d, t, tab1)
    print_tab(tab1, True)
    cont_b+=1
print(""), print(""), print(""), print(""), print(""), print(""), print(""), print(""), print(""), print(""), print(""), print(""), 
print(""), print(""), print(""), print(""), print(""), print(""), print(""), print(""), print(""), print(""), print(""), print(""), 
print(""), print(""), print(""), print(""), print(""), print(""), print(""), print(""), print(""), print(""), print(""), print(""), 
print(""), print(""), print(""), print(""), print(""), print(""), print(""), print(""), print(""), print(""), print(""), print("")
#Para um jogador não ver as posiçoes dos navios do outro.

 

while cont_c<5:  #Aqui é a mesma coisa, porém para o jogador 2.
    pos, d, t = tuple(input("Jogador 2, onde você quer colocar o barco? (posição(ex: 4,5)-direção(N, S, L, O)-embarcação): ").split('-'))
    linha, coluna = tuple(pos.split(','))
    coords = (int(linha), int(coluna))
    while not validar2(coords, d, t, tab2):
        pos, d, t = tuple(input("Onde você quer colocar o barco? (posição(ex: 4,5)-direção(N, S, L, O)-embarcação): ").split('-'))
        linha, coluna = tuple(pos.split(','))
        coords = (int(linha), int(coluna))

    posiciona_barco(coords, d, t, tab2)
    print_tab2(tab2, True)
    cont_c+=1
print(""), print(""), print(""), print(""), print(""), print(""), print(""), print(""), print(""), print(""), print(""), print(""), 
print(""), print(""), print(""), print(""), print(""), print(""), print(""), print(""), print(""), print(""), print(""), print(""), 
print(""), print(""), print(""), print(""), print(""), print(""), print(""), print(""), print(""), print(""), print(""), print(""), 
print(""), print(""), print(""), print(""), print(""), print(""), print(""), print(""), print(""), print(""), print(""), print("")

print("")
print("Vamos começar!")
print("")
    
while jogo==True:  #Aqui começa os ataques, e caso um jogador ganhe, irá avisa-lo disso e sair do jogo.
    n1=input("Jogador 1, digite a posição que você quer atacar: ")
    li, co = tuple(n1.split(','))
    if tab2[int(li)][int(co)] == "░░":
        print("Parabéns! Você atingiu um navio!")
        tab_at2[int(li)][int(co)] = '**'
        blocos1.pop()
        for line in tab_at2:
            print(''.join(line))
        if blocos1==[]:
            print("Parabéns Jogador 1! Você ganhou!")
            break
    else:
        print("Não foi dessa vez...")
        tab_at2[int(li)][int(co)] = '~~'
        for line in tab_at2:
            print(''.join(line))
        
    n2=input("Jogador 2, digite a posição que você quer atacar: ") #A mesma coisa que o anterior, porém para o jogador 2 poder atacar.
    li, co = tuple(n2.split(','))
    if tab1[int(li)][int(co)] == "░░":
        print("Parabéns! Você atingiu um navio!")
        tab_at1[int(li)][int(co)] = '**'
        blocos2.pop()
        for line in tab_at1:
            print(''.join(line))
        if blocos2==[]:
            print("Parabéns Jogador 1! Você ganhou!")
            break
    else:
        print("Não foi dessa vez...")
        tab_at1[int(li)][int(co)] = '~~'
        for line in tab_at1:
            print(''.join(line))
