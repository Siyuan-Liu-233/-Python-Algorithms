from random import randrange
#1.1
L=[randrange(10000) for i in range(1000)]
42 in L
#1.2 更快
S=set(L)
42 in S

#####################
#2.1
s=''
for chunk in string_producer():
	s+=chunk
#2.2 更快
chunks=[]
for chunk in string_producer():
	chunks.append(chunk)
s="".join(chunks)

#######################
#3.1
lists=[[1,2],[3,4,5].[6]]
sum(lists,[])
#3.2 更快
res=[]
for lst in lists:
	res.extend(lst)


