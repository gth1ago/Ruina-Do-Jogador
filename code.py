from numpy import random as rnd
import numpy as np

fortunaA = 10
fortunaB = 10

contador = 0
n = 1000
nJogadas = []

for j in range(n):
    #declarando fortuna do Jogador A
    Fj = fortunaA
    #declarando fortuna do Jogador B
    Fm = fortunaB

    #probabilidade de sair cara ou coroa
    p = 0.5
    q = 1-p

    #vetores para armazenamento do histórico ao longo do jogo
    mFm = []
    mFj = []
    x = []
    i = 0

    while (Fj>0 and Fm>0):
        #lança a moeda
        face = rnd.random()
        #Avalia qual o vencedor da rodada, transferindo 1 unidade do perdedor para o vencedor
        if (face <=p):
            Fm += 1
            Fj -= 1
        else:
            Fj += 1
            Fm -= 1
        #registra histórico da rodada
        mFm.append(Fm)
        mFj.append(Fj)
        i+=1
        x.append(i)
    #faz a contagem de vezes em que A foi vencedor em cada um dos n jogos
    if (Fj != 0):
        contador +=1
    nJogadas.append(i)

#calcula a probabilidade de A vencer o jogo em n repetições usando a definição frequentista de probabilidade:
#número de jogos vencidos sobre o total de jogos.
print("-" * 30)
print("Quantidade de repeticao = ", n)
print("Fortuna A - Inicial ", fortunaA)
print("Fortuna B - Inicial ", fortunaB)
print("Probabilidade P = ", p);
print("Probabilidade Q = ", q);
print("Probabilidade de A vencer o jogo em n repeticao = ", contador/n)
print("Media de Partidas necessarias para finalizacao do jogo = ", np.mean(nJogadas))
print("\nJogadas em cada repeticao = ", nJogadas)
