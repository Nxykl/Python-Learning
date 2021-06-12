from collections import deque
class Tree_Node():


    def __init__(self, data):
        self.data = data
        self.children = []


def print_Tree_recursive(root):

    print(root.data, ":", end=" ")
    for value in root.children:
        print(value.data, end= " ")
    print()
    for  child in root.children:
         print_Tree_recursive(child)

def take_input_recursive():

    data = int(input("Enter data : "))

    root = Tree_Node(data)
    n = int(input("how many children of %s : " %data))

    for i in range(n):
        children = take_input_recursive()
        root.children.append(children)

    return root

def take_input_iterative():

    data = int(input("Enter the data : "))
    q=deque()
    root = Tree_Node(data)
    q.append(root)

    while q:
        node = q[0]
        q.popleft()

        child = int(input("how many children for %s : " % node.data))
        for i in range(1, child+1):
            child_data = int(input(f"enter data for {i} th child  of {node.data} : "))
            child_node = Tree_Node(child_data)
            q.append(child_node)
            node.children.append(child_node)
    return root

def print_Tree_iterative(root):
    q = deque()
    q.append(root)
    while q:
        node = q[0]
        q.popleft()

        print(node.data, " : ", end=" ")
        for child in range(len(node.children)):
            child_node = node.children[child]
            print(child_node.data, end= " ")
            q.append(child_node)
        print()

    return root


def count_tree_nodes(root):
    count = 1

    for child in root.children:
        count += count_tree_nodes(child)
    return count

'''
root = Tree_Node(1)
n1 = Tree_Node(2)
n2 = Tree_Node(3)
n3 = Tree_Node(4)
n4 = Tree_Node(5)

root.children.append(n1)
root.children.append(n2)
n1.children.append(n3)
n2.children.append(n4)
'''
cp_root=take_input_iterative()
print(count_tree_nodes(cp_root))
#print_Tree_iterative(cp_root)


