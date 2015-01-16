import sys

#
# Data classes
#


# Class representing a node
class Node:
	def con(self, newnode):
		self.visited[newnode] = False

	def __init__(self, num):
		self.num = num
		self.visited = {}
		self.count = 1
		pass

	def getNum(self):
		return self.num

	def scan(self, upnode):
		global removed

		for node in self.visited:
			if node == upnode:
				self.visited[node] = True
				continue
			if not self.visited[node]:
				self.visited[node] = True
				self.count += node.scan(self)
		if (not (self.count % 2) and upnode is not None):
			removed += 1
			return 0

		return self.count

# set of nodes
nodes = {}

removed = 0

#
# Setup Functions
#


# add an edge to the set
def addEdge(newEdge):
	addNode(newEdge[0])
	addNode(newEdge[1])
	connect(newEdge)


# add a node to the nodes list if it is not present
def addNode(newNode):
	if newNode not in nodes:
		nodes[newNode] = Node(newNode)


# connect the two nodes of an edge
def connect(edge):
	nodes[edge[0]].con(nodes[edge[1]])
	nodes[edge[1]].con(nodes[edge[0]])

header = None
for line in sys.stdin:
	if not header:
		header = line
		continue
	edge = line.replace("\n","").split(" ")
	addEdge(edge)

#
# Actual algorithm
#

nodes[edge[0]].scan(None)

#
# Output
#


print(removed)
