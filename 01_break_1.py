'''
    break : break를 감싸고 있는 반복문을 강제 종료
        반드시 if문과 사용
        반복문을 실행 중 원하는 데이터를 찾았으니 task 종료
        원하지 않는 데이터가 나올 때 task 종료
'''

total = 0
for i in range(1000):
    total += i
    if total > 3000:
        break   # break를 감싸고 있는 반복문을 강제종료
print(total)

