def swap(tree, index_1, index_2):
    """완전 이진 트리의 노드 index_1과 노드 index_2의 위치를 바꿔준다"""
    temp = tree[index_1]
    tree[index_1] = tree[index_2]
    tree[index_2] = temp


def heapify(tree, index, tree_size):
    """heapify 함수"""

    # 왼쪽 자식 노드의 인덱스와 오른쪽 자식 노드의 인덱스를 계산
    left_child_index = 2 * index
    right_child_index = 2 * index + 1

    # 최대 인덱스가 트리의 크기를 넘지 않도록 한다.
    while left_child_index <= tree_size:
        # 두 자식 간의 크기를 비교하여 큰 자식을 선별
        bigger_child = tree.index(max(tree[left_child_index], tree[right_child_index]))
        # 큰 자식의 값이 인덱스의 값보다 큰 경우, 둘을 치환
        if tree[bigger_child] > tree[index]:    
            swap(tree, index, bigger_child)
            # 치환된 자식 아래로도 힙 정렬이 되어있는지 확인
            return heapify(tree, bigger_child, tree_size)

# 실행 코드
tree = [None, 15, 5, 12, 14, 9, 10, 6, 2, 11, 1]  # heapify하려고 하는 완전 이진 트리
heapify(tree, 2, len(tree))  # 노드 2에 heapify 호출
print(tree) 