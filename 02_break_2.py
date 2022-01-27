while True :  # 무한루프 - 일반적인 프로그램의 경우 출구가 있음 --> 무한루프의 경우 반드시 break가 나옴
    city = input('대한민국의 수도는 어디인가요? > ')
    if city == '서울' or city == 'seoul' or city == 'SEOUL':
        print('정답입니다.')
        break
    else :
        print('오답입니다. 다시 시도하세요.')