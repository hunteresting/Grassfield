
"""리스트"""
# 접근
    list_[0], list_1[0] = 5     # O(1)
# 추가
    list_1.append(2)    # O(1) (분할상환)
# 맨 뒤 삭제
    list_1.pop()    # O(1) (분할상환)
# 길이 확인
    len(list_1)     # O(1)
# 삽입
    list_1.insert(3, "성태호")     # O(n)
# 삭제
    del list_1[0], list_1.pop(3)    # O(n)
# 팀색
    "이재하" in list_1     # O(n)
    
"""deque (더블리 링크드 리스트)"""
# 맨 앞 삭제
    deque_1.popleft()   # O(1)
# 맨 앞 삽입
    deque_1.appendlesft("김신의")    # O(1)
# 맨 뒤 삭제
    deque_1.pop()   # O(1)
# 맨 뒤 삽입
    deque_1.append("이규식")    # O(1)
# 길이 확인
    len(deque_1)    # O(1)

"""딕셔너리 (해시테이블)"""
# 탐색
    dict_1["성태호"]   # O(1)(평균)
# 삽입
    dict_1["강영훈"] = 100     # O(1)(평균)
# 삭제
    del dict_1["강영훈"]. dict_1.pop("강영훈")    # O(1)(평균)
# 길이 확인
    len(dict_1)     # O(1)
    
"""세트 (해시테이블)"""
# 탐색 
    "최지웅" in set_1      # O(1)(평균)
# 삽입
    set_1.add("손동욱")    # O(1)(평균)
# 삭제
    set_1.remove("김현승")
    set_1.pop("김현승")    # O(1)(평균)
# 길이 확인
    len(set_1)      # O(1)