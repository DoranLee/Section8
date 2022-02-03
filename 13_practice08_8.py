'''
    숫자 하나를 입력받아 소수인지 아닌지 판단하시오.
    break 반드시 사용
'''
# sol1(my sol)
n = int(input('숫자 입력 > '))
lst=[]
for i in range(1,n+1):
    if n%i==0:
        lst.append(i)
if len(lst)==2 or n==1:
    print('입력하신 숫자는 소수입니다.')
else:
    print('입력하신 숫자는 소수가 아닙니다.')

# sol2(teacher sol)
if n>2:
    for a in range(2,n):
        if n%a==0:
            break
    if n == a + 1:
        print('소수입니다.')
    else:
        print('소수가 아닙니다.')
elif n == 2:
    print('소수입니다.')