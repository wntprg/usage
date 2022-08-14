# 로또 번호 저장 공간
f = open("C:/Users/JeongMin/Desktop/파이썬 공부/lotto_machine_learning_git/lotto_number.txt","r")
lotto_numbers = f.readline()

# 로또 번호 회차 별로 나누기
#lotto_numbers = lotto_numbers.replace(" "," ").split(",")
round_lotto_nmber = []
lotto_data = []
lotto_numbers = lotto_numbers.replace('[',"").replace(']',"").replace(' ',"")
lotto_numbers = list(lotto_numbers.split(","))

for lotto_number in lotto_numbers:
    lotto_data.append(int(lotto_number))

# 확률
percentage_lotto = [0] * 45

# 로또 번호 총 개수
entire_count = len(lotto_data)

# 로또 번호 탐색

for i in range(45):
    find_lotto = lotto_data.count(i+1)
    print(find_lotto)

    percentage_lotto[i] = find_lotto/entire_count

print(entire_count)

number = [0] *45

for j in range(45):
    number[j] = j+1

# 확률 밀도 함수
from numpy import random
x = random.choice(number, p=percentage_lotto, size=(7))

print(x)