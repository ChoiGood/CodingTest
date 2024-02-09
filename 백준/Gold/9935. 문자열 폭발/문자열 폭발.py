# 문자열 폭발
s = input()
check = input()
n = len(check) # check 문자열의 길이

st = []

for ch in s:
    if len(st) < n - 1:
        st.append(ch)
    else:
        st.append(ch)
        if ''.join(st[len(st) - n:]) == check:
            for _ in range(n):
                st.pop()

if len(st) == 0:
    print('FRULA')
else:
    print(''.join(st))    
