def triShape(edge_list):
    max_len = max(edge_list)
    if (max_len >= sum(edge_list) - max_len):
        return 'Invalid'
    
    tri = len(set(edge_list))
    if(tri == 1):
        return 'Equilateral'
    if(tri == 2):
        return 'Isosceles'
    if(tri == 3):
        return 'Scalene'
    
        
while True:
    my_list = list(map(int, input().split()))
    if(sum(my_list) == 0):
        break
    print(triShape(my_list))