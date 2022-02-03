# 구구단을 홀수단만 출력하시오. N단은 N줄만 출력하고, 단마다 간격을 두시오.

# sol1 ..> if를 최대한 줄여보자
for dan in range(2,10):
    if dan%2==0 :
        continue
    for i in range(1,dan+1):
        print(f'{dan}X{i}={dan*i}')
    print()

# sol2
for dan in range(2, 10):
    if dan % 2 == 0:
        continue
    for i in range(1, 10):
        print(f'{dan}X{i}={dan * i}')
        if i == dan :
            break
    print()