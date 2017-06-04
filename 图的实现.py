#邻接集表示法
a,b,c,d,e,f,g,h=range(8)
N=[
{b,c,d,e,f},    #a
{c,e},          #b
{d},            #c
{e},            #d
{f},            #e
{c,g,h},        #f
{f,h},          #g
{f,g}           #h
]

#邻接列表
a,b,c,d,e,f,g,h=range(8)
N=[
[b,c,d,e,f],    #a
[c,e],          #b
[d],            #c
[e],            #d
[f],            #e
[c,g,h],        #f
[f,h],          #g
[f,g]           #h
]

#加权邻接字典
a,b,c,d,e,f,g,h=range(8)
N=[
{b:2,c:1,d:3,e:9,f:4},  #a
{c:4,e:3},              #b
{d:8},                  #c
{e:7},                  #d
{f:5},                  #e
{c:2,g:2,h:2},          #f
{f:1,h:6},              #g
{f:1,g:8}               #h
]
b in N[a]   #是否相连
len(N[f])   #度
N[a][b]     #权值（a，b）

#邻接集字典
N={
    'a':set('bcdef'),
    'b':set('ce'),
    'c':set('d'),
    'd':set('e'),
    'e':set('f'),
    'f':set('cgh'),
    'g':set('fh'),
    'h':set('fg')
}

#邻接矩阵
a,b,c,d,e,f,g,h=range(8)
N=[
[0,1,1,1,1,1,0,0], #a
[0,0,1,0,1,0,0,0], #b
[0,0,0,1,0,0,0,0], #c
[0,0,0,0,1,0,0,0], #d
[0,0,0,0,0,1,0,0], #e
[0,0,1,0,0,0,1,1], #f
[0,0,0,0,0,1,0,1], #g
[0,0,0,0,0,1,1,0]  #h
]
N[a][b]     #是否连接
sum(N[f])   #度

#加权矩阵
a,b,c,d,e,f,g,h=range(8)
inf=float('inf')

#  a    b    c    d    e    f    g    h

W = [
[  0,   2,   1,   3,   9,   4, inf, inf],  # a
[inf,   0,   4, inf,   3, inf, inf, inf],  # b
[inf, inf,   0,   8, inf, inf, inf, inf],  # c
[inf, inf, inf,   0,   7, inf, inf, inf],  # d
[inf, inf, inf, inf,   0,   5, inf, inf],  # e
[inf, inf,   2, inf, inf,   0,   2,   2],  # f
[inf, inf, inf, inf, inf,   1,   0,   6],  # g
[inf, inf, inf, inf, inf,   9,   8,   0]   # h

]  
W[a][b]<inf
sum(1 for w in W[a] if w < inf)-1   #度


