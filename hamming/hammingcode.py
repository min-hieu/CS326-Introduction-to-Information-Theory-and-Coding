# Name : Nguyen Minh Hieu
# studentid: 20210722
# EE326 - Introduction to Information Theory and Coding
# Homework 4

import numpy as np
import matplotlib.pyplot as plt
from math import factorial as f
import os

# sample from bernoulli with probability p
def B(p):
    return np.random.choice(2,p=[1-p,p])

# sample from binomial with probability p
def Bi(n,k):
    return f(n)/(f(k)*f(n-k))


# Hamming matrix
H = [ [0,0,0,1,1,1,1],
      [0,1,1,0,0,1,1],
      [1,0,1,0,1,0,1], ]
H = np.array(H)

# null space of hamming matrix
codewords = [
        [0,0,0,0,0,0,0],[0,0,0,1,1,1,1],[0,0,1,0,1,1,0],[0,0,1,1,0,0,1],
        [0,1,0,0,1,0,1],[0,1,0,1,0,1,0],[0,1,1,0,0,1,1],[0,1,1,1,1,0,0],
        [1,0,0,0,0,1,1],[1,0,0,1,1,0,0],[1,0,1,0,1,0,1],[1,0,1,1,0,1,0],
        [1,1,0,0,1,1,0],[1,1,0,1,0,0,1],[1,1,1,0,0,0,0],[1,1,1,1,1,1,1],
        ]

codewords = np.array(codewords)

def bitFlip(bit, p):
    return (B(p)+bit)%2

def BSC(c, p):
    r = np.zeros(7)
    for i,bit in enumerate(c):
        r[i] = bitFlip(bit, p)
    return r

# get the distance between r and all codewords
def dist(r,code):
    s = 0
    for i in range(7):
        s += ( r[i] + code[i] ) % 2
    return s

def estimate(r):
    c_hat = codewords[np.argmin([dist(r,code) for code in codewords])]
    return c_hat

# calculate emperical error
def calErr(p):
    codes = []
    for i in range(10000):
        choice = np.random.choice(len(codewords))
        codes.append(codewords[choice])

    uCnt = 0
    dcCnt = 0
    duCnt = 0
    for i,c in enumerate(codes):
        r = BSC(c,p)
        c_hat = estimate(r)
        if sum(np.dot(H,r) % 2) == 0 and any(r != c):
            uCnt += 1
        if sum(np.dot(H,r) % 2) != 0 and all(c_hat == c):
            dcCnt += 1
        if sum(np.dot(H,r) % 2) != 0 and any(c_hat != c):
            duCnt += 1

    return (uCnt/10000, dcCnt/10000, duCnt/10000)


# Theoretical derivation of error probability
def analErr(p):
    p_u = p**7 + 7*p**4*(1-p)**3 + 7*p**3*(1-p)**4
    p_dc = 7*p*(1-p)**6
    p_du = sum([Bi(7,i)*p**i*(1-p)**(7-i) for i in range(2,8)]) - p_u
    return (p_u,p_dc,p_du)


# plotting result
p0 = range(1,10)
p1 = list(map(lambda x:round(x*0.001,3), p0))
p2 = list(map(lambda x:round(x*0.01,3), p0))
p3 = range(1,6)
p3 = list(map(lambda x:round(x*0.1,3), p3))
ps = (p1,p2,p3)

fig, ax = plt.subplots(3,4)
for i,p in enumerate(ps):
    unum = []
    dcnum = []
    dunum = []
    snum = []

    uanal = []
    dcanal = []
    duanal = []
    sanal = []
    for pr in p:
        a,b,c = calErr(pr)
        unum.append(a)
        dcnum.append(b)
        dunum.append(c)
        u,dc,du = analErr(pr)
        uanal.append(u)
        dcanal.append(dc)
        duanal.append(du)

    snum = [unum[i] + dunum[i] for i in range(len(p))]
    sanal = [uanal[i] + duanal[i] for i in range(len(p))]

    ax[i,0].plot(p, unum, label="numerical")
    ax[i,0].plot(p, uanal, label="analysis")
    ax[i,0].set(xscale='log', yscale='log')

    ax[i,1].plot(p, dcnum, label="numerical")
    ax[i,1].plot(p, dcanal, label="analysis")
    ax[i,1].set(xscale='log', yscale='log')

    ax[i,2].plot(p, dunum, label="numerical")
    ax[i,2].plot(p, duanal, label="analysis")
    ax[i,2].set(xscale='log', yscale='log')

    ax[i,3].plot(p, snum, label="numerical")
    ax[i,3].plot(p, sanal, label="analysis")
    ax[i,3].set(xscale='log', yscale='log')


cols = ["p_u", "p_dc", "p_du", "p_u + p_du"]
rows = ["p 1","p 2","p 3"]

for x, col in zip(ax[0], cols):
    x.set_title(col)

for x, row in zip(ax[:,0], rows):
    x.set_ylabel(row, rotation=0, size='large')

fig.set_size_inches(25, 13)
fig.tight_layout()
fig.savefig('./result.png', dpi=100)
