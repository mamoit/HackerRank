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

    # Remove this branch if it doesn't have more upstreams
    if (end.getPrevCount() == 0):
        del toMerge[end]
        return False
    else:
        return True


def runBranch(start):
    current = start

    while current is not None:
        print("# checking {} - count {}".format(current.getNum(),
              current.getPrevCount()))
        current.decPrevCount()
        if current in toMerge:
            merge(start, toMerge[current], current)
        if current.getPrevCount() > 0:
            toMerge[current] = start
            print("{} - {} # {}".format(current.getNum(), start.getNum(),
                  current.getPrevCount()))
            return

        nextNodes = current.getNextNodes()

        if len(nextNodes) == 0:
            if start == end:
                return
            else:
                # FIXME handle end that needs to be merged
                pass
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

run()

for node in nodes:
    print(nodes[node].getNum())

# ACTUAL ALGORITHM
nodes[edge[0]].scan(None)

# OUTPUT
print(removed)
