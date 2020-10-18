# Lib functions
def arrProduct(arr,func=lambda x:x):
    prod = 1
    for i in arr: prod*=func(i)
    return prod



class RadixTree:
    def __init__(self, *tree):
        if type(tree[0]) in [list, tuple]: tree = tree[0]
        for branch in tree:
            if type(branch) != int: raise TypeError(f"Invalid data type given, expected int, given {type(branch)}")
        self.map = list(tree)
    def genAddress(self, *address):
        return RadixAddress(self,*address)
    def __len__(self):
        return len(self.map)
    def __getitem__(self,index):
        if len(self) < index-1: raise IndexError("Index out of bounds")
        else: return self.map[index]
    def mapIndexToAddress(self, index):
        prod = arrProduct(self.map[1:],lambda x:x+1)
        radixAddress = [math.floor(index/prod)]
        for i in range(1,len(self.map)):
            prod /= self.map[i]+1
            radixAddress.append(math.floor(index%(prod*(self.map[i]+1))/(prod)))
        return radixAddress
    def maxIndex(self):
        return arrProduct(self.map,lambda x:x+1)-1
    def __str__(self):
        mapCopy = self.map.copy()
        for i in range(len(mapCopy)): mapCopy[i] = str(mapCopy[i])
        return f"Radix Tree >> ({','.join(mapCopy)[:-1]})"
rTree = RadixTree(3,4,5,19)
# for branch in tree:
#     print(branch)
class RadixAddress:
    def __init__(self, tree, *address):
        self.addr = []
        self.tree = tree
        if type(tree) != RadixTree: raise TypeError(f'Invalid second argument/tree argument, expected RadixTree but got {type(tree)}')
        elif len(tree) != len(address):
            if len(address) == 0:
                for branch in tree: self.addr.append(0)
            elif type(address[0]) in [list,tuple]: self.addr = address[0]
            else: raise Exception(f"Invalid length of address, the address and the tree have to have the same length")
        else: self.addr = list(address)
    def getIndex(self):
        prod = arrProduct(self.tree,lambda x:x+1)
        total = 0
        for pos in range(len(self.tree)):
            prod /= self.tree[pos]+1
            total += self.addr[pos]*prod
        return int(total)
    def resetAddress(self):
        self.addr = list(map(lambda x:0,self.addr))
    def increment(self,prt=False):
        revIndex = 1
        # print(prt)
        if self.getIndex() < self.tree.maxIndex():
            self.addr[-revIndex] = self.addr[-revIndex] + 1
            while self.tree[-revIndex] < self.addr[-revIndex] and self.tree[0] >= self.addr[0]:
                if revIndex + 1 > len(self.addr): break
                self.addr[-revIndex] = 0
                revIndex = revIndex + 1
                self.addr[-revIndex] = self.addr[-revIndex] + 1
    def toString(self):
        return str(self.addr)
rAddress = rTree.genAddress()
# print(rAddress.toString())
