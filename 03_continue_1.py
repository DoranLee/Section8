'''
    continue : 남은 반복문 코드를 무시하고 바로 다음 반복 회차로 넘어감
                break, continue는 if와 함께 쓰임
'''

for i in range(1,101) :
    if i % 2 == 0 :
        continue
    print(i)

# 짝수이면 continue를 만나 남은 코드인 print를 무시하고, 바로 line 5로 돌아감 --> 홀수만 print됨
