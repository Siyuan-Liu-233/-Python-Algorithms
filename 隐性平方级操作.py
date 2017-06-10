from random import randrange
# #1.1
# L=[randrange(10000) for i in range(1000)]
# 42 in L
# #1.2 更快
# S=set(L)
# 42 in S

# #####################
# #2.1
# s=''
# for chunk in string_producer():
# 	s+=chunk
# #2.2 更快  +操作会复制上一字符串内容
# chunks=[]
# for chunk in string_producer():
# 	chunks.append(chunk)
# s="".join(chunks)

# #######################
# #3.1
# lists=[[1,2],[3,4,5].[6]]
# sum(lists,[])
# #3.2 更快
# res=[]
# for lst in lists:
# 	res.extend(lst)


#浮点运算的麻烦
a=sum(0.1 for i in range(10))==1.0
print(a)	#输出False！！不要对浮点数进行等值比较
from decimal import *
a=(sum(Decimal('0.1') for i in range(10))==Decimal('1.0'))
print(a)	#借助decimal进行比较

from math import sqrt
x=8762348761.13
a=sqrt(x+1)-sqrt(x)
b=1/(sqrt(x+1)+sqrt(x))
print(a,b)		#后者更精确

