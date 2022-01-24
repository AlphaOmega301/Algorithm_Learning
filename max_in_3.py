#세 정수 입력 받아 최댓값 구하기

print('세 정수의 최댓값 구하기')
a = int(input('정수 a의 값을 선택하세요. : '))
b = int(input('정수 b의 값을 선택하세요. : '))
c = int(input('정수 c의 값을 선택하세요. : '))

maximum = a
if b > maximum: maximum = b
if c > maximum: maximum = c

print(f'최댓값은 {maximum} 입니다.')