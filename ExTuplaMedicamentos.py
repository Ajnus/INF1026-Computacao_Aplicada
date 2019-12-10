# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 16:39:56 2019

@author: ajnas
"""

#Parte1
def trataUmGrupo(arquivo):
    arq = open(arquivo, 'r')
    grupo = arq.read()
    lGrupo = grupo.split('\n')
    tGrupo = tuple(lGrupo)
    nomedaSubstancia = tGrupo[0]
    tempoCuraTotal=0
    qtdColaterais=0
    
    for el in tGrupo:
        linha = tuple(el.split(','))
        if len(linha) == 1:
            continue    
        tempoCuraTotal+=int(linha[0])
        if linha[1] != 'ausente':
                qtdColaterais+=1
    
    tempoCuraMedio = tempoCuraTotal/10    
    return (nomedaSubstancia, tempoCuraMedio, qtdColaterais)

#Parte2
def menorTempoMedio(lRespostas):
    menorTempoCuraMedio = 100
    for el in lRespostas:
        if el[1] < menorTempoCuraMedio:
            menorTempoCuraMedio = el[1]
            substMenorTempoCuraMedio = el[0]
            qtdColaterais = el[2]
        
    
    return (substMenorTempoCuraMedio, menorTempoCuraMedio, qtdColaterais)

#Parte3
def efeitosColateraisMaxMin(lRespostas):
    maxQtdColaterais=0
    minQtdColaterais = 100
    for el in lRespostas:
        if el[2] > maxQtdColaterais:
            maxQtdColaterais = el[2]
            maxTempoCuraMedio = el[1]
            maxSubstEfeitos = el[0]
        if el[2] < minQtdColaterais:
            minQtdColaterais = el[2]
            minTempoCuraMedio = el[1]
            minSubstEfeitos = el[0]
    
    return ((maxSubstEfeitos, maxTempoCuraMedio, maxQtdColaterais),
            (minSubstEfeitos, minTempoCuraMedio, minQtdColaterais))


#Programa
lRespostas=[]
lRespostas.append(trataUmGrupo("grupoa.txt"))
lRespostas.append(trataUmGrupo("grupob.txt"))
lRespostas.append(trataUmGrupo("grupoc.txt"))
lRespostas.append(trataUmGrupo("grupod.txt"))

print(lRespostas)
print('A substância que teve o menor tempo médio de cura foi:\n',
      menorTempoMedio(lRespostas))
print('A substância com MAIOR e MENOR número de efeitos colaterais foram, respectivamente:\n',
      efeitosColateraisMaxMin(lRespostas))
