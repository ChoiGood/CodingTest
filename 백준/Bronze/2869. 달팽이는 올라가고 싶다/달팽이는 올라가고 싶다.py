rise, drop, height = map(int, input().split())
day = 0

day_rise = rise - drop

# 하루 전 날까지 rise 하기 전까지 day_rise 로 쭉 계산
day += (height - rise) // day_rise

rest_height = (height - rise) % day_rise + rise


my_height = 0

## 너무 오래걸림...
while(True):
    day += 1
    my_height += rise
    if(my_height >= rest_height):
        break
    my_height -= drop

print(day)



