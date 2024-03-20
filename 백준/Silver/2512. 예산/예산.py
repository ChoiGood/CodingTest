# 예산
def CalTotalBuget(limit):
    total_budget = 0
    for budget_req in budget_req_lst:
        if budget_req <= limit:
            total_budget += budget_req
        else: # budget_req > limit
            total_budget += limit
    
    return total_budget

def parameter_search(low, high):
    result = -1

    while low <= high:
        mid = (low + high) // 2

        # mid 값을 매개변수로 매개변수함수를 실행 후 결정 변수 구하기
        total_budget = CalTotalBuget(mid)

        # 만약 해당 상한액으로 구한 총 액이 M 보다 크다면 => 상한액을 낮춘다.
        #                                       작다면 => 상한액을 높인다. + 결과를 저장시킨다
        if total_budget > M:
            high = mid - 1
        else: # total_budget <= M
            low = mid + 1
            result = mid
    
    return result

# 지방의 수
N = int(input()) 
# 각 지방의 예산 요청 리스트
budget_req_lst = list(map(int, input().split()))
# 총 예산
M = int(input())

start = 0
end = max(budget_req_lst)

result = parameter_search(start, end)
print(result)