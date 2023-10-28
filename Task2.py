def find_common_participants(one,two,raz=","):
    sort_one = set(one.split(raz))
    sort_two = set(two.split(raz))
    sort = sorted(list(sort_one.intersection(sort_two)))
    return sort


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
result = find_common_participants(participants_first_group,participants_second_group,"|")
print(result)

