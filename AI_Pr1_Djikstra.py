# This will need to be revised.  Right now, each entry in the next-right-hand-column
# is a successor
def succ(point,matrix):
	succ=[]
	x,y=point
	for i in matrix[:,y+1]:

		succ.append(n2a)
	return succ

# Define a stack class to be used in the algorithm
class Stack:
     def __init__(self):
         self.items = []
     def isEmpty(self):
         return self.items == []
     def push(self, item):
         self.items.append(item)
     def pop(self):
         return self.items.pop()
     def peek(self):
         return self.items[len(self.items)-1]
     def size(self):
         return len(self.items)

# Djikstra, Depth First Search Algorithm
def search(start,goal):
	# Start is always from the empty-left-most column
	# Goal=desiredReturn, a numerical value
	P=stack()
	P.push(start)
	for i in succ(start):
		P.push(i)
		# Below line needs to be fixed.  We must compute node.h(rate,time)
	while P is empty==False and h(P.peek())<desiredReturn: 
	# 
		if succ(P.peek()) is empty:
			P.pop()
		else
			expandOfTopP=succ(P.peek)
			s=expandOfTopP[0]
			del expandOfTopP[0]
			for i in succ(s):
				P.push(i)
	if P is empty
		return Failure
	else:
		return P




