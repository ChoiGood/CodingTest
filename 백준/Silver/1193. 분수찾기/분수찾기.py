X = int(input())

count = 0
value = 0
temp_value = 0 # 이전 값 저장

while(True):
    count += 1
    temp_value = value
    value += count
    if(value >= X):
        break

#print(value,temp_value, count)

index = X - temp_value # 요소

if(count % 2 == 0) : # 짝수
    print(f'{index}/{count - index + 1}')
else : # 홀수 
    print(f'{count - index + 1}/{index}')

