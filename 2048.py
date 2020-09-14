import readchar
from itertools import chain
import random
n=5
c= ""# quit:0 down:2 left:4 right:6 up:8 pass_but_generate_random:1,3,7,9 
l=[]
for i in range(n):
    l.append([])
    l[i]=[]
    for j in range(n):
        l[i].append(0)
def input():
    global c
    c=readchar.readchar()
    move()
def rand(l):
    ll=list(chain.from_iterable(l))
    len_ll=len(list(filter(lambda x : x==0,ll)))
    rnd=random.randint(0,len_ll)
    cnt=0
    for i in range(len(ll)):
        if ll[i] == 0: 
            if cnt==rnd:
                ll[i]=1
                cnt+=1
            else:
                cnt+=1
    return list(zip(*(iter(ll),)*n))
def board():
    print('___________')
    for i in range(len(l)):
        for j in range(len(l)):
            print('{:^5s}'.format(str(l[i][j])),end='')
        print()
def reduce_row(mat):
    for i in range(len(mat)):#col
        mat[i]=list(mat[i])
        list_without_zero=list(filter(lambda x:x!=0,mat[i]))
        new_list_merged=[]
        for k in range(len(list_without_zero)-1):
            if list_without_zero[k]!=-1:
                if list_without_zero[k]!=list_without_zero[k+1]:
                    new_list_merged.append(list_without_zero[k])
                else:
                    new_list_merged.append(list_without_zero[k]*2)
                    list_without_zero[k+1]=-1
        if  len(list_without_zero)>0 and list_without_zero[-1]!=-1:
            new_list_merged.append(list_without_zero[-1])        
        while len(new_list_merged)<len(mat):
            new_list_merged.append(0)
        mat[i]=new_list_merged
    return mat

def move():
    global l
    if c =='8':
        l=list(zip(*l))
        l=reduce_row(l)
        l=list(zip(*l))
    if c=='4':
        l=reduce_row(l)
    if c=='6':
        l=[ll[::-1] for ll in l]
        l=reduce_row(l)
        l=[ll[::-1] for ll in l]
    if c=='2':
        l=list(zip(*l))
        l=[ll[::-1] for ll in l]
        l=reduce_row(l)
        l=[ll[::-1] for ll in l]
        l=list(zip(*l))
rand(l)
board()
while c != '0' :
    input()
    l=rand(l)
    board()
