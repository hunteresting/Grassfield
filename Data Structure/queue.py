# deque 는 파이썬 collections 모듈에서 가지고 온다.
from collections import deque

queue = deque()

# 큐의 맨 끝에 데이터 삽입
queue.append("태호")
queue.append("현승")
queue.append("지웅")
queue.append("동욱")
queue.append("신의")

# 큐의 가장 앞 데이터에 접근
print(queue[0])

# 큐 맨 앞 데이터 삭제. 데이터를 삭제하고 해당 데이터를 리턴한다.
print(queue.popleft())
