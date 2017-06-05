#链表
class Node:
	def __init__(self,value,next=None):
		self.value=value
		self.next=next
L=Node('a',Node('b',Node('c',Node('d'))))


#二维列表
T=[["a","b"],["c"],['d',[e,f]]]
T[0][1]
T[2][1][0]

#二叉树类
class Tree:
	def __init__(self,left=None,right=None):
		self.left=left
		self.right=right
t=Tree(Tree('a','b'),Tree('c','d'))
t.right.left

#多路搜索数类
class Tree:
	def __init__(self,kids,next=None):
		self.kids=self.val=kids
		self.next=next
t=Tree(Tree('a',Tree()))	#next 是兄弟结点，Kids是孩子结点

#Bunch模式
class Bunch(dict):
	def __init__(self,*args,**kwds)
		super(Bunch,self).__init__(*args,**kwds)
		self.__dict__=self

T=Bunch
t=T(left=T(left='a',right='b'),right=T(left='c'))
t.left.right