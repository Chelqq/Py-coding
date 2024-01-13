import Nodo

#Depth First Search, using stackk DS
def DFS(self):
    stack = []
    #while something in my stack = do something
    while len(stack) > 0:
        current = stack.pop()
        print(current.val)

        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

