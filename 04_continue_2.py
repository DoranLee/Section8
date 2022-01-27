frts = ['사과', '감귤']
count = 3

while count > 0 :
    frt = input('어떤 과일을 저장할까요? > ')
    if frt in frts :
        print('동일한 과일이 있습니다.')
        continue  #line4로 돌아감
    frts.append(frt)
    count -= 1
    print(f'입력이 {count}번 남았습니다.')
print(f'5개 과일은 {frts}입니다.')