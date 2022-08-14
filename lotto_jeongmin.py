import numpy as np
from numpy import random


# 로또 번호 저장 공간
f = open("C:/Users/JeongMin/Desktop/파이썬 공부/lotto_machine_learning_git/lotto_number.txt","r")
lotto_numbers = f.readline()


# 초기화
round_lotto_number = []
tmp = []
per_value = float(0)
seven_lotto_number = []

# 로또 번호 문자열에서 [,],공백 제거
lotto_numbers = lotto_numbers.replace('[',"").replace(']',"").replace(' ',"")
lotto_numbers = list(lotto_numbers.split(","))

# 로또 번호 문자열을 숫자로 바꾸기
for lotto_number in lotto_numbers:
    tmp.append(int(lotto_number))

    # 로또 번호 숫자 7자리 회차별로 나누기
    if len(tmp) == 7:
        round_lotto_number.append(list(tmp))
        tmp = []


# 초기화
count = 0                                                                   # 확률 업 카운트
percentage = [0] * 45                                                       # 각 공이 나올 확률
molecule = [1] * 45                                                         # 분자
denominator = list(range(45))                                               # 분모

# 기준 비교값 생성
standard = list(range(1,46,1))

# 두 배열의 교집합 찾기
for i in range(1027):
    arr1 = np.array(standard)
    arr2 = np.array(round_lotto_number[i])
    percentage_up = np.intersect1d(arr1,arr2, assume_unique=True)

    for j in range(len(percentage_up)):
        molecule[percentage_up[j]-1] += 100000000000000000000000 
        count += 1

# 분모 계산      
denominator =  [len(denominator) + count*100000000000000000000000] * 45

# 확률 계산
for k in range(45):
    percentage[k] = molecule[k] / denominator[k]
 




# 같은 숫자는 나오지 않음
for l in range(7):
    random_lotto_number = random.choice(list(range(1,46,1)), p=percentage)
    seven_lotto_number.append(random_lotto_number)

    # 뽑힌 숫자의 확률
    per_value = percentage[random_lotto_number-1]/(44-l)

    # 뽑힌 숫자의 확률 나머지 확륭에 더해주기
    for m in range(45):
        percentage[m] = percentage[m] + per_value

    # 뽑힌 숫자의 확률 제거
    for n in seven_lotto_number:
        percentage[n-1] = 0    

# 로또 번호 7자리
print(seven_lotto_number)



