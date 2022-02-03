'''
    숫자 두 개를 입력 받아서 최대공약수를 출력하시오.
'''
# sol1(my sol)
n1 = int(input('첫번째 숫자 > '))
n2 = int(input('두번째 숫자 > '))

lst=[]
x=1
while True:
    if n1%x==0 and n2%x==0:
        lst.append(x)
    x+=1
    if x > n1 and x > n2:
        break
print(f'두 수의 최대 공약수 : {max(lst)}')
print(lst[-1])

# sol2(teacher sol)
gcm = 1
if n1 > n2 :
    temp = n1 # temp : 임시변수(브로커) 필수!
    n1 = n2
    n2 = temp # n1 > n2일 경우, 둘의 자리를 바꿔줌 --> 이 이후로는 무조건 n1 < n2되도록
for i in range(2,n1+1) :
    if n1%i==0 and n2%i==0:
        gcm = i
print(f'두 수의 최대 공약수 : {gcm}')