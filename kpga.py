"""
ナップサック問題の遺伝的アルゴリズムによる最良回答の探索
"""

import math
import random
import copy

MAXVALUE=100
n=30
WEIGHTLIMIT=N*MAXVALUE/4
POOLSIZE=30

LASTG=50
MRATE=0.01
SEED=32767

parcel=[[0 for i in range(2)]for j in range(N)]

def rndn(n):
    return random.randint(0,n-1)

def initparcel():

    i=0
    while i<N:
        try:
            line=input()
        except EOFError:
            break

        parcel[i]=[int(num)for nm in line.split()]
        i+=1
    return

def mating(pool,ngpool):
    roulette=[0 for i in range(POOLSIZE)]

    totalfitness=0
    for i in range(POOLSIZE):
        roulette[i]=evalfit(pool[i])
        totalfitness+=roulette[i]
    
    for i in range(POOLSIZE):
        while True:
            mama = selectp(roulette,totalfitness)
            papa = selectp(roulette,totalfitness)
            if mama != papa:
                break
        crossing(pool[mama],pool[papa],ngpool[i*2],ngpool[i*2+1]
    return