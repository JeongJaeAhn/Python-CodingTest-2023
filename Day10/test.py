# n = 학생수, lost = 여벌 체육복가져온 학생들번호, reserve = 여분가져온 학생들번호
def solution2(n, lost, reserve):
    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)
    for i in reserve_set:
        if i-1 in lost_set:
            lost_set.remove(i-1)
        elif i+1 in lost_set:
            lost_set.remove(i+1)
    answer = n - len(lost_set)
    

    return answer

n = 5
lost = [2, 4]
reserve = [1,3,5]

print(solution2(n, lost, reserve)) # return 5


n = 5
lost = [2, 4]
reserve = [3]

print(solution2(n, lost, reserve)) # return 4


n = 3
lost = [3]
reserve = [1]

print(solution2(n, lost, reserve)) # return 2