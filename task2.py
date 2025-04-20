def find_common_participants(first,second):
    first_ = set(first.split("|"))
    second_ = set(second.split("|"))
    common = first_.intersection(second_)
    return sorted(common)
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group))

