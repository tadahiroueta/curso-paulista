import re
import math

def le_assinatura():
    print()
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print()
    
    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    print()
    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        print()
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    return frase.split()

def n_palavras_unicas(listPA_palavras):
    freq = dict()
    unicas = 0
    for palavra in listPA_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(listPA_palavras):
    freq = dict()
    for palavra in listPA_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):

    walD = difPos(as_a[0],as_b[0])
    ttrD = difPos(as_a[1],as_b[1])
    hlrD = difPos(as_a[2],as_b[2])
    salD = difPos(as_a[3],as_b[3])
    sacD = difPos(as_a[4],as_b[4])
    palD = difPos(as_a[5],as_b[5])

    Sab = (walD + ttrD + hlrD + salD + sacD + palD) / 6
    return Sab

def calcula_assinatura(texto):

    listS = separa_sentencas(texto)
    listF = setListF(listS)
    listP = setListP(listF)
    
    wal = tamMedF(listP)
    ttr = (n_palavras_diferentes(listP)) / (len(listP))
    hlr = (n_palavras_unicas(listP)) / (len(listP))
    sal = tamMedF(listS)
    sac = (len(listF)) / (len(listS))
    pal = tamMedF(listF)

    return [wal,ttr,hlr,sal,sac,pal]

def avalia_textos(textos, ass_cp):
    cp=100
    nCp=0
    
    for i in textos:
        nCp += 1
        texCp = compara_assinatura(calcula_assinatura(i),ass_cp)
        
        if texCp < cp:
            cp = texCp
            nCpTex = nCp
            
    return nCpTex

def difPos(fa,fb):
    return math.sqrt((fa-fb)**2)
    
def tamMedF(listSFP):
    tamMed=0
    
    for i in listSFP:
        tamMed += len(i)

    return(tamMed/len(listSFP))

def setListF(listS):
    listF=[]
    
    for i in range(len(listS)):
        x = separa_frases(listS[i])
        listF += x

    return listF

def setListP(listF):
    x=''
    
    for i in listF:
        x += i
        x += ' '

    return separa_palavras(x)

############################################################################################

ass = le_assinatura()
print()
print('O autor do texto',avalia_textos(le_textos(),ass),'está infectado com COH-PIAH')
