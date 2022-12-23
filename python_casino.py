#Python blackjak 

""" 
딜러가 모두에게 카드를 두 장씩 돌림
딜러의 카드 한 장(A)을 오픈
딜러의 또 다른 카드 한 장(B)는 오픈하지 않음
플레이어는 자신의 카드 두 장과 딜러의 카드 A을 보고 카드를 자유롭게 추가하며 숫자의 합을 최대한 21에 맞춤
딜러가 B를 오픈했을 떄 딜러의 숫자 합이 16이하면 카드를 무조건 추가
최종적으로 카드에 적힌 숫자의 합이 21에 가까운 사람이 승리.
""" 

import random
import time     # sleep 함수 사용

user_number1 = random.randint(1,11) #플레이어의 첫번째 카드 a
user_number2 = random.randint(1,11) #플레이어의 두번째 카드 b
user_sum = user_number1 + user_number2

com_number1 = random.randint(1,11) #딜러의 첫번째 카드 A
com_number2 = random.randint(1,11) #딜러의 두번째 카드 B
com_sum = com_number1 + com_number2

print(f"플레이어의 첫 번째 카드 : {user_number1}")
time.sleep(1)
print(f"플레이어의 두 번째 카드 : {user_number2}")
time.sleep(1)
print(f"플레이어 카드 숫자의 합 : {user_sum}")
time.sleep(1)
print(f"딜러의 첫번째 숫자(A) : {com_number1}")

question = True #카드를 더 받을건지 물어봄

if user_sum == 21: #플레이어가 21이라면 카드를 더 받을건지 물어보지 않음
    print("블랙잭! 더 이상 카드를 받지 않습니다.")
    question = False 

while question:
    answer = input(f"카드를 한 장 더 받으시겠습니까? Y / N (PLAYER : {user_sum})")
    if answer == "Y" or answer == "y":
        print("카드를 한 장 더 받습니다. HIT")
        time.sleep(1)
        k = random.randint(1,11)
        print(f"추가로 받은 카드의 숫자 : {k}")
        time.sleep(1)
        user_sum = user_sum + k
        print(f"현재 플레이어 숫자의 합 : {user_sum} ")

        if user_sum > 21:
            print(f"숫자의 합이 21을 초과하여 플레이어의 패배! BURST")
            question = False
        elif user_sum == 21:
            print("블랙잭! 더 이상 카드를 받지 않습니다.")
            question = False

    elif answer == "N" or answer == "n":
        print("카드를 더 이상 받지 않습니다. STAY")
        question = False
    else:
        print("Y 또는 N 으로 대답해주세요.")

time.sleep(2)

print(f"딜러의 첫 번째 카드(A) : {com_number1}")
time.sleep(1)
print(f"딜러의 두 번째 카드(B) : {com_number2} ")
time.sleep(1)
print(f"딜러 카드 숫자 합은 : {com_sum}")

time.sleep(2)

while com_sum <= 16:
    print("딜러 카드 숫자의 합이 16 이하이므로 카드를 더 받습니다.")
    time.sleep(1)
    p = random.randint(1,11)
    print(f"추가로 받은 카드의 숫자 : {p}")
    time.sleep(1)
    com_sum = com_sum + p
    print(f"현재 딜러 카드 숫자의 합 : {com_sum}")   
    time.sleep(3)

if abs(com_sum - 21) > abs(user_sum - 21):
    print("플레이어의 승리!")
elif abs(com_sum - 21) < abs(user_sum - 21):
    print("딜러의 승리!")
elif abs(com_sum - 21) == abs(user_sum - 21):
    print("무승부!")

    
