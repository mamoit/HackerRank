import sys


class Node:
    def __init__(self, num):
        self.num = num      # number this node represents
        self.next = []      # list of downstream nodes
        self.prevCount = 0  # number of upstream trails leading to this node
        self.heads = []     # nodes without forking which lead here
        pass

    # Adds a downstream node
    def addNext(self, newnode):
        self.next.append(newnode)

    # Adds a previous node to the count
    def addPrev(self):
        self.prevCount += 1

    # Decrements the previous node count
    def decPrevCount(self):
        self.prevCount -= 1

    # Gets the previous node count
    def getPrevCount(self):
        return self.prevCount

    # Gets next nodes
    def getNextNodes(self):
        return self.next

    def setNextNode(self, nextNode):
        self.next = [nextNode]

    def getNum(self):
        return self.num

# set of nodes
nodes = {}
head = []
toMerge = {}


# SETUP FUNCTIONS
# add an edge to the set
def addSequence(newSequence):
    prevNode = None
    for num in newSequence:
        if prevNode is None:
            prevNode = addNode(num, True)
            continue
        newNode = addNode(num, False)
        prevNode.addNext(newNode)
        newNode.addPrev()
        prevNode = newNode


def run():
    for branch in head:
        runBranch(branch)


def merge(start1, start2, end):
    # FIXME implement
    current = None

    while start1 != end or start2 != end:
        if start1.getNum() < start2.getNum():
            if current is not None:
                current.setNextNode(start1)
            current = start1
            start1 = start1.getNextNodes()[0]
        else:
            if current is not None:
                current.setNextNode(start2)
            current = start2
            start2 = start2.getNextNodes()[0]

    # Remove this branch if it doesn't have more upstreams
    if (end.getPrevCount() == 0):
        del toMerge[end]


def runBranch(start):
    current = start

    while current is not None:
        current.decPrevCount()
        if current in toMerge:
            merge(start, toMerge[current], current)
        if current.getPrevCount() > 0:
            toMerge[current] = start
            return

        nextNodes = current.getNextNodes()

        if len(nextNodes) == 0:
            return
        elif len(nextNodes) == 1:
            current = nextNodes[0]
        else:
            for node in nextNodes:
                runBranch(node)
            return


# add a node to the nodes list if it is not present
def addNode(newNum, isFirst):
    if newNum not in nodes:
        nodes[newNum] = Node(newNum)
        if isFirst:
            head.append(nodes[newNum])
    return nodes[newNum]

header = None
discard = True
for line in sys.stdin:
    if not header:
        header = line
        continue
    if (discard):
        discard = False

    sequence = line.replace("\n", "").split(" ")
    addSequence(sequence)
    discard = True

# ACTUAL ALGORITHM
run()

# OUTPUT
for node in nodes:
    for a in nodes[node].getNextNodes():
        print("{} -> {}".format(nodes[node].getNum(), a.getNum()))
