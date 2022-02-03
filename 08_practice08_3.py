
    # 비밀번호 입력
    # 비밀번호가 qwerty인지 체크
    # True면 비밀번호를 맞췄습니다. 출력 후 멈춤
    # False면 횟수 -1
# 횟수를 전부 소진하면 '비밀번호 입력횟수를 초과' 출력

count = 5
while count > 0:
    pw = input('비밀번호 입력 > ')
    if pw == 'qwerty' :
        print('비밀번호를 맞췄습니다.')
        break
    else :
        count -= 1
if count == 0 :
    print('비밀번호 입력횟수를 초과')