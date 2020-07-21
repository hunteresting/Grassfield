from collections import deque

stack = deque()

# 스택 맨 끝에 데이터 추가
stack.append("T")
stack.append("a")
stack.append("e")
stack.append("h")
stack.append("o")

# 스택 맨 끝 데이터에 접근
print(stack[-1])

# 스택 맨 끝 데이터 삭제. 식제하는 데이터를 리턴한다.
print(stack.pop())