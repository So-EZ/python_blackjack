import random
import time   

user_number1 = random.randint(1,11) #플레이어의 첫번째 카드 a
user_number2 = random.randint(1,11) #플레이어의 두번째 카드 b
user_sum = user_number1 + user_number2

com_number1 = random.randint(1,11) #딜러의 첫번째 카드 A
com_number2 = random.randint(1,11) #딜러의 두번째 카드 B
com_sum = com_number1 + com_number2

sys = "[BlackJack]"

user_step = True #플레이어의 카드 추가 여부
dealer_step = True #딜러의 카드 확인
output = True #승부 결과 산출

print(f"{sys} 플레이어의 첫 번째 카드 : {user_number1}")
time.sleep(1)
print(f"{sys} 플레이어의 두 번째 카드 : {user_number2}")
time.sleep(1)
print(f"{sys} 딜러의 첫번째 숫자(A) : {com_number1}")
time.sleep(1)
print("//////////////////////////////////////////")
time.sleep(2)
print(f"{sys} 플레이어 카드 숫자의 합 : {user_sum}")
time.sleep(1)

if user_sum == 21: #플레이어가 21이라면 카드를 더 받을건지 물어보지 않음
    print(f"{sys} 블랙잭! 더 이상 카드를 받지 않습니다.")
    user_step = False 

while user_step:
    time.sleep(2)
    answer = input(f"{sys} 카드를 한 장 더 받으시겠습니까? Y / N (PLAYER : {user_sum})")

    if answer == "Y" or answer == "y" or answer == "ㅛ" or answer == "t":
        print(f"[HIT] 카드를 한 장 더 받습니다.")
        time.sleep(1)
        k = random.randint(1,11)
        print(f"{sys} 추가로 받은 카드의 숫자 : {k}")
        time.sleep(1)
        user_sum = user_sum + k
        print(f"{sys} 현재 플레이어 숫자의 합 : {user_sum} ")
        if user_sum > 21:
            print(f"[BUST] 숫자의 합이 21을 초과하여 플레이어의 패배!")
            user_step = False
            dealer_step = False
            output = False #플레이어의 패배 확정.
        elif user_sum == 21:
            print(f"{sys} 블랙잭! 더 이상 카드를 받지 않습니다.")
            user_step = False

    elif answer == "N" or answer == "n" or answer == "ㅜ" or answer == "m":
        print(f"[STAY] 카드를 더 이상 받지 않습니다.")
        user_step = False

    else:
        print(f"{sys} Y 또는 N 으로 대답해주세요.")

if dealer_step:
    print(f"{sys} 딜러의 첫 번째 카드(A) : {com_number1}")
    time.sleep(1)
    print(f"{sys} 딜러의 두 번째 카드(B) : {com_number2} ")
    time.sleep(1)
    print(f"{sys} 딜러 카드 숫자 합 : {com_sum}")
    if com_sum == 21:
        print(f"{sys} 블랙잭! 더 이상 카드를 받지 않습니다.")

    while com_sum <= 16:
        time.sleep(1)
        print(f"{sys} 딜러 카드 숫자의 합이 16 이하이므로 카드를 더 받습니다.")
        time.sleep(1)
        p = random.randint(1,11)
        print(f"{sys} 추가로 받은 카드의 숫자 : {p}")
        time.sleep(1)
        com_sum = com_sum + p
        print(f"{sys} 현재 딜러 카드 숫자의 합 : {com_sum}")   
        time.sleep(1)
        if com_sum > 21:
            print("[BUST] 숫자의 합이 21을 초과하여 딜러의 패배!")
            output = False #딜러의 패배 확정.
        elif com_sum == 21:
            print(f"{sys} 블랙잭! 더 이상 카드를 받지 않습니다.")

def out_put(user,com): #결과 산출 정의
    if user > com:
        time.sleep(1)
        print(f"[결과] PLAYER : {user_sum} / DEALER : {com_sum}")
        time.sleep(1)    
        print(f"{sys} 플레이어의 승리!")
    elif user < com:
        time.sleep(1)
        print(f"[결과] PLAYER : {user_sum} / DEALER : {com_sum}")
        time.sleep(1)
        print(f"{sys} 딜러의 승리!")
    elif user == com:
        time.sleep(1)
        print(f"[결과] PLAYER : {user_sum} / DEALER : {com_sum}")
        time.sleep(1)
        print(f"{sys} 무승부!")
    
if output == True:
    out_put(user_sum,com_sum)
    
