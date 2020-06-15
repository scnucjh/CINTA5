q , p = 131,263  # p,q都是素数且p = 2q+1

h = 2            # 选取的h
g = h * h % p

gk = g           # g的k次方

for k in range(0,q): #打印 <g> 
    print(gk,end=' ')
    gk = gk * g % p