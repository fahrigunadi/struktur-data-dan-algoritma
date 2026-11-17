from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder(node):
    if node is None:
        return

    print(node.data, end=' ')
    preorder(node.left)
    preorder(node.right)


def inorder(node):
    if node is None:
        return

    inorder(node.left)
    print(node.data, end=' ')
    inorder(node.right)


def postorder(node):
    if node is None:
        return

    postorder(node.left)
    postorder(node.right)
    print(node.data, end=' ')


def preorder_list(node):
    if node is None:
        return []
    return [node.data] + preorder_list(node.left) + preorder_list(node.right)


def inorder_list(node):
    if node is None:
        return []
    return inorder_list(node.left) + [node.data] + inorder_list(node.right)


def postorder_list(node):
    if node is None:
        return []
    return postorder_list(node.left) + postorder_list(node.right) + [node.data]


def preorder_iterative(root):
    if root is None:
        return []

    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node.data)

        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)

    return result


def level_order(root):
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.data)

        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

    return result


def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


def count_leaves(node):
    if node is None:
        return 0

    if node.left is None and node.right is None:
        return 1

    return count_leaves(node.left) + count_leaves(node.right)


def height(node):
    if node is None:
        return -1

    left_height = height(node.left)
    right_height = height(node.right)

    return 1 + max(left_height, right_height)


def search(node, target):
    if node is None:
        return False

    if node.data == target:
        return True

    return search(node.left, target) or search(node.right, target)


# ============================================================
# Praktik Mandiri 9.1 - 9.3: tree A-G + node H di bawah D
# ============================================================
print('=== Praktik Mandiri 9.1 ===')
root = Node('A')
root.left = Node('B')
root.right = Node('C')

root.left.left = Node('D')
root.left.right = Node('E')
root.right.left = Node('F')
root.right.right = Node('G')

root.left.left.left = Node('H')

print('root.left.left.left.data =', root.left.left.left.data)

print('\n=== Praktik Mandiri 9.2 ===')
print('Preorder    :', preorder_list(root))
print('Inorder     :', inorder_list(root))
print('Postorder   :', postorder_list(root))
print('Level-order :', level_order(root))

print('\n=== Praktik Mandiri 9.3 ===')
print('Jumlah node :', count_nodes(root))
print('Jumlah leaf :', count_leaves(root))
print('Height      :', height(root))


# ============================================================
# Praktik Mandiri 9.4: membangun tree sendiri (root K)
# ============================================================
print('\n=== Praktik Mandiri 9.4 ===')
root_k = Node('K')
root_k.left = Node('D')
root_k.right = Node('M')

root_k.left.left = Node('B')
root_k.left.right = Node('F')

root_k.right.right = Node('Z')

print('Preorder    :', preorder_list(root_k))
print('Inorder     :', inorder_list(root_k))
print('Postorder   :', postorder_list(root_k))
print('Level-order :', level_order(root_k))
print('Jumlah node :', count_nodes(root_k))
print('Jumlah leaf :', count_leaves(root_k))
print('Height      :', height(root_k))
print("Cari 'F'    :", search(root_k, 'F'))
print("Cari 'X'    :", search(root_k, 'X'))


# ============================================================
# Praktik Mandiri 9.6: rekursif vs iteratif
# ============================================================
print('\n=== Praktik Mandiri 9.6 ===')
assert preorder_list(root) == preorder_iterative(root)
print('Hasil sama')
