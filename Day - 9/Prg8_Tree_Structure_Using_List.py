# WAP For Tree Structure Using List

class Tree:
    def __init__(self, data):
        self.data = data                                    # instace variable creates seprate memory for each object
        self.children = []

    def addChild(self,child):
        self.children.append(child)

    def __str__(self,level=0):
        ret = "  " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

# Object Creation

rootNode = Tree("Drinks")

hot = Tree("Hot")
cold = Tree("Cold")

tea = Tree("Tea")
coffee = Tree("Coffee")

nonAlcoholic = Tree("Non Alcoholic")
alcoholic = Tree("Alcoholic")

# Add child nodes in Tree

rootNode.addChild(hot)
rootNode.addChild(cold)

hot.addChild(tea)
hot.addChild(coffee)

cold.addChild(nonAlcoholic)
cold.addChild(alcoholic)

# Print Tree

print(rootNode)




# Output = 
# Drinks
#   Hot
#     Tea
#     Coffee
#   Cold
#     Non Alcoholic
#     Alcoholic