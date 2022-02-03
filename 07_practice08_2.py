# 영화 평점을 입력
# 평점이 1~5 사이인지 체크
# True면 평점을 ★개수로 출력
# False면 다시 입력

while True:
    g = int(input('영화 평점을 입력 > '))
    if 1 <= g <= 5 :
        print(f'평점 : {"★"*g}')
        break
    else :
        print('평점은 1~5 사이만 입력 가능함')