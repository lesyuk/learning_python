def distance(km_list):
    progress_day = 0
    for i in range(1, len(km_list)):
        if km_list[i - 1] < km_list[i]:
            progress_day += 1
    print(progress_day)


distance([1, 5, 3, 4])