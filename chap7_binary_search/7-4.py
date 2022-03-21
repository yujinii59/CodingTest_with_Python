import sys
# 하나의 문자열 데이터 입력받기
input_data = sys.stdin.readline()

# 입력받은 문자열 그대로 출력
print(len(input_data))
print(len(input_data.rstrip()))
# readline()은 rstrip()을 안해주면 엔터도 하나의 문자열로 받기 때문에 rstrip()을 해줘야 입력받은 문자열 그대로 출력이 가능하다.
print(input_data.rstrip())