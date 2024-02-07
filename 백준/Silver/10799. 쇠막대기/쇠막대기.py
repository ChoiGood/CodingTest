# 쇠막대기
# 시간 제한 : 1초
# n : 100,000

s = input()
s = s.replace('()', '1')

#print(s)

st = []
result = 0 # 결과값 (나눠지는 막대기 수)
for ch in s:
    #print(st)
    if ch == '1':
        if len(st) != 0:
            st.append(ch)
    elif ch == '(':
        st.append(ch)
    elif ch == ')':
        cnt = 0 # ( ) 사이의 레이저 수
        while len(st) != 0 and st[-1] != '(':
            # 이 안에서는 - 밖에 없으므로 pop()을 하며 cnt 늘림
            value = st.pop()
            cnt += int(value)
        # len(st) ==0 이거나 st[-1] 이 '(' 임 ==> 문제 조건에 따라 ( 만 있을 거임
        st.pop() # '(' 버리고
        st.append(str(cnt)) # 레이저 수 적어주기
        result += cnt + 1 # 결과값 업데이트 (레이저로 나눠지는 막대기)
    else:
        pass

print(result)