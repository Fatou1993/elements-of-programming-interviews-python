def convertBSTToDoublyLinkedList(root) :
    prev = None
    tree = root
    stack = []
    head = None
    while tree or stack :
        if tree:
            stack.append(tree)
            tree = tree.left
        else:
            tree = stack.pop()
            if prev :
                prev.right = tree
                tree.left = prev
            if not prev :
                head = tree
            prev = tree
            tree = tree.right
    return head
