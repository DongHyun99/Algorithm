def solution(people:list, limit:int):
    answer = 0
    copy = people[:]
    copy.sort()
    count_min = 0
    count_max = len(copy)-1
    while(count_min<=count_max):
        min_weight = copy[count_min]
        max_weight = copy[count_max]
        count_max -=1
        answer += 1
        if min_weight + max_weight <= limit:
            count_min += 1
    return answer