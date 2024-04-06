def count_problems(n, problems):
    count=0
    for i in range(n):
        sure_count = problems[i].count(1)
        if sure_count >=2:
            count += 1
    return count

n = int(input())    
problems=[]
for _ in range(n):
    problems.append(list(map(int,input().split())))
print(count_problems(n, problems))
