# 5052 전화번호 목록
import sys
input = sys.stdin.readline

# Trie에 사용할 Node
class Node:
    def __init__(self, key:int,data=False) -> None:
        self.key = key
        self.data = data
        self.children = {}

# Trie 알고리즘
class Trie:
    # 클래스 생성 시 생성자
    def __init__(self) -> None:
        # 가장 최상위 루트, 시작점
        self.root = Node(None)
    
    # 단어를 Trie 에 넣으면서 체크
    def insert(self, string:str) -> bool:
        # root에서 시작
        current_node = self.root
        for char in string:
            # 한글자씩 넣어보자
            # 다음 노드가 없으면
            if char not in current_node.children.keys():
                # 다음 노드에 현재를 넣음
                current_node.children[char] = Node(char)
            # 다음단계로 이동(현재 넣었던 노드를 키로 받아 사용)
            # children {char : Node<class>}
            current_node = current_node.children[char]
            if current_node.data:
                return True
        # 마지막에 끝남 처리
        current_node.data = True
        return False


def solution():
    number_book = Trie()
    N = int(input())
    # Trie 알고리즘은 탐색 알고리즘이기에 정렬이 필수
    numbers = sorted([input().strip() for _ in range(N)])
    flag = 0
    # 입력을 모두 받아야 다음 케이스가 정상적으로 돌아감
    for i in range(N):
        if flag:
            continue
        if number_book.insert(numbers[i]):
            print("NO")
            # 불필요한 탐색을 줄이기 위한 flag
            flag = 1
        
    else:
        if not flag:
            print("YES")
    return 


if __name__ == "__main__":
    for _ in range(int(input())):
        solution()