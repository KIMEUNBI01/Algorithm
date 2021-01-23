# 백준 1991 김은비 

import sys

class Node:
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right

def preorder(node): #전위순회(루트)(왼쪽 자식)(오른쪽 자식)
    print(node.item, end='')
    if node.left != '.':
        preorder(tree[node.left])
    if node.right != '.':
        preorder(tree[node.right])

def inorder(node): #중위순회(왼쪽 자식)(루트)(오른쪽 자식)
    if node.left != '.':
        inorder(tree[node.left])
    print(node.item, end='')
    if node.right != '.':
        inorder(tree[node.right])

def postorder(node): #후위순회(왼쪽 자식)(오른쪽 자식)(루트)
    if node.left != '.':
        postorder(tree[node.left])
    if node.right != '.':
        postorder((tree[node.right]))
    print(node.item, end='')

N = int(sys.stdin.readline()) #이진 트리의 노드의 개수
tree = {}
for _ in range(N): #둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다
    item, left, right = map(str, sys.stdin.readline().split()) # 항상 A가 루트 노드이며 자식 노드가 없는 경우에는 .으로 표현된다
    tree[item] = Node(item, left, right)

preorder((tree['A']))
print()
inorder(tree['A'])
print()
postorder(tree['A'])
print()