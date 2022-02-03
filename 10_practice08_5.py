'''
    숫자 하나를 입력 받아서 해당 숫자의 약수를 전부 출력하시오.
    break문 사용 가능
'''

# sol1(my sol-teacher sol)
msg = int(input('숫자입력 >> '))
lst = []
for i in range(1,msg+1):
    if msg%i ==0 :
        lst.append(i)
print(f'약수 목록 : {lst}')

# sol1-1(save ver.)
for i in range(1,msg//2+1): #약수는 절반 이후로는 자기 자신밖에 없음
    if msg%i ==0 :
        lst.append(i)
lst.append(msg) #절반까지만 나오면 자기 자신이 나오질 않음
print(f'약수 목록 : {lst}')

# sol2(my sol) --> 의미있나?
lst2=[]
for i in range(1,msg+1):
    if msg%i==0:
        lst2.append(i)
    if i == msg :
        break
print(lst2)

# sol3(my sol)
lst3=[]
a = 1
while True:
    if msg%a==0:
        lst3.append(a)
    a+=1
    if a > msg :
        break
print(lst3)