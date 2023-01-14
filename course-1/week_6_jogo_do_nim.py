f=False
def r():
    global n
    global t
    global f
    if n==1:
        print('Agora resta apenas uma peça no tabuleiro.')
        return
    if n>1:
        print('Agora restam',n,'peças no tabuleiro.')
        return
    f=True
    print('Fim do jogo! O computador ganhou!')
    return
def computador_escolhe_jogada(a,b):
    print()
    global n
    global m
    global t
    n=a
    m=b
    t=1
    p=n%(m+1)
    if p==1:
        n-=p
        print('O computador tirou uma peça.')
        return
    n-=p
    print('O computador tirou',p,'peças')
    return
def usuario_escolhe_jogada(a,b):
    print()
    p=int(input('Quantas peças você vai tirar? '))
    global n
    global m
    n=a
    m=b
    if p>n or p>m:
        print()
        print('Oops! Jogada inválida! Tente de novo.')
        usuario_escolhe_jogada(n,m)
        return
    n-=p
    global t
    t=0
    if p==1:
        print('Você tirou uma peça.')
        return
    print('Você tirou',p,'peças.')
    return
def partida():
    print()
    global n
    global m
    global t
    global f
    n=int(input('Quantas peças? '))
    m=int(input('Limite de peças por jogada? '))
    print()
    if n%(m+1)==0:
        print('Voce começa!')
        t=1
    else:
        print('Computador começa!')
        t=0
    while f==False:
        if t==0:
            computador_escolhe_jogada(n,m)
            r()
        else:
            usuario_escolhe_jogada(n,m)
            r()
    f=False
def campeonato():
    print()
    print('Voce escolheu um campeonato!')
    print()
    print('**** Rodada 1 ****')
    partida()
    print()
    print('**** Rodada 2 ****')
    partida()
    print()
    print('**** Rodada 3 ****')
    partida()
    print()
    print('**** Final do campeonato! ****')
    print()
    print('Placar: Você 0 X 3 Computador')
print('Bem-vindo ao jogo do NIM! Escolha:')
print()
print('1 - para jogar uma partida isolada')
o=int(input('2 - para jogar um campeonato '))
if o==1:
    partida()
else:
    campeonato()
