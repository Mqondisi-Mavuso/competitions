from statistics import median

test = int(input())


def success_matrix(population):
    population.sort()               # This sorts the population data
    global n, m                     # declair the n and m from the global scope
    my_list = []                     # this will store the medians
    if m == 1:
        return float(median(population))
    else:
        current_max_median = 0.0
        for i in range(m - 1):              # This is for adding the maximum numbers as the median
            current_max_median += population[-1]    # adds the current maximum
            population.remove(population[-1])  # this removes the current maximum

        my_list.append(current_max_median + median(population))

    max_matrix = my_list[-1]
    return max_matrix


case = 0
while test:
    case += 1
    smallList = list(map(int, input().split()))
    n = smallList[0]
    m = smallList[1]
    population_ = list(map(int, input().split()))  # number of participants from each region
    suc_matrix = round(success_matrix(population_), 6)
    print(f"Case #{case}: {suc_matrix}")
    test -= 1
    smallList.clear()           # we need to clear the list so that we can use in another test case
    population_.clear()

    
