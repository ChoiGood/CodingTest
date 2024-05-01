import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
# 이진 검색 트리 만들기
# 자리 탐색 후 기입
def Search(idx):
    # 탐색 시작 위치 1부터
    p_idx = 1
    num = arr[idx]

    while True:
        
        if arr[p_idx] > num:
            if left[p_idx] == 0:
                left[p_idx] = idx
                break
            else:
                p_idx = left[p_idx]
        else:
            if right[p_idx] == 0:
                right[p_idx] = idx
                break
            else:
                p_idx = right[p_idx]

def PostTraversal(x):
    if x == 0:
        return
    
    PostTraversal(left[x])
    PostTraversal(right[x])
    print(arr[x])
    


arr = [0] * 10001
right = [0] * 10001
left = [0] * 10001

# 입력 파일의 끝까지 search 하며 graph (이진 검색 트리) 만들기
n = 0
while True:
    try:
        x = int(input().strip())
        
        n += 1
        arr[n] = x

    except ValueError:
        break

for i in range(2, n + 1):
    Search(i)

PostTraversal(1)
