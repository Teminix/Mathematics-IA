from trees import RadixTree,RadixAddress
rTree = RadixTree(3,3,3)
rAddr = rTree.genAddress()
# print(rAddr.toString())
rAddr.increment()
