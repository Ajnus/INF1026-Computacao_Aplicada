# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 19:06:25 2019

@author: ajnas
"""
'''
#1
def decidePresente(valorEmCaixa, valorPresente):
    if (valorPresente > valorEmCaixa*0.8):
        return (5, valorPresente*1.1/5)
    elif (valorPresente >= valorPresente*0.4):
        return (3, valorPresente*1.08/3)
    else:
        return (1, valorPresente*0.95/1)
     
    
valorEmCaixa = float(input("Insira o valor em caixa: "))
valorPresente = float(input("Insira o valor do Presente: "))
print(decidePresente(valorEmCaixa, valorPresente))
'''
'''
#2
def ordena(a, b, c):
    if a > b:
        if a > c:
            if b > c:
                return (a, b, c)
            else:
                return (a, c, b)
        else:
            return (c, a, b)
    else:
        if b > c:
            if a > c:
                return (b, a, c)
            else:
                return (b, c, a)
        else:
            return (c, b, a)
        
arq = open("ordena.txt", 'r')
candidatos = arq.readlines()
#print(candidatos)
for line in candidatos:
    candidato = line.split(';')
    #print(candidato)
    inscricao = candidato[0]
    ndoA = candidato[1]
    ndoB = candidato[2]
    ndoC = candidato[3]
    ndbA = candidato[4]
    ndbB = candidato[5]
    ndbC = candidato[6]
    originalidadeFinal = ordena(ndoA, ndoB, ndoC)
    belezaFinal = ordena(ndbA, ndbB, ndbC)
    #print(originalidadeFinal[1])
    notaFinal = float(originalidadeFinal[1])*0.6+float(belezaFinal[1])*0.4
    print("%s, sua nota final é: %.2f"% (inscricao, notaFinal))
'''
'''    
#3
def HMS(sec):
    minutos = sec//60
    s = sec%60
    return (minutos//60, minutos%60, s)

arq = open("inscritempo.txt", 'r')
atletas = arq.readlines()
maior_valor = 0
menor_valor = 36000

for line in atletas:
    atleta = line.split('\t')
    inscricao = atleta[0]
    sec = float(atleta[1])
    if (sec > 36000):
        print("O atleta %s foi desclassificado." % inscricao)
    else:
        if (sec>maior_valor):
            maior_valor = sec
            maior_id = inscricao
        if (sec<menor_valor):
            menor_valor = sec
            menor_id = inscricao
        oTempo = HMS(sec)
        print("O tempo do atleta %s foi de %.2f horas, %.2f minutos, %.2f segundos." % (inscricao, oTempo[0], oTempo[1], oTempo[2]))
print("\nO atleta que levou mais tempo foi %s." % maior_id)
print("O atleta que levou menos tempo foi %s." % menor_id)
'''
'''
#4
def ehPerfeito(num):
    divisor=1
    lDivisores=[]
    soma=0
    while (divisor!=num):
        if (num % divisor ==0):
            lDivisores.append(divisor)
        divisor+=1
    for el in lDivisores:
        soma+=el
    return (soma == num, lDivisores)

def avaliaNumero(num):
    tupla = ehPerfeito(num)
    print("O número é: %s\nSeus divisores são: %s" %(num, tupla[1]))
    if tupla[0] == True:
        print("O número é perfeito.")
    else:
        print("O número não é perfeito.")

avaliaNumero(8)
'''
'''
#5
def contaElementos(tupla):
    count = 0
    for el in tupla:
        if isinstance(el, int):
            count+=1
        elif isinstance(el,list) or isinstance(el,tuple):
            count+=contaElementos(el)
    return count

print(contaElementos( ([1,2],'a',7.3,3, [10,20]) ))
print(contaElementos( ([1,2,3] ,[ 'a', 'b', 'c']) ))
print(contaElementos(([1, (2, 3), ('a', (2.0, ([3, 9.0], 'casa', (1,), 'Ana'), [ 'a', 'b']))],
4.4, 20, 10, ['a', 'b', 'c']) ))
'''
'''
#6
def testaContida(tupla):
    lPalavra=[]
    i=0
    while i < len(tupla):
        if isinstance(tupla[i],str):
            lPalavra=list(tupla[i])
            j=0
            while j < len(lPalavra):
                if lPalavra[j] == 'o':
                    if lPalavra[j+1]=='i':
                        return True
                j+=1
        
        elif isinstance(tupla[i],list) or isinstance(tupla[i],tuple):
            result = testaContida(tupla[i])
            if result == True:
                return True
        #elif isinstance(tupla[i],int) or isinstance(tupla[i],float):
         #   continue
        i+=1
        
    return False
    
print(testaContida( ("foi",) ))
print(testaContida( ([1,2,3],(('onde',2.3), 'oi',78), ['a', 'b', 'c']) ))
print(testaContida( ( ('MAO', 'MOA') , 13.8 , 'c' , 6 , [2,3] ) ))
'''
'''
#7 
def testa(tupla, string):
    count=0
    lPalavra=[]
    lString = list(string)
    i=0
    while i < len(tupla):
        if isinstance(tupla[i],str):
            lPalavra=list(tupla[i])
            j=0
            while j < len(lPalavra):
                k=0
                ok=0
                while k < len(lString) and (j+k) < len(lPalavra):
                    if lPalavra[j+k] == lString[k]:
                            ok+=1
                    k+=1        
                    if ok == len(lString):
                        count+=1
                j+=1
        
        elif isinstance(tupla[i],list) or isinstance(tupla[i],tuple): 
                count+= testa(tupla[i], string)
        #elif isinstance(tupla[i],int) or isinstance(tupla[i],float):
         #   continue
        i+=1
        
    return count

print(testa (("foi",),"oi"))
print(testa ( ([1,2,3],(('onde',2.3), 'oi',78), ['a', 'b', 'c']),"oi") )
print(testa (([1,2,3],(('onde', 'noiva',2.3), 'oi',78), ['a', 'b', 'c']) ,"oi"))
print(testa (( ('MAO', 'MOA') , 13.8 , 'c' , 6 , [2,3] ) ,"oi"))
'''
'''
#8
def temperaturas(tTempMedia):
    tMeses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
    maior_valor = 0
    menor_valor = 36000
    mediaAnual = sum(tTempMedia)/len(tTempMedia)
    
    print("Os meses com temperaturas acima da média (%.1f ºC) são:" % mediaAnual)
    for i, el in enumerate(tTempMedia):
        if (el > maior_valor):
            maior_valor = el
            maior_id = i
        if (el<menor_valor):
            menor_valor = el
            menor_id = i
        if el > mediaAnual:
            print("%s: %.1f ºC" % (tMeses[i], el))
            
    return ( (menor_valor, tMeses[menor_id]), (maior_valor, tMeses[maior_id]) ) 
    
             

tTempMedia = (40, 38, 33, 30, 28, 27, 26, 29, 31, 25, 26)
tMais = temperaturas(tTempMedia)
print("O mês mais frio foi: ", tMais[0])
print("O mês mais quente foi: ", tMais[1])
'''

'''
#9
def organiza(tIntegrantes):
    altura = tIntegrantes[0][1] - tIntegrantes[1][1]
    if altura < 0:
        altura = -altura
        return (altura, (tIntegrantes[1][0], tIntegrantes[0][0]))
    else:
        return (altura, (tIntegrantes[0][0], tIntegrantes[1][0]))
    
    
lPrimeiroDia = []
lSegundoDia = []
nDupla = int(input("Número da dupla: "))
while nDupla!=0:
    nomeIntegrante1 = input("Nome do primeiro integrante: ") 
    alturaIntegrante1 = float(input("Sua altura? (cm) "))
    nomeIntegrante2 = input("Nome do segundo integrante: ") 
    alturaIntegrante2 = float(input("Sua altura? (cm) "))
    
    Integrante1 = (nomeIntegrante1, alturaIntegrante1)
    Integrante2 = (nomeIntegrante2, alturaIntegrante2)
    tIntegrantes=(Integrante1, Integrante2)
    
    tDupla = (nDupla, organiza(tIntegrantes)[1][0], organiza(tIntegrantes)[1][1])
    
    
    if organiza(tIntegrantes)[0] <= 15:
        lPrimeiroDia.append(tDupla)
    else:
        lSegundoDia.append(tDupla)

    print("---\n")
    nDupla = int(input("Número da dupla: "))
    
lProgramacao = (lPrimeiroDia, lSegundoDia)
print("A programação das apresentações é: ", lProgramacao)
'''
'''
#10
def um_sensor(arquivo, sensor):
    arq = open(arquivo, 'r')
    sensores = arq.read()
    lSensores = sensores.split('\n')
    leituraSensor=[]
    #i=0
    menorTemp = 100
    menorUmi = 100
    
    for el in lSensores:
        if el == '':
            break
        leituraSensor = el.split(';')
        sens = int(leituraSensor[0])
        if sens != sensor:
            continue
    
        temp = leituraSensor[2]
        temp = float(temp)
        umi = leituraSensor[3]
        umi = float(umi)
        
        if temp < menorTemp:
            menorTemp = temp
            menorTempId = leituraSensor[1]
        if umi < menorUmi:
            menorUmi = umi
            menorUmiId = leituraSensor[1]
                
    return (sensor, (menorTemp, menorTempId), (menorUmi, menorUmiId))

resultados3 = um_sensor("Registros.txt", 3)
print("Sensor %s- Temperatura Mínima %.1fºC às %sh e Umidade Mínima: %.1f%% às %sh" % (resultados3[0], resultados3[1][0], resultados3[1][1], resultados3[2][0], resultados3[2][1]))
resultados2 = um_sensor("Registros.txt", 2)
print("Sensor %s- Temperatura Mínima %.1fºC às %sh e Umidade Mínima: %.1f%% às %sh" % (resultados2[0], resultados2[1][0], resultados2[1][1], resultados2[2][0], resultados2[2][1]))
resultados4 = um_sensor("Registros.txt", 4)
print("Sensor %s- Temperatura Mínima %.1fºC às %sh e Umidade Mínima: %.1f%% às %sh" % (resultados4[0], resultados4[1][0], resultados4[1][1], resultados4[2][0], resultados4[2][1]))
resultados5 = um_sensor("Registros.txt", 5)
print("Sensor %s- Temperatura Mínima %.1fºC às %sh e Umidade Mínima: %.1f%% às %sh" % (resultados5[0], resultados5[1][0], resultados5[1][1], resultados5[2][0], resultados5[2][1]))
resultados1 = um_sensor("Registros.txt", 1)
print("Sensor %s- Temperatura Mínima %.1fºC às %sh e Umidade Mínima: %.1f%% às %sh" % (resultados1[0], resultados1[1][0], resultados1[1][1], resultados1[2][0], resultados1[2][1]))
resultados6 = um_sensor("Registros.txt", 6)
print("Sensor %s- Temperatura Mínima %.1fºC às %sh e Umidade Mínima: %.1f%% às %sh" % (resultados6[0], resultados6[1][0], resultados6[1][1], resultados6[2][0], resultados6[2][1]))

print("\nHora %sh:\n\tSensor: %s - Temperatura: %.1fºC" % (resultados3[1][1], resultados3[0], resultados3[1][0]))
print("Hora %sh:\n\tSensor: %s - Temperatura: %.1fºC" % (resultados2[1][1], resultados2[0], resultados2[1][0]))
print("Hora %sh:\n\tSensor: %s - Temperatura: %.1fºC" % (resultados4[1][1], resultados4[0], resultados4[1][0]))
print("Hora %sh:\n\tSensor: %s - Temperatura: %.1fºC" % (resultados5[1][1], resultados5[0], resultados5[1][0]))
print("\tSensor: %s - Temperatura: %.1fºC" % (resultados1[0], resultados1[1][0]))
print("Hora %sh:\n\tSensor: %s - Temperatura: %.1fºC" % (resultados6[1][1], resultados6[0], resultados6[1][0]))
'''
'''
#11
def sorteadosnaCartela(cartela):
    count=0
    for el in cartela:
        if el[0][1] == 1:
            count+=1
    return count

def lugarVago(lugarDaCartela, cartela):
    for el in cartela:
        if el[0] == lugarDaCartela:
            if el[0][1] == 0:
                return True
            else:
                return False
    
def vizinhoLivre (lugarDaCartela, cartela):
    lLivres=[]
    lugarDaCartela[1] +=1
    if (cartela[lugarDaCartela][1] == 0):
        lLivres.append(cartela)
    cartela[0][1] -=2
    if (cartela[lugarDaCartela][1] == 0):
        lLivres.append(cartela)
    cartela[0][1] +=1
    cartela[0][0] +=1
    if (cartela[lugarDaCartela][1] == 0):
        lLivres.append(cartela)
    cartela[0][0]-=2
    if (cartela[lugarDaCartela][1] == 0):
        lLivres.append(cartela)
    
    return lLivres

def maiorNumLugLivres(cartela):
    maiorLinha = 0
    for el in cartela:
        lugarDaCartela = el[0] 
        for el in lugarDaCartela[0]:
            count=0
            for el in lugarDaCartela[1]:
                if cartela[1] == 0:
                    count+=1
                if count > maiorLinha:
                    maiorLinha = lugarDaCartela[0][0]
                
    return maiorLinha

def Vencedores(jogoFinalizado):
    lVencedores=[]
    for el in jogoFinalizado:
        jogador = el[0]
        cartela = el[1]
        count=0
        for el in cartela:
            #lugarDaCartela = el[0]
            situacao = el[1]
            if situacao == 1:
                count+=1
        if count == 60:
            lVencedores.append(jogador)
                
    return lVencedores
            
lugarDaCartela = (linha, posicao, numero) 
cartela = [(lugarDaCartela, situacao),(lugarDaCartela, situacao), (lugarDaCartela, situacao)]
jogoFinalizado = [(jogador, cartela), (jogador, cartela), (jogador, cartela)]
'''

#12

def trataUmLaboratorio(arquivo, lab):
    arq = open(arquivo, 'r')
    sensores = arq.read()
    lSensores = sensores.split('\n')
    leituraSensor=[]
    #i=0
    menorTemp = 100
    menorUmi = 100
    
    for el in lSensores:
        if el == '':
            break
        leituraSensor = el.split(';')
        labe = leituraSensor[0]
        if labe != lab:
            continue
    
        temp = leituraSensor[2]
        temp = float(temp)
        umi = leituraSensor[3]
        umi = int(umi)
        
        if temp < menorTemp:
            menorTemp = temp
            menorTempId = leituraSensor[1]
            menorTempId = int(menorTempId)
        if umi < menorUmi:
            menorUmi = umi
            menorUmiId = leituraSensor[1]
            menorUmiId = int(menorUmiId)
                
    return (lab, (menorTemp, menorTempId), (menorUmi, menorUmiId))

resultadosDI546 = trataUmLaboratorio("RegistrosLab.txt", 'DI546')
print("Lab %s- Temperatura Mínima %.1fºC às %sh e Umidade Mínima: %.1f%% às %sh" % (resultadosDI546[0], resultadosDI546[1][0], resultadosDI546[1][1], resultadosDI546[2][0], resultadosDI546[2][1]))
resultadosCB252 = trataUmLaboratorio("RegistrosLab.txt", 'CB252')
print("Lab %s- Temperatura Mínima %.1fºC às %sh e Umidade Mínima: %.1f%% às %sh" % (resultadosCB252[0], resultadosCB252[1][0], resultadosCB252[1][1], resultadosCB252[2][0], resultadosCB252[2][1]))
resultadosDI548 = trataUmLaboratorio("RegistrosLab.txt", 'DI548')
print("Lab %s- Temperatura Mínima %.1fºC às %sh e Umidade Mínima: %.1f%% às %sh" % (resultadosDI548[0], resultadosDI548[1][0], resultadosDI548[1][1], resultadosDI548[2][0], resultadosDI548[2][1]))
resultadosFI362 = trataUmLaboratorio("RegistrosLab.txt", 'FI362')
print("Lab %s- Temperatura Mínima %.1fºC às %sh e Umidade Mínima: %.1f%% às %sh" % (resultadosFI362[0], resultadosFI362[1][0], resultadosFI362[1][1], resultadosFI362[2][0], resultadosFI362[2][1]))
resultadosCB318 = trataUmLaboratorio("RegistrosLab.txt", 'CB318')
print("Lab %s- Temperatura Mínima %.1fºC às %sh e Umidade Mínima: %.1f%% às %sh" % (resultadosCB318[0], resultadosCB318[1][0], resultadosCB318[1][1], resultadosCB318[2][0], resultadosCB318[2][1]))
resultadosQI170 = trataUmLaboratorio("RegistrosLab.txt", 'QI170')
print("Lab %s- Temperatura Mínima %.1fºC às %sh e Umidade Mínima: %.1f%% às %sh" % (resultadosQI170[0], resultadosQI170[1][0], resultadosQI170[1][1], resultadosQI170[2][0], resultadosQI170[2][1]))

print("\nDep DI:\n\tLab: %s - Mínima: %.1fºC - %dh" % (resultadosDI546[0], resultadosDI546[1][0], resultadosDI546[1][1]))
print("\tLab: %s - Mínima: %.1fºC - %dh" % (resultadosDI548[0], resultadosDI548[1][0], resultadosDI548[1][1]))
print("Dep CB:\n\tLab: %s - Mínima: %.1fºC - %dh" % (resultadosCB252[0], resultadosCB252[1][0], resultadosCB252[1][1]))
print("\tLab: %s - Mínima: %.1fºC - %dh" % (resultadosCB318[0], resultadosCB318[1][0], resultadosCB318[1][1]))
print("Dep FI:\n\tLab: %s - Mínima: %.1fºC - %dh" % (resultadosFI362[0], resultadosFI362[1][0], resultadosFI362[1][1]))
print("Dep QI:\n\tLab: %s - Mínima: %.1fºC - %dh" % (resultadosQI170[0], resultadosQI170[1][0], resultadosQI170[1][1]))