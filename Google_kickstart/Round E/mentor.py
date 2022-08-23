
test_cases = int(input())
case = 0
sorted_list = []
final_list = []

while test_cases:
    num_students = int(input())
    case += 1
    students = list(map(int, input().split()))              # read and save to a list

    for s in students:
        sorted_list.append(s)

    sorted_list.sort(reverse=True)

    for i in range(num_students - 1):
        for j in range(num_students - 1):
            if students[i] <= (sorted_list[j])/2:
                final_list.append(sorted_list[j])

            if j < num_students - 1:
                if students[i] == sorted_list[j] and students[i] == sorted_list[j+1]:
                    final_list.append(sorted_list[j])

            else:
                continue

    for final in final_list:
        print(final)

    # print(f"Case #{case}: {suc_matrix}")
    test_cases -= 1
