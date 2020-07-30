def hash_function_remainder(key, array_size):
	"""해시 테이블의 key를 나누기 방법으로 0 ~ array_size - 1 범위의 자연수로 바꿔주는 함수"""

	return key % array_size

def hash_function_multiplication(key, array_size, a):
    """해시 테이블의 key를 곱셈 방법으로 0 ~ array_size - 1 범위의 자연수로 바꿔주는 함수"""
    temp = a * key # a와 key를 곱한다
    temp = temp - int(temp) # a와 key를 곱한 값의 소숫점 오른쪽 부분만 저장한다
    
    return int(array_size * temp) # temp와 배열 크기를 곱한 수의 자연수 부분만 리턴한다

#파이썬의 해시 함수

print(hash(12345))
print(hash(15.1234))
print(hash("파이썬"))

# 파이썬 해시 함수는 불변 타입 자료형에만 사용할 수 있음
# 불린형 / 정수형 / 소수형 / 튜플 / 문자열