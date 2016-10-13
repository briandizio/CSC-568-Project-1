grid points


gridpoints=[]
for i in range(0,11):
	for j in range(0,11):
		gridpoints.append((i,j))


Node Class
	def __init__(self,value,point)
		self.value = value
		self.point = point
		self.gcost = euclidean(starting node and neighbor node)
		self.hcost = manhattan(starting node and goal node)
	def move_cost(self,other):
		return 0 if self.value == '.' else 1

# make each gridpoint into a note
S=(a,b)
OpenNodes=[]
OpenNodes.append((S,S.fcost))
ClosedNodes=[]

def aStar(start, goal, graph)
	# Open and closed sets
	openNodes = set()
	closedNodes = set()
	# Current point is the the starting point
	current = start
	# Add starting point to open set
	openNodes.add(current)
	# While the open nodes set is not empty
	while openNodes:
		# Find the node in openNodes with minimal G + H
		current = min(openNodes, key=lambda, o:o.G + o.H)
		# If this is the correct node, backtrack and return
		if current == goal
			path = []
			while current.parent:
				path.append(current)
				current = current.parent
		if neighbor.walkable=True:
			add neighbors to open list
	order the OpenNodes by fcost
		Then n=first element
	if N=G:
		break, find out what the path is within this loop and return it
	else: n=n+1
		if n.fcost=n+1.fcost
			if n.hcost=n+1.cost:
			

			select min(n.hcost,n+1.hcost)


Priority queues Open and Closed begin empty. 
Put S into Open with priority f(s) = g(s) + h(s)
Is Open empty?
Yes? No solution. 
No. Remove node with lowest f(n). Call it n. 
If n is a goal, stop and report success (for pathfinding, return the path)
Otherwise, expand n. For each n’ in successors(n)
Let f’ = g(n’) + h(n’) = g(n) + cost (n, n’) + h(n’)
If n’ not seen before or n’ previously expanded with f(n’) > f’ or n’ currently in Open with f(n’) > f’ 
Then place or promote n’ on Open with priority f’
Else ignore n’
Place record for n in Closed
